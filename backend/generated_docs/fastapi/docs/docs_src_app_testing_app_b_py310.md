# Module : docs_src/app_testing/app_b_py310

3 fichier(s), 1 classe(s), 6 fonction(s).

## Vue d'ensemble

- **Classes principales** : Item
- **Fonctions principales** : test_create_existing_item, test_create_item, test_create_item_bad_token, test_read_item, test_read_item_bad_token, test_read_nonexistent_item
- **Dépendances** : .main, fastapi, fastapi.testclient, pydantic
- **Endpoints API** : /items/, /items/{item_id}

## Détail des fichiers

### `main.py`

Module Python. Nombre de lignes: 27. Elements detectés: class Item

**Classes** : Item
**Dépendances** : fastapi, pydantic
**API** : /items/{item_id}, /items/

### `test_main.py`

Module Python. Nombre de lignes: 51. Elements detectés: def test_read_item, def test_read_item_bad_token, def test_read_nonexistent_item

**Fonctions** : test_read_item, test_read_item_bad_token, test_read_nonexistent_item, test_create_item, test_create_item_bad_token, test_create_existing_item
**Dépendances** : fastapi.testclient, .main
