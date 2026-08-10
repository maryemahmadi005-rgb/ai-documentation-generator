# Module : Racine du projet

Ce module regroupe 5 fichier(s) source.

## Vue d'ensemble

- **Classes principales** : Historique, Utilisateurs
- **Fonctions principales** : __repr__, _adapter_fichiers_pour_detection, _adapter_infos_ast_pour_architecture_cible, _build_tree_from_files, _inserer_dans_arbre, ajouter_chemin, analyser, arborescence, arborescence_cible, calculer_radar_data, calculer_score_global, calculer_stats_transformation, construire_tree_json, dashboard, detecter_conflits
- **Dépendances** : architecture.detecteur, architecture.ollama_detecteur, datetime, dotenv, flask, flask_sqlalchemy, generation.analyzer, generation.ecrivain, generation.mkdocs_generator, json, logging, models
- **Endpoints API** : /, /analyser, /dashboard, /historique/<int:id>, /historique/<int:id>/statut, /historique/supprimer-tout, /historique/supprimer/<int:id>, /login, /logout, /register

## Détail des fichiers

### `app.py`

Module Python. Nombre de lignes: 266. Elements detectés: def inject_user, def home, def login

**Fonctions** : inject_user, home, login, register, logout, dashboard, analyser, voir_historique, statut_historique, supprimer_historique, supprimer_tout_historique, set_theme, arborescence, generer_resume_ia, arborescence_cible
**Dépendances** : os, json, logging, threading, shutil, tempfile, yaml, flask, werkzeug.security, dotenv, models, pipeline
**API** : /, /login, /register, /logout, /dashboard, /analyser, /historique/<int:id>, /historique/<int:id>/statut, /historique/supprimer/<int:id>, /historique/supprimer-tout

### `constants.py`

Module Python. Nombre de lignes: 59.

**Dépendances** : os

### `models.py`

Module Python. Nombre de lignes: 73. Elements detectés: class Utilisateurs, def __repr__, class Historique

**Classes** : Utilisateurs, Historique
**Fonctions** : __repr__, get_langages, get_tree, get_fichiers_liste, to_dict
**Dépendances** : flask_sqlalchemy, datetime, json, utils.tree_utils

### `pipeline.py`

Module Python. Nombre de lignes: 456. Elements detectés: def _adapter_fichiers_pour_detection, def _build_tree_from_files, def _inserer_dans_arbre

**Fonctions** : _adapter_fichiers_pour_detection, _build_tree_from_files, _inserer_dans_arbre, _adapter_infos_ast_pour_architecture_cible, lister_fichiers_depuis_arbre, extraire_resume, construire_tree_json, ajouter_chemin, extraire_pourcentage_confiance, calculer_radar_data, calculer_score_global, get_description_architecture, calculer_stats_transformation, detecter_conflits, get_architecture_fallback
**Dépendances** : logging, subprocess, os, shutil, json, typing, generation.ecrivain, generation.mkdocs_generator, scanners.scanner, architecture.detecteur, architecture.ollama_detecteur, generation.analyzer

### `summarize_repo.py`

Module Python. Nombre de lignes: 49. Elements detectés: def resumer_repo

**Fonctions** : resumer_repo
**Dépendances** : logging, utils.ollama_client, scanners.scanner
