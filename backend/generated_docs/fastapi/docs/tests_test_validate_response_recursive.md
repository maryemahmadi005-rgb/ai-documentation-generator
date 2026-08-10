# Module : tests/test_validate_response_recursive

3 fichier(s), 3 classe(s), 3 fonction(s).

## Vue d'ensemble

- **Classes principales** : RecursiveItem, RecursiveItemViaSubmodel, RecursiveSubitemInSubmodel
- **Fonctions principales** : get_recursive, get_recursive_submodel, test_recursive
- **Dépendances** : .app, fastapi, fastapi.testclient, pydantic
- **Endpoints API** : /items/recursive, /items/recursive-submodel

## Détail des fichiers

### `app.py`

Module Python. Nombre de lignes: 34. Elements detectés: class RecursiveItem, class RecursiveSubitemInSubmodel, class RecursiveItemViaSubmodel

**Classes** : RecursiveItem, RecursiveSubitemInSubmodel, RecursiveItemViaSubmodel
**Fonctions** : get_recursive, get_recursive_submodel
**Dépendances** : fastapi, pydantic
**API** : /items/recursive, /items/recursive-submodel

### `test_validate_response_recursive.py`

Module Python. Nombre de lignes: 26. Elements detectés: def test_recursive

**Fonctions** : test_recursive
**Dépendances** : fastapi.testclient, .app
