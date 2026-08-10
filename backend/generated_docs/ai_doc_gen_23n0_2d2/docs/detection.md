# Détection automatique

Architecture : **Flask Architecture**

Confiance : 47.2%

## Classement

| Architecture | Score | Confiance |
|---|---|---|
| Flask Architecture | 17 | 47.2% |
| Hexagonal Architecture | 2 | 15.4% |

## Analyse IA

## Objectif du projet

**ai_doc_gen_23n0_2d2** est un projet basé sur Python, pip (Python). 

## Fonctionnement général

Le projet démarre via `app.py`, puis suit une organisation de type **Flask Architecture**. Une analyse IA plus poussée (Ollama) permettrait de détailler précisément l'enchaînement des appels entre modules.

## Technologies utilisées

Python, pip (Python)

## Architecture

Architecture détectée : **Flask Architecture** (confiance estimée : 47.2%).

## Modules principaux

- `generation/ecrivain.py` : Module Python. Nombre de lignes: 151. Elements detectés: def nettoyer_nom_repo, def chemin_doc_fichier, def ecrire_fichier
- `generation/mkdocs_generator.py` : Module Python. Nombre de lignes: 63. Elements detectés: def construire_arbre_nav, def arbre_vers_nav_yaml, def generer_mkdocs_yml
- `architecture/rapport.py` : Module Python. Nombre de lignes: 256. Elements detectés: def _generer_barre, def _formater_liste_signaux, def _section_resultat
- `app.py` : Module Python. Nombre de lignes: 266. Elements detectés: def inject_user, def home, def login
- `architecture/detecteur.py` : Module Python. Nombre de lignes: 249. Elements detectés: def _normaliser, def _poids_profondeur, def _collecter_tous_signaux_par_categorie
- `utils/tree_utils.py` : Module Python. Nombre de lignes: 34. Elements detectés: def aplatir_arbre, def parcourir, def trier_arbre
- `publisher/repo_creator.py` : Module Python. Nombre de lignes: 149. Elements detectés: class RepoCreationError, def creer_repo_github, def creer_repo_gitlab
- `architecture/api_route_detector.py` : Module Python. Nombre de lignes: 183. Elements detectés: def detecter_routes, def _extraire_routes_du_fichier, def _analyser_decorateur

## Flux de données

Flux de données non déterminé automatiquement (analyse IA indisponible) :
se référer au diagramme de flux de données généré ci-dessous pour un
schéma générique basé sur l'architecture détectée.

## Points d'entrée

- `app.py`
- `models.py`

## Dépendances importantes

- Aucune dépendance clé identifiée automatiquement.

## Recommandations

- Maintenir une séparation claire des responsabilités entre modules.
- Vérifier la couverture de tests des modules principaux.
- Documenter les points d'entrée du projet (API, scripts, jobs).
