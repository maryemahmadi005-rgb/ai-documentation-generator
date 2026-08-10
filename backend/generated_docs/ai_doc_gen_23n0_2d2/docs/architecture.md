# Module : architecture

8 fichier(s), 79 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : _ajouter_dossier_documentation, _analyser_decorateur, _calculer_score_signaux, _collecter_fichiers, _collecter_tous_signaux_par_categorie, _construire_index_alias, _construire_operations, _construire_parametres, _construire_prompt_conflit, _construire_prompt_normal, _deduire_tag, _deja_bien_range, _elaguer_dossiers_vides, _elaguer_dossiers_vides_disque, _est_fichier_de_test
- **Dépendances** : .signaux, architecture.classifieur_fichiers, architecture.signaux, ast, datetime, json, logging, os, pathlib, re, shutil, typing
- **Endpoints API** : /path

## Détail des fichiers

### `api_route_detector.py`

Module Python. Nombre de lignes: 183. Elements detectés: def detecter_routes, def _extraire_routes_du_fichier, def _analyser_decorateur

**Fonctions** : detecter_routes, _extraire_routes_du_fichier, _analyser_decorateur, _nom_objet_racine, _extraire_chemin, _extraire_methodes_flask
**Dépendances** : ast, os, typing, logging
**API** : /path

### `classifieur_fichiers.py`

Module Python. Nombre de lignes: 225. Elements detectés: def _parser_mots_cles, def _parser_imports, def _tokeniser_nom

**Fonctions** : _parser_mots_cles, _parser_imports, _tokeniser_nom, deviner_role_par_nom, _texte_imports, deviner_role_par_contenu, deviner_role
**Dépendances** : logging, os, re, typing

### `detecteur.py`

Module Python. Nombre de lignes: 249. Elements detectés: def _normaliser, def _poids_profondeur, def _collecter_tous_signaux_par_categorie

**Fonctions** : _normaliser, _poids_profondeur, _collecter_tous_signaux_par_categorie, extraire_dossiers, extraire_fichiers_caracteristiques, extraire_frameworks, extraire_imports_depuis_ast, extraire_decorateurs, extraire_classes_depuis_ast, extraire_dependances, _calculer_score_signaux, calculer_scores, normaliser_scores_par_taille, decider_architecture, detecter_conflit
**Dépendances** : logging, os, .signaux

### `ollama_detecteur.py`

Module Python. Nombre de lignes: 430. Elements detectés: def choisir_fichier_strategique, def _formater_liste_signaux, def construire_prompt

**Fonctions** : choisir_fichier_strategique, _formater_liste_signaux, construire_prompt, _construire_prompt_conflit, _construire_prompt_normal, interroger_ollama, _tenter_nettoyage_json, detecter_avec_ollama, _resultat_scoring_simple, _resultat_fallback_ollama, _traiter_reponse_conflit, _traiter_reponse_normale
**Dépendances** : json, logging, os, typing, utils.ollama_client, re

### `openapi_generator.py`

Module Python. Nombre de lignes: 137. Elements detectés: def _grouper_routes_par_chemin, def _normaliser_chemin, def _construire_operations

**Fonctions** : _grouper_routes_par_chemin, _normaliser_chemin, _construire_operations, _construire_parametres, _deduire_tag, sauvegarder_spec
**Dépendances** : json, os, re, typing

### `rapport.py`

Module Python. Nombre de lignes: 256. Elements detectés: def _generer_barre, def _formater_liste_signaux, def _section_resultat

**Fonctions** : _generer_barre, _formater_liste_signaux, _section_resultat, _section_signaux_detectes, _section_signaux_contributeurs, _section_regles, _section_anti_signaux, _section_scores, _section_couverture, _section_ollama, _section_projet, _section_footer, generer_rapport, generer_rapport_json, sauvegarder_rapport
**Dépendances** : os, typing, datetime

### `restructeur.py`

Module Python. Nombre de lignes: 617. Elements detectés: def _est_fichier_de_test, def _construire_index_alias

**Fonctions** : _est_fichier_de_test, _construire_index_alias, _trouver_categorie_cible, _deja_bien_range, _resoudre_collision, _inserer_chemin, _collecter_fichiers, _elaguer_dossiers_vides, _elaguer_dossiers_vides_disque, _ajouter_dossier_documentation, _nettoyer_roles, construire_arbre_cible, construire_arbre_avec_mappings, _noms_existants_dans, restructurer_physiquement
**Dépendances** : logging, os, shutil, pathlib, typing, architecture.classifieur_fichiers, architecture.signaux, utils.tree_utils

### `signaux.py`

Module Python. Nombre de lignes: 543.

**Fonctions** : get_architectures_supportees, get_categories_architecture, get_description_architecture
**Dépendances** : os
