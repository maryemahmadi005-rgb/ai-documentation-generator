"""
ollama_client.py

Client Ollama local.
Avec fallback heuristique si Ollama indisponible.

Optimisations de performance :
- instance CLIENT PARTAGÉE (singleton) : le test de disponibilité
  (is_available) n'est plus refait à chaque fichier, mais une seule
  fois par run.
- circuit breaker : après plusieurs échecs/timeouts consécutifs,
  on arrête d'appeler Ollama pour le reste de l'analyse et on
  bascule automatiquement sur le résumé heuristique.
- timeout par génération réduit et configurable (au lieu de 60s
  fixes, multipliés par le nombre de fichiers).

Protection anti-fuite de contexte / anti-bruit dans le README :
- Le README généré est volontairement limité à un ensemble FIXE de
  sections (Description, Features, Technologies Used, Prerequisites,
  Installation, Usage, Project Structure). Aucune autre section n'est
  autorisée : pas d'arborescence complète, pas d'informations Git
  (branche, commit, auteur, nombre de commits), pas de score/
  confiance d'architecture, pas de mention de génération automatique/
  IA/Ollama/DocGen AI.
- `_contains_leaked_meta_language` détecte le vocabulaire interne de
  l'outil (DocGen AI, pipeline, Ollama...).
- `_contains_forbidden_readme_markers` détecte en plus tout ce qui
  reviendrait à afficher l'arborescence du dépôt, les infos Git, ou
  un score/confiance dans le README (autorisé uniquement dans la doc
  technique).
- Si l'un des deux détecte un problème, on rejette la réponse IA et
  on bascule sur le fallback neutre.
"""
import json
import os
import re
import threading
import requests

from urllib.parse import urlparse
from typing import Optional


OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/generate")
DEFAULT_MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2:3b")

# Timeout par appel de génération. Volontairement réduit par rapport à
# l'ancien timeout de 60s : sur un repo de plusieurs centaines de
# fichiers, un timeout élevé multiplié par le nombre de fichiers est
# l'une des causes principales des temps d'analyse très longs.
GENERATE_TIMEOUT = int(os.environ.get("OLLAMA_GENERATE_TIMEOUT", "80"))
GENERATE_NUM_PREDICT = int(os.environ.get("OLLAMA_NUM_PREDICT", "2000"))
AVAILABILITY_TIMEOUT = 2

# Timeout spécifique à l'analyse globale du projet (prompt plus long,
# une seule fois par run donc on peut se permettre plus de marge que
# pour un résumé de fichier individuel).
PROJECT_ANALYSIS_TIMEOUT = int(
    os.environ.get("OLLAMA_PROJECT_ANALYSIS_TIMEOUT", "600")
)

# Circuit breaker : après N échecs/timeouts consécutifs, on considère
# qu'Ollama est indisponible ou trop lent, et on bascule
# automatiquement et définitivement (pour ce run) sur le fallback
# heuristique, sans retenter d'appel réseau à chaque fichier.
MAX_CONSECUTIVE_FAILURES = int(os.environ.get("OLLAMA_MAX_FAILURES", "3"))

DEFAULT_MAX_CHARS = 15000
NOT_DETECTED = "Non déterminé"


# ==========================================================
# Anti-fuite de contexte DocGen AI
# ==========================================================
#
# Si l'un de ces termes apparaît dans une réponse générée pour
# décrire le DÉPÔT ANALYSÉ (README, doc technique, analyse globale),
# c'est le signe d'une fuite de contexte : le modèle (ou un fallback
# codé en dur) décrit DocGen AI lui-même au lieu du projet cible.
# Dans ce cas, on rejette la réponse et on bascule sur le fallback
# neutre plutôt que d'exposer ce texte à l'utilisateur.
LEAKED_META_PHRASES = [
    # Nom de l'outil, sous toutes ses formes
    "docgen ai", "docgen", "doc gen", "doc-gen",

    # Mécanismes internes de génération
    "pipeline d'analyse", "pipeline de documentation", "pipeline d'ingestion",
    "générateur de readme",
    "outil de génération", "outil d'analyse",
    "moteur d'analyse", "moteur de documentation",
    "système d'analyse", "système de documentation", "système interne",
    "api de documentation",

    # Références directes à l'IA / au modèle utilisé
    "analyse ia", "résumé ia", "assistant ia", "assistant de documentation",
    "intelligence artificielle du projet",
    "ollama",
    "circuit breaker", "client ollama", "modèle ollama",

    # Formulations de type "généré automatiquement" côté outil
    "analyse automatique du dépôt", "génération automatique de documentation",
    "documentation automatique", "documentation générée automatiquement",
    "généré automatiquement pour ce projet",
    "readme généré automatiquement",
]

def _contains_leaked_meta_language(text: str) -> bool:
    """
    True si `text` contient un terme appartenant au vocabulaire interne
    de DocGen AI (l'outil), signe que le contenu généré décrit l'outil
    au lieu du dépôt analysé.
    """
    if not text:
        return False
    lowered = text.lower()
    return any(phrase in lowered for phrase in LEAKED_META_PHRASES)


# ==========================================================
# Marqueurs interdits SPÉCIFIQUEMENT dans le README
# ==========================================================
#
# Ces éléments ne sont pas des "fuites de contexte DocGen AI" au sens
# strict, mais du contenu qui n'a rien à faire dans un README de
# présentation : arborescence complète, informations Git détaillées,
# score/confiance d'une détection automatique. Ce contenu reste
# légitime dans la documentation technique (`documentation.md`),
# jamais dans le README.
FORBIDDEN_README_MARKERS = [
    # Caractères d'arborescence (tree Unicode)
    "├──", "└──", "│  ", "│",

    # Informations Git détaillées
    "informations git", "branche :", "commit :", "auteur :",
    "nombre de commits",

    # Score / confiance de détection automatique
    "score d'analyse", "score :", "confiance :", "confiance estimée",
    "architecture détectée", "analyse détaillée des fichiers",

    # Mentions explicites de génération automatique
    "généré automatiquement", "documentation générée automatiquement",
]
LEAKED_DIGEST_MARKERS = [
    "nombre de lignes",
    "elements détectés",
    "elements detectés",
    "module python",
    "module javascript",
    "module typescript",
    "fichier source",
    "script php",
]
def _contains_leaked_digest_language(text: str) -> bool:
    """
    True si `text` contient des traces du digest technique brut
    (heuristic_summary / key_files_digest) recopié tel quel dans une
    section censée être rédigée en langage humain (ex: Features).
    """
    if not text:
        return False
    lowered = text.lower()
    return any(marker in lowered for marker in LEAKED_DIGEST_MARKERS)


def _contains_disallowed_readme_language(text: str) -> bool:
    """
    True si le README contient des termes de fuite de contexte ou des
    mentions explicites de génération automatique ou d'outil.
    """
    if not text:
        return False
    lowered = text.lower()
    disallowed_terms = [
        " ia ",
        "l'ia",
        "intelligence artificielle",
        "ollama",
        "pipeline",
        "docgen",
        "documentation automatique",
        "généré automatiquement",
        "génération automatique",
        "score d'analyse",
        "score :",
        "confiance estimée",
        "confiance :",
        "informations git",
        "branche :",
        "commit :",
        "arborescence",
    ]
    return any(term in lowered for term in disallowed_terms)
def _contains_readme_meta_phrases(text: str) -> bool:
    """
    Detecte les phrases ajoutées par Ollama au lieu du README réel.
    """
    if not text:
        return False

    lowered = text.lower()

    forbidden_phrases = [
        "here is",
        "here's",
        "note:",
        "following the strict output",
        "strict output rules",
        "guidelines provided",
        "i have removed",
        "i removed",
        "rewritten version",
        "this readme follows",
    ]

    return any(
        phrase in lowered
        for phrase in forbidden_phrases
    )

def _validate_readme_content(readme: str, project_name: str) -> bool:
    """
    Minimal validation:
    - README must exist
    - Must start with project title
    """

    if not readme:
        print("❌ EMPTY README")
        return False

    first_line = readme.splitlines()[0].strip()

    if first_line.lower() != f"# {project_name}".lower():
        print(
            "❌ README does not start with project title:",
            repr(first_line)
        )
        return False

    return True

def _contains_forbidden_readme_markers(text: str) -> bool:
    """
    True si `text` contient un marqueur interdit dans un README
    (arborescence, infos Git, score/confiance, mention de génération
    automatique). Ces éléments doivent rester dans la documentation
    technique uniquement.
    """
    if not text:
        return False
    lowered = text.lower()
    return any(marker.lower() in lowered for marker in FORBIDDEN_README_MARKERS)


class OllamaClient:

    def __init__(
        self,
        model: str = DEFAULT_MODEL,
        url: str = OLLAMA_URL,
        timeout: int = GENERATE_TIMEOUT
    ):

        self.model = model
        self.url = url
        self.timeout = timeout

        parsed = urlparse(url)
        self.base_url = f"{parsed.scheme}://{parsed.netloc}"

        self.available_cache = None
        self.consecutive_failures = 0
        self.circuit_open = False

        self._lock = threading.Lock()

    def limit_code_inventory(
        self,
        code_inventory,
        max_chars=120000
    ):
        """
       Limite la taille de l'inventaire
       en gardant la structure complète.
       """
        if not code_inventory:
            return "Aucun détail de code détecté."

        return code_inventory[:max_chars]


    # ======================================================
    # Check Ollama
    # ======================================================

    def is_available(self):

        if self.circuit_open:
            return False

        if self.available_cache is not None:
            return self.available_cache

        try:
            response = requests.get(
                self.base_url,
                timeout=AVAILABILITY_TIMEOUT
            )
            self.available_cache = response.status_code == 200

        except requests.exceptions.RequestException:
            self.available_cache = False

        return self.available_cache

    # ======================================================
    # Circuit breaker helpers
    # ======================================================

    def _register_failure(self):
        with self._lock:
            self.consecutive_failures += 1
            if self.consecutive_failures >= MAX_CONSECUTIVE_FAILURES:
                self.circuit_open = True

    def _register_success(self):
        with self._lock:
            self.consecutive_failures = 0

    # ======================================================
    # Generate
    # ======================================================

    def generate(
        self,
        prompt: str,
        system: str = "",
        timeout: Optional[int] = None,
        temperature: float = 0.0
    ) -> Optional[str]:

        if not self.is_available():
            return None

        payload = {
            "model": self.model,
            "prompt": prompt,
            "system": system,
            "stream": False,
            "options": {
                "temperature": temperature,
                "num_predict": GENERATE_NUM_PREDICT,
            },
        }
        import time
        print("🚀 START OLLAMA REQUEST")
        start = time.time()



        try:
            response = requests.post(
                self.url,
                json=payload,
                timeout=timeout if timeout is not None else self.timeout,
            )
            print("✅ OLLAMA RESPONSE RECEIVED")
            print("OLLAMA TIME:", round(time.time() - start, 2), "seconds")

            response.raise_for_status()
            data = response.json()
            result_text = data.get("response", "")
            if not isinstance(result_text, str) or not result_text.strip():
                self._register_failure()
                return None
            self._register_success()
            return result_text.strip()
        except requests.exceptions.Timeout as exc:
            print("OLLAMA TIMEOUT:", repr(exc))
            self._register_failure()
            return None
        except requests.exceptions.ConnectionError as exc:
            print("OLLAMA CONNECTION ERROR:", repr(exc))
            self._register_failure()
            return None
        except requests.exceptions.RequestException as exc:
            print("OLLAMA REQUEST ERROR:", repr(exc))
            self._register_failure()
            return None
        except ValueError as exc:
            print("OLLAMA JSON PARSE ERROR:", repr(exc))
            self._register_failure()
            return None
        except Exception as exc:
            print("OLLAMA ERROR:", repr(exc))
            self._register_failure()
            return None

    # ======================================================
    # Summarize file
    # ======================================================

    def summarize_file(
            self,
            filepath,
            content,
            max_chars=DEFAULT_MAX_CHARS
            ):
        """
        Résumé rapide d'un fichier sans appel Ollama.
        L'analyse IA est effectuée uniquement au niveau du projet
        global via analyze_project().
        """
        return heuristic_summary(
            filepath,
            content
            )

    # ======================================================
    # README generation
    # ======================================================
    #
    # Le README généré est STRICTEMENT limité à ces sections :
    #   Description, Features, Technologies Used, Prerequisites,
    #   Installation, Usage, Project Structure
    # Aucune arborescence complète, aucune information Git, aucun
    # score/confiance d'architecture, aucune mention de génération
    # automatique/IA/Ollama/DocGen AI ne doit apparaître.
    def generate_readme_content(
        self,
        project_name,
        tech_stack,
        dependencies=None,
        entry_points=None,
        existing_readme_excerpt=None,
        key_files_digest=None,
        code_inventory=None,
        structure_overview=None,
        databases=None,
        repository_url=None,
        detected_scripts=None,
        install_command=None,
        run_command=None,
        api_endpoints=None,


    ):
        """
        Generate a short professional README.

        README is independent from technical documentation.
        It contains only high-level project presentation.
        """

        tech_text = (
            ", ".join(tech_stack)
            if tech_stack
            else "Not detected"
        )

        dependencies_text = (
            "\n".join(
                f"- {dep}"
                for dep in (dependencies or [])[:10]
            )
            if dependencies
            else "No dependencies detected."
        )

        scripts_text = (
            "\n".join(
                f"- {name}: {command}"
                for name, command in (detected_scripts or {}).items()
                )
                if detected_scripts
                else "No scripts detected."
                )
        install_text = (
            install_command
            if install_command
            else "See the official project documentation."
            )
        run_text = (
            run_command
            if run_command
            else "See the official project documentation."
            )
        code_inventory_text = self.limit_code_inventory(code_inventory,max_chars=60000)
        print("README CODE INVENTORY SIZE:", len(code_inventory_text))
        print(code_inventory_text[:5000])
        api_text = (
            "\n".join(
                f"- {api}"
                for api in (api_endpoints or [])
                )
            if api_endpoints
            else "No API endpoints detected."
            )



        readme_context = ""

        if existing_readme_excerpt:
            readme_context += f"""
Original project description:
{existing_readme_excerpt[:10]}

"""

        prompt = f"""
Tu es un rédacteur technique spécialisé dans la création de fichiers README.md.

Ta mission est de générer uniquement le contenu final du README en Markdown, entièrement en français (les noms de technologies, bibliothèques et commandes restent en anglais).

==============================
DONNÉES DU PROJET
==============================

Nom :
{project_name}

Technologies détectées :
{tech_text}

Dépendances détectées :
{dependencies_text}

URL du dépôt :
{repository_url or "Non détecté."}

Scripts détectés :
{scripts_text}

Commande d'installation détectée :
{install_text}

Commande d'exécution détectée :
{run_text}

Endpoints API détectés :
{api_text}

==============================
CODE INVENTORY
==============================

Le Code Inventory est la seule source principale de vérité.

Utilise-le pour comprendre :

- l'objectif réel du projet
- les fonctionnalités réellement implémentées
- les technologies réellement utilisées
- les commandes détectées

{code_inventory_text}

==============================
README EXISTANT
==============================

Le README ci-dessous est fourni uniquement comme contexte.

Ne copie jamais son texte.
Ne copie jamais sa structure.
Ignore toute information non confirmée par le Code Inventory.

{readme_context if readme_context else "Non détecté."}

==============================
RÈGLES
==============================

- Utilise uniquement les informations présentes dans le Code Inventory et les données détectées.
- Le Code Inventory est prioritaire sur toutes les autres sources.
- N'interprète pas le code.
- Ne déduis pas une fonctionnalité qui n'est pas clairement visible.
- Décris uniquement ce qui est explicitement présent.
- N'invente jamais :
  - fonctionnalités
  - technologies
  - API
  - bases de données
  - dépendances
  - commandes
  - scénarios d'utilisation
- Si une information est absente ou ambiguë, écris exactement :
  Non détecté.
- Ne mentionne jamais :
  - fichiers
  - dossiers
  - classes
  - fonctions
  - modules
  - architecture
  - implémentation
  - migrations
  - tests
  - organisation du code

==============================
FORMAT OBLIGATOIRE
==============================

La réponse doit commencer immédiatement par :

# {project_name}

Aucun texte avant.
Aucun texte après.
Aucune section supplémentaire.

Utilise exactement cette structure :

# {project_name}

## Description

## Features

## Technologies Used

## Prerequisites

## Installation

## Usage

==============================
CONTENU DES SECTIONS
==============================

Description
- 2 à 3 phrases.
- Décris uniquement l'objectif réel du projet.
- Explique ce que le projet apporte à son utilisateur ou à son développeur.
- Ne décris jamais son implémentation.

Features
- Entre 3 et 5 fonctionnalités maximum.
- Une fonctionnalité = une capacité visible pour l'utilisateur.
- Si moins de 3 fonctionnalités sont détectées, n'en invente pas.

Technologies Used
- Utilise uniquement la liste "Technologies détectées".
- Format :
  - Technologie : rôle
- N'ajoute aucune technologie supplémentaire.

Prerequisites
- Utilise uniquement les prérequis détectés.
- Si aucun prérequis n'est détecté, écris :
  - Non détecté.

Installation
- Utilise uniquement la commande d'installation détectée.
- Si elle est absente, écris exactement :
  Non détecté.

Usage
- Utilise uniquement la commande d'exécution détectée.
- Si elle est absente, écris exactement :
  Non détecté.

Génère maintenant uniquement le README.
"""
        print("README PROJECT NAME:", project_name)
        print("README TECH:", tech_stack)

        result = self.generate(
            prompt,
            system=(
                "You are a senior software engineer and technical writer. "
                "You write clean, professional, production-quality README "
                "files for software repositories, entirely in French, "
                "following the exact structure and rules given to you. "
                "You never add preambles, comments, or explanations "
                "outside the markdown."
            ),
            timeout=PROJECT_ANALYSIS_TIMEOUT,
            temperature=0.2,
        )

        if result:

            result = result.strip()

            # Remove text before README title
            title_pos = result.lower().find(
                f"# {project_name}".lower()
            )

            if title_pos > 0:
                print("⚠️ Removing Ollama preamble")
                result = result[title_pos:].strip()


            # Remove assistant/meta endings
            result = re.sub(
                r"(?i)(Note:.*|Please let me know.*|If you need.*|Hope this helps.*)$",
                "",
                result,
                flags=re.DOTALL
            ).strip()


            # Remove common introductions
            markers = [
                "Here is",
                "Sure",
                "Voici",
                "Bien sûr"
            ]

            if any(result.startswith(x) for x in markers):

                pos = result.find("# ")

                if pos != -1:
                    result = result[pos:].strip()


            # Auto-fix missing Description section
            if "## Description" not in result:

                lines = result.split("\n")

                if len(lines) > 1:

                    result = (
                        lines[0]
                        + "\n\n## Description\n"
                        + lines[1]
                        + "\n"
                        + "\n".join(lines[2:])
                    )


            print("========== README FROM OLLAMA ==========")
            print(result)
            print("========================================")

            validation = _validate_readme_content(
                result,
                project_name
            )

            print("VALIDATION RESULT:", validation)


            if validation:
                return result


            print("README validation failed, using fallback")


        return _fallback_readme_content(
            project_name,
            tech_stack,
            dependencies=dependencies,
            entry_points=entry_points,
            key_files_digest=None,
            structure_overview=None,
        )
    def generate_technical_documentation_content(
        self,
        project_name,
        tech_stack,
        databases,
        architecture_type,
        architecture_confidence,
        structure_overview,
        key_files_digest,
        entry_points=None,
        dependencies=None,
        code_inventory="",
        existing_readme_excerpt=None,
        repository_url=None,
        language=None,
    ) -> str:
        """
        Génère la documentation technique basée sur les informations détectées.
        
        Pas d'appel Ollama ici pour éviter une génération IA supplémentaire.
        """

        return _fallback_technical_documentation_content(
            project_name,
            tech_stack,
            databases,
            architecture_type,
            architecture_confidence,
            structure_overview,
            entry_points=entry_points,
            dependencies=dependencies,
            key_files_digest=key_files_digest,
            existing_readme_excerpt=existing_readme_excerpt,
        )



    def analyze_project(
        self,
        project_name,
        tech_stack,
        databases,
        architecture_type,
        architecture_confidence,
        structure_overview,
        key_files_digest,
        existing_readme_excerpt=None,
        entry_points=None,
        dependencies=None,
        code_inventory="",
        repository_url=None,
        language=None,
        routes=None,
        blueprints=None,
        module_relations=None,
        
        ):
        """
        Analyse le projet globalement (et non fichier par fichier) afin de générer :
       - objectif du projet
       - fonctionnement général
       - technologies
       - architecture
       - modules principaux
       - flux de données
       - points d'entrée
       - dépendances
       - recommandations

       Le résultat est utilisé comme résumé global (`ai_summary`) et documentation
       technique.

       Règles :
       - Ne jamais inventer de bases de données, APIs, technologies ou fonctionnalités.
       - Si une information manque, indiquer "Non détecté".

       Paramètres :
       - existing_readme_excerpt : extrait optionnel du README original pour fournir
       un contexte supplémentaire sur l'objectif du projet.
       - entry_points / dependencies : informations détectées utilisées dans l'analyse
       et dans le fallback heuristique.
       """
        tech_text = ", ".join(tech_stack) if tech_stack else "Non déterminées"
        databases_text = (
            ", ".join(databases)
            if databases
            else "Non détectées"
            )

        digest_text = (
            "\n".join(key_files_digest[:10])
            if key_files_digest
            else "Aucun fichier clé identifié."
        )

        entry_points_text = (
            "\n".join(f"- {ep}" for ep in entry_points)
            if entry_points
            else "Aucun point d'entrée identifié automatiquement."
        )
        routes_text = (
            "\n".join(
                f"- {r['route']} ({r['file']})"
                for r in routes
                )
            if routes
            else "No routes detected."
                )


        blueprints_text = (
            "\n".join(
                f"- {b['name']}: {', '.join(b['files'])}"
                for b in blueprints
                )
            if blueprints
            else "No blueprints detected."
            )

        dependencies_text = (
            "\n".join(f"- {dep}" for dep in dependencies)
            if dependencies
            else "Aucune dépendance clé identifiée automatiquement."
        )
        if isinstance(module_relations, dict):

            module_relations_text = "\n".join(
                f"- {module} dépend de {', '.join(dependencies)}"
                for module, dependencies in module_relations.items()
            )

        elif isinstance(module_relations, list):

            module_relations_text = "\n".join(
                f"- {relation.get('source')} dépend de {relation.get('target')}"
                for relation in module_relations
                if isinstance(relation, dict)
            )

        else:

            module_relations_text = (
                "Aucune relation entre modules détectée."
            )
        code_inventory_text = self.limit_code_inventory(code_inventory,max_chars=60000)
        print("========== CODE INVENTORY ==========")
        print(code_inventory_text[:40000])
        print("====================================")
        print("========== FILES SENT TO OLLAMA ==========")
        for line in code_inventory_text.splitlines():
            if line.startswith("## "):
                print(line)
        print("==========================================")
        print("========== ROUTES ==========")
        print(routes_text)
        print("========== BLUEPRINTS ==========")
        print(blueprints_text)
        print("========== MODULE RELATIONS ==========")
        print(module_relations_text)

        readme_block = (
            f"""
README d'origine du projet (extrait) :
\"\"\"
{existing_readme_excerpt}
\"\"\"
"""
            if existing_readme_excerpt
            else ""
        )
        prompt = f"""
Projet : {project_name}

Tu es un architecte logiciel senior spécialisé dans l'analyse de dépôts Git et la production de documentation technique.

Ta mission est de comprendre le fonctionnement réel du projet uniquement à partir des informations détectées.

==================================================
SOURCES D'INFORMATION (ordre de priorité)
==================================================

Utilise les informations dans cet ordre :
1. Inventaire du code (preuve principale)
2. Routes et blueprints détectés
3. Relations entre modules
4. Points d'entrée
5. Fichiers clés
6. Dépendances détectées
7. Structure du projet
8. README d'origine

Le README ne doit jamais remplacer l'analyse du code.

==================================================
RÈGLES STRICTES
==================================================

- N'invente jamais une fonctionnalité.
- N'invente jamais une API.
- N'invente jamais une base de données.
- N'invente jamais une architecture.
- N'invente jamais un framework.
- N'invente jamais des modules.

Chaque affirmation doit pouvoir être justifiée par :

- un fichier
- une classe
- une fonction
- un import
- une dépendance
- un point d'entrée

Si une information n'est pas visible :

Écris exactement :

Non détecté.

N'utilise jamais :

- probablement
- semble
- pourrait
- il est possible
- on peut supposer

Ne mentionne jamais :

- IA
- Ollama
- modèle de langage
- génération automatique
- pipeline
- analyse interne
- outil de documentation

==================================================
INFORMATIONS DU PROJET
==================================================

Nom :
{project_name}

Technologies détectées :

{tech_text}

Bases de données :

{databases_text}

Architecture détectée :

{architecture_type}
Cette valeur est issue d'une détection statique.
Tu dois la respecter.

Si architecture_type = Flask Application:
- décris une application Flask monolithique/modulaire.
- ne mentionne jamais microservices sauf présence réelle de plusieurs services indépendants.

Confiance :

{architecture_confidence} %

Organisation du projet :

{structure_overview}

README d'origine (contexte uniquement) :

{readme_block}

Fichiers clés :

{digest_text}

Inventaire du code :

{code_inventory_text}

Points d'entrée :

{entry_points_text}

Dépendances :

{dependencies_text}
Routes détectées :

{routes_text}


Blueprints détectés :

{blueprints_text}


Relations entre modules :

{module_relations_text}

==================================================
ANALYSE ATTENDUE
==================================================

Analyse le code pour comprendre :

- le rôle global du projet
- les responsabilités des modules
- les interactions entre composants
- les classes principales
- les fonctions importantes
- le flux d'exécution
- les technologies réellement utilisées

Ne résume jamais uniquement le README.

Explique ce que fait réellement le projet à partir du code.

==================================================
FORMAT DE SORTIE
==================================================

Réponds UNIQUEMENT en Markdown.

Respecte STRICTEMENT cet ordre.

# Objectif du projet

Décris l'objectif réel du projet.

Base-toi principalement sur :

- les points d'entrée
- les classes
- les fonctions
- le code

Le README peut compléter cette description uniquement si les informations sont cohérentes avec le code.

---

# Fonctionnement général

Explique le fonctionnement global.

Décris :

- les composants principaux
- leur rôle
- leurs interactions

---

# Architecture

Explique :

- pourquoi cette architecture a été détectée
- quels signaux ont permis cette détection
- les limites éventuelles

Règles obligatoires :

Le type d'architecture fourni par le détecteur est prioritaire.

Ne remplace jamais l'architecture détectée par une autre appellation
(MVC, Clean Architecture, Layered Architecture, Microservices, Monolithique, etc.)
sauf si des preuves explicites dans le code confirment cette architecture.

L'analyse doit toujours respecter :
- le nom de l'architecture détectée
- le score/confiance fourni
- les signaux ayant permis cette détection

Les concepts architecturaux supplémentaires peuvent être mentionnés uniquement comme observations secondaires et jamais comme architecture principale.

Prends en compte :

- les routes détectées
- les blueprints
- les relations entre modules
- les points d'entrée

pour expliquer l'organisation réelle de l'application.

Mentionne toujours le niveau de confiance fourni.

---

# Technologies utilisées
La liste des technologies détectées est la seule source autorisée.

Pour chaque technologie :
- utilise uniquement les éléments fournis dans "Technologies détectées"
- explique son rôle avec les fichiers détectés

N'ajoute aucune technologie supplémentaire même si elle apparaît dans :
- un nom de fichier
- une route
- un commentaire
- un README

Une technologie absente de la liste doit être considérée comme :
"Non détectée."

---

# Modules principaux
Sélectionne uniquement les modules présents dans l'inventaire du code.

Ne crée jamais de module logique non présent.

Chaque module cité doit avoir :
- chemin exact du fichier
- éléments détectés dans ce fichier
- rôle observable

Pour chaque module important :

- chemin du fichier
- rôle
- classes principales
- fonctions importantes
- dépendances internes
- routes exposées
- blueprint associé
- dépendances
- interaction avec les autres modules

---

# Flux de données

Décris uniquement le flux réellement observable.
Décris uniquement les flux d'exécution visibles dans le code.

Ne suppose jamais :
- qu'une fonction appelle une autre fonction
- qu'une valeur est retournée vers un autre module
- qu'un utilisateur suit un scénario précis

Un flux doit être justifié par :
- un appel de fonction visible
- une route liée à une fonction
- une interaction entre modules détectée

Si le flux n'est pas clairement observable :
Écris exactement :
"Flux non détecté."

Exemple :

Entrée

↓

Traitement

↓

Sortie

Si le flux ne peut pas être identifié :

Écris :

Flux non détecté.

---

# Points d'entrée

Présente chaque point d'entrée détecté.

Explique son rôle.

---

# Dépendances importantes

Pour chaque dépendance :

- Nom
- Utilisation
- Pourquoi elle est présente

---

# Recommandations

Les recommandations doivent être basées uniquement sur des problèmes ou améliorations visibles dans le code analysé.

Ne propose jamais :
- migration d'une technologie
- ajout d'un outil
- changement d'architecture
- optimisation de performance

sauf si un problème concret est identifié dans le code.

Si aucun problème n'est détecté :
Écris :
"Aucune recommandation spécifique détectée."

==================================================
STYLE
==================================================

- Français
- Technique
- Clair
- Professionnel
- Structuré
- Sans répétition
- Sans texte inutile

Ne réponds que par le Markdown demandé.
"""
        try:
            print("=" * 60)
            print("PROMPT SIZE:", len(prompt))
            print("CODE INVENTORY SIZE:", len(code_inventory_text))
            print("DIGEST SIZE:", len(digest_text))
            print("STRUCTURE SIZE:", len(structure_overview or ""))
            print("ENTRY SIZE:", len(entry_points_text))
            print("DEPENDENCY SIZE:", len(dependencies_text))
            print("=" * 60)
            result = self.generate(
                prompt,
                system=(
                    "Tu es un architecte logiciel senior chargé de documenter "
                    "un projet pour un onboarding rapide."
                ),
                timeout=PROJECT_ANALYSIS_TIMEOUT,
                temperature=0.0,
            )
        except Exception as exc:

            print("OLLAMA PROJECT ANALYSIS ERROR:", repr(exc))
            self._register_failure()
            result = None
        if result and not _contains_leaked_meta_language(result): 
            return result



        return heuristic_project_summary(
            project_name,
            tech_stack,
            databases,
            architecture_type,
            architecture_confidence,
            key_files_digest,
            existing_readme_excerpt=existing_readme_excerpt,
            entry_points=entry_points,
            dependencies=dependencies,
        )


# ==========================================================
# Client partagé (singleton)
# ==========================================================
#
# Avant cette optimisation, generate_summary() créait un nouveau
# OllamaClient() à CHAQUE fichier. Cela forçait un nouveau test de
# disponibilité (requête HTTP, jusqu'à 2s) à chaque fichier, même si
# Ollama était indisponible. Sur un repo de 200 fichiers, cela pouvait
# ajouter à lui seul jusqu'à 200 x 2s = 400s, avant même de tenter une
# seule génération.
#
# Le client partagé ne teste la disponibilité qu'une seule fois par
# run, et porte le circuit breaker pour tout le pipeline.

_default_client_lock = threading.Lock()
_default_client: Optional[OllamaClient] = None


def get_default_client() -> OllamaClient:
    """Retourne l'instance OllamaClient partagée pour ce run."""
    global _default_client
    with _default_client_lock:
        if _default_client is None:
            _default_client = OllamaClient()
        return _default_client


def reset_default_client():
    """
    Réinitialise le client partagé (force un nouveau test de
    disponibilité et remet le circuit breaker à zéro). Utile entre
    deux analyses de repository distinctes, ou pour les tests.
    """
    global _default_client
    with _default_client_lock:
        _default_client = None


# ==========================================================
# Compatibility function
# Utilisée par documentation_service.py
# ==========================================================

# ==========================================================
# FALLBACK — résumé par fichier
# ==========================================================

EXTENSION_HINTS = {
    ".py": "Module Python",
    ".js": "Module JavaScript",
    ".ts": "Module TypeScript",
    ".java": "Classe Java",
    ".php": "Script PHP",
    ".html": "Page HTML",
    ".css": "Style CSS",
    ".sql": "Script SQL",
    ".json": "Fichier JSON"
}


def heuristic_summary(filepath, content):
    """
    Génère un résumé simple d'un fichier
    quand l'analyse complète n'est pas disponible.
    """
    ext = os.path.splitext(filepath)[1].lower()
    file_type = EXTENSION_HINTS.get(ext, "Source file")
    lines = [
        x.strip()
        for x in content.splitlines()
        if x.strip()
    ]

    elements = []

    for line in lines[:100]:

        if line.startswith(
            (
                "def ",
                "class ",
                "function ",
            )
        ):
            elements.append(
                line.split("(")[0]
            )

    extra = ""

    if elements:
        extra = (
            " Elements detectés: "
            + ", ".join(elements[:3])
        )

    return (
        f"{file_type}. "
        f"Nombre de lignes: {len(lines)}."
        f"{extra}"
    )




# ==========================================================
# FALLBACK — README
# ==========================================================
#
# Respecte EXACTEMENT le même ensemble de sections que le prompt IA :
# Description, Features, Technologies Used, Prerequisites,
# Installation, Usage, Project Structure. Ne mentionne jamais IA,
# Ollama, pipeline, ni score/confiance/arborescence/infos Git.

def _fallback_readme_content(
    project_name,
    tech_stack,
    dependencies=None,
    entry_points=None,
    key_files_digest=None,
    structure_overview=None,
):
    tech_text = ", ".join(tech_stack) if tech_stack else "Not determined"
    dependency_text = (
        ", ".join((dependencies or [])[:5])
        if dependencies
        else "No information available."
    )
    entry_text = (
        ", ".join((entry_points or [])[:3])
        if entry_points
        else "No information available."
    )


    return f"""# {project_name}

## Description
No information available.

## Features
No information available.

## Technologies Used
{tech_text}

## Prerequisites
No information available.

## Installation
No information available.

## Usage
No information available.






"""


def _fallback_technical_documentation_content(
    project_name,
    tech_stack,
    databases,
    architecture_type,
    architecture_confidence,
    structure_overview,
    entry_points=None,
    dependencies=None,
    key_files_digest=None,
    existing_readme_excerpt=None,
):
    tech_text = ", ".join(tech_stack) if tech_stack else "Non déterminées"
    databases_text = ", ".join(databases) if databases else NOT_DETECTED

    entry_points_text = (
        "\n".join(f"- {ep}" for ep in (entry_points or [])[:8])
        if entry_points
        else f"- {NOT_DETECTED}"
    )

    dependencies_text = (
        "\n".join(f"- {dep}" for dep in (dependencies or [])[:12])
        if dependencies
        else f"- {NOT_DETECTED}"
    )

    modules_text = (
        "\n".join(key_files_digest[:10])
        if key_files_digest
        else NOT_DETECTED
    )

    structure_text = structure_overview or NOT_DETECTED

    # --- Objectif du projet ---
    first_hint = _first_meaningful_sentence(existing_readme_excerpt)
    objective_parts = []
    if tech_stack:
        objective_parts.append(f"Projet basé sur {tech_text}.")
    if first_hint:
        objective_parts.append(f"D'après son README, il s'agit de : « {first_hint} ».")
    if not objective_parts:
        objective_parts.append(NOT_DETECTED)
    objective_text = " ".join(objective_parts)

    # --- Fonctionnement général ---
    functioning_text = _build_functioning_paragraph(
        architecture_type, entry_points, tech_stack
    )

    # --- Flux de données (reconstruit si un entry point existe) ---
    if entry_points:
        dataflow_text = (
            f"Le point de démarrage identifié est {entry_points[0]}. "
            "Les autres relations entre modules n'ont pas pu être "
            "déterminées automatiquement : se référer au code source."
        )
    else:
        dataflow_text = NOT_DETECTED

    return f"""# Documentation technique - {project_name}

## Objectif du projet
{objective_text}

## Fonctionnement général
{functioning_text}

## Architecture
Architecture détectée : **{architecture_type}** 
(confiance estimée : {architecture_confidence}%).

Cette détection est basée sur des signaux structurels et doit être validée manuellement.

## Technologies utilisées
{tech_text}

## Bases de données
{databases_text}



## Modules principaux
{modules_text}

## Flux de données
{dataflow_text}

## Points d'entrée
{entry_points_text}

## Dépendances importantes
{dependencies_text}



## Recommandations
- Vérifier les modules principaux manuellement.
- Compléter la documentation avec une analyse approfondie du code source.
"""

def heuristic_project_summary(
    project_name,
    tech_stack,
    databases,
    architecture_type,
    architecture_confidence,
    key_files_digest,
    existing_readme_excerpt=None,
    entry_points=None,
    dependencies=None,
):
    """
    Fallback utilisé quand Ollama est indisponible/trop lent pour
    l'analyse globale (`ai_summary`, PAS le README). Reste structuré
    avec des sections d'analyse d'ensemble — mais sans jamais
    recopier le README d'origine mot pour mot : seule sa toute
    première phrase (nettoyée) sert d'indice, le reste de chaque
    section est reconstruit à partir de faits structurels
    (technologies, points d'entrée, dépendances) plutôt que de texte
    généré à partir de rien. Ne mentionne jamais l'IA, Ollama, ou un
    quelconque mécanisme de génération automatique.
    """

    tech_text = ", ".join(tech_stack) if tech_stack else "Non déterminées"

    modules_text = (
        "\n".join(key_files_digest[:8])
        if key_files_digest
        else "- Aucun module clé identifié automatiquement."
    )

    entry_points_text = (
        "\n".join(f"- {ep}" for ep in entry_points)
        if entry_points
        else "- Aucun point d'entrée identifié automatiquement."
    )

    dependencies_text = (
        "\n".join(f"- {dep}" for dep in dependencies)
        if dependencies
        else "- Aucune dépendance clé identifiée automatiquement."
    )

    # Au lieu de citer un bloc entier du README (perçu comme un simple
    # copier/coller), on n'en retient que la première phrase utile,
    # comme un indice de contexte parmi d'autres faits structurels.
    first_hint = _first_meaningful_sentence(existing_readme_excerpt)

    objective_parts = [
        f"**{project_name}** est un projet "
        + (f"basé sur {tech_text}. " if tech_stack else "dont les technologies n'ont pas pu être déterminées automatiquement. ")
    ]

    if first_hint:
        objective_parts.append(
            f"D'après son README, il s'agit de : « {first_hint} »."
        )

    if not first_hint and not tech_stack:
        objective_parts.append(
            "L'objectif précis du projet n'a pas pu être déduit "
            "automatiquement à partir des informations disponibles : "
            "se référer au code source pour plus de détails."
        )

    objective_section = " ".join(objective_parts)

    functioning_section = (
        _build_functioning_paragraph(
            architecture_type, entry_points, tech_stack
        )
    )

    return f"""
## Objectif du projet

{objective_section}

## Fonctionnement général

{functioning_section}

## Technologies utilisées

{tech_text}

## Architecture détectée : **{architecture_type}** \
(confiance estimée : {architecture_confidence}%).

## Modules principaux

{modules_text}

## Flux de données

Flux de données non déterminé à partir des informations disponibles.

## Points d'entrée

{entry_points_text}

## Dépendances importantes

{dependencies_text}

## Recommandations

- Maintenir une séparation claire des responsabilités entre modules.
- Vérifier la couverture de tests des modules principaux.
- Documenter les points d'entrée du projet (API, scripts, jobs).
"""


def _first_meaningful_sentence(text, max_len=180):
    """
    Extrait la première phrase "utile" d'un texte (typiquement un
    README) : ignore les titres Markdown, badges, images et lignes
    vides, coupe à une longueur raisonnable. Retourne None si rien
    d'exploitable n'est trouvé. Volontairement limité à UNE phrase,
    pour donner un indice de contexte plutôt que de reproduire un
    passage entier du document d'origine.
    """
    if not text:
        return None

    for raw_line in text.splitlines():
        line = raw_line.strip()

        if not line:
            continue
        if line.startswith(("#", "![", "<", "[!", "[![")):
            continue
        if line.startswith(("- ", "* ", "```")):
            continue

        sentence = re.split(r"(?<=[.!?])\s", line)[0]
        sentence = sentence.strip(" .")

        if len(sentence) < 15:
            continue

        return sentence[:max_len]

    return None


def _build_functioning_paragraph(architecture_type, entry_points, tech_stack):
    """
       Construit le paragraphe "Fonctionnement général"
    à partir des faits structurels observés.

    Ne mentionne jamais :
    - outil de génération ;
    - modèle de langage ;
    - IA.

    Utilise uniquement :
    - architecture détectée ;
    - points d'entrée.
    """
    if entry_points:
        first_entry = entry_points[0]
        return (
            f"Le projet démarre via {first_entry}, puis suit une "
            f"organisation de type **{architecture_type}**. Se référer "
            "au code source pour le détail exact de l'enchaînement "
            "entre modules."
        )

    return (
        f"Aucun point d'entrée explicite n'a été identifié dans les "
        f"fichiers analysés. Le projet semble organisé selon une "
        f"architecture de type **{architecture_type}** ; se référer à "
        "la structure du projet ci-dessous pour identifier le point "
        "de démarrage."
    )

 