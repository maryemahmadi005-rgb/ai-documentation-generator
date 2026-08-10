"""

documentation_service.py



Pipeline complet:



GitHub URL

    ->

clone repository

    ->

git analysis

    ->

AI summaries

    ->

architecture detection

    ->

documentation generation



No database operations.

"""



import json
import os

import re
from collections import Counter

import subprocess

import time
import traceback



from services.git_service import clone_repository



from services.analyzers.git_analyzer import GitAnalyzer



from services.ollama_client import (

    get_default_client,

    heuristic_summary,

)



from services.analyzers.architecture_analyzer import (

    detect_architecture,

    build_comparison_markdown,

    generate_mermaid_diagram,

    generate_architecture_layers_diagram,

    generate_dataflow_diagram,

    generate_module_dependency_diagram,

)



from services.doc_builder import DocBuilder

from services.document_service import create_document



class DocumentationPipelineError(Exception):

    pass





# ==========================================================

# Réglages de performance

# ==========================================================

#

# Nombre maximum de fichiers envoyés au LLM. Avant cette optimisation,

# TOUS les fichiers texte du repo étaient envoyés à Ollama un par un :

# c'était la cause principale des temps d'analyse très longs. Les

# fichiers non sélectionnés reçoivent quand même un résumé (via le

# fallback heuristique local, rapide), donc la doc reste complète.

MAX_AI_SUMMARIES = int(os.environ.get("DOC_MAX_AI_SUMMARIES","100"))



# Par défaut, DÉSACTIVÉ : un seul appel IA global (analyze_project)

# suffit pour produire la documentation, conformément à l'objectif de

# performance ("une seule requête IA globale"). Les résumés par

# fichier utilisent alors uniquement le fallback heuristique local

# (rapide, sans appel réseau), ce qui élimine à la fois la latence de

# jusqu'à MAX_AI_SUMMARIES appels IA supplémentaires et le risque de

# contenu redondant entre résumés de fichiers et synthèse globale.

# Remettre à "true" pour retrouver l'ancien comportement (résumé IA

# par fichier prioritaire, en plus de l'analyse globale).

ENABLE_PER_FILE_AI_SUMMARIES = (

    os.environ.get("DOC_ENABLE_PER_FILE_AI_SUMMARIES", "false").lower() == "true"

)



# Budget de temps total pour la phase de résumés IA. Une fois ce

# budget dépassé, tous les fichiers restants basculent automatiquement

# sur le résumé heuristique, ce qui garantit un temps d'analyse borné

# même si Ollama répond lentement sans pour autant déclencher le

# circuit breaker (ex : réponses lentes mais valides).

AI_SUMMARY_TIME_BUDGET_SECONDS = int(

    os.environ.get("DOC_AI_TIME_BUDGET_SECONDS", "120")

)



# Nombre minimal de lignes qu'un fichier doit contenir pour être

# considéré comme pertinent (évite de documenter des fichiers vides,

# des stubs ou des fichiers générés quasi vides).

MIN_FILE_LINES = int(os.environ.get("DOC_MIN_FILE_LINES", "10"))
# عدد الملفات اللي نبعثولهم code حقيقي للـ AI
TOP_N_FILES_WITH_SOURCE = int(
    os.environ.get("DOC_TOP_N_FILES_WITH_SOURCE", "10")
)

# أقصى حجم code من كل fichier
CODE_SNIPPET_MAX_CHARS = int(
    os.environ.get("DOC_CODE_SNIPPET_MAX_CHARS", "2000")
)



# Noms de fichiers considérés comme des points d'entrée / fichiers clés

# d'un projet, donc prioritaires pour un résumé par IA.

PRIORITY_FILENAMES = {

    "app.py", "main.py", "manage.py", "wsgi.py", "asgi.py",

    "settings.py", "urls.py", "routes.py", "models.py",

    "server.js", "index.js", "index.ts", "app.js", "app.tsx",

    "app.jsx", "index.php", "artisan", "index.html",

}



# Fragments de chemin pénalisant la priorité (tests, fichiers générés,

# dépendances verrouillées, migrations...).

LOW_PRIORITY_HINTS = (

    "test",

    "spec",

    "migrations",

    "__pycache__",

    ".lock",

    "node_modules",

    "vendor",

    "assets",


    "dist",

    "build",

    "ckeditor",

    "flot",

    "bootstrap",

    "jquery",

    "demos",

    "demo",

    "examples",

    "example",

    "docs/book",

)



# ==========================================================

# Filtrage des fichiers / dossiers non pertinents

# ==========================================================

#

# Ces dossiers ne contiennent jamais de code métier : ce sont soit des

# artefacts générés (build, dist, site mkdocs...), soit des

# dépendances (node_modules, venv...), soit des caches / VCS internes.

IGNORED_DIR_NAMES = {

    ".git", ".cache", "output", "generated_docs", "generated-docs",

    "doc-output", "site", "venv", ".venv", "node_modules",

    "__pycache__", "dist", "build",

}



# Suffixes de fichiers temporaires / non pertinents pour la doc.

TEMP_FILE_SUFFIXES = (".tmp", ".temp", ".swp", ".bak", ".log", "~")



# Extensions de code source considérées comme pertinentes à analyser.

# Tout le reste (assets, fichiers de config figés, images, etc.) est

# ignoré par le pipeline de documentation.

RELEVANT_EXTENSIONS = {



    # Backend

    ".py",

    ".java",

    ".php",

    ".go",

    ".rb",



    # Frontend

    ".js",

    ".jsx",

    ".mjs",

    ".cjs",

    ".ts",

    ".tsx",



    # Documentation

    ".md",

    ".mdx",



    # Configuration

    ".json",

    ".yaml",

    ".yml",

    ".toml",



    # Styles




    ".sql",
    ".sh",
    ".bat",
    ".xml",
    ".properties",
    ".html",
    ".css",



}





def _is_temporary_file(filename: str) -> bool:

    lower = filename.lower()

    return lower.endswith(TEMP_FILE_SUFFIXES) or filename.startswith(".~")





def _is_ignored_path(path: str) -> bool:

    """

    True si le fichier se trouve dans un dossier généré/caché, ou si

    c'est lui-même un fichier caché / temporaire.

    """

    normalized = path.replace("\\", "/")

    segments = [s for s in normalized.split("/") if s]



    if not segments:

        return True



    filename = segments[-1]

    dir_segments = segments[:-1]



    for segment in dir_segments:

        if segment in IGNORED_DIR_NAMES:

            return True

        if segment.startswith("."):

            return True



    # Cas particulier du site MkDocs généré : docs/site/...

    if "docs/site/" in normalized or normalized.startswith("docs/site/"):

        return True



    if filename.startswith(".") and filename not in {
        ".gitignore",
        ".env.example",
        ".flaskenv",
    }:
        

        return True



    if _is_temporary_file(filename):

        return True



    return False





SPECIAL_FILES = {
    "Dockerfile",
    "docker-compose.yml",
    "docker-compose.yaml",
    "Procfile",
    "README",
    "README.md",
    "LICENSE",
    ".gitignore",
}


def _is_relevant_source_file(path: str) -> bool:
    filename = os.path.basename(path)

    if filename in SPECIAL_FILES:
        return True

    ext = os.path.splitext(path)[1].lower()

    return ext in RELEVANT_EXTENSIONS




def _filter_source_files(text_files):
    """
    Ne garde que les fichiers de code source pertinents, en excluant
    les dossiers générés/cachés et les extensions non pertinentes.
    """

    return [
        f
        for f in text_files
        if _is_relevant_source_file(f["path"])
    ]





def _select_ai_candidate_files(text_files):

    """

    Sélectionne les fichiers pertinents pour l'analyse IA, en incluant

    les documents et fichiers de configuration utiles au contexte du

    dépôt, sans inclure les assets binaires ou médias.

    """

    return [

        f for f in text_files

        if not _is_ignored_path(f["path"])

       

    ]





def _count_lines(content: str) -> int:

    if content is None:

        return 0

    return content.count("\n") + 1





# ==========================================================

# Extraction légère de structure de code (heuristique, pas d'AST)

# ==========================================================

#

# Objectif : donner à la doc des informations concrètes (classes,

# fonctions, dépendances, endpoints API) sans dépendre d'un parseur

# complet par langage. C'est volontairement basé sur des regex :

# suffisant pour une vue d'ensemble lisible, pas pour une analyse

# exhaustive.



_PY_PATTERNS = {

    "class": re.compile(r'^[ \t]*class\s+(\w+)', re.MULTILINE),

    "function": re.compile(r'^[ \t]*def\s+(\w+)\s*\(', re.MULTILINE),

    "blueprint": re.compile(r'^\s*(\w+)\s*=\s*Blueprint\(', re.MULTILINE),

    "import": re.compile(

        r'^[ \t]*(?:from\s+([\w\.]+)\s+import|import\s+([\w\.]+))',

        re.MULTILINE,

    ),

    "api": re.compile(

        r'@(?:\w+)\.(?:route|get|post|put|delete|patch)\(\s*[\'"]([^\'"]+)[\'"]',

        re.MULTILINE,

    ),

}



_JS_PATTERNS = {

    "class": re.compile(r'(?:export\s+)?class\s+(\w+)', re.MULTILINE),

    "function": re.compile(

        r'(?:export\s+)?(?:async\s+)?function\s+(\w+)\s*\('

        r'|(?:export\s+)?const\s+(\w+)\s*=\s*(?:async\s*)?\([^)]*\)\s*=>',

        re.MULTILINE,

    ),

    "import": re.compile(

        r'(?:import\s+.*?from\s+|require\(\s*)[\'"]([^\'"]+)[\'"]',

        re.MULTILINE,

    ),

    "api": re.compile(

        r'(?:router|app)\.(?:get|post|put|delete|patch)\(\s*[\'"]([^\'"]+)[\'"]',

        re.MULTILINE,

    ),

}



_PHP_PATTERNS = {

    "class": re.compile(r'class\s+(\w+)', re.MULTILINE),

    "function": re.compile(r'function\s+(\w+)\s*\(', re.MULTILINE),

    "import": re.compile(r'use\s+([\w\\]+)\s*;', re.MULTILINE),

    "api": re.compile(

        r'Route::(?:get|post|put|delete|patch)\(\s*[\'"]([^\'"]+)[\'"]',

        re.MULTILINE,

    ),

}



_JAVA_LIKE_PATTERNS = {

    "class": re.compile(r'class\s+(\w+)', re.MULTILINE),

    "function": re.compile(

        r'(?:public|private|protected|static|final|\s)+[\w<>\[\],\s]+\s+'

        r'(\w+)\s*\([^)]*\)\s*\{',

        re.MULTILINE,

    ),

    "import": re.compile(r'(?:import|using)\s+([\w\.]+)\s*;', re.MULTILINE),

    "api": re.compile(

        r'@(?:GetMapping|PostMapping|PutMapping|DeleteMapping|RequestMapping)'

        r'\(\s*[\'"]([^\'"]+)[\'"]',

        re.MULTILINE,

    ),

}



_GO_PATTERNS = {

    "class": re.compile(r'type\s+(\w+)\s+struct', re.MULTILINE),

    "function": re.compile(r'func\s+(?:\([^)]*\)\s*)?(\w+)\s*\(', re.MULTILINE),

    "import": re.compile(r'^\s*"([\w\./\-]+)"', re.MULTILINE),

    "api": re.compile(

        r'\.(?:GET|POST|PUT|DELETE|PATCH)\(\s*"([^"]+)"',

        re.MULTILINE,

    ),

}



_EXTENSION_PATTERNS = {

    ".py": _PY_PATTERNS,

    ".js": _JS_PATTERNS, ".jsx": _JS_PATTERNS, ".mjs": _JS_PATTERNS,

    ".cjs": _JS_PATTERNS, ".ts": _JS_PATTERNS, ".tsx": _JS_PATTERNS,

    ".vue": _JS_PATTERNS,

    ".php": _PHP_PATTERNS,

    ".java": _JAVA_LIKE_PATTERNS, ".kt": _JAVA_LIKE_PATTERNS,

    ".cs": _JAVA_LIKE_PATTERNS,

    ".go": _GO_PATTERNS,

}



_EMPTY_STRUCTURE = {

    "classes": [], "functions": [], "imports": [], "api_endpoints": [], "blueprints": [],

}





def _find_all(pattern, content, join_groups=False):

    if pattern is None:

        return []



    results = []



    for match in pattern.finditer(content):

        groups = [g for g in match.groups() if g]



        if not groups:

            continue



        results.append(" ".join(groups) if join_groups else groups[0])



    return results





def _dedupe_limit(values, limit):

    seen = []

    for value in values:

        if value not in seen:

            seen.append(value)

        if len(seen) >= limit:

            break

    return seen





def _extract_code_structure(path: str, content: str) -> dict:

    """

    Extraction heuristique (regex, pas d'AST) des classes, fonctions,

    imports et endpoints API d'un fichier. Suffisant pour donner une

    vue d'ensemble lisible dans la doc générée.

    """

    ext = os.path.splitext(path)[1].lower()

    patterns = _EXTENSION_PATTERNS.get(ext)



    if not patterns or not content:

        return dict(_EMPTY_STRUCTURE)



    return {

        "classes": _dedupe_limit(

            _find_all(patterns.get("class"), content), 8

        ),

        "functions": _dedupe_limit(

            _find_all(patterns.get("function"), content), 15

        ),

        "imports": _dedupe_limit(

            _find_all(patterns.get("import"), content), 12

        ),

        "api_endpoints": _dedupe_limit(

            _find_all(patterns.get("api"), content, join_groups=True), 10

        ),

        "blueprints": _dedupe_limit(

            _find_all(patterns.get("blueprint"), content), 5

        ),

    }





def _build_architecture_explanation(architecture_result: dict) -> str:

    """

    Construit une explication lisible de l'architecture détectée, à

    partir de ce que `detect_architecture()` retourne déjà (type,

    confiance, signaux, classement complet). Ne modifie pas la

    logique de détection elle-même.

    """

    arch_type = architecture_result.get("type") or "Non déterminée"

    confidence = architecture_result.get("confidence_pct")

    score_out_of_10 = architecture_result.get("score_out_of_10")

    signals = architecture_result.get("signals", [])

    ranking = architecture_result.get("full_ranking", [])



    parts = [

        f"Architecture détectée : {arch_type}"

        + (f" (confiance {confidence}%)" if confidence is not None else "")

        + (

            f", score {score_out_of_10}/10"

            if score_out_of_10 is not None

            else ""

        )

        + "."

    ]



    if signals:

        parts.append(

            "Signaux principaux ayant motivé cette détection : "

            + "; ".join(signals[:5]) + "."

        )



    alternatives = [

        item for item in ranking

        if item.get("type") != arch_type

    ][:2]



    if alternatives:

        alt_text = ", ".join(

            f"{item.get('type')} ({item.get('confidence_pct')}%)"

            for item in alternatives

        )

        parts.append(

            f"Architectures alternatives envisagées : {alt_text}."

        )



    ambiguous_with = architecture_result.get("ambiguous_with")



    if ambiguous_with:

        parts.append(

            f"Attention : le score est proche de celui de "

            f"« {ambiguous_with} », la distinction n'est pas "

            f"totalement tranchée."

        )



    return " ".join(parts)





def _build_project_statistics(file_summaries: dict, structure: dict) -> dict:

    """Construit des statistiques globales réutilisables par l'API et la doc."""

    extension_counts = Counter()

    total_classes = 0

    total_functions = 0

    total_api_endpoints = 0

    total_lines_of_code = 0

    total_complexity_score = 0

    complexity_entries = []

    largest_entries = []

    for path, data in file_summaries.items():

        structure_data = data.get("structure", {}) or {}

        ext = os.path.splitext(path)[1].lower()

        if ext:

            extension_counts[ext] += 1

        classes = len(structure_data.get("classes", []) or [])

        functions = len(structure_data.get("functions", []) or [])

        imports = len(structure_data.get("imports", []) or [])

        api_endpoints = len(structure_data.get("api_endpoints", []) or [])

        line_count = data.get("line_count", 0) or 0

        total_classes += classes

        total_functions += functions

        total_api_endpoints += api_endpoints

        total_lines_of_code += line_count

        complexity_score = (classes * 4) + (functions * 2) + imports
        total_complexity_score += complexity_score

        complexity_entries.append({
            "path": path,
            "score": complexity_score,
            "classes": classes,
            "functions": functions,
            "imports": imports,
        })

        largest_entries.append({
            "path": path,
            "line_count": line_count,
        })

    def _label_for_extension(ext: str) -> str:

        labels = {
            ".py": "Python",
            ".js": "JavaScript",
            ".jsx": "JavaScript",
            ".ts": "TypeScript",
            ".tsx": "TypeScript",
            ".html": "HTML",
            ".css": "CSS",
            ".md": "Markdown",
        }

        return labels.get(ext, ext.upper() or "Autre")

    average_complexity_score = (
        round(total_complexity_score / len(file_summaries), 2)
        if file_summaries
        else 0
    )

    return {

        "total_files": len(file_summaries or {}),

        "total_directories": _count_directories(structure),

        "python_files": extension_counts.get(".py", 0),

        "javascript_files": extension_counts.get(".js", 0) + extension_counts.get(".jsx", 0),

        "typescript_files": extension_counts.get(".ts", 0) + extension_counts.get(".tsx", 0),

        "html_files": extension_counts.get(".html", 0),

        "css_files": extension_counts.get(".css", 0),

        "markdown_files": extension_counts.get(".md", 0),

        "total_classes": total_classes,

        "total_functions": total_functions,

        "total_api_endpoints": total_api_endpoints,

        "total_lines_of_code": total_lines_of_code,

        "lines": total_lines_of_code,

        "complexity_score": average_complexity_score,

        "average_complexity_score": average_complexity_score,

        "file_type_distribution": {
            _label_for_extension(ext): count
            for ext, count in sorted(extension_counts.items())
            if ext in {".py", ".js", ".jsx", ".ts", ".tsx", ".html", ".css", ".md"}
        },

        "largest_files": sorted(
            largest_entries,
            key=lambda item: item.get("line_count", 0),
            reverse=True,
        )[:10],

        "file_types": {
            _label_for_extension(ext): count
            for ext, count in sorted(extension_counts.items())
            if ext in {".py", ".js", ".jsx", ".ts", ".tsx", ".html", ".css", ".md"}
        },

        "most_complex_files": sorted(
            complexity_entries,
            key=lambda item: item.get("score", 0),
            reverse=True,
        )[:10],

    }



def _build_file_dependencies(file_summaries: dict) -> dict:

    """Construit les dépendances internes entre fichiers à partir des imports extraits."""

    available_modules = {}

    for path in file_summaries.keys():

        normalized_path = path.replace("\\", "/").lstrip("./")

        if not normalized_path:

            continue

        ext = os.path.splitext(normalized_path)[1].lower()

        if not ext:

            continue

        module_name = normalized_path[:-len(ext)].replace("/", ".")

        if module_name:

            available_modules[module_name] = path

    dependencies = {}

    for path, data in file_summaries.items():

        imports = (data.get("structure", {}) or {}).get("imports", []) or []

        local_dependencies = []

        seen = set()

        for imp in imports:

            if not imp:

                continue

            normalized_import = imp.split(" as ")[0].strip()

            if not normalized_import:

                continue

            for module_name, candidate_path in available_modules.items():

                if candidate_path == path:

                    continue

                if normalized_import in {module_name, module_name + "."}:

                    if candidate_path not in seen:

                        seen.add(candidate_path)

                        local_dependencies.append(candidate_path)

                elif normalized_import.startswith(module_name + "."):

                    if candidate_path not in seen:

                        seen.add(candidate_path)

                        local_dependencies.append(candidate_path)

                elif module_name.startswith(normalized_import + "."):

                    if candidate_path not in seen:

                        seen.add(candidate_path)

                        local_dependencies.append(candidate_path)

        dependencies[path] = local_dependencies

    return dependencies



def _build_blueprints(file_summaries: dict) -> list:

    """Regroupe les fichiers par blueprint Flask détecté, avec un fallback par nom de dossier."""

    blueprint_names = set()

    for data in file_summaries.values():

        for blueprint in (data.get("structure", {}) or {}).get("blueprints", []) or []:

            if blueprint:

                blueprint_names.add(blueprint)

    blueprints = []

    for blueprint_name in sorted(blueprint_names):

        files = []

        for path, data in file_summaries.items():

            structure_data = data.get("structure", {}) or {}

            normalized_path = path.replace("\\", "/").lower()

            if blueprint_name in structure_data.get("blueprints", []) or blueprint_name in normalized_path.split("/"):

                files.append(path)

        if files:

            blueprints.append({
                "name": blueprint_name,
                "files": sorted(files),
            })

    return blueprints



def _build_files_list(file_summaries: dict) -> list:

    """

    Transforme le dict interne file_summaries (path -> {summary,

    line_count, structure}) en une liste à plat sérialisable en JSON,

    prête à être renvoyée à l'API / au frontend.

    """

    dependencies_map = _build_file_dependencies(file_summaries)

    return [

        {

            "path": path,

            "line_count": data.get("line_count", 0),

            "classes": data.get("structure", {}).get("classes", []),

            "functions": data.get("structure", {}).get("functions", []),

            "imports": data.get("structure", {}).get("imports", []),

            "api_endpoints": data.get("structure", {}).get("api_endpoints", []),

            "blueprints": data.get("structure", {}).get("blueprints", []),

            "dependencies": dependencies_map.get(path, []),

            "complexity_score": (
                (len(data.get("structure", {}).get("classes", []) or []) * 4)
                + (len(data.get("structure", {}).get("functions", []) or []) * 2)
                + (len(data.get("structure", {}).get("imports", []) or []))
            ),

            "summary": data.get("summary", ""),
            "content": data.get("content", ""),

        }

        for path, data in file_summaries.items()

    ]





# Mapping extension -> technologie, utilisé pour construire la liste

# des technologies détectées passée au prompt d'analyse globale.

EXTENSION_TO_TECH = {

    ".py": "Python",

    ".js": "JavaScript", ".jsx": "JavaScript (React)",

    ".mjs": "JavaScript", ".cjs": "JavaScript",

    ".ts": "TypeScript", ".tsx": "TypeScript (React)",

    ".vue": "Vue.js",

    ".java": "Java", ".kt": "Kotlin",

    ".go": "Go",

    ".cs": "C#",

    ".php": "PHP",

    ".rb": "Ruby",

    ".c": "C", ".cpp": "C++", ".h": "C/C++", ".hpp": "C++",

    ".rs": "Rust",

    ".swift": "Swift",

}





READMES_CANDIDATES = (

    "README.md", "Readme.md", "readme.md",

    "README.rst", "README.txt", "README",

)



# Nombre de caractères max du README d'origine transmis au prompt IA

# (pour rester dans un budget de contexte raisonnable).

README_EXCERPT_MAX_CHARS = 1000





def _read_project_readme(repo_path: str):

    """

    Lit le README d'origine du projet (s'il existe) directement depuis

    le repo cloné, indépendamment du pipeline d'analyse fichier par

    fichier (s'il existe) directement depuis le dépôt cloné, en

    complément du pipeline d'analyse fichier par fichier. Sert de

    contexte supplémentaire pour l'analyse IA globale : évite le

    fallback générique "objectif non déduit" quand un README existe

    déjà et décrit le projet.

    """

    for candidate in READMES_CANDIDATES:

        candidate_path = os.path.join(repo_path, candidate)



        if os.path.isfile(candidate_path):

            try:

                content = GitAnalyzer.read_file(candidate_path)

            except Exception:

                content = None



            if content:

                return content[:README_EXCERPT_MAX_CHARS]



    return None





def _count_directories(structure) -> int:

    if not isinstance(structure, dict):

        return 0



    count = 0



    for child in structure.get("dirs", {}).values():

        count += 1 + _count_directories(child)



    return count





def _infer_tech_stack(file_summaries):

    techs = set()



    for path in file_summaries.keys():

        ext = os.path.splitext(path)[1].lower()

        tech = EXTENSION_TO_TECH.get(ext)

        if tech:

            techs.add(tech)



    return sorted(techs)





# ==========================================================

# Détection enrichie des technologies (au-delà des extensions)

# ==========================================================

#

# Repère, via des fichiers/signatures caractéristiques, le framework,

# la base de données, l'ORM, le gestionnaire de paquets, la

# containerisation, la CI/CD, les tests, la documentation, le cloud et

# l'IA utilisés. Complète `_infer_tech_stack` (basé sur les extensions)

# sans le remplacer : le champ `technologies` reste une liste plate de

# chaînes, compatible avec l'existant (DB, frontend, API).



_TECH_SIGNATURE_FILES = {

    "package.json": "Node.js",

    "requirements.txt": "pip (Python)",

    "pyproject.toml": "Python (pyproject)",

    "Pipfile": "Pipenv",

    "composer.json": "Composer (PHP)",

    "pom.xml": "Maven (Java)",

    "build.gradle": "Gradle (Java/Kotlin)",

    "Gemfile": "Bundler (Ruby)",

    "go.mod": "Go Modules",

    "Cargo.toml": "Cargo (Rust)",

    "Dockerfile": "Docker",

    "docker-compose.yml": "Docker Compose",

    "docker-compose.yaml": "Docker Compose",

    "mkdocs.yml": "MkDocs",

    "serverless.yml": "Serverless Framework",

    "pytest.ini": "Pytest",

    "jest.config.js": "Jest",

    "phpunit.xml": "PHPUnit",

    ".flaskenv": "Flask",

}



_PACKAGE_JSON_DEP_HINTS = {

    "react": "React", "vue": "Vue.js", "next": "Next.js",

    "express": "Express.js", "@nestjs/core": "NestJS",

    "mongoose": "MongoDB (Mongoose)", "sequelize": "Sequelize ORM",

    "typeorm": "TypeORM", "prisma": "Prisma ORM",

    "axios": "Axios", "tailwindcss": "Tailwind CSS",

}



_REQUIREMENTS_DEP_HINTS = {

    "flask": "Flask", "django": "Django", "fastapi": "FastAPI",

    "sqlalchemy": "SQLAlchemy ORM", "psycopg2": "PostgreSQL",

    "pymongo": "MongoDB", "redis": "Redis",

    "celery": "Celery", "ollama": "Ollama (LLM local)",

    "openai": "OpenAI API", "langchain": "LangChain",

    "pytest": "Pytest",

}

_DATABASE_HINTS = {

    "sqlite": "SQLite",

    "mysql": "MySQL",

    "postgres": "PostgreSQL",

    "postgresql": "PostgreSQL",

    "mongodb": "MongoDB",

}

def _read_json(repo_path: str, filename: str) -> dict:
    path = os.path.join(repo_path, filename)
    if not os.path.isfile(path):
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def _read_requirements(repo_path: str) -> list[str]:
    path = os.path.join(repo_path, "requirements.txt")
    if not os.path.isfile(path):
        return []
    try:
        with open(path, encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    except Exception:
        return []


def _detect_technologies_with_evidence(repo_path, file_summaries=None):

    """

    Détecte les technologies à partir de preuves visibles dans le dépôt

    (dépendances, fichiers de config, imports, extensions) et retourne

    une structure compatible avec les besoins existants : une liste de

    dictionnaires {name, evidence}. L'API / frontend restent inchangés

    car la liste plate de technologies reste construite plus bas.

    """

    detections = []

    evidence_map = {}



    def add_tech(name, evidence):

        if not name:

            return

        if name not in evidence_map:

            evidence_map[name] = []

        if evidence not in evidence_map[name]:

            evidence_map[name].append(evidence)



    try:

        root_files = set(os.listdir(repo_path))

    except OSError:

        return []



    for filename, label in _TECH_SIGNATURE_FILES.items():

        if filename in root_files:

            add_tech(label, f"fichier racine: {filename}")



    if ".github" in root_files and os.path.isdir(os.path.join(repo_path, ".github", "workflows")):

        add_tech("GitHub Actions", "dossier .github/workflows")



    package_data = _read_json(repo_path, "package.json")
    deps = {**package_data.get("dependencies", {}), **package_data.get("devDependencies", {})}
    for dep_name in deps:
        if dep_name in _PACKAGE_JSON_DEP_HINTS:
            add_tech(_PACKAGE_JSON_DEP_HINTS[dep_name], f"package.json: dépendance {dep_name}")
        if dep_name in {"vite", "vitest", "tailwindcss", "typescript", "react", "next"}:
            add_tech("Vite", "package.json: vite")
    if "next" in deps:
        add_tech("Next.js", "package.json: next")
    if "react" in deps:
        add_tech("React", "package.json: react")
    if "tailwindcss" in deps:
        add_tech("Tailwind CSS", "package.json: tailwindcss")
    if "typescript" in deps:
        add_tech("TypeScript", "package.json: typescript")
    if "vite" in deps:
        add_tech("Vite", "package.json: vite")

    for line in _read_requirements(repo_path):
        pkg_name = re.split(r"[=<>~!\[]", line)[0].strip().lower()
        if pkg_name in _REQUIREMENTS_DEP_HINTS:
            add_tech(_REQUIREMENTS_DEP_HINTS[pkg_name], f"requirements.txt: {pkg_name}")
        for db_key, db_name in _DATABASE_HINTS.items():
            if db_key in pkg_name:
                add_tech(db_name, f"requirements.txt: {pkg_name}")



    for filename in ("next.config.js", "next.config.mjs", "next.config.ts", "vite.config.js", "vite.config.ts", "vite.config.mjs", "tsconfig.json", "mkdocs.yml", "docker-compose.yml", "docker-compose.yaml", "Dockerfile"):

        if filename in root_files:

            if filename.startswith("next.config"):

                add_tech("Next.js", f"fichier racine: {filename}")

            elif filename.startswith("vite.config"):

                add_tech("Vite", f"fichier racine: {filename}")

            elif filename == "tsconfig.json":

                add_tech("TypeScript", f"fichier racine: {filename}")

            elif filename == "mkdocs.yml":

                add_tech("MkDocs", f"fichier racine: {filename}")

            elif filename in {"docker-compose.yml", "docker-compose.yaml", "Dockerfile"}:

                add_tech("Docker", f"fichier racine: {filename}")



    if file_summaries:

        for path, data in file_summaries.items():

            lower_path = path.lower()

            if lower_path.endswith((".md", ".mdx")):

                add_tech("MDX", f"fichier: {path}")

            if lower_path.endswith((".yaml", ".yml")):

                add_tech("YAML", f"fichier: {path}")

            if lower_path.endswith(".tsx"):

                add_tech("TypeScript", f"fichier: {path}")

            if lower_path.endswith(".jsx"):

                add_tech("JavaScript", f"fichier: {path}")

            if lower_path.endswith(".mdx"):

                add_tech("MDX", f"fichier: {path}")

            if lower_path.endswith((".md", ".mdx")) and any(token in lower_path for token in ("docs", "doc")):

                add_tech("Docusaurus", f"fichier: {path}")

            if "openapi" in lower_path or "swagger" in lower_path:

                add_tech("OpenAPI", f"fichier: {path}")

            if "asyncapi" in lower_path:

                add_tech("AsyncAPI", f"fichier: {path}")



    for name, evidence_items in evidence_map.items():

        detections.append({"name": name, "evidence": evidence_items})



    return sorted(detections, key=lambda item: item["name"].lower())





def _detect_database_from_files(file_summaries):

    databases = set()

    database_signals = {

        "MySQL": [
            "mysql",
            "pymysql",
            "mysql+pymysql",
            "mysqlclient"
        ],

        "SQLAlchemy ORM": [
            "sqlalchemy",
            "SQLAlchemy",
            "db.Model",
            "db.Column",
            "__tablename__",
            "session.query"
        ],

        "PostgreSQL": [
            "postgres",
            "postgresql",
            "psycopg2"
        ],

        "MongoDB": [
            "mongodb",
            "pymongo",
            "mongoengine"
        ]

    }


    for path, data in file_summaries.items():

        structure = data.get(
            "structure",
            {}
        )

        imports = structure.get(
            "imports",
            []
        )


        # imports
        content = ""

        if data.get("source_excerpt"):
            content += data["source_excerpt"]


        summary = data.get("summary", "")
        content += summary


        # نضيف imports
        content += " ".join(imports)


        content_lower = content.lower()


        for database, signals in database_signals.items():

            for signal in signals:

                if signal.lower() in content_lower:

                    databases.add(database)
                    break


    return sorted(databases)





def _detect_technology_signals(repo_path):

    """

    Retourne (technologies_supplémentaires: list[str], dependencies:

    list[str]) détectées via des fichiers signatures à la racine du

    projet, sans dépendre du LLM.

    """

    evidence = _detect_technologies_with_evidence(repo_path)

    extra_techs = [item["name"] for item in evidence]

    dependencies = []



    try:

        root_files = set(os.listdir(repo_path))

    except OSError:

        return [], []



    if ".github" in root_files and os.path.isdir(os.path.join(repo_path, ".github", "workflows")):

        extra_techs.append("GitHub Actions")



    package_json_path = os.path.join(repo_path, "package.json")

    if os.path.isfile(package_json_path):

        try:

            import json as _json

            with open(package_json_path, encoding="utf-8") as f:

                pkg = _json.load(f)

            deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}

            dependencies += [f"{name}@{version}" for name, version in list(deps.items())[:10]]

        except Exception:

            pass



    requirements_path = os.path.join(repo_path, "requirements.txt")

    if os.path.isfile(requirements_path):

        try:

            with open(requirements_path, encoding="utf-8") as f:

                req_lines = [line.strip() for line in f.readlines() if line.strip() and not line.startswith("#")]

            dependencies += req_lines[:10]

        except Exception:

            pass



    return sorted(set(extra_techs)), dependencies

ENTRY_FILES = {
    "app.py",
    "main.py",
    "run.py",
    "server.py",
    "manage.py",
    "wsgi.py",
    "asgi.py",
    "__main__.py",

    # Frontend
    "index.js",
    "index.ts",
    "main.js",
    "main.jsx",
    "app.js",
    "app.jsx",
}


def is_entry_point(file_path):
    name = os.path.basename(file_path).lower()
    return name in ENTRY_FILES


def _detect_entry_points(important_files):

    print("===== ENTRY DETECTOR START =====")
    print("COUNT:", len(important_files))

    entry_points = []

    for file_info in important_files:

        path = file_info["path"]
        filename = os.path.basename(path).lower()


        # تجاهل ملفات الاختبار
        if (
            filename.startswith("test_")
            or filename.endswith("_test.py")
            or "/tests/" in path.lower()
        ):
            continue
        path_lower = path.replace("\\", "/").lower()
        if "/templates/" in path_lower:
            continue
        if "/static/" in path_lower:
            continue
        if is_entry_point(path):
            entry_points.append(
                path
            )
        elif filename == "index.html":
            ath_lower = path.replace("\\", "/").lower()

        # index.html في templates/static ليست entry point
            if (
                "/templates/" not in path_lower
                and "/static/" not in path_lower
                ):
                entry_points.append(path)


        # كشف scripts Python التي تتنفذ مباشرة
        elif filename.endswith(".py"):

            try:
                with open(
                    file_info["full_path"],
                    "r",
                    encoding="utf-8"
                ) as f:

                    content = f.read()
                is_flask_file = (
                    "flask" in content.lower()
                    or "from flask import" in content
                )


                if (
                    "sys.argv" in content
                    or "__main__" in content
                    or "app.run(" in content
                ):
                    entry_points.append(
                        path
                    )
                elif(
                    "create_app(" in content
                    and is_flask_file

                    ):
                    entry_points.append(
                        path)

                

            except Exception:
                pass
        elif filename.endswith((".js", ".jsx")):
            try:
                with open(
                    file_info["full_path"],
                    "r",
                    encoding="utf-8"
                ) as f:

                    content = f.read()


                if (
                    "React" in content
                    or "ReactDOM" in content
                    or "createRoot" in content
                ):
                    entry_points.append(path)

            except Exception:
                pass

    print("DETECTED ENTRY POINTS:", entry_points)
    print("===== ENTRY DETECTOR END =====")

    return entry_points[:6]





def _build_structure_overview(structure, max_depth=2, max_lines=400):
    """
    Convert repository_tree (list format) into compact text
    for Ollama prompt.
    """

    lines = []

    def walk(nodes, prefix="", depth=0):

        if depth > max_depth:
            return

        if not isinstance(nodes, list):
            return

        for node in nodes:

            if len(lines) >= max_lines:
                return

            name = node.get("name")

            if not name:
                continue

            if node.get("type") == "file":

                lines.append(
                    f"{prefix}{name}"
                )

            elif node.get("type") == "folder":

                lines.append(
                    f"{prefix}{name}/"
                )

                walk(
                    node.get("children", []),
                    prefix + "  ",
                    depth + 1
                )

    walk(structure)

    if not lines:
        return "Structure indisponible."

    return "\n".join(lines)





def _build_key_files_digest(file_summaries, important_paths, limit=10):

    """

    Construit un résumé court des fichiers importants.

    Utilise le contenu généré par l'analyse fichier sans prendre

    uniquement le premier titre Markdown.

    """



    digest = []



    for path in important_paths:



        data = file_summaries.get(path)



        if not data:

            continue
      



        summary = (data.get("summary") or "").strip()



        if not summary:

            continue



        # Nettoyage des titres Markdown inutiles

        lines = [

            line.strip()

            for line in summary.splitlines()

            if line.strip()

            and not line.startswith("#")

        ]



        description = ""



        for line in lines:

            if len(line) > 20:

                description = line

                break



        if not description:

            description = "Information non disponible."



        digest.append(

            f"- `{path}` : {description}"

        )



        if len(digest) >= limit:

            break



    return digest

def _build_technical_documentation_content(

    project_name,

    ai_summary,

    architecture_explanation,

    tech_stack,

    dependencies,

    entry_points,

    structure,

    file_summaries,

):

    objective = ""

    if ai_summary:

        objective = "\n".join(

            line.strip() for line in ai_summary.splitlines() if line.strip()

        )

    if not objective:

        objective = (

            f"{project_name} est un projet logiciel dont l'objectif est "

            "d'automatiser l'analyse et la documentation du dépôt."

        )



    workflow = (

        "Le système analyse automatiquement les fichiers du dépôt, "

        "détecte l'architecture et génère une documentation technique "

        "ainsi que des diagrammes de structure et de dépendances."

    )

    if entry_points:

        workflow += (

            " Les points d'entrée principaux observés sont "

            + ", ".join(entry_points[:4])

            + "."

        )

    if dependencies:

        workflow += (

            " Les dépendances importantes détectées incluent "

            + ", ".join(dependencies[:6])

            + "."

        )



    technologies = ", ".join(tech_stack) if tech_stack else "Non déterminées"

    recommendations = [

        "Conserver une séparation nette entre le README de présentation et la documentation technique complète.",

        "Documenter les interfaces et dépendances lors des évolutions majeures.",

        "Ajouter des tests automatisés autour des modules critiques pour sécuriser l'évolution du système.",

    ]



    lines = [

        f"# Documentation technique - {project_name}",

        "",

        "## Objectif du projet",

        "",

        objective,

        "",

        "## Description générale du fonctionnement",

        "",

        workflow,

        "",

        "## Architecture détectée",

        "",

        architecture_explanation or "Architecture non déterminée.",

        "",

        "## Technologies utilisées",

        "",

        technologies,

        "",

        "## Modules principaux",

        "",

    ]



    module_entries = []

    for path, data in sorted(file_summaries.items())[:12]:

        summary = (data.get("summary") or "Résumé indisponible").strip().splitlines()[0]

        module_entries.append(f"- **{path}** : {summary}")

    if module_entries:

        lines.extend(module_entries)

    else:

        lines.append("- Aucun module principal n'a été identifié automatiquement.")



    lines.extend([

        "",

        "## Flux de données",

        "",

        "Le flux principal part des fichiers sources du dépôt, passe par l'analyse structurelle et l'analyse IA, puis produit des fichiers de documentation et des diagrammes de synthèse.",

        "",

        "## Points d'entrée",

        "",

    ])



    if entry_points:

        lines.extend(f"- {entry_point}" for entry_point in entry_points[:8])

    else:

        lines.append("- Aucun point d'entrée explicite n'a été détecté automatiquement.")



    lines.extend([

        "",

        "## Dépendances importantes",

        "",

    ])



    if dependencies:

        lines.extend(f"- {dependency}" for dependency in dependencies[:12])

    else:

        lines.append("- Aucune dépendance majeure n'a été identifiée automatiquement.")



    lines.extend([

        "",

        "## Recommandations",

        "",

    ])

    lines.extend(f"- {recommendation}" for recommendation in recommendations)

    lines.extend([

        "",

        "## Analyse détaillée des fichiers",

        "",

    ])



    for path, data in sorted(file_summaries.items()):

        structure = data.get("structure", {})

        summary = (data.get("summary") or "Résumé indisponible").strip()

        classes = ", ".join(structure.get("classes", [])) or "Aucune"

        functions = ", ".join(structure.get("functions", [])) or "Aucune"

        imports = ", ".join(structure.get("imports", [])) or "Aucune"



        lines.extend([

            f"### {path}",

            "",

            summary,

            "",

            f"- Classes : {classes}",

            f"- Fonctions : {functions}",

            f"- Dépendances : {imports}",

            "",

        ])



    return "\n".join(lines)





def _select_important_files(text_files, max_files=None):
    """
    Sélection intelligente des fichiers importants pour l'analyse IA.
    Priorise le vrai code métier et les points d'entrée.
    """

    ranked = []

    for file_info in text_files:

        try:
            content = GitAnalyzer.read_file(
                file_info["full_path"]
            ) or ""

            score = _advanced_score_file(
                file_info,
                content
            )
            print(
                "SELECT SCORE:",
                file_info["path"],
                "=>",
                score
                )

            file_info["importance_score"] = score

            ranked.append(file_info)

        except Exception:
            continue


    # Trier par score décroissant
    ranked.sort(
        key=lambda x: x.get(
            "importance_score",
            -999999
        ),
        reverse=True
    )


    if max_files is None:
        max_files = int(
            os.environ.get(
                "DOC_IMPORTANT_FILES_LIMIT",
                "35"
            )
        )


    # حذف الملفات غير المفيدة نهائيا
    ranked = [
        f for f in ranked
        if f.get("importance_score", -999999) > -5000
    ]


    # DEBUG واضح
    print("\n========== TOP IMPORTANT FILES ==========")

    for f in ranked[:max_files]:
        print(
            f"{f.get('path')} score={f.get('importance_score')}"
        )

    print("=========================================\n")


    return ranked[:max_files]





def _score_file(file_info):

    path_lower = file_info["path"].replace("\\", "/").lower()
    filename = os.path.basename(path_lower)

    score = 0


    # ==================================================
    # ENTRY POINTS (أعلى أولوية)
    # ==================================================

    entry_points = {
        "app.py",
        "main.py",
        "server.py",
        "index.py",
        "index.js",
        "index.ts",
        "manage.py",
        "wsgi.py",
        "asgi.py",
        "flasky.py"
        
    }

    if filename in entry_points:
        score += 9000
    if (
         filename == "__init__.py"
         and any(
             x in path
             for x in [
                 "app/",
                 "src/",
                 "backend/"
                ]
        )
    ):
        score += 7000



    # ==================================================
    # BUSINESS DIRECTORIES
    # ==================================================

    business_paths = [
        "app/",
        "src/",
        "backend/",
        "server/",
        "core/",
        "services/",
        "service/",
        "controllers/",
        "controller/",
        "routes/",
        "routers/",
        "models/",
        "entities/",
        "domain/",
        "modules/"
    ]

    if any(p in path_lower for p in business_paths):
        score += 5000



    # ==================================================
    # CODE FILES
    # ==================================================

    code_extensions = (
        ".py",
        ".js",
        ".ts",
        ".jsx",
        ".tsx",
        ".java",
        ".go",
        ".php",
        ".rb"
    )

    if path_lower.endswith(code_extensions):
        score += 1500



    # ==================================================
    # CONFIG NECESSAIRE
    # (أقل من الكود دائما)
    # ==================================================

    configs = {
        "requirements.txt",
        "package.json",
        "pyproject.toml",
        "setup.py",
        "pom.xml",
        "composer.json",
        "cargo.toml"
    }

    if filename in configs:
        score += 2000



    # ==================================================
    # DOCKER / DEPLOY CONFIG
    # ==================================================

    deploy_configs = {
        "dockerfile",
        "docker-compose.yml",
        "docker-compose.yaml",
        "vite.config.js",
        "vite.config.ts",
        "tsconfig.json"
    }

    if filename in deploy_configs:
        score += 500



    # ==================================================
    # LOW VALUE FILES
    # ==================================================

    if filename.startswith("readme"):
        score -= 12000


    if filename.endswith(
        (
            ".md",
            ".txt"
        )
    ):
        score -= 8000



    low_dirs = [
        "docs/",
        "documentation/",
        "static/",
        "assets/",
        "images/",
        "public/",
        "coverage/",
        "examples/",
        "example/",
        "samples/",
        "sample/",
        "tests/",
        "test/"
    ]


    if any(x in path_lower for x in low_dirs):
        score -= 15000



    # scripts simples
    if filename in {
        "boot.sh",
        "start.sh",
        "run.sh",
        "build.sh"
    }:
        score -= 40000



    # الحجم المتوسط أفضل
    size = file_info.get("size", 0)

    if 1000 < size < 200000:
        score += 500


    return score





def _advanced_score_file(file_info, content):

    path = file_info["path"].replace("\\", "/").lower()
    filename = os.path.basename(path)

    content_lower = content.lower()

    score = _score_file(file_info)


    # ==================================================
    # EXCLUDE GENERATED / DEPENDENCIES
    # ==================================================

    excluded = [
        "node_modules/",
        "vendor/",
        "__pycache__/",
        "dist/",
        "build/",
        "coverage/",
        ".next/",
        ".nuxt/",
        "migrations/",
        "templates/",
        "static/",
        "assets/",
        "public/"
    ]

    if any(x in path for x in excluded):
        return -999999



    # ==================================================
    # TESTS LOW PRIORITY
    # ==================================================

    if any(
        x in path
        for x in [
            "test/",
            "tests/",
            "__tests__/",
            "spec/"
        ]
    ):
        score -= 30000



    # ==================================================
    # BUSINESS CODE
    # ==================================================

    if any(
        x in path
        for x in [
            "services/",
            "controllers/",
            "routes/",
            "models/",
            "core/",
            "repositories/",
            "api/",
            "auth/",
            "/api/" ,
            "/auth/",
            "/main/" 
        ]
    ):
        score += 50000
    if path.endswith("models.py"):
        score += 60000



    # ==================================================
    # ENTRY POINT
    # ==================================================

    if filename in {
        "app.py",
        "main.py",
        "server.py",
        "index.py",
        "index.js",
        "index.ts",
        "manage.py",
        "wsgi.py",
        "asgi.py"
    }:
        score += 9000



    if (
        filename == "__init__.py"
        and any(
            x in path
            for x in [
                "app/",
                "src/",
                "backend/",
                "server/"
            ]
        )
    ):
        score += 7000



    # ==================================================
    # CODE SIGNALS
    # ==================================================

    signals = {
        "flask": 500,
        "fastapi": 500,
        "django": 500,
        "express": 500,

        "router": 400,
        "@app.route": 600,
        "blueprint": 500,
        "controller": 300,
        "service": 300,
        "repository": 300,

        "class ": 150,
        "def ": 100,
        "async def": 150,

        "sqlalchemy": 400,
        "mongoose": 400,
        "sequelize": 300
    }


    for key, value in signals.items():
        if key in content_lower:
            score += value



    # ==================================================
    # LOW VALUE FILES
    # ==================================================

    if filename.startswith("readme"):
        score -= 5000


    if path.startswith("docs/"):
        score -= 20000



    if filename.endswith(
        (
            ".html",
            ".css"
        )
    ):
        score -= 15000



    if any(
        x in path
        for x in [
            "static/",
            "assets/",
            "public/"
        ]
    ):
        score -= 30000



    # ==================================================
    # CONFIGURATION
    # ==================================================

    config_files = {
        "docker-compose.yml",
        "docker-compose.yaml",
        "dockerfile",
        "vite.config.js",
        "vite.config.ts",
        "tsconfig.json",
        "mkdocs.yml",
        "package.json",
        "requirements.txt",
        "pyproject.toml"
    }


    if filename in config_files:
        if filename in {
            "requirements.txt",
            "package.json",
            "pyproject.toml",
            "pom.xml",
            "cargo.toml"
            }:
            score += 10000
        else:
            score = min(score, 4000)


    # ==================================================
    # FAKE / MOCK
    # ==================================================

    if any(
        x in filename
        for x in [
            "fake",
            "mock",
            "dummy",
            "sample"
        ]
    ):
        score -= 999999


    # ==================================================
    # SCRIPTS
    # ==================================================

    if filename.endswith(
        (
            ".sh",
            ".bat",
            ".cmd"
        )
    ):
        score -= 50000



    # ==================================================
    # PROJECT SPECIFIC PRIORITY
    # ==================================================

    priority_files = {

        "app/__init__.py": 50000,
        "app/models.py": 45000,

        "config.py": 30000,
        "flasky.py": 30000,

        "requirements.txt": 10000,
        
    }
    normalized_path = path.replace("\\", "/").lower()




    # Flask API
    for p, bonus in priority_files.items():
        if normalized_path.endswith(p):
            score += bonus
            break



    # Flask Auth
    if path.startswith("app/auth/") and filename.endswith(".py"):
        score += 40000



    # Exclude explicitly
    if filename in {
        "fake.py",
        "boot.sh",
        "docker-compose.yml",
        "docker-compose.yaml"
    }:
        score -= 70000



    if path in priority_files:
        score += priority_files[path]



    # ==================================================
    # DEBUG FINAL SCORE
    # ==================================================

    print(
        "FINAL SCORE:",
        file_info["path"],
        score
    )
    normalized = path.replace("\\","/").lower()
    

    if normalized.endswith("app/__init__.py"):
        score += 100000
    


    return score

def _get_code_language(path):

    ext = os.path.splitext(path)[1].lower()

    languages = {
        ".py": "python",
        ".js": "javascript",
        ".jsx": "jsx",
        ".ts": "typescript",
        ".tsx": "tsx",
        ".html": "html",
        ".css": "css",
        ".json": "json",
        ".md": "markdown",
        ".yml": "yaml",
        ".yaml": "yaml"
    }

    return languages.get(ext, "")
def _contains_leaked_digest_language(text):
    """
    Detecte les résumés générés qui contiennent
    des traces internes ou du prompt.
    """

    if not text:
        return False

    bad_patterns = [
        "code inventory",
        "digest",
        "prompt",
        "final code sent",
        "important files",
        "here is",
        "as an ai",
        "summary generated",
    ]

    text_lower = text.lower()

    return any(
        p in text_lower
        for p in bad_patterns
    )
        

def _build_code_inventory(
    file_summaries,
    important_files,
    entry_points=None,
    limit=300
):
    """
       Construit un inventaire technique compact.

    Tous les fichiers sont envoyés avec :
    - path
    - structure
    - functions
    - classes
    - imports
    - summary
Les fichiers importants uniquement contiennent
le code source réel.
    """

    sections = []
    print("IMPORTANT FILES COUNT:", len(important_files))
    print(
        "IMPORTANT FILES:",
        [f["path"] for f in important_files]
    )


    important_paths = {
        f["path"].replace("\\","/").replace("**", "__")
        for f in important_files
        }
    for path, data in file_summaries.items():
        if not data:
            continue
        filename = os.path.basename(path).lower()
        dependency_files = {
            "requirements.txt",
            "package.json",
            "pyproject.toml",
            "pom.xml",
            "cargo.toml"
            }
        if filename in dependency_files:
            content = data.get("content", "")
            sections.append(
                 f"""
                 ## {path}

Type:
Dependency file

Language:
Configuration

Role:
Liste des dépendances et technologies utilisées par le projet.

Dependencies:
{content[:5000]}

"""
        )
            continue
        

        structure = data.get("structure", {})

        summary = data.get("summary", "").strip()
 

        # entry_points يجب أن يحتوي على paths بدون `
        is_entry = path in (entry_points or [])

        description = "Résumé indisponible."
        if summary:
            if not _contains_leaked_digest_language(summary):
                description = summary
        language = _get_code_language(path)
        
        normalized_path = path.replace("\\","/").replace("**", "__")
        code_extensions = (
            ".py",
            ".js",
            ".ts",
            ".jsx",
            ".tsx",
            ".java",
            ".go",
            ".php",
            ".cpp",
            ".c"
            )
        source_code = ""
        if( 
            normalized_path in important_paths  and normalized_path.lower().endswith(code_extensions)
        ):
            source_code = data.get(
                "content",
                ""
            )
            if source_code:
                print("🔥 CODE SENT:", path)
            elif normalized_path in important_paths:
                print("⚠️ IMPORTANT WITHOUT CONTENT:", path)
        else:
            print("📄 METADATA ONLY:", path)



        source_code = (
            source_code[:8000].replace("```", "'''")
            if source_code
            else ""
        )
        

        snippet_block = ""
        if source_code:
            snippet_block = (
                f"Code snippet:\n"
                f"```{language}\n"
                f"{source_code}\n"
                f"```\n"
            )

        sections.append(
            f"""
## {path}

Type:
{"Entry point" if is_entry else "Module"}

Language:
{language}

Role:
{description}

Lines:
{data.get("line_count", 0)}

Classes:
{", ".join(structure.get("classes", []))
if structure.get("classes")
else "None"}

Functions:
{", ".join(structure.get("functions", []))
if structure.get("functions")
else "None"}

Imports:
{", ".join(structure.get("imports", []))
if structure.get("imports")
else "None"}

API:
{", ".join(structure.get("api_endpoints", []))
if structure.get("api_endpoints")
else "None"}
{snippet_block}

"""
)
        if len(sections) >= limit:
            break


    MAX_CONTEXT_SIZE = 100000

    result = ""

    for block in sections:

        if len(result) + len(block) > MAX_CONTEXT_SIZE:
            break

        result += block + "\n"
    print("================ INVENTORY DEBUG ================")
    print("TOTAL FILE SECTIONS:", len(sections))
    print("FINAL INVENTORY SIZE:", len(result))

    for s in sections:
        print(s.split("\n")[1])
    print("==================================================")


    return result
        
def _build_dependencies(repo_path, file_summaries):

    dependencies = []

    # ==========================
    # 1) requirements.txt
    # ==========================

    requirements_path = os.path.join(
        repo_path,
        "requirements.txt"
    )

    if os.path.exists(requirements_path):

        try:
            with open(
                requirements_path,
                "r",
                encoding="utf-8"
            ) as f:

                for line in f:

                    line = line.strip()

                    if (
                        line
                        and not line.startswith("#")
                    ):
                        dependencies.append(line)

        except Exception:
            pass



    # ==========================
    # 2) Imports détectés
    # ==========================

    standard_libs = {
        "os",
        "sys",
        "json",
        "re",
        "time",
        "datetime",
        "typing",
        "pathlib",
        "logging",
        "collections",
        "math",
        "random",
    }


    imports = set()


    for data in file_summaries.values():

        structure = data.get(
            "structure",
            {}
        )

        for imp in structure.get(
            "imports",
            []
        ):

            root = imp.split(".")[0]

            if root not in standard_libs:

                imports.add(root)



    for imp in sorted(imports):

        if imp not in dependencies:

            dependencies.append(imp)



    return dependencies[:20]
def detect_technologies_from_dependencies(dependencies):

    tech = []

    mapping = {
        "flask": "Flask",
        "django": "Django",
        "fastapi": "FastAPI",
        "sqlalchemy": "SQLAlchemy",
        "react": "React",
        "express": "Express",
        "pymongo": "MongoDB",
        "mongoose": "MongoDB",
        "pytest": "Pytest",
    }

    for dep in dependencies:

        dep_lower = dep.lower()

        for key, name in mapping.items():

            if key in dep_lower:
                tech.append(name)

    return list(set(tech))


IGNORED_TREE_DIRS = {
    # Version control
    ".git",

    # Dependencies
    "node_modules",
    "vendor",

    # Python cache
    "__pycache__",
    ".pytest_cache",

    # Build/generated
    "dist",
    "build",
    "coverage",
    ".next",
    ".nuxt",

    # Virtual environments
    "venv",
    ".venv",

    # Documentation generated
    "site",
    "output",
    "generated_docs",
    "doc-output",

    # Assets lourds
    "images",
    "files",
    "uploads",
    "static",

    # Localization noise
    "fr",
    "es",
    "zh",
}
def filter_tree_structure(structure):
    """
    Retire récursivement de l'arborescence les dossiers listés dans
    IGNORED_TREE_DIRS...
    """
    if not isinstance(structure, dict):
        return structure

    cleaned = {}

    for name, value in structure.items():
        if name.lower() in IGNORED_TREE_DIRS:
            continue
        if isinstance(value, dict):
            cleaned[name] = filter_tree_structure(value)
        else:
            cleaned[name] = value

    return cleaned
def _detect_install_command(repo_path):
    if os.path.exists(os.path.join(repo_path, "requirements.txt")):
        return "pip install -r requirements.txt"

    if os.path.exists(os.path.join(repo_path, "pyproject.toml")):
        return "pip install ."

    package_json = os.path.join(repo_path, "package.json")
    if os.path.exists(package_json):
        return "npm install"

    return None
def _detect_run_command(repo_path, entry_points):
    names = {os.path.basename(x) for x in entry_points}

    if "manage.py" in names:
        return "python manage.py runserver"

    if "app.py" in names:
        return "python app.py"

    if "main.py" in names:
        return "python main.py"

    package_json = os.path.join(repo_path, "package.json")

    if os.path.exists(package_json):
        try:
            with open(package_json, encoding="utf-8") as f:
                pkg = json.load(f)

            scripts = pkg.get("scripts", {})

            if "start" in scripts:
                return "npm start"

            if "dev" in scripts:
                return "npm run dev"

        except Exception:
            pass

    return None
def normalize_structure(tree):

    result = {
        "files": [],
        "dirs": {}
    }

    def walk(nodes, current_dir=""):

        for node in nodes:

            path = node.get("path")

            if node.get("type") == "file":

                result["files"].append(path)

            elif node.get("type") == "folder":

                folder_name = node.get("name")

                result["dirs"].setdefault(folder_name, {})

                walk(
                    node.get("children", []),
                    folder_name
                )

    walk(tree)

    return result
def _extract_module_relations(file_summaries):

    relations = []

    # نكوّن قائمة modules Python فقط
    module_paths = {
        p.replace("\\", ".")
         .replace("/", ".")
         .replace(".py", "")
        for p in file_summaries.keys()
        if p.endswith(".py")
    }


    for path, data in file_summaries.items():

        # نتجاهلو html/css/tests إذا تحب فقط modules التطبيق
        if not path.endswith(".py"):
                if not path.endswith(".py"):
                    continue

    # تجاهل tests و migrations
        if (
            path.startswith("tests/")
            or path.startswith("migrations/")
            ):
            continue


        structure = data.get(
            "structure",
            {}
        )

        imports = structure.get(
            "imports",
            []
        )


        source_module = (
            path.replace("\\", ".")
                .replace("/", ".")
                .replace(".py", "")
        )


        for imp in imports:

            if not isinstance(imp, str):
                continue


            for module in module_paths:

                # relation حقيقية بين modules فقط
                if (
                    imp == module
                    or imp.startswith(module + ".")
                    or module.startswith(imp + ".")
                ):

                    relations.append(
                        {
                            "source": source_module,
                            "target": module
                        }
                    )


    # إزالة التكرار
    unique = []

    seen = set()

    for r in relations:

        key = (
            r["source"],
            r["target"]
        )

        if key not in seen:

            seen.add(key)
            unique.append(r)


    return unique
    
def _extract_blueprints(file_summaries):

    blueprints = []

    for path, data in file_summaries.items():

        content = data.get(
            "content",
            ""
        )

        if "Blueprint(" in content:

            blueprints.append(
                path
            )

    return blueprints
def _extract_routes(file_summaries):

    routes = []

    for path, data in file_summaries.items():

        structure = data.get(
            "structure",
            {}
        )

        endpoints = structure.get(
            "api_endpoints",
            []
        )

        for endpoint in endpoints:

            routes.append(
                {
                    "file": path,
                    "route": endpoint
                }
            )

    return routes





def generate_documentation(
    github_url: str,
    analysis_id=None,
    log_callback=None
):
    print("🚀 START generate_documentation")


    def log(level, message):

        if log_callback:

            log_callback(
                level,
                message
            )



    try:


        # ==================================================
        # 1) Clone repository
        # ==================================================

        log(
            "INFO",
            "Clonage du dépôt GitHub..."
        )


        repo_path = clone_repository(
            github_url,
            full_history=True
        )


        log(
            "INFO",
            f"Dépôt cloné : {repo_path}"
        )




        # ==================================================
        # 2) Git analysis
        # ==================================================

        log(
            "INFO",
            "Analyse du repository..."
        )


        analyzer = GitAnalyzer(
            repo_path
        )


        analysis_data = analyzer.analyze()



        structure = analysis_data.get(
            "structure",
            {}
        )




        tree_structure = filter_tree_structure(
            structure
        )



        metadata = analysis_data.get(
            "metadata",
            {}
        )



        project_name = (
            github_url
            .rstrip("/")
            .split("/")[-1]
            .replace(".git","")
        )



        commit_hash = metadata.get(
            "last_commit_hash"
        )



        if commit_hash:

            log(
                "INFO",
                f"Commit analysé : {commit_hash}"
            )

        else:

            log(
                "WARNING",
                "Impossible de récupérer le commit hash."
            )







        # ==================================================
        # 3) Sélection fichiers
        # ==================================================


        log(
            "INFO",
            "Filtrage des fichiers..."
        )



        raw_text_files = analyzer.list_text_files()



        text_files = _filter_source_files(
            raw_text_files
        )



        log(
            "INFO",
            f"{len(text_files)} fichiers conservés."
        )

        # --- DEBUG مؤقت ---
        print(f"RAW FILES COUNT: {len(raw_text_files)}")
        for f in raw_text_files:
            print(f"RAW => {f['path']}")
        print(f"FILTERED FILES COUNT: {len(text_files)}")
        for f in text_files:
            print(f"FILTERED => {f['path']}")





        ai_files = _select_ai_candidate_files(
            text_files
        )
        print("========== AI FILES ==========")
        for f in ai_files:
            print(f["path"])
            print("TOTAL:", len(ai_files))
        print("==============================")



        important_files = _select_important_files(
            ai_files,
            max_files=int(
                os.environ.get(
                    "DOC_IMPORTANT_FILES_LIMIT",
                    "35"
                )
            )
        )



        important_paths = {
            f["path"]
            for f in important_files
        }
        print("===== IMPORTANT FILES =====")
        for p in important_paths:
            print(p)
        print("==========================")



        for f in important_files:

            log(
                "INFO",
                f"AI FILE => {f['path']} "
                f"score={f.get('importance_score')}"
            )




        log(
            "INFO",
            f"{len(important_files)} fichiers prioritaires sélectionnés."
        )




        # ==================================================
        # Initialisation AI
        # ==================================================

        ai_client = get_default_client()



        ai_start_time = time.monotonic()


        ai_calls_made = 0


        skipped_small_files = 0



        file_summaries = {}



        total_files = len(
            text_files
        )



        # ==================================================
        # Analyse fichiers
        # ==================================================

        for index, file_info in enumerate(
            text_files,
            start=1
        ):


            path = file_info["path"]


            try:


                content = GitAnalyzer.read_file(
                    file_info["full_path"]
                )
                print("FILE:", path)
                print("CONTENT SIZE:", len(content) if content else 0)
                print(content[:200] if content else "EMPTY")
                print("===================")



                if not content:


                    file_summaries[path] = {

                        "summary":
                            "Impossible de lire le fichier",

                        "line_count":
                            0,

                        "structure":
                            dict(_EMPTY_STRUCTURE)

                    }


                    continue





                line_count = _count_lines(
                    content
                )



                if line_count < MIN_FILE_LINES:


                    skipped_small_files += 1


                    continue





                file_structure = _extract_code_structure(
                    path,
                    content
                )
                source_excerpt = None
                if path in important_paths:
                    source_excerpt = content[:CODE_SNIPPET_MAX_CHARS]
                print("====== STRUCTURE DEBUG ======")
                print(path)
                print(file_structure)
                print("==============================")




                elapsed = (
                    time.monotonic()
                    -
                    ai_start_time
                )



                use_ai = (

                    ENABLE_PER_FILE_AI_SUMMARIES

                    and path in important_paths

                    and ai_client.is_available()

                    and elapsed <
                    AI_SUMMARY_TIME_BUDGET_SECONDS

                )



                if use_ai:


                    summary = ai_client.summarize_file(
                        path,
                        content
                    )


                    ai_calls_made += 1



                else:


                    summary = heuristic_summary(
                        path,
                        content
                    )




            except Exception as exc:
                log(
                    "WARNING",
                    f"Résumé impossible pour {path}: {exc}"
                    )
                summary = "Résumé indisponible"
                line_count = 0
                file_structure = dict(_EMPTY_STRUCTURE)
                print("FILE STRUCTURE DEBUG:", path)
                print(file_structure)
            


       


        
                  
            dependency_files = {
                "requirements.txt",
                "package.json",
                "pyproject.toml",
                "pom.xml",
                "cargo.toml"
                }
            file_summaries[path] = {

                "summary":
                    summary,

                "line_count":
                    line_count,

                "structure":
                    file_structure,
                "content":(
                    content
                    if path in important_paths
                    or path.startswith("requirements/")
                    or os.path.basename(path).lower() in dependency_files
                    else ""
                    ),

                "source_excerpt":
                     source_excerpt

            }
            print("========== FILE DEBUG ==========")
            print("PATH:", path)
            print("CONTENT SIZE:", len(file_summaries[path]["content"]))
            print(file_summaries[path]["content"][:500])
            print("================================")




            if index % 10 == 0:


                log(
                    "INFO",
                    f"Résumés générés : "
                    f"{index}/{total_files} "
                    f"({ai_calls_made} via IA)"
                )



        if skipped_small_files:

            log(
                "INFO",
                f"{skipped_small_files} fichier(s) ignoré(s) "
                f"(moins de {MIN_FILE_LINES} lignes)."
            )



        if not ai_client.is_available():

            log(
                "WARNING",
                "Ollama indisponible ou trop lent : "
                "résumés heuristiques utilisés."
            )


        module_relations = _extract_module_relations(

            file_summaries

            )





        blueprints = _extract_blueprints(

            file_summaries

            )



 

        routes = _extract_routes(

            file_summaries

            )

        analysis_data["module_relations"] = module_relations

        analysis_data["blueprints"] = blueprints

        analysis_data["routes"] = routes
   
       



        # ==================================================
        # 4) Détection architecture
        # ==================================================

        log(
            "INFO",
            "Détection architecture..."
        )



        files = _build_files_list(file_summaries)
        file_list = files
        print("\n========== FILES SENT TO ARCH ==========")
        for f in files[:20]:
            print(
                "\nFILE:", f.get("path"),
                "\nIMPORTS:", f.get("imports"),
                "\nFUNCTIONS:", f.get("functions"),
                "\nENDPOINTS:", f.get("api_endpoints"),
                "\nBLUEPRINTS:", f.get("blueprints"),
                )
        print("========================================\n")


        arch_structure = normalize_structure(structure)
        print("ARCH STRUCTURE DEBUG")
        print(arch_structure)


        architecture_result = detect_architecture(
            arch_structure,
            files=files
        )
        print("ARCH RESULT =", architecture_result)



        architecture = (
            architecture_result.get("type")
            or architecture_result.get("detected_architecture")
            or architecture_result.get("name")
            or "Unknown"
            )



        ranking = architecture_result.get(
            "full_ranking",
            []
        )



        architecture_score = None


        if ranking:

            architecture_score = ranking[0].get(
                "raw_score"
            )


        architecture_confidence = (
            architecture_result.get("confidence_pct")
            or architecture_result.get("confidence")
            or architecture_result.get("architecture_confidence")
            or 0
            )



        architecture_explanation = (
            _build_architecture_explanation(
                architecture_result
            )
        )





        # ==================================================
        # 5) Analyse globale du projet IA
        # ==================================================

        log(
            "INFO",
            "Analyse globale du projet (IA)..."
        )



        existing_readme_excerpt = _read_project_readme(
            repo_path
        )
        if not existing_readme_excerpt:
            existing_readme_excerpt = """
No README file is available.

Generate the project description from:
- detected architecture
- technologies
- entry points
- important modules
- code inventory
- dependencies
"""



        # Technologies

        tech_stack = _infer_tech_stack(
            file_summaries
        )



        extra_techs, detected_dependencies = (
            _detect_technology_signals(
                repo_path
            )
        )



        database_techs = _detect_database_from_files(
            file_summaries
        )
        dependencies = _build_dependencies(
            repo_path,
            file_summaries
        )
        tech_stack.extend(
            detect_technologies_from_dependencies(dependencies)
        )



        tech_stack = sorted(
            set(tech_stack)
            |
            set(extra_techs)
            |
            set(database_techs)
        )
        if important_files:
            print("IMPORTANT FILE SAMPLE:")
            print(important_files[0].keys())



        entry_points = _detect_entry_points(
            important_files
        )
        print("===== ENTRY POINTS DEBUG =====")
        for ep in entry_points:
            print("ENTRY =>", ep)
        print("==============================")



        structure_overview = _build_structure_overview(
            structure
        )



        key_files_digest = _build_key_files_digest(
            file_summaries,
            important_paths
        )
    



        code_inventory = _build_code_inventory(
            file_summaries,
            important_files,
            entry_points
        )
        print("===== CODE INVENTORY DEBUG =====")
        print(code_inventory[:3000])
        print("================================")




        package_json = _read_json(repo_path, "package.json")
        detected_scripts = package_json.get("scripts", {})
        install_command = _detect_install_command(repo_path)
        run_command = _detect_run_command(
            repo_path,
            entry_points
            )



        # Fusion dependencies détectées

        dependencies = sorted(
            set(dependencies)
            |
            set(detected_dependencies)
        )



        databases = _detect_database_from_files(
            file_summaries
            )
        print(
            "DATABASE DETECTED:",
            databases
            )





        # ==================================================
        # Analyse IA globale
        # ==================================================

        start = time.time()
        print("\n========== FILES SENT TO OLLAMA ==========")
        import re
        files_in_prompt = re.findall(
            r"## (.+)",
            code_inventory
            )
        for f in files_in_prompt:
            print("OLLAMA FILE =>", f)
        print("==========================================")
        print("TOTAL FILES SENT TO OLLAMA:", len(files_in_prompt))


        ai_summary = ai_client.analyze_project(
            
            project_name=project_name,
            tech_stack=tech_stack,
            databases=databases,
            architecture_type=architecture,
            architecture_confidence=architecture_confidence,
            structure_overview=structure_overview,
            key_files_digest=key_files_digest,
            existing_readme_excerpt=existing_readme_excerpt,
            entry_points=entry_points,
            dependencies=dependencies,
            code_inventory=code_inventory,
            module_relations=module_relations,
            blueprints=blueprints,
            routes=routes
        )


        # ==================================================
        # Conversion JSON -> Markdown
        # ==================================================



        print(
            "AI PROJECT TIME:",
            time.time() - start
        )





        # ==================================================
        # Génération README IA
        # ==================================================

        readme_ai_content = (
            ai_client.generate_readme_content(
                
                project_name=project_name,

                tech_stack=tech_stack,

                dependencies=dependencies,

                entry_points=entry_points,

                existing_readme_excerpt=
                    existing_readme_excerpt,

                key_files_digest=
                    key_files_digest,

                code_inventory=
                    code_inventory,

                structure_overview=
                    structure_overview,

                databases=
                    databases,
                repository_url=github_url, 
                detected_scripts=detected_scripts,
                install_command=install_command,
                run_command=run_command,
            )
        )





        # ==================================================
        # Documentation technique IA
        # ==================================================

  


        documentation_ai_content = ai_summary
        print(
            "AI SUMMARY SIZE:",
            len(json.dumps(ai_summary, ensure_ascii=False))
        )

        print(
            "README AI SIZE:",
            len(readme_ai_content)
        )

        print(
            "TECH DOC SIZE:",
            len(documentation_ai_content)
        )



        # ==================================================
        # 5) Documentation generation
        # ==================================================

        log("INFO", "Création documentation...")


        summaries_by_folder = {}

        for path, file_data in file_summaries.items():

            folder = os.path.dirname(path) or "."

            summaries_by_folder.setdefault(folder, {})[path] = file_data



        folder_descriptions = {}
        folder_imports = {}


        for folder, files in summaries_by_folder.items():

            total_classes = sum(
                len(f["structure"].get("classes", []))
                for f in files.values()
            )

            total_functions = sum(
                len(f["structure"].get("functions", []))
                for f in files.values()
            )


            parts = [
                f"{len(files)} fichier(s)"
            ]


            if total_classes:
                parts.append(
                    f"{total_classes} classe(s)"
                )


            if total_functions:
                parts.append(
                    f"{total_functions} fonction(s)"
                )


            folder_descriptions[folder] = (
                ", ".join(parts) + "."
            )


            imports = set()

            for f in files.values():

                imports.update(
                    f["structure"].get(
                        "imports",
                        []
                    )
                )
                print("FINAL IMPORTS =", imports)


            folder_imports[folder] = imports



        output_dir = os.path.join(
            "generated_docs",
            project_name
        )


        builder = DocBuilder(
            project_name,
            output_dir,
            min_lines_for_page=MIN_FILE_LINES
        )



        # ==================================================
        # Mermaid diagrams
        # ==================================================

        tree_structure = filter_tree_structure(
            structure
        )


        mermaid_code = generate_mermaid_diagram(
            tree_structure,
            project_name
        )


        diagrams = {

            "architecture":
                generate_architecture_layers_diagram(
                    structure,
                    files=file_list,
                    detection=architecture_result
                ),


            "dataflow":
                generate_dataflow_diagram(
                    structure,
                    files=file_list,
                    technologies=tech_stack,
                    detection=architecture_result
                ),


            "module_dependency":
                generate_module_dependency_diagram(
                    folder_imports
                ),


            "project_tree":
                mermaid_code
        }




        # ==================================================
        # README
        # ==================================================

        readme_content = builder.build_readme(

            intro=
            f"Documentation automatique du projet {project_name}.",

            metadata=metadata,

            structure=None,

            architecture_explanation=
            architecture_explanation,

            code_overview=None,

            readme_body=
            readme_ai_content
        )



        technical_documentation_content = (
            documentation_ai_content
            or
            _build_technical_documentation_content(
                project_name=project_name,
                ai_summary=ai_summary,
                architecture_explanation=
                    architecture_explanation,
                tech_stack=tech_stack,
                dependencies=dependencies,
                entry_points=entry_points,
                structure=structure,
                file_summaries=file_summaries
            )
        )



        documentation_content = (
            builder.build_documentation_page(

                ai_summary=ai_summary,

                files=file_summaries,

                architecture=
                    architecture_explanation,

                diagrams=diagrams,

                technical_content=
                    technical_documentation_content
            )
        )



        print(
            "README SIZE:",
            len(readme_content)
        )

        print(
            "DOC SIZE:",
            len(documentation_content)
        )



        # ==================================================
        # MkDocs pages
        # ==================================================

        builder.build_index_page(
            intro=
            f"Documentation technique générée automatiquement pour {project_name}.",
            metadata=metadata
        )



        builder.build_architecture_page(
            architecture_result
        )



        builder.build_detection_page(
            architecture_result,
            ai_summary
        )



        # Comparaison architecture

        comparison_markdown = (
            build_comparison_markdown(
                architecture
            )
        )


        builder.build_comparison_page(
            comparison_markdown
        )



        # Diagrammes

        builder.build_diagram_page(
            diagrams
        )



        # ==================================================
        # Modules pages
        # ==================================================

        nav_entries = [

            (
                "Documentation technique",
                "documentation.md"
            ),

            (
                "Architecture",
                "architecture.md"
            ),

            (
                "Diagramme de structure",
                "diagramme.md"
            ),

            (
                "Comparaison architectures",
                "comparaison.md"
            ),

            (
                "Détection & recommandations",
                "detection.md"
            )

        ]



        for folder in sorted(
            summaries_by_folder.keys()
        ):


            page = builder.build_folder_page(

                folder,

                folder_descriptions.get(
                    folder,
                    ""
                ),

                summaries_by_folder[folder]
            )


            if page:

                nav_entries.append(

                    (
                        "Racine"
                        if folder == "."
                        else folder,

                        page
                    )
                )



        # ==================================================
        # MkDocs config
        # ==================================================

        remotes = metadata.get(
            "remotes",
            []
        )


        builder.build_mkdocs_yml(

            nav_entries,

            repo_url=
            remotes[0]
            if remotes
            else None

        )



        # ==================================================
        # Build HTML
        # ==================================================

        site_path= None


        try:

            subprocess.run(

                [
                    "mkdocs",
                    "build"
                ],

                cwd=output_dir,

                check=True,

                capture_output=True,

                text=True,

                timeout=120
            )


            site_path = os.path.join(
                output_dir,
                "site",
            )


            log(
                "INFO",
                f"Site HTML généré : {site_path }"
            )


        except FileNotFoundError:

            log(
                "ERROR",
                "MkDocs introuvable."
            )


        except subprocess.TimeoutExpired:

            log(
                "ERROR",
                "MkDocs build timeout."
            )


        except subprocess.CalledProcessError as e:

            log(
                "ERROR",
                f"MkDocs erreur : {e.stderr}"
            )



        # ==================================================
        # Final result
        # ==================================================

        return {

            "readme_content":
                readme_content,


            "documentation_content":
                documentation_content,


            "documentation_path":
                os.path.join(
                    output_dir,
                    "docs"
                ),


            "file_path":
                os.path.join(
                    output_dir,
                    "README.md"
                ),


            "site_path":
                 site_path,


            "commit_hash":
                commit_hash,


            "architecture":
                architecture,


            "architecture_score":
                architecture_score,


            "architecture_confidence":
                architecture_confidence,


            "architecture_explanation":
                architecture_explanation,


            "ai_summary":
                ai_summary,


            "structure":
                structure,


            "repository_tree":
                tree_structure,


            "files":
                _build_files_list(
                    file_summaries
                ),


            "project_statistics":
                _build_project_statistics(
                    file_summaries,
                    structure
                ),


            "file_dependencies":
                _build_file_dependencies(
                    file_summaries
                ),


            "blueprints":
                _build_blueprints(
                    file_summaries
                ),


            "files_count":
                len(important_files),


            "directories_count":
                _count_directories(
                    structure
                ),


            "technologies":
                tech_stack,


            "entry_points":
                entry_points,


            "dependencies":
                dependencies,


            "diagrams":
                diagrams,


            "metadata":
                metadata


        }
   
    except Exception as e:
        traceback.print_exc()


        log(
            "ERROR",
            str(e)
        )


        raise DocumentationPipelineError(
            str(e)
        )