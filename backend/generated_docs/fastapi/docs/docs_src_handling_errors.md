# Module : docs_src/handling_errors

7 fichier(s), 2 classe(s), 1 fonction(s).

## Vue d'ensemble

- **Classes principales** : Item, UnicornException
- **Fonctions principales** : __init__
- **Dépendances** : fastapi, fastapi.encoders, fastapi.exception_handlers, fastapi.exceptions, fastapi.responses, pydantic, starlette.exceptions
- **Endpoints API** : /items-header/{item_id}, /items/, /items/{item_id}, /unicorns/{name}

## Détail des fichiers

### `tutorial001_py310.py`

Module Python. Nombre de lignes: 8.

**Dépendances** : fastapi
**API** : /items/{item_id}

### `tutorial002_py310.py`

Module Python. Nombre de lignes: 12.

**Dépendances** : fastapi
**API** : /items-header/{item_id}

### `tutorial003_py310.py`

Module Python. Nombre de lignes: 17. Elements detectés: class UnicornException, def __init__

**Classes** : UnicornException
**Fonctions** : __init__
**Dépendances** : fastapi, fastapi.responses
**API** : /unicorns/{name}

### `tutorial004_py310.py`

Module Python. Nombre de lignes: 19.

**Dépendances** : fastapi, fastapi.exceptions, fastapi.responses, starlette.exceptions
**API** : /items/{item_id}

### `tutorial005_py310.py`

Module Python. Nombre de lignes: 18. Elements detectés: class Item

**Classes** : Item
**Dépendances** : fastapi, fastapi.encoders, fastapi.exceptions, fastapi.responses, pydantic
**API** : /items/

### `tutorial006_py310.py`

Module Python. Nombre de lignes: 21.

**Dépendances** : fastapi, fastapi.exception_handlers, fastapi.exceptions, starlette.exceptions
**API** : /items/{item_id}
