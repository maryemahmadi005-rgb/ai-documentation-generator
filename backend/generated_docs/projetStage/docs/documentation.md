# Documentation technique - projetStage

## Objectif du projet
Non déterminé

## Fonctionnement général
Non déterminé

## Architecture
Architecture détectée : **Flask Application** 
(confiance estimée : 95.8%).

Cette détection est basée sur des signaux structurels et doit être validée manuellement.

## Technologies utilisées
Python, pip (Python)

## Structure du projet
.gitignore
app.py
constants.py
models.py
pipeline.py
requirements.txt
summarize_repo.py
architecture/
  api_route_detector.py
  classifieur_fichiers.py
  detecteur.py
  ollama_detecteur.py
  openapi_generator.py
  rapport.py
  restructeur.py
  signaux.py
generation/
  analyzer.py
  doc_generator.py
  ecrivain.py
  mkdocs_generator.py
  project_doc.py
  prompts.py
  readme_generator.py
  swagger_page_generator.py
publisher/
  git_publisher.py
  repo_creator.py
  strategie.py
scanners/

## Modules principaux
Non déterminé

## Flux de données
Non déterminé

## Points d'entrée
- `app.py`
- `models.py`

## Dépendances importantes
- 
- architecture
- ast
- constants
- dotenv
- flask
- flask_sqlalchemy
- functools
- gc
- generation
- git
- hashlib

## Analyse détaillée des fichiers
Non déterminé

## Recommandations
- Vérifier les modules principaux manuellement.
- Compléter la documentation avec une analyse approfondie du code source.
