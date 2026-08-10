# Module : utils

4 fichier(s), 9 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : _nettoyer_reponse, aplatir_arbre, decorated_function, generer, get_historique_or_403, get_historique_or_403_api, login_required, parcourir, trier_arbre
- **Dépendances** : dotenv, flask, functools, logging, models, os, requests

## Détail des fichiers

### `auth.py`

Module Python. Nombre de lignes: 12. Elements detectés: def login_required, def decorated_function

**Fonctions** : login_required, decorated_function
**Dépendances** : functools, flask

### `db_helpers.py`

Module Python. Nombre de lignes: 16. Elements detectés: def get_historique_or_403, def get_historique_or_403_api

**Fonctions** : get_historique_or_403, get_historique_or_403_api
**Dépendances** : flask, models

### `ollama_client.py`

Module Python. Nombre de lignes: 76. Elements detectés: def generer, def _nettoyer_reponse

**Fonctions** : generer, _nettoyer_reponse
**Dépendances** : requests, logging, os, dotenv

### `tree_utils.py`

Module Python. Nombre de lignes: 34. Elements detectés: def aplatir_arbre, def parcourir, def trier_arbre

**Fonctions** : aplatir_arbre, parcourir, trier_arbre
