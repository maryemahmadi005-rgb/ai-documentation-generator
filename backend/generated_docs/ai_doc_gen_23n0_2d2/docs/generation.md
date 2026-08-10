# Module : generation

8 fichier(s), 36 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : _batch_size_dynamique, _ecrire_cache, _extraire_resume, _generer_index_module, _generer_resume_module, _get_parser, _hash_fichier, _lire_cache, _parcourir, _parser_extensions, _parser_sortie_batch, _score_fichier, analyser_projet_disque, analyser_projet_memoire, arbre_vers_nav_yaml
- **Dépendances** : .prompts, generation.ecrivain, hashlib, importlib, json, logging, os, pathlib, re, time, tree_sitter, typing

## Détail des fichiers

### `analyzer.py`

Module Python. Nombre de lignes: 236. Elements detectés: def _parser_extensions, def _get_parser, def _parcourir

**Fonctions** : _parser_extensions, _get_parser, _parcourir, extraire_infos_depuis_code, extraire_infos_fichier, analyser_projet_disque, analyser_projet_memoire
**Dépendances** : os, logging, pathlib, typing, tree_sitter, importlib

### `doc_generator.py`

Module Python. Nombre de lignes: 318. Elements detectés: def _hash_fichier, def _lire_cache, def _ecrire_cache

**Fonctions** : _hash_fichier, _lire_cache, _ecrire_cache, _score_fichier, _batch_size_dynamique, grouper_fichiers, formater_classes, formater_fonctions, _extraire_resume, _generer_resume_module, _generer_index_module, generer_doc_batch, _parser_sortie_batch, generer_doc_rapide, generer_doc_tous_fichiers
**Dépendances** : logging, time, hashlib, json, os, re, typing, utils.ollama_client

### `ecrivain.py`

Module Python. Nombre de lignes: 151. Elements detectés: def nettoyer_nom_repo, def chemin_doc_fichier, def ecrire_fichier

**Fonctions** : nettoyer_nom_repo, chemin_doc_fichier, ecrire_fichier, ecrire_documentation_complete, lister_fichiers_generes
**Dépendances** : os, logging, pathlib, typing

### `mkdocs_generator.py`

Module Python. Nombre de lignes: 63. Elements detectés: def construire_arbre_nav, def arbre_vers_nav_yaml, def generer_mkdocs_yml

**Fonctions** : construire_arbre_nav, arbre_vers_nav_yaml, generer_mkdocs_yml
**Dépendances** : os, yaml, logging, generation.ecrivain

### `project_doc.py`

Module Python. Nombre de lignes: 61. Elements detectés: def generer_doc_globale, def generer_doc_architecture

**Fonctions** : generer_doc_globale, generer_doc_architecture
**Dépendances** : logging, .prompts, utils.ollama_client

### `prompts.py`

Module Python. Nombre de lignes: 117.

### `readme_generator.py`

Module Python. Nombre de lignes: 33. Elements detectés: def construire_structure_fichiers, def generer_readme

**Fonctions** : construire_structure_fichiers, generer_readme
**Dépendances** : logging, .prompts, utils.ollama_client

### `swagger_page_generator.py`

Module Python. Nombre de lignes: 48. Elements detectés: def generer_page_swagger, def entree_nav_mkdocs

**Fonctions** : generer_page_swagger, entree_nav_mkdocs
**Dépendances** : json, os
