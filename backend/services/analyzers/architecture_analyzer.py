#!/usr/bin/env python3
"""
architecture_analyzer.py
-------------------------

Analyse automatique de l'architecture d'un projet, et génération des
diagrammes Mermaid associés.

Principe de conception :
- DÉTECTION et RENDU sont strictement séparés. La détection ne
  retourne jamais un diagramme ; le rendu ne recalcule jamais un
  score.
- Chaque architecture a une fonction de règles indépendante qui
  retourne une liste de signaux `(poids, libellé)`. Ajouter ou ajuster
  un signal = modifier une fonction, jamais une chaîne de if/elif
  géante.
- Les signaux sont pondérés : un signal fort (import réel, route
  détectée, app factory...) pèse beaucoup plus qu'un signal faible
  (nom de dossier seul). Certaines architectures (Flask notamment)
  exigent un score minimum de signaux FORTS avant d'être retenues du
  tout — la simple présence de `templates/`/`static/` ne suffit plus.
- Rien ne plante : structure vide, fichiers manquants, IA
  indisponible → fallback sûr à chaque étage.

Fonctions publiques (signatures conservées pour compatibilité) :
- detect_architecture(structure, files=None)
- analyze_with_ai(client, project_name, detection, structure_overview)
- generate_mermaid_diagram(structure, project_name)
- generate_architecture_layers_diagram(structure, files=None, detection=None)
- generate_dataflow_diagram(structure, files=None, technologies=None, detection=None)
- generate_module_dependency_diagram(files, max_nodes=15)
- build_comparison_markdown(detected_architecture)

`files` (optionnel, partout où c'est accepté) est la liste plate déjà
produite par documentation_service.py (`_build_files_list`) :
    [{"path": ..., "classes": [...], "functions": [...],
      "imports": [...], "api_endpoints": [...], ...}, ...]

Si `files` n'est pas fourni, tout fonctionne quand même (dégradé sur
la structure seule) — voir note de compatibilité en fin de fichier.
"""

import os
import re
from collections import OrderedDict


# ==========================================================
# 1) Construction du contexte d'analyse (une seule fois)
# ==========================================================

DB_IMPORT_HINTS = {
    "sqlalchemy", "pymongo", "psycopg2", "mysql", "mysqlclient",
    "sqlite3", "asyncpg", "motor", "redis", "cassandra",
    "mongoengine", "peewee",
}

DB_FILE_HINTS = ("database", "db.py", "migrations", ".sql", "orm")


def _collect_directories(structure):
    directories = set()

    def walk(node):
        if not isinstance(node, dict):
            return
        for folder, child in node.get("dirs", {}).items():
            directories.add(folder.lower())
            walk(child)

    walk(structure)
    return directories


def _collect_files(structure):
    all_files = []

    def walk(node):
        if not isinstance(node, dict):
            return
        for file in node.get("files", []):
            all_files.append(file)
        for folder, child in node.get("dirs", {}).items():
            walk(child)

    walk(structure)
    return all_files


def _build_context(structure, files=None):
    """
    Construit une seule fois toutes les informations dont les règles
    de détection et les générateurs de diagrammes ont besoin :
    dossiers, fichiers, imports, endpoints API, classes, fonctions.

    `files` est optionnel : sans lui, la détection se base uniquement
    sur les noms de dossiers/fichiers (dégradé mais fonctionnel).
    """
    print("🔥 ENTER BUILD CONTEXT")
    structure = structure or {}

    directories = _collect_directories(structure)
    all_files_raw = _collect_files(structure)
    all_files = [f.lower() for f in all_files_raw]
    root_files = {f.lower() for f in structure.get("files", [])}

    imports = set()
    api_endpoints = []
    classes = []
    functions = []

    for f in (files or []):
        imports.update(str(i).lower() for i in (f.get("imports") or []))
        print("FINAL IMPORTS =", imports)
        api_endpoints.extend(f.get("api_endpoints") or [])
        classes.extend(f.get("classes") or [])
        functions.extend(f.get("functions") or [])

    has_database_signal = (
        bool(imports & DB_IMPORT_HINTS)
        or any(any(hint in f for hint in DB_FILE_HINTS) for f in all_files)
        or "migrations" in directories
    )

    return {
        "directories": directories,
        "all_files": all_files,
        "root_files": root_files,
        "imports": imports,
        "api_endpoints": api_endpoints,
        "classes": classes,
        "functions": functions,
        "has_file_level_data": bool(files),
        "has_database_signal": has_database_signal,
    }


# ==========================================================
# 2) Règles de détection par architecture
# ==========================================================
#
# Chaque règle retourne une liste de (poids, libellé) ; les signaux forts
# (>=5) doivent être appuyés par plusieurs preuves visibles dans le
# dépôt pour éviter les faux positifs basés sur un seul indice faible.


def _has_any_path(ctx, fragments):
    for fragment in fragments:
        if any(fragment in f for f in ctx["all_files"]):
            return True
    return False


def _rules_flask(ctx):
    signals = []

    if "flask" in ctx["imports"]:
        signals.append((8, "Import Flask détecté dans le code (`import flask` / `from flask import ...`)"))

    if ctx["api_endpoints"]:
        signals.append((7, f"{len(ctx['api_endpoints'])} route(s) Flask/Blueprint détectée(s) (@app.route, @blueprint.route...)"))

    if "create_app" in [str(fn).lower() for fn in ctx["functions"]]:
        signals.append((6, "App factory pattern détecté (fonction `create_app()`)"))

    if any(f in ctx["root_files"] for f in ("app.py", "wsgi.py", "run.py")):
        signals.append((3, "Point d'entrée probable détecté à la racine (app.py/wsgi.py/run.py)"))

    if "templates" in ctx["directories"]:
        signals.append((2, "Dossier templates/ détecté"))
    if "static" in ctx["directories"]:
        signals.append((2, "Dossier static/ détecté"))

    if any(name in ctx["root_files"] for name in ("requirements.txt", "pyproject.toml")):
        signals.append((1, "Manifestes Python détectés"))

    strong_score = sum(w for w, _ in signals if w >= 5)
    if strong_score < 8:
        return []
    return signals


def _rules_django(ctx):
    signals = []
    if "django" in ctx["imports"]:
        signals.append((8, "Import Django détecté"))
    if any(name in ctx["root_files"] for name in ("manage.py", "settings.py", "urls.py")):
        signals.append((5, "Fichiers Django typiques présents"))
    if any(folder in ctx["directories"] for folder in ("templates", "static")):
        signals.append((3, "Structure Django web typique détectée"))
    if any(name in ctx["root_files"] for name in ("requirements.txt", "pyproject.toml")):
        signals.append((2, "Manifestes Python détectés"))
    if strong_score := sum(w for w, _ in signals if w >= 5):
        if strong_score < 8:
            return []
    return signals


def _rules_fastapi(ctx):
    signals = []
    if "fastapi" in ctx["imports"]:
        signals.append((8, "Import FastAPI détecté"))
    if any(path.endswith("router.py") or "/routers/" in path for path in ctx["all_files"]):
        signals.append((4, "Structure de routeurs FastAPI détectée"))
    if ctx["api_endpoints"]:
        signals.append((5, f"{len(ctx['api_endpoints'])} endpoint(s) détecté(s)"))
    if any(name in ctx["root_files"] for name in ("requirements.txt", "pyproject.toml")):
        signals.append((2, "Manifestes Python détectés"))
    strong_score = sum(w for w, _ in signals if w >= 5)
    if strong_score < 8:
        return []
    return signals


def _rules_nextjs(ctx):
    signals = []
    if any(name in ctx["root_files"] for name in ("next.config.js", "next.config.mjs", "next.config.ts")):
        signals.append((8, "Configuration Next.js détectée"))
    if "package.json" in ctx["root_files"]:
        signals.append(
            (2, "package.json détecté")
        )

    if any(
        "next/" in imp or imp == "next"
        for imp in ctx["imports"]
    ):
        signals.append(
            (6, "Imports Next.js détectés")
        )
    if any(path.startswith("app/") or path.startswith("pages/") for path in ctx["all_files"]):
        signals.append((6, "Structure Next.js app/ ou pages/ détectée"))
    if any(name in ctx["all_files"] for name in ("app/layout.tsx", "app/layout.jsx", "app/page.tsx", "app/page.jsx", "pages/index.tsx", "pages/index.jsx")):
        signals.append((6, "Fichier de page/layout Next.js détecté"))
    if "next" in ctx["imports"]:
        signals.append((7, "Dépendance Next.js détectée dans les imports"))
    strong_score = sum(w for w, _ in signals if w >= 5)
    if strong_score < 8:
        return []
    return signals


def _rules_react_spa(ctx):
    signals = []
    if "react" in ctx["imports"]:
        signals.append((7, "Import React détecté"))
    if any(name in ctx["root_files"] for name in ("vite.config.js", "vite.config.ts", "vite.config.mjs", "package.json")):
        signals.append((4, "Configuration de build front-end détectée"))
    if any(name in ctx["all_files"] for name in ("src/main.jsx", "src/main.tsx", "src/app.jsx", "src/app.tsx", "src/index.jsx", "src/index.tsx")):
        signals.append((6, "Point d'entrée React SPA détecté"))
    if "src" in ctx["directories"]:
        signals.append((3, "Dossier src/ détecté"))
    if any(
        path.endswith((".tsx", ".jsx"))
        for path in ctx["all_files"]
    ):
        signals.append(
            (2, "Composants React détectés")
        )
    strong_score = sum(w for w, _ in signals if w >= 5)
    if strong_score < 8:
        return []
    return signals


def _rules_vue(ctx):
    signals = []
    if "vue" in ctx["imports"] or any(name.endswith(".vue") for name in ctx["all_files"]):
        signals.append((8, "Composants Vue.js détectés"))
    if any(name in ctx["root_files"] for name in ("vite.config.js", "vite.config.ts", "package.json")):
        signals.append((4, "Configuration de build front-end détectée"))
    if any(path.startswith("src/") for path in ctx["all_files"]):
        signals.append((3, "Structure src/ détectée"))
    strong_score = sum(w for w, _ in signals if w >= 5)
    if strong_score < 8:
        return []
    return signals


def _rules_angular(ctx):
    signals = []
    if "@angular" in ctx["imports"] or any(name.endswith(".component.ts") for name in ctx["all_files"]):
        signals.append((8, "Imports Angular ou composants Angular détectés"))
    if any(name in ctx["root_files"] for name in ("angular.json", "tsconfig.json", "package.json")):
        signals.append((4, "Configuration Angular/TypeScript détectée"))
    strong_score = sum(w for w, _ in signals if w >= 5)
    if strong_score < 8:
        return []
    return signals


def _rules_documentation_platform(ctx):
    signals = []
    doc_dirs = {d for d in ctx["directories"] if d in {"docs", "doc", "documentation"}}
    if doc_dirs:
        signals.append((6, "Dossier(s) de documentation détecté(s)"))
    if any(name.endswith((".md", ".mdx")) for name in ctx["all_files"]):
        signals.append((5, "Fichiers Markdown/MDX détectés"))
    if any(name in ctx["root_files"] for name in ("mkdocs.yml", "mint.json", "mintlify.json", "docusaurus.config.js", "docusaurus.config.ts")):
        signals.append((7, "Configuration de plateforme de documentation détectée"))
    if any(name in ctx["all_files"] for name in ("openapi.yaml", "openapi.json", "asyncapi.yaml", "asyncapi.json")):
        signals.append((3, "Spécifications OpenAPI/AsyncAPI détectées"))
    if any(name.endswith((".md", ".mdx")) and "docs" in name.lower() for name in ctx["all_files"]):
        signals.append((3, "Contenus de documentation dans un dossier docs/"))
    if any(name in ctx["all_files"] for name in ("src/components/Docs.tsx", "src/components/DocPage.tsx", "src/pages/docs.tsx")):
        signals.append((4, "Composants React orientés documentation détectés"))
    if "snippets" in ctx["directories"]:
        signals.append(
            (4, "Dossier snippets/ détecté (documentation components)")
        )

    if any(name.endswith(".mdx") for name in ctx["all_files"]):
        signals.append(
            (4, "Pages MDX détectées")
        )

    if any("openapi" in name for name in ctx["all_files"]):
        signals.append(
            (3, "Fichiers OpenAPI détectés")
        )
        # Mintlify-specific structure
    if "agent" in ctx["directories"]:
        signals.append(
            (3, "Dossier agent/ détecté")
        )

    if "agent-context" in ctx["directories"]:
        signals.append(
            (3, "Dossier agent-context/ détecté")
        )

    if any(
        "mintlify" in file.lower()
        for file in ctx["all_files"]
    ):
        signals.append(
            (5, "Fichiers Mintlify détectés")
        )

    total_score = sum(w for w, _ in signals)

    if total_score < 10:
        return []
    return signals


def _rules_rest_api(ctx):
    signals = []
    if ctx["api_endpoints"]:
        weight = min(8, 2 + len(ctx["api_endpoints"]))
        signals.append((weight, f"{len(ctx['api_endpoints'])} endpoint(s) API détecté(s) dans le code"))
    if {"routes", "controllers", "middleware"} & ctx["directories"]:
        signals.append((4, "Dossiers routes/controllers/middleware détectés"))
    if any("route" in f for f in ctx["all_files"]):
        signals.append((3, "Fichier(s) *route(s)* détecté(s)"))
    if any(name in ctx["all_files"] for name in ("openapi.yaml", "openapi.json", "swagger.json")):
        signals.append((4, "Spécification OpenAPI/Swagger détectée"))
    strong_score = sum(w for w, _ in signals if w >= 5)
    if strong_score < 8:
        return []
    return signals


def _rules_graphql_api(ctx):
    signals = []
    has_schema = any(name in ctx["all_files"] for name in ("schema.graphql", "schema.gql"))
    has_resolver = any("resolver" in f for f in ctx["all_files"]) or any("resolver" in imp for imp in ctx["imports"])
    has_graphql_dep = any("graphql" in imp for imp in ctx["imports"]) or any("apollo" in imp for imp in ctx["imports"])
    has_graphql_endpoint = any("graphql" in f for f in ctx["all_files"]) or any("/graphql" in str(ep) for ep in ctx["api_endpoints"])

    if has_schema:
        signals.append((10, "Schéma GraphQL détecté"))
    if has_resolver:
        signals.append((8, "Resolvers GraphQL détectés"))
    if has_graphql_dep:
        signals.append((7, "Dépendances GraphQL/Apollo détectées"))
    if has_graphql_endpoint:
        signals.append((6, "Endpoint GraphQL détecté"))

    strong_score = sum(w for w, _ in signals if w >= 5)
    if strong_score < 10:
        return []
    return signals


def _rules_monolithic(ctx):
    signals = []
    directory_count = len(ctx["directories"])
    if directory_count <= 3:
        signals.append((5, "Structure centralisée et peu de dossiers spécialisés détectée"))
    if not ctx["has_file_level_data"]:
        signals.append((2, "Aucune donnée de fichiers détaillées disponible"))
    if not ctx["api_endpoints"] and not ctx["imports"]:
        signals.append((2, "Peu d'indices d'architecture distribuée ou orientée API"))
    strong_score = sum(w for w, _ in signals if w >= 5)
    if strong_score < 5:
        return []
    return signals


def _rules_layered(ctx):
    signals = []
    trio = {"controllers", "services", "repositories"} & ctx["directories"]
    if len(trio) == 3:
        signals.append((8, "Dossiers controllers/, services/ et repositories/ tous présents"))
    elif len(trio) == 2:
        signals.append((5, f"{len(trio)} des 3 couches détectées ({', '.join(sorted(trio))})"))
    if any("service" in f for f in ctx["all_files"]):
        signals.append((3, "Fichiers de service détectés"))
    if any("repository" in f for f in ctx["all_files"]):
        signals.append((3, "Fichiers repository détectés"))
    strong_score = sum(w for w, _ in signals if w >= 5)
    if strong_score < 5:
        return []
    return signals


def _rules_mvc(ctx):
    signals = []
    trio = {"models", "views", "controllers"} & ctx["directories"]
    if len(trio) == 3:
        signals.append((8, "Dossiers models/, views/ et controllers/ tous présents"))
    elif len(trio) == 2:
        signals.append((5, f"{len(trio)} des 3 dossiers MVC détectés ({', '.join(sorted(trio))})"))
    if any("controller" in f for f in ctx["all_files"]):
        signals.append((3, "Fichier(s) *controller* détecté(s)"))
    if any("model" in f for f in ctx["all_files"]):
        signals.append((2, "Fichier(s) *model* détecté(s)"))
    strong_score = sum(w for w, _ in signals if w >= 5)
    if strong_score < 8:
        return []
    return signals


def _rules_clean(ctx):
    signals = []
    trio = {"domain", "application", "infrastructure"} & ctx["directories"]
    if len(trio) == 3:
        signals.append((8, "Dossiers domain/, application/ et infrastructure/ tous présents"))
    elif len(trio) == 2:
        signals.append((5, f"{len(trio)} des 3 couches Clean Architecture détectées"))
    if any("entity" in f for f in ctx["all_files"]):
        signals.append((3, "Fichier(s) *entity* détecté(s)"))
    if any("usecase" in f for f in ctx["all_files"]):
        signals.append((3, "Fichier(s) *usecase* détecté(s)"))
    strong_score = sum(w for w, _ in signals if w >= 5)
    if strong_score < 8:
        return []
    return signals


def _rules_hexagonal(ctx):
    signals = []
    trio = {"domain", "ports", "adapters"} & ctx["directories"]
    if len(trio) == 3:
        signals.append((8, "Dossiers domain/, ports/ et adapters/ tous présents"))
    elif len(trio) == 2:
        signals.append((5, f"{len(trio)} des 3 dossiers Hexagonal détectés"))
    if any("port" in f for f in ctx["all_files"]):
        signals.append((2, "Fichier(s) *port* détecté(s)"))
    if any("adapter" in f for f in ctx["all_files"]):
        signals.append((3, "Fichier(s) *adapter* détecté(s)"))
    strong_score = sum(w for w, _ in signals if w >= 5)
    if strong_score < 8:
        return []
    return signals


def _rules_microservices(ctx):
    signals = []
    if "docker-compose.yml" in ctx["root_files"] or "docker-compose.yaml" in ctx["root_files"]:
        signals.append((6, "docker-compose détecté (orchestration multi-services)"))
    service_like_dirs = {d for d in ctx["directories"] if "service" in d or d.startswith("app_")}
    if len(service_like_dirs) >= 3:
        signals.append((6, f"{len(service_like_dirs)} dossiers de services indépendants détectés"))
    if {"kubernetes", "k8s"} & ctx["directories"]:
        signals.append((4, "Manifests Kubernetes détectés"))
    strong_score = sum(w for w, _ in signals if w >= 5)
    if strong_score < 6:
        return []
    return signals
def _rules_sveltekit(ctx):
    signals = []

    if any(
        "svelte" in imp
        for imp in ctx["imports"]
    ):
        signals.append(
            (8, "Imports Svelte détectés")
        )

    if any(
        f.startswith("src/routes")
        for f in ctx["all_files"]
    ):
        signals.append(
            (7, "Structure SvelteKit src/routes détectée")
        )

    if any(
        name in ctx["root_files"]
        for name in (
            "svelte.config.js",
            "svelte.config.ts"
        )
    ):
        signals.append(
            (8, "Configuration SvelteKit détectée")
        )

    if "package.json" in ctx["root_files"]:
        signals.append(
            (2, "Projet Node.js détecté")
        )


    strong_score = sum(
        w for w, _ in signals if w >= 5
    )

    if strong_score < 8:
        return []

    return signals


ARCHITECTURE_RULES = OrderedDict([
    ("Flask Application", _rules_flask),
    ("Django", _rules_django),
    ("FastAPI", _rules_fastapi),
    ("Next.js Application", _rules_nextjs),
    ("React SPA", _rules_react_spa),
    ("Vue", _rules_vue),
    ("SvelteKit Application", _rules_sveltekit),
    ("Angular", _rules_angular),
    ("Documentation Platform", _rules_documentation_platform),
    ("REST API", _rules_rest_api),
    ("GraphQL API", _rules_graphql_api),
    ("Monolithic", _rules_monolithic),
    ("Layered Architecture", _rules_layered),
    ("MVC", _rules_mvc),
    ("Hexagonal Architecture", _rules_hexagonal),
    ("Microservices", _rules_microservices),
])

ARCHITECTURE_MAX_SCORE = {
    "Flask Application": 24,
    "Django": 20,
    "FastAPI": 20,
    "Next.js Application": 24,
    "React SPA": 20,
    "Vue": 20,
    "Angular": 20,
    "Documentation Platform": 20,
    "REST API": 22,
    "GraphQL API": 20,
    "SvelteKit Application": 25,
    "Monolithic": 10,
    "Layered Architecture": 14,
    "MVC": 14,
    "Hexagonal Architecture": 15,
    "Microservices": 16,
}


# ==========================================================
# 3) Agrégation / scoring
# ==========================================================

def _score_all(ctx):
    results = []

    for name, rule_fn in ARCHITECTURE_RULES.items():
        signals = rule_fn(ctx)
        if not signals:
            continue

        raw_score = sum(w for w, _ in signals)
        if raw_score <= 0:
            continue

        max_score = ARCHITECTURE_MAX_SCORE.get(name, 20)
        confidence_pct = min(round(raw_score / max_score * 100, 1), 100)

        results.append({
            "type": name,
            "raw_score": raw_score,
            "max_score": max_score,
            "score_out_of_10": round(min(raw_score / max_score, 1) * 10, 1),
            "confidence_pct": confidence_pct,
            "signals": [
                label for _, label in
                sorted(signals, key=lambda s: s[0], reverse=True)
            ][:6],
        })

    results.sort(key=lambda r: r["raw_score"], reverse=True)
    return results


def _monolithic_fallback(ctx):
    """
    Fallback quand aucune architecture n'obtient de score positif.
    La confiance est calculée à partir de la taille réelle du projet
    plutôt que codée en dur à 50% — un projet à 2 dossiers a une
    confiance "Monolithic" plus élevée qu'un projet à 10 dossiers qui
    n'a simplement pas matché de pattern connu.
    """
    directory_count = len(ctx["directories"])

    if directory_count <= 2:
        confidence_pct = 65
        signals = ["Très peu de dossiers distincts détectés : structure centralisée typique d'un monolithe."]
    elif directory_count <= 5:
        confidence_pct = 45
        signals = ["Peu de séparation en dossiers spécialisés détectée."]
    else:
        confidence_pct = 30
        signals = [
            "Le projet a plusieurs dossiers mais aucun pattern architectural "
            "reconnu (MVC, Clean, Hexagonal, Microservices...) n'a été "
            "identifié avec suffisamment de preuves."
        ]

    if not ctx["has_file_level_data"]:
        signals.append(
            "Détection basée uniquement sur la structure de dossiers "
            "(aucune donnée d'imports/fonctions fournie) : la confiance "
            "réelle peut être plus élevée avec une analyse plus poussée."
        )

    return {
        "type": "Monolithic",
        "raw_score": 0,
        "max_score": 0,
        "score_out_of_10": round(confidence_pct / 10, 1),
        "confidence_pct": confidence_pct,
        "signals": signals,
    }


# ==========================================================
# 4) Détection principale (signature conservée)
# ==========================================================

def detect_architecture(structure, files=None):
    """
    `structure` : arbre {"files": [...], "dirs": {...}} (obligatoire).
    `files` (optionnel) : liste plate avec imports/api_endpoints/
        classes/fonctions par fichier — voir _build_files_list() dans
        documentation_service.py. Sans lui, la détection reste
        fonctionnelle mais moins précise (dégradée sur la structure
        seule, jamais d'erreur).
    """
    print("🔥🔥 DETECT CALLED")
    print("STRUCTURE TYPE:", type(structure))
    print("STRUCTURE VALUE:", structure)
    print("FILES COUNT:", len(files or []))
    if not structure or not isinstance(structure, dict):
        return {
            "type": "Unknown",
            "confidence": "low",
            "confidence_pct": 0,
            "score_out_of_10": 0,
            "signals": [],
            "full_ranking": [],
            "ambiguous_with": None,
        }

    try:
        ctx = _build_context(structure, files)
        print("\n===== ARCH CONTEXT =====")
        print("FILES:", ctx["has_file_level_data"])
        print("IMPORTS:", list(ctx["imports"])[:20])
        print("ENDPOINTS:", ctx["api_endpoints"][:10])
        print("FUNCTIONS:", ctx["functions"][:20])
        print("=========================================================================================================================================================================================\n")
        ranking = _score_all(ctx)

        if not ranking:
            ranking = [_monolithic_fallback(ctx)]

        best = ranking[0]
        confidence_pct = best["confidence_pct"]

        ambiguous = None
        if len(ranking) > 1 and (best["raw_score"] - ranking[1]["raw_score"]) <= 2:
            ambiguous = ranking[1]["type"]

        if confidence_pct < 35 or best["raw_score"] < 6:
            best_type = "Unknown Architecture"
            best_confidence = max(0, min(confidence_pct, 35))
            best_signals = [
                "Peu de preuves structurelles ou d’imports suffisantes pour établir une architecture avec confiance."
            ]
            return {
                "type": best_type,
                "confidence": "low",
                "confidence_pct": best_confidence,
                "score_out_of_10": round(best_confidence / 10, 1),
                "signals": best_signals,
                "full_ranking": ranking,
                "ambiguous_with": ambiguous,
            }

        return {
            "type": best["type"],
            "confidence": (
                "high" if confidence_pct >= 70 else
                "medium" if confidence_pct >= 40 else
                "low"
            ),
            "confidence_pct": confidence_pct,
            "score_out_of_10": best.get("score_out_of_10", 0),
            "signals": best["signals"],
            "full_ranking": ranking,
            "ambiguous_with": ambiguous,
        }

    except Exception as e :
        print("🔥 ARCH ERROR:", e)
        import traceback
        traceback.print_exc()
        # Filet de sécurité : ne jamais faire planter le pipeline de
        # documentation à cause de la détection d'architecture.
        return {
            "type": "Unknown",
            "confidence": "low",
            "confidence_pct": 0,
            "score_out_of_10": 0,
            "signals": ["La détection d'architecture a rencontré une erreur inattendue."],
            "full_ranking": [],
            "ambiguous_with": None,
        }


# ==========================================================
# 5) AI analysis (signature conservée)
# ==========================================================

def analyze_with_ai(client, project_name, detection, structure_overview):
    """
    RÈGLE ABSOLUE imposée dans le prompt : ne jamais inventer une
    base de données, un framework, un module ou un outil de
    déploiement qui n'est pas explicitement dans les signaux
    détectés ou la structure fournie. Le fallback (sans IA) applique
    la même règle en ne citant que `detection["signals"]`.
    """
    signals = detection.get("signals", []) or []
    signals_block = "\n".join(f"- {s}" for s in signals) or "- Aucun signal spécifique détecté."
    structure_text = structure_overview[:1000]

    prompt = f"""
Projet : {project_name}

Architecture détectée : {detection.get('type')}
Confiance : {detection.get('confidence_pct')}%

Signaux ayant motivé cette détection :
{signals_block}

Structure (aperçu) :
{structure_text}
Analyse ce projet comme un·e architecte logiciel·le senior.

RÈGLE ABSOLUE : n'utilise QUE les informations fournies ci-dessus.
Si une information n'est pas explicitement listée dans les signaux ou
la structure (base de données, framework, outil de déploiement,
module métier), NE L'INVENTE PAS — écris "non déterminé" ou "aucune
preuve détectée dans le repository" plutôt que de supposer.

Réponds en Markdown avec :

# Points forts

# Points faibles

# Recommandations
"""

    try:
        result = client.generate(prompt)
        if result:
            return result
    except Exception:
        pass

    return f"""# Analyse architecture

## Points forts

- Architecture détectée : **{detection.get('type')}** (confiance {detection.get('confidence_pct')}%)

## Signaux détectés

{signals_block}

## Points faibles

- Analyse IA indisponible : cette section est générée uniquement à
  partir des signaux structurels détectés ci-dessus, sans modèle de
  langage.

## Recommandations

- Maintenir une séparation claire des responsabilités entre modules.
- Vérifier manuellement les points ci-dessus avant de les considérer
  comme définitifs.
"""


# ==========================================================
# 6) Comparaison architecture (signature conservée, inchangée)
# ==========================================================

def build_comparison_markdown(detected_architecture):

    return f"""

# Comparaison des architectures


Architecture détectée :

**{detected_architecture}**


## MVC

Séparation :
Model / View / Controller.


Avantages :

- Organisation claire
- Très utilisée


## Layered Architecture

Séparation :

Controller
Service
Repository


Avantages :

- Bonne maintenabilité
- Facile à tester


## Clean Architecture

Séparation du métier de la technique.


Avantages :

- Très évolutive


"""


# ==========================================================
# 7) Diagrammes Mermaid — utilitaires communs
# ==========================================================

def _sanitize_id(raw):
    """ID Mermaid sûr : alphanumérique/underscore, jamais vide, jamais
    commençant par un chiffre."""
    cleaned = re.sub(r"[^a-zA-Z0-9_]", "_", str(raw)).strip("_")
    if not cleaned:
        cleaned = "node"
    if cleaned[0].isdigit():
        cleaned = f"n_{cleaned}"
    return cleaned[:40]


def _unique_id(base, used_ids):
    node_id = _sanitize_id(base)
    if node_id not in used_ids:
        used_ids.add(node_id)
        return node_id
    counter = 2
    while f"{node_id}_{counter}" in used_ids:
        counter += 1
    unique = f"{node_id}_{counter}"
    used_ids.add(unique)
    return unique


def _node_shape(node_id, label, kind="process"):
    safe_label = str(label).replace('"', "'")[:60]
    if kind == "datastore":
        return f'{node_id}[("{safe_label}")]'
    if kind == "external":
        return f'{node_id}(("{safe_label}"))'
    if kind == "actor":
        return f'{node_id}(["{safe_label}"])'
    return f'{node_id}["{safe_label}"]'


def _render_mermaid(components, edges):
    """
    `components` : liste de (key, label, kind).
    `edges` : liste de (key_source, key_target) référençant les
    `key` des composants ci-dessus (pas les IDs Mermaid finaux).
    """
    used_ids = set()
    id_map = {}
    lines = ["graph TD"]

    for key, label, kind in components:
        node_id = _unique_id(key, used_ids)
        id_map[key] = node_id
        lines.append(_node_shape(node_id, label, kind))

    for source, target in edges:
        if source in id_map and target in id_map:
            lines.append(f"{id_map[source]} --> {id_map[target]}")

    return "\n".join(lines)


_FALLBACK_DIAGRAM_COMPONENTS = [
    ("input", "Input (composants non identifiés)", "actor"),
    ("processing", "Processing", "process"),
    ("output", "Output", "process"),
]
_FALLBACK_DIAGRAM_EDGES = [("input", "processing"), ("processing", "output")]


# ==========================================================
# 8) Diagramme structure (signature conservée, inchangé)
# ==========================================================

def generate_mermaid_diagram(structure, project_name):

    lines = [
        "graph TD",
        f'ROOT["{project_name}"]'
    ]

    def sanitize(name):
        name = str(name)
        name = re.sub(r'[^a-zA-Z0-9_]', '_', name)
        return name[:30]

    def walk(node, parent, depth=0):
        if depth >= 2:
            return
        if not isinstance(node, dict):
            return

        for folder, child in node.get("dirs", {}).items():
            node_id = sanitize(parent + "_" + folder)
            lines.append(f'{node_id}["{folder}/"]')
            lines.append(f"{parent} --> {node_id}")
            walk(child, node_id, depth + 1)

    walk(structure, "ROOT")

    return "\n".join(lines)


# ==========================================================
# 9) NOUVEAU — Diagramme des couches architecturales
# ==========================================================

def _has_presentation_layer(ctx):
    return bool(ctx["directories"] & {"routes", "controllers", "views", "api"}) or bool(ctx["api_endpoints"])


def _has_business_layer(ctx):
    return "services" in ctx["directories"] or any("service" in f for f in ctx["all_files"])


def _has_data_layer(ctx):
    return bool(ctx["directories"] & {"repositories", "repository", "models", "dao"})


def generate_architecture_layers_diagram(structure, files=None, detection=None):
    """
    Diagramme vertical des couches réellement détectées
    (Présentation -> Métier -> Données -> Base de données). Une
    couche n'apparaît QUE si elle a un signal réel — jamais de
    Controller/Service/Repository par défaut.
    """
    try:
        ctx = _build_context(structure or {}, files)

        layer_candidates = [
            ("presentation", "Presentation / Routes", _has_presentation_layer(ctx)),
            ("business", "Business / Service Layer", _has_business_layer(ctx)),
            ("data", "Data / Repository Layer", _has_data_layer(ctx)),
            ("database", "Database", ctx["has_database_signal"]),
        ]

        layers = [(key, label) for key, label, present in layer_candidates if present]

        if not layers:
            return _render_mermaid(
                [("app", "Application (couches non différenciées — preuve insuffisante)", "process")],
                [],
            )

        components = [
            (key, label, "datastore" if key == "database" else "process")
            for key, label in layers
        ]
        edges = [(components[i][0], components[i + 1][0]) for i in range(len(components) - 1)]

        return _render_mermaid(components, edges)

    except Exception:
        return _render_mermaid(
            [("app", "Application", "process")], []
        )


# ==========================================================
# 10) NOUVEAU — Diagramme de flux de données (Data Flow)
# ==========================================================

def _classify_dataflow_category(ctx, technologies=None):
    tech_lower = {str(t).lower() for t in (technologies or [])}
    directories = ctx["directories"]

    has_backend_signal = bool(directories & {"routes", "controllers", "services"}) or bool(ctx["api_endpoints"])
    has_frontend_signal = bool(directories & {"components", "pages", "views"}) or bool(
        tech_lower & {"react", "vue", "angular", "javascript (react)", "typescript (react)"}
    )
    has_docker_compose = "docker-compose.yml" in ctx["root_files"] or "docker-compose.yaml" in ctx["root_files"]
    service_like_dirs = {d for d in directories if "service" in d or d.startswith("app_")}

    if has_docker_compose or len(service_like_dirs) >= 3:
        return "microservices"
    if has_frontend_signal and has_backend_signal:
        return "fullstack"
    if has_frontend_signal:
        return "frontend_spa"
    if has_backend_signal:
        return "web_backend"
    if "setup.py" in ctx["root_files"] or (
        "pyproject.toml" in ctx["root_files"]
        and not ctx["root_files"] & {"app.py", "manage.py", "wsgi.py"}
    ):
        return "library"
    if any(f in ctx["root_files"] for f in ("cli.py", "__main__.py")) or "bin" in directories:
        return "cli"
    if directories & {"android", "ios"} or any("main.dart" in f for f in ctx["all_files"]):
        return "mobile"
    return "unknown"


def _dataflow_components(category, ctx):
    if category == "web_backend":
        candidates = [
            ("user", "User", "actor", True),
            ("request", "Request", "process", True),
            ("routes", "Routes / API", "process", bool(ctx["api_endpoints"]) or "routes" in ctx["directories"]),
            ("controller", "Controller", "process", "controllers" in ctx["directories"]),
            ("service", "Service Layer", "process", "services" in ctx["directories"]),
            ("repository", "Repository", "process", bool(ctx["directories"] & {"repositories", "repository"})),
            ("database", "Database", "datastore", ctx["has_database_signal"]),
            ("response", "Response", "process", True),
        ]
    elif category == "microservices":
        service_names = sorted({d for d in ctx["directories"] if "service" in d or d.startswith("app_")})[:6]
        candidates = [("gateway", "API Gateway", "process", True)]
        candidates += [(f"svc_{n}", n, "process", True) for n in service_names]
        candidates += [("database", "Database", "datastore", ctx["has_database_signal"])]
    elif category == "frontend_spa":
        candidates = [
            ("user", "User", "actor", True),
            ("ui", "UI Components", "process", True),
            ("api_client", "API Client", "process", True),
            ("external_api", "Backend API", "external", True),
        ]
    elif category == "fullstack":
        candidates = [
            ("user", "User", "actor", True),
            ("ui", "Frontend UI", "process", True),
            ("routes", "Routes / API", "process", True),
            ("service", "Service Layer", "process", "services" in ctx["directories"]),
            ("database", "Database", "datastore", ctx["has_database_signal"]),
        ]
    elif category == "library":
        candidates = [
            ("caller", "Calling Code", "actor", True),
            ("public_api", "Public API", "process", True),
            ("core", "Core Logic", "process", True),
        ]
    elif category == "cli":
        candidates = [
            ("user", "User", "actor", True),
            ("cli", "CLI Entry Point", "process", True),
            ("core", "Core Logic", "process", True),
            ("output", "Output", "datastore", True),
        ]
    elif category == "mobile":
        candidates = [
            ("user", "User", "actor", True),
            ("app_ui", "Mobile UI", "process", True),
            ("external_api", "Backend API", "external", True),
        ]
    else:
        return []

    return [(k, l, kind) for k, l, kind, present in candidates if present]


def generate_dataflow_diagram(structure, files=None, technologies=None, detection=None):
    """
    Diagramme de flux de données adapté au type de projet détecté
    (backend web, microservices, frontend, fullstack, librairie, CLI,
    mobile). Jamais de Controller/Service/Repository/Database
    fictifs : chaque nœud correspond à un signal réel. `detection`
    est accepté pour cohérence d'appel mais n'est pas requis (la
    catégorisation se fait indépendamment, sur la structure).
    """
    try:
        ctx = _build_context(structure or {}, files)
        category = _classify_dataflow_category(ctx, technologies)
        components = _dataflow_components(category, ctx)

        if not components:
            components = _FALLBACK_DIAGRAM_COMPONENTS
            edges = _FALLBACK_DIAGRAM_EDGES
        else:
            edges = [(components[i][0], components[i + 1][0]) for i in range(len(components) - 1)]

        return _render_mermaid(components, edges)

    except Exception:
        return _render_mermaid(_FALLBACK_DIAGRAM_COMPONENTS, _FALLBACK_DIAGRAM_EDGES)


# ==========================================================
# 11) NOUVEAU — Diagramme de dépendances entre modules
# ==========================================================

def generate_module_dependency_diagram(files, max_nodes=15):
    """
    Diagramme des dépendances internes entre fichiers/modules, basé
    sur les imports déjà extraits par documentation_service.py
    (`_extract_code_structure` -> `imports`). Heuristique par
    correspondance de noms de module (pas un vrai résolveur
    d'imports) : suffisant pour une vue d'ensemble, pas pour une
    analyse exhaustive.

    Si `files` est vide ou ne contient aucune donnée d'imports
    exploitable, retourne un diagramme d'un seul nœud explicatif —
    ne lève jamais d'exception.
    """
    try:
        files = files or []

        if not files:
            return _render_mermaid(
                [("info", "No file-level import data available", "process")], []
            )

        module_index = {}
        for f in files:
            path = f.get("path", "")
            if not path:
                continue
            module_id = os.path.splitext(path)[0].replace("/", ".").replace("\\", ".")
            module_index[module_id] = f

        edges_set = set()
        nodes_used = set()

        for f in files:
            source_path = f.get("path")
            if not source_path:
                continue
            source_module = os.path.splitext(source_path)[0].replace("/", ".").replace("\\", ".")

            for imp in (f.get("imports") or []):
                imp_lower = str(imp).lower()
                match = next(
                    (
                        mod for mod in module_index
                        if mod != source_module and (
                            imp_lower == mod.lower()
                            or imp_lower.endswith("." + mod.lower().split(".")[-1])
                        )
                    ),
                    None,
                )
                if match:
                    edges_set.add((source_module, match))
                    nodes_used.add(source_module)
                    nodes_used.add(match)

        if not edges_set:
            return _render_mermaid(
                [("info", "No internal module dependency detected from imports", "process")], []
            )

        limited_nodes = list(nodes_used)[:max_nodes]
        limited_edges = [
            (a, b) for a, b in edges_set
            if a in limited_nodes and b in limited_nodes
        ][: max_nodes * 2]

        components = [
            (node, os.path.basename(node.replace(".", "/")) or node, "process")
            for node in limited_nodes
        ]

        return _render_mermaid(components, limited_edges)

    except Exception:
        return _render_mermaid(
            [("info", "Module dependency diagram unavailable", "process")], []
        )


# ==========================================================
# Note de compatibilité — pour tirer pleinement parti des imports/
# endpoints détectés (notamment pour la détection Flask basée sur de
# vraies preuves), documentation_service.py doit passer `files` en
# plus de `structure` :
#
#   detect_architecture(structure, files=_build_files_list(file_summaries))
#
# et `_build_files_list()` doit inclure `imports`/`api_endpoints`
# (actuellement elle ne copie que classes/functions/summary/
# line_count). Sans ce petit ajout, tout fonctionne quand même mais
# en mode dégradé (structure seule) — voir la réponse jointe.
# ========================================================== 