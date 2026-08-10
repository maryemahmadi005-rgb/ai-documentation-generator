"""
doc_builder.py
---------------

Responsible for generating documentation files:

- README.md
- MkDocs pages
- Architecture pages
- Mermaid diagrams
- Pages module (groupées par dossier, avec vue d'ensemble
  classes / fonctions / dépendances / API)
"""

import os
import re

try:
    import yaml
except ImportError:
    yaml = None


# Lignes de type "Fichier source. Nombre de lignes : ..." générées par
# le résumé heuristique de secours : bruit répétitif à retirer avant
# affichage dans la doc finale.
_BOILERPLATE_PATTERNS = [
    re.compile(r'^\s*Fichier source.*$', re.IGNORECASE | re.MULTILINE),
    re.compile(r'^\s*Nombre de lignes\s*:.*$', re.IGNORECASE | re.MULTILINE),
]


class DocBuilder:


    def __init__(
        self,
        project_name: str,
        output_dir: str,
        min_lines_for_page: int = 10,
    ):

        self.project_name = project_name

        self.output_dir = os.path.abspath(
            output_dir
        )

        self.docs_dir = os.path.join(
            self.output_dir,
            "docs"
        )

        self.min_lines_for_page = min_lines_for_page

        os.makedirs(
            self.docs_dir,
            exist_ok=True
        )



    # ======================================================
    # README generation
    # ======================================================

    def build_readme(
            self,
            intro: str,
            metadata: dict,
            structure: dict,
            folder_summaries: dict = None,
            architecture_explanation: str = None,
            diagrams: dict = None,
            code_overview: str = "",
            readme_body: str = None,
            ):

        if readme_body:
            forbidden_sections = [
                "## Architecture",
                "## Flux de données",
                "## Analyse détaillée des fichiers",
                "## Recommandations",
                "## Modules principaux"
                ]
            if any(section in readme_body for section in forbidden_sections):
                print("README AI returned technical doc, fallback used")
                body = intro
            else:
                body = readme_body.strip()
        else:
            body = intro or "Documentation générée automatiquement."
        lines = [
            f"# {self.project_name}",
            "",
            body,
            "",
            ]
        content = "\n".join(lines)
        path = os.path.join(
            self.output_dir,
            "README.md"
            )
        self._write_file(
            path,
            content
            )
        return content

    def build_documentation_page(
            self,
            ai_summary,
            files,
            architecture,
            diagrams,
            technical_content=None,
    ):
        if technical_content:
            content = technical_content
        else:
            content = self._build_default_documentation_page(
                ai_summary,
                files,
                architecture,
                diagrams,
            )

        self._write_file(
            os.path.join(
                self.docs_dir,
                "documentation.md"
                ),
                content
            )
        return content

    def _build_default_documentation_page(
        self,
        ai_summary,
        files,
        architecture,
        diagrams
        ):
        if not isinstance(files, dict):
            files = {}

        
    

        content = [
            "# Documentation technique",
            "",
            ai_summary or "Documentation technique générée automatiquement.",
            "",
            "## Architecture",
            "",
            architecture or "Architecture non déterminée.",
            "",
            "## Analyse des fichiers",
            ""
        ]
        for filename, info in files.items():
            content.append(
                f"### {filename}"
            )

            content.append("")
            content.append(
                info.get("summary", "Pas de résumé")
            )
            content.append("")

        return "\n".join(content)
        
    




    # ======================================================
    # Tree renderer compatible JSON tree
    # ======================================================
    def render_tree(self, node, prefix=""):
        lines = []
        
        if not isinstance(node, dict):
            return ""
        
        # files
        
        files = sorted(node.get("files", []))
        dirs = sorted(node.get("dirs", {}).items())
        for index, file in enumerate(files):
            
            last = index == len(files)-1
            connector = "└── " if last else "├── "
            
            lines.append(
            prefix + connector + file
            )

        for index, (folder, child) in enumerate(dirs):
            last = index == len(dirs)-1

            connector = "└── " if last else "├── "

            lines.append(
                prefix + connector + folder + "/"
                )
            
            new_prefix = (
                prefix + "    "
                if last
                else prefix + "│   "
                )
            
            lines.append(
                self.render_tree(
                    child,
                    new_prefix
                    )
                )


        return "\n".join(
            x for x in lines if x
            )




    # ======================================================
    # MkDocs index
    # ======================================================

    def build_index_page(
        self,
        intro: str,
        metadata: dict
    ):


        content = [

            f"# {self.project_name}",

            "",

            intro or "Documentation technique du projet.",

            ""

        ]



        if metadata.get("is_git_repo"):


            content += [

                "!!! info Git Repository",

                "",

                f"- Branch : `{metadata.get('branch','N/A')}`",

                f"- Commit : `{metadata.get('last_commit_hash','N/A')}`",

                ""

            ]



        self._write_file(

            os.path.join(
                self.docs_dir,
                "index.md"
            ),

            "\n".join(content)

        )





    # ======================================================
    # Architecture page
    # ======================================================

    def build_architecture_page(
        self,
        architecture: dict
    ):


        content = [

            "# Analyse Architecture",

            "",

            f"Architecture détectée : **{architecture.get('type')}**",

            "",

            f"Confiance : {architecture.get('confidence_pct')}%",

            "",

            "## Signaux",

            ""

        ]



        for signal in architecture.get(
            "signals",
            []
        ):

            content.append(
                f"- {signal}"
            )



        self._write_file(

            os.path.join(
                self.docs_dir,
                "architecture.md"
            ),

            "\n".join(content)

        )





    # ======================================================
    # Detection page
    # ======================================================

    def build_detection_page(
        self,
        detection: dict,
        ai_analysis: str = None
    ):


        lines = [

            "# Détection automatique",

            "",

            f"Architecture : **{detection.get('type')}**",

            "",

            f"Confiance : {detection.get('confidence_pct')}%",

            "",

            "## Classement",

            "",

            "| Architecture | Score | Confiance |",

            "|---|---|---|"

        ]



        for item in detection.get(
            "full_ranking",
            []
        ):


            lines.append(

                f"| {item['type']} | "
                f"{item['raw_score']} | "
                f"{item['confidence_pct']}% |"

            )



        if ai_analysis:


            lines += [

                "",

                "## Analyse IA",

                "",

                ai_analysis

            ]



        self._write_file(

            os.path.join(
                self.docs_dir,
                "detection.md"
            ),

            "\n".join(lines)

        )





    # ======================================================
    # Mermaid diagram
    # ======================================================

    def build_diagram_page(
        self,
        diagrams: dict
    ):


        lines = [
            "# Diagrammes du projet",
            ""
            ]
        titles = {
            "architecture": "Architecture",
            "dataflow": "Flux de données",
            "module_dependency": "Dépendances des modules",
            "project_tree": "Arborescence du projet",
            }
        for key, title in titles.items():
            code = diagrams.get(key)
            if not code:
                continue
            lines += [
                f"## {title}",
                "",
                "```mermaid",
                code,
                "```",
                ""
                ]
        self._write_file(
            os.path.join(self.docs_dir, "diagramme.md"),
            "\n".join(lines)
            )




    # ======================================================
    # MkDocs config
    # ======================================================

    def build_mkdocs_yml(
        self,
        nav_entries,
        repo_url=None
    ):


        config = {
            "site_name":
            self.project_name,
            
            "docs_dir":
            "docs",
            
            "theme": {
                "name": "material"
                },
            
            "markdown_extensions": [
                "tables",
                "admonition",
                "toc",
                "pymdownx.superfences"
            ],
            
            "nav": [
                {
                    title: page
                }
                for title, page in nav_entries
            ]

        }



        if repo_url:


            config["repo_url"] = repo_url



        content = yaml.dump(

            config,

            allow_unicode=True,

            sort_keys=False

        ) if yaml else str(config)



        self._write_file(

            os.path.join(
                self.output_dir,
                "mkdocs.yml"
            ),

            content

        )
    # ======================================================
    # Architecture comparison page
    # ======================================================

    def build_comparison_page(
        self,
        comparison_markdown: str
    ):

        self._write_file(

            os.path.join(
                self.docs_dir,
                "comparaison.md"
            ),

            comparison_markdown

        )



    # ======================================================
    # Summary cleanup (strip repetitive boilerplate lines)
    # ======================================================

    def _clean_summary_text(self, text):

        if not text:
            return ""

        cleaned = text

        for pattern in _BOILERPLATE_PATTERNS:
            cleaned = pattern.sub("", cleaned)

        lines = [line.rstrip() for line in cleaned.splitlines()]
        lines = [line for line in lines if line.strip()]

        return "\n".join(lines).strip()



    # ======================================================
    # Module documentation page (grouped by folder)
    # ======================================================
    #
    # `files` is a dict: filename -> {
    #     "summary": str,
    #     "line_count": int,
    #     "structure": {
    #         "classes": [...], "functions": [...],
    #         "imports": [...], "api_endpoints": [...]
    #     }
    # }
    #
    # Tiny/empty files are skipped so a module page never turns into
    # a wall of near-empty file entries.

    def build_folder_page(
        self,
        folder_name,
        description,
        files
    ):

        relevant_files = {
            fname: info
            for fname, info in files.items()
            if info.get("line_count", 0) >= self.min_lines_for_page
            and (info.get("summary") or "").strip()
        }

        if not relevant_files:
            return None

        safe_name = (
            folder_name
            .replace("/", "_")
            .replace("\\", "_")
        )

        if safe_name in (".", ""):
            safe_name = "root"

        filename = f"{safe_name}.md"

        display_name = (
            "Racine du projet" if folder_name == "." else folder_name
        )

        all_classes, all_functions = set(), set()
        all_deps, all_api = set(), set()

        for info in relevant_files.values():
            structure = info.get("structure", {})
            all_classes.update(structure.get("classes", []))
            all_functions.update(structure.get("functions", []))
            all_deps.update(structure.get("imports", []))
            all_api.update(structure.get("api_endpoints", []))

        content = [
            f"# Module : {display_name}",
            "",
            description or (
                f"Ce module regroupe {len(relevant_files)} fichier(s) source."
            ),
            "",
        ]

        if all_classes or all_functions or all_deps or all_api:

            content += ["## Vue d'ensemble", ""]

            if all_classes:
                content.append(
                    f"- **Classes principales** : "
                    f"{', '.join(sorted(all_classes)[:12])}"
                )

            if all_functions:
                content.append(
                    f"- **Fonctions principales** : "
                    f"{', '.join(sorted(all_functions)[:15])}"
                )

            if all_deps:
                content.append(
                    f"- **Dépendances** : {', '.join(sorted(all_deps)[:12])}"
                )

            if all_api:
                content.append(
                    f"- **Endpoints API** : {', '.join(sorted(all_api)[:10])}"
                )

            content.append("")

        content += ["## Détail des fichiers", ""]

        for fname in sorted(relevant_files.keys()):

            info = relevant_files[fname]
            structure = info.get("structure", {})
            summary = self._clean_summary_text(info.get("summary", ""))

            content.append(f"### `{fname}`")
            content.append("")

            if summary:
                content.append(summary)
                content.append("")

            detail_lines = []

            if structure.get("classes"):
                detail_lines.append(
                    f"**Classes** : {', '.join(structure['classes'])}"
                )

            if structure.get("functions"):
                detail_lines.append(
                    f"**Fonctions** : {', '.join(structure['functions'])}"
                )

            if structure.get("imports"):
                detail_lines.append(
                    f"**Dépendances** : {', '.join(structure['imports'])}"
                )

            if structure.get("api_endpoints"):
                detail_lines.append(
                    f"**API** : {', '.join(structure['api_endpoints'])}"
                )

            content.extend(detail_lines)

            if detail_lines:
                content.append("")

        path = os.path.join(
            self.docs_dir,
            filename
        )

        self._write_file(
            path,
            "\n".join(content)
        )

        return filename





    # ======================================================
    # Save file
    # ======================================================

    def _write_file(
        self,
        path,
        content
    ):


        os.makedirs(

            os.path.dirname(path),

            exist_ok=True

        )



        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:


            file.write(
                content
            )