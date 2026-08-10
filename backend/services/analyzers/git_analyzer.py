import os
 
from git import (
    Repo,
    InvalidGitRepositoryError,
    NoSuchPathError
)
import json
 
# ==========================================================
# Ignored files / folders
# ==========================================================
 
IGNORED_DIRS = {
    ".git",
    "node_modules",
    "__pycache__",
    ".venv",
    "venv",
    "dist",
    "build",
    ".mypy_cache",
}
 
 
IGNORED_FILES = {
    ".DS_Store",
    "package-lock.json",
    "yarn.lock"
}
 
 
TEXT_EXTENSIONS = {
 
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".php",
    ".html",
    ".css",
    ".scss",
    ".md",
    ".json",
    ".yml",
    ".yaml",
    ".sql",
    ".sh",
    ".java",
    ".c",
    ".cpp",
    ".h",
    ".go",
    ".rb",
    ".rs",
    ".vue",
    ".mdx"
 
}
 
 
MAX_FILE_SIZE = 200_000
 
 
# ==========================================================
# Git Analyzer
# ==========================================================
 
class GitAnalyzer:
 
    def __init__(self, repo_path: str):
 
        self.repo_path = os.path.abspath(repo_path)
 
        try:
            self.repo = Repo(self.repo_path)
 
        except (InvalidGitRepositoryError, NoSuchPathError):
            self.repo = None
 
        # Cache du parcours disque : avant cette optimisation,
        # walk_structure() (un os.walk complet du repo) était appelé
        # jusqu'à 3 fois par analyse (repo_metadata, build_tree_structure,
        # analyze), et detect_languages() relisait en plus le CONTENU de
        # tous les fichiers texte rien que pour regarder leur extension.
        # Le cache garantit un seul os.walk par analyse.
        self._structure_cache = None
 
    def _get_structure(self):
        if self._structure_cache is None:
            self._structure_cache = self.walk_structure()
        return self._structure_cache
 
    # ======================================================
    # Project name
    # ======================================================
 
    def project_name(self):
        return os.path.basename(self.repo_path.rstrip(os.sep))
 
    # ======================================================
    # Git metadata
    # ======================================================

    def _get_branch_name(self):
        if not self.repo:
            return "unknown"

        try:
            if self.repo.head.is_detached:
                return "detached"
        except Exception:
            pass

        try:
            return self.repo.active_branch.name
        except Exception:
            pass

        try:
            branch = self.repo.git.rev_parse("--abbrev-ref", "HEAD")
            if branch and branch.strip() not in {"HEAD", ""}:
                return branch.strip()
        except Exception:
            pass

        try:
            git_dir = getattr(self.repo, "git_dir", None)
            if git_dir and os.path.exists(git_dir):
                head_path = os.path.join(git_dir, "HEAD")
                if os.path.exists(head_path):
                    with open(head_path, "r", encoding="utf-8") as handle:
                        ref = handle.read().strip()
                    if ref.startswith("ref:"):
                        ref_name = ref.split("refs/heads/", 1)[-1]
                        if ref_name:
                            return ref_name
                    if ref and ref != "HEAD":
                        return ref
        except Exception:
            pass

        return "unknown"
    def analyze_package_json(self, file_path):
        technologies = []
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                dependencies = {}
                dependencies.update(data.get("dependencies", {}))
                dependencies.update(data.get("devDependencies", {}))
                for package in dependencies.keys():
                    if package == "react":
                        technologies.append("React")
                    elif package == "next":
                        technologies.append("Next.js")
                    elif package == "typescript":
                        technologies.append("TypeScript")
                    else:
                        technologies.append(package)
        except Exception:
            pass

        return technologies
    

    def _get_commit_info(self):
        if not self.repo:
            return None

        try:
            if not self.repo.head.is_valid():
                return None
        except Exception:
            return None

        try:
            return self.repo.head.commit
        except Exception:
            try:
                return next(self.repo.iter_commits("HEAD", max_count=1))
            except Exception:
                return None

    def _get_total_commits(self):
        if not self.repo:
            return 0

        try:
            return int(self.repo.git.rev_list("--count", "HEAD"))
        except Exception:
            try:
                return len(list(self.repo.iter_commits("HEAD")))
            except Exception:
                return 0

    def repo_metadata(self):
        if not self.repo:
            return {
                "is_git_repo": False,
                "branch": "unknown",
                "last_commit_hash": None,
                "last_commit_message": None,
                "last_commit_author": None,
                "last_commit_date": None,
                "total_commits": 0,
                "remotes": [],
                "total_files": 0,
                "total_directories": 0
            }

        metadata = {
            "is_git_repo": True,
            "branch": "unknown",
            "last_commit_hash": None,
            "last_commit_message": None,
            "last_commit_author": None,
            "last_commit_date": None,
            "total_commits": 0,
            "remotes": [],
            "total_files": 0,
            "total_directories": 0
        }

        try:
            commit = self._get_commit_info()
            if not commit:
                metadata.update({
                    "note": "Dépôt initialisé sans commit"
                })
                return metadata

            branch = self._get_branch_name()
            files_structure = self._get_structure()

            total_files = len(
                [f for f in files_structure if f["type"] == "file"]
            )

            total_directories = len(
                [d for d in files_structure if d["type"] == "directory"]
            )

            metadata.update({
                "branch": branch,
                "last_commit_hash": commit.hexsha[:8],
                "last_commit_message": (getattr(commit, "message", None) or "").strip() or "No commit message",
                "last_commit_author": str(getattr(commit, "author", "unknown") or "unknown"),
                "last_commit_date": getattr(commit.committed_datetime, "isoformat", lambda: None)(),
                "total_commits": self._get_total_commits(),
                "remotes": [remote.url for remote in self.repo.remotes if getattr(remote, "url", None)],
                "total_files": total_files,
                "total_directories": total_directories
            })
        except Exception as e:
            metadata.update({
                "error": str(e)
            })

        return metadata
 
    # ======================================================
    # Flat structure
    # Compatible DB repository_files
    # ======================================================
 
    def walk_structure(self):
 
        structure = []
        IGNORED_DIRS = {
            ".git",
            ".cache",
            "__pycache__",
            "node_modules",
            "venv",
            ".venv",
            "env",
            "output",
            "generated_docs",
            "doc-output",
            "dist",
            "build",
        }


        MIN_FILE_LINES = 5
 
        for root, dirs, files in os.walk(self.repo_path):
 
            dirs[:] = [d for d in dirs if d not in IGNORED_DIRS and not d.startswith(".")]
 
            for file in files:
 
                if file in IGNORED_FILES:
                    continue
 
                full_path = os.path.join(root, file)
 
                relative_path = os.path.relpath(
                    full_path, self.repo_path
                ).replace("\\", "/")
 
                try:
                    size = os.path.getsize(full_path)
                except OSError:
                    size = 0
 
                structure.append({
                    "path": relative_path,
                    "type": "file",
                    "size": size
                })
 
            for directory in dirs:
 
                full_dir = os.path.join(root, directory)
 
                relative_dir = os.path.relpath(
                    full_dir, self.repo_path
                ).replace("\\", "/")
 
                structure.append({
                    "path": relative_dir,
                    "type": "directory",
                    "size": 0
                })
 
        return structure
 

    def build_tree_structure(self):

        root = []

        for item in self._get_structure():

            parts = item["path"].split("/")

            current = root

            for index, part in enumerate(parts):

                last = index == len(parts) - 1

                if last:

                    if item["type"] == "file":
                        current.append({
                            "name": part,
                            "type": "file",
                            "path": item["path"]
                        })

                    else:
                        current.append({
                            "name": part,
                            "type": "folder",
                            "children": []
                        })

                else:

                    folder = next(
                        (
                            x for x in current
                            if x["name"] == part
                            and x["type"] == "folder"
                        ),
                        None
                    )

                    if not folder:
                        folder = {
                            "name": part,
                            "type": "folder",
                            "children": []
                        }

                        current.append(folder)

                    current = folder["children"]

        return root
    # ======================================================
    # List text files WITHOUT reading their content
    # ======================================================
    #
    # Permet de choisir les fichiers "importants" à envoyer à l'IA
    # avant de payer le coût d'un accès disque, en se basant
    # uniquement sur le chemin et la taille déjà connus via le cache
    # de structure.
 
    def list_text_files(self):
 
        files = []
 
        for item in self._get_structure():
 
            if item["type"] != "file":
                continue
 
            ext = os.path.splitext(item["path"])[1].lower()
 
            if ext not in TEXT_EXTENSIONS:
                continue
 
            full_path = os.path.join(
                self.repo_path,
                item["path"].replace("/", os.sep)
            )
 
            files.append({
                "path": item["path"],
                "full_path": full_path,
                "size": item["size"]
            })
 
        return files
 
    @staticmethod
    def read_file(full_path):
        """Lecture paresseuse du contenu d'un fichier, à la demande."""
        try:
            if os.path.getsize(full_path) > MAX_FILE_SIZE:
                return None
 
            with open(
                full_path, "r", encoding="utf-8", errors="ignore"
            ) as f:
                return f.read()
        except Exception as e:
            print("READ FILE ERROR:", full_path)
            print(type(e).__name__, str(e))
            return None
 
    # ======================================================
    # Read text files (conservé pour compatibilité ascendante)
    # ======================================================
 
    def iter_text_files(self):
 
        for root, dirs, files in os.walk(self.repo_path):
 
            dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
 
            for file in files:
 
                if file in IGNORED_FILES:
                    continue
 
                extension = os.path.splitext(file)[1].lower()
 
                if extension not in TEXT_EXTENSIONS:
                    continue
 
                full_path = os.path.join(root, file)
 
                try:
                    if os.path.getsize(full_path) > MAX_FILE_SIZE:
                        continue
 
                    with open(
                        full_path, "r", encoding="utf-8", errors="ignore"
                    ) as f:
                        content = f.read()
 
                except OSError:
                    continue
 
                relative_path = os.path.relpath(
                    full_path, self.repo_path
                ).replace("\\", "/")
 
                yield (relative_path, full_path, content)
 
    # ======================================================
    # Detect programming language
    # ======================================================
    #
    # Avant : relisait le contenu de tous les fichiers texte
    # (iter_text_files) rien que pour regarder leur extension.
    # Maintenant : réutilise le cache de structure (path + taille),
    # sans aucun accès disque supplémentaire.
 
    def detect_languages(self):
 
        mapping = {
            ".py": "Python",
            ".js": "JavaScript",
            ".ts": "TypeScript",
            ".java": "Java",
            ".php": "PHP",
            ".cpp": "C++",
            ".c": "C",
            ".go": "Go",
            ".rb": "Ruby",
            ".rs": "Rust"
        }
 
        languages = {}
 
        for item in self._get_structure():
 
            if item["type"] != "file":
                continue
 
            extension = os.path.splitext(item["path"])[1].lower()
 
            if extension in mapping:
                lang = mapping[extension]
                languages[lang] = languages.get(lang, 0) + 1
 
        if not languages:
            return None
 
        return max(languages, key=languages.get)
    def detect_databases(self):
        databases = []
        for item in self._get_structure():
            if item["type"] != "file":
                continue
            extension = os.path.splitext(item["path"])[1].lower()
            if extension not in TEXT_EXTENSIONS:
                continue
            full_path = os.path.join(
                self.repo_path,
                item["path"].replace("/", os.sep)
                )
            content = self.read_file(full_path)
            if content is None:
                continue
            content = content.lower()
            if "sqlite" in content:
                databases.append("SQLite")
            if "sqlalchemy" in content or "flask_sqlalchemy" in content:
                databases.append("SQL Database (SQLAlchemy)")
            if "mysql" in content:
                databases.append("MySQL")
            if (
                "mongodb" in content
                or "pymongo" in content
                or "mongoengine" in content
                ):
                databases.append("MongoDB")
            if "postgres" in content or "postgresql" in content:
                databases.append("PostgreSQL")

        return list(set(databases))
    def detect_technologies(self):
        technologies = set()
        for item in self._get_structure():
            if item["type"] != "file":
                continue

            path = item["path"].lower()
            filename = os.path.basename(path)
            if filename == "package.json":
                technologies.add("Node.js")
                full_path = os.path.join(
                    self.repo_path,
                    item["path"].replace("/", os.sep)
                    )
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        dependencies = {}
                        dependencies.update(data.get("dependencies", {}))
                        dependencies.update(data.get("devDependencies", {}))

                        if "react" in dependencies:
                            technologies.add("React")
                        if "next" in dependencies:
                            technologies.add("Next.js")
                        if "vue" in dependencies:
                            technologies.add("Vue.js")
                        if "@angular/core" in dependencies:
                            technologies.add("Angular")
                        if "typescript" in dependencies:
                            technologies.add("TypeScript")
                        if "tailwindcss" in dependencies:
                            technologies.add("Tailwind CSS")
                        if "vite" in dependencies:
                            technologies.add("Vite")
                        if "express" in dependencies:
                            technologies.add("Express.js")
                except Exception:
                    pass
            if path.startswith(".github/workflows/"):
                technologies.add("GitHub Actions")
            if filename in ("mkdocs.yml",):
                technologies.add("MkDocs")
            if filename in ("mint.json", "mintlify.json"):
                technologies.add("Mintlify")
            if "openapi" in filename:
                technologies.add("OpenAPI")

            if path.endswith(".mdx"):
                technologies.add("MDX")

            if path.endswith(".md"):
                technologies.add("Markdown")
        return sorted(technologies)
    
    
 
    # ======================================================
    # Complete analysis result
    # ======================================================
 
    def analyze(self):
        tree = self.build_tree_structure()
        return {
            "project_name": self.project_name(),
            "metadata": self.repo_metadata(),

            "structure": tree,
            "repository_tree": tree,


            "files": self._get_structure(),
            "language": self.detect_languages(),
            "technologies": self.detect_technologies(),
            "databases": self.detect_databases()
    }
 
