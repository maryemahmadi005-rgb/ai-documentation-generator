# Module : tests/test_tutorial/test_security

8 fichier(s), 63 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : cache_verify_password, get_access_token, get_client, get_mod, test_create_access_token, test_get_password_hash, test_inactive_user, test_incorrect_token, test_incorrect_token_type, test_login, test_login_incorrect_password, test_login_incorrect_username, test_no_token, test_openapi_schema, test_security_http_basic
- **Dépendances** : ...utils, base64, fastapi.testclient, functools, importlib, inline_snapshot, pytest, types, typing, unittest.mock

## Détail des fichiers

### `test_tutorial001.py`

Module Python. Nombre de lignes: 61. Elements detectés: def get_client, def test_no_token, def test_token

**Fonctions** : get_client, test_no_token, test_token, test_incorrect_token, test_openapi_schema
**Dépendances** : importlib, pytest, fastapi.testclient, inline_snapshot

### `test_tutorial002.py`

Module Python. Nombre de lignes: 62. Elements detectés: def get_client, def test_no_token, def test_token

**Fonctions** : get_client, test_no_token, test_token, test_openapi_schema
**Dépendances** : importlib, pytest, fastapi.testclient, inline_snapshot, ...utils

### `test_tutorial003.py`

Module Python. Nombre de lignes: 192. Elements detectés: def get_client, def test_login, def test_login_incorrect_password

**Fonctions** : get_client, test_login, test_login_incorrect_password, test_login_incorrect_username, test_no_token, test_token, test_incorrect_token, test_incorrect_token_type, test_inactive_user, test_openapi_schema
**Dépendances** : importlib, pytest, fastapi.testclient, inline_snapshot, ...utils

### `test_tutorial004.py`

Module Python. Nombre de lignes: 330. Elements detectés: def get_mod, def get_access_token, def test_login

**Fonctions** : get_mod, get_access_token, test_login, test_login_incorrect_password, test_login_incorrect_username, test_no_token, test_token, test_incorrect_token, test_incorrect_token_type, test_verify_password, test_get_password_hash, test_create_access_token, test_token_no_sub, test_token_no_username, test_token_nonexistent_user
**Dépendances** : importlib, types, unittest.mock, pytest, fastapi.testclient, inline_snapshot, ...utils

### `test_tutorial005.py`

Module Python. Nombre de lignes: 378. Elements detectés: def get_mod, def cache_verify_password, def get_access_token

**Fonctions** : get_mod, cache_verify_password, get_access_token, test_login, test_login_incorrect_password, test_login_incorrect_username, test_no_token, test_token, test_incorrect_token, test_incorrect_token_type, test_verify_password, test_get_password_hash, test_create_access_token, test_token_no_sub, test_token_no_username
**Dépendances** : importlib, functools, types, typing, pytest, fastapi.testclient, inline_snapshot, ...utils

### `test_tutorial006.py`

Module Python. Nombre de lignes: 66. Elements detectés: def get_client, def test_security_http_basic, def test_security_http_basic_no_credentials

**Fonctions** : get_client, test_security_http_basic, test_security_http_basic_no_credentials, test_security_http_basic_invalid_credentials, test_security_http_basic_non_basic_credentials, test_openapi_schema
**Dépendances** : importlib, base64, pytest, fastapi.testclient, inline_snapshot

### `test_tutorial007.py`

Module Python. Nombre de lignes: 75. Elements detectés: def get_client, def test_security_http_basic, def test_security_http_basic_no_credentials

**Fonctions** : get_client, test_security_http_basic, test_security_http_basic_no_credentials, test_security_http_basic_invalid_credentials, test_security_http_basic_non_basic_credentials, test_security_http_basic_invalid_username, test_security_http_basic_invalid_password, test_openapi_schema
**Dépendances** : importlib, base64, pytest, fastapi.testclient, inline_snapshot
