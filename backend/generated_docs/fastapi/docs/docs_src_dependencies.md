# Module : docs_src/dependencies

31 fichier(s), 17 classe(s), 41 fonction(s).

## Vue d'ensemble

- **Classes principales** : CommonQueryParams, FixedContentQueryChecker, InternalError, MySuperContextManager, OwnerError, User
- **Fonctions principales** : __call__, __enter__, __exit__, __init__, generate, generate_stream, get_item, get_session, get_user, get_user_me, get_username, query_extractor, query_or_cookie_extractor
- **Dépendances** : fastapi, fastapi.responses, sqlmodel, time, typing
- **Endpoints API** : /generate, /items/, /items/{item_id}, /query-checker/, /users/, /users/me

## Détail des fichiers

### `tutorial001_02_an_py310.py`

Module Python. Nombre de lignes: 12.

**Dépendances** : typing, fastapi
**API** : /items/, /users/

### `tutorial001_an_py310.py`

Module Python. Nombre de lignes: 11.

**Dépendances** : typing, fastapi
**API** : /items/, /users/

### `tutorial001_py310.py`

Module Python. Nombre de lignes: 10.

**Dépendances** : fastapi
**API** : /items/, /users/

### `tutorial002_an_py310.py`

Module Python. Nombre de lignes: 17. Elements detectés: class CommonQueryParams:, def __init__

**Classes** : CommonQueryParams
**Fonctions** : __init__
**Dépendances** : typing, fastapi
**API** : /items/

### `tutorial002_py310.py`

Module Python. Nombre de lignes: 16. Elements detectés: class CommonQueryParams:, def __init__

**Classes** : CommonQueryParams
**Fonctions** : __init__
**Dépendances** : fastapi
**API** : /items/

### `tutorial003_an_py310.py`

Module Python. Nombre de lignes: 17. Elements detectés: class CommonQueryParams:, def __init__

**Classes** : CommonQueryParams
**Fonctions** : __init__
**Dépendances** : typing, fastapi
**API** : /items/

### `tutorial003_py310.py`

Module Python. Nombre de lignes: 16. Elements detectés: class CommonQueryParams:, def __init__

**Classes** : CommonQueryParams
**Fonctions** : __init__
**Dépendances** : fastapi
**API** : /items/

### `tutorial004_an_py310.py`

Module Python. Nombre de lignes: 17. Elements detectés: class CommonQueryParams:, def __init__

**Classes** : CommonQueryParams
**Fonctions** : __init__
**Dépendances** : typing, fastapi
**API** : /items/

### `tutorial004_py310.py`

Module Python. Nombre de lignes: 16. Elements detectés: class CommonQueryParams:, def __init__

**Classes** : CommonQueryParams
**Fonctions** : __init__
**Dépendances** : fastapi
**API** : /items/

### `tutorial005_an_py310.py`

Module Python. Nombre de lignes: 17. Elements detectés: def query_extractor, def query_or_cookie_extractor

**Fonctions** : query_extractor, query_or_cookie_extractor
**Dépendances** : typing, fastapi
**API** : /items/

### `tutorial005_py310.py`

Module Python. Nombre de lignes: 13. Elements detectés: def query_extractor, def query_or_cookie_extractor

**Fonctions** : query_extractor, query_or_cookie_extractor
**Dépendances** : fastapi
**API** : /items/

### `tutorial006_an_py310.py`

Module Python. Nombre de lignes: 13.

**Dépendances** : typing, fastapi
**API** : /items/

### `tutorial006_py310.py`

Module Python. Nombre de lignes: 12.

**Dépendances** : fastapi
**API** : /items/

### `tutorial008_an_py310.py`

Module Python. Nombre de lignes: 20.

**Dépendances** : typing, fastapi

### `tutorial008_py310.py`

Module Python. Nombre de lignes: 19.

**Dépendances** : fastapi

### `tutorial008b_an_py310.py`

Module Python. Nombre de lignes: 22. Elements detectés: class OwnerError, def get_username, def get_item

**Classes** : OwnerError
**Fonctions** : get_username, get_item
**Dépendances** : typing, fastapi
**API** : /items/{item_id}

### `tutorial008b_py310.py`

Module Python. Nombre de lignes: 21. Elements detectés: class OwnerError, def get_username, def get_item

**Classes** : OwnerError
**Fonctions** : get_username, get_item
**Dépendances** : fastapi
**API** : /items/{item_id}

### `tutorial008c_an_py310.py`

Module Python. Nombre de lignes: 21. Elements detectés: class InternalError, def get_username, def get_item

**Classes** : InternalError
**Fonctions** : get_username, get_item
**Dépendances** : typing, fastapi
**API** : /items/{item_id}

### `tutorial008c_py310.py`

Module Python. Nombre de lignes: 20. Elements detectés: class InternalError, def get_username, def get_item

**Classes** : InternalError
**Fonctions** : get_username, get_item
**Dépendances** : fastapi
**API** : /items/{item_id}

### `tutorial008d_an_py310.py`

Module Python. Nombre de lignes: 22. Elements detectés: class InternalError, def get_username, def get_item

**Classes** : InternalError
**Fonctions** : get_username, get_item
**Dépendances** : typing, fastapi
**API** : /items/{item_id}

### `tutorial008d_py310.py`

Module Python. Nombre de lignes: 21. Elements detectés: class InternalError, def get_username, def get_item

**Classes** : InternalError
**Fonctions** : get_username, get_item
**Dépendances** : fastapi
**API** : /items/{item_id}

### `tutorial008e_an_py310.py`

Module Python. Nombre de lignes: 11. Elements detectés: def get_username, def get_user_me

**Fonctions** : get_username, get_user_me
**Dépendances** : typing, fastapi
**API** : /users/me

### `tutorial008e_py310.py`

Module Python. Nombre de lignes: 10. Elements detectés: def get_username, def get_user_me

**Fonctions** : get_username, get_user_me
**Dépendances** : fastapi
**API** : /users/me

### `tutorial010_py310.py`

Module Python. Nombre de lignes: 10. Elements detectés: class MySuperContextManager:, def __init__, def __enter__

**Classes** : MySuperContextManager
**Fonctions** : __init__, __enter__, __exit__

### `tutorial011_an_py310.py`

Module Python. Nombre de lignes: 14. Elements detectés: class FixedContentQueryChecker:, def __init__, def __call__

**Classes** : FixedContentQueryChecker
**Fonctions** : __init__, __call__
**Dépendances** : typing, fastapi
**API** : /query-checker/

### `tutorial011_py310.py`

Module Python. Nombre de lignes: 13. Elements detectés: class FixedContentQueryChecker:, def __init__, def __call__

**Classes** : FixedContentQueryChecker
**Fonctions** : __init__, __call__
**Dépendances** : fastapi
**API** : /query-checker/

### `tutorial012_an_py310.py`

Module Python. Nombre de lignes: 16.

**Dépendances** : typing, fastapi
**API** : /items/, /users/

### `tutorial012_py310.py`

Module Python. Nombre de lignes: 15.

**Dépendances** : fastapi
**API** : /items/, /users/

### `tutorial013_an_py310.py`

Module Python. Nombre de lignes: 24. Elements detectés: class User, def get_session, def get_user

**Classes** : User
**Fonctions** : get_session, get_user, generate_stream, generate
**Dépendances** : time, typing, fastapi, fastapi.responses, sqlmodel
**API** : /generate

### `tutorial014_an_py310.py`

Module Python. Nombre de lignes: 25. Elements detectés: class User, def get_session, def get_user

**Classes** : User
**Fonctions** : get_session, get_user, generate_stream, generate
**Dépendances** : time, typing, fastapi, fastapi.responses, sqlmodel
**API** : /generate
