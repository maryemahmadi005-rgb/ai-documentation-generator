# Module : fastapi/security

5 fichier(s), 17 classe(s), 12 fonction(s).

## Vue d'ensemble

- **Classes principales** : APIKeyBase, APIKeyCookie, APIKeyHeader, APIKeyQuery, HTTPAuthorizationCredentials, HTTPBase, HTTPBasic, HTTPBasicCredentials, HTTPBearer, HTTPDigest, OAuth2, OAuth2AuthorizationCodeBearer
- **Fonctions principales** : __init__, check_api_key, login, make_authenticate_headers, make_not_authenticated_error, read_current_user
- **Dépendances** : .api_key, .http, .oauth2, .open_id_connect_url, annotated_doc, base64, binascii, fastapi, fastapi.exceptions, fastapi.openapi.models, fastapi.param_functions, fastapi.security
- **Endpoints API** : /items/, /login, /users/me

## Détail des fichiers

### `__init__.py`

Module Python. Nombre de lignes: 15.

**Dépendances** : .api_key, .http, .oauth2, .open_id_connect_url

### `api_key.py`

Module Python. Nombre de lignes: 254. Elements detectés: class APIKeyBase, def __init__, def make_not_authenticated_error

**Classes** : APIKeyBase, APIKeyQuery, APIKeyHeader, APIKeyCookie
**Fonctions** : __init__, make_not_authenticated_error, check_api_key
**Dépendances** : typing, annotated_doc, fastapi.openapi.models, fastapi.security.base, starlette.exceptions, starlette.requests, starlette.status, fastapi, fastapi.security
**API** : /items/

### `http.py`

Module Python. Nombre de lignes: 335. Elements detectés: class HTTPBasicCredentials, class HTTPAuthorizationCredentials, class HTTPBase

**Classes** : HTTPBasicCredentials, HTTPAuthorizationCredentials, HTTPBase, HTTPBasic, HTTPBearer, HTTPDigest
**Fonctions** : __init__, make_authenticate_headers, make_not_authenticated_error, read_current_user
**Dépendances** : binascii, base64, typing, annotated_doc, fastapi.exceptions, fastapi.openapi.models, fastapi.security.base, fastapi.security.utils, pydantic, starlette.requests, starlette.status, fastapi
**API** : /users/me

### `oauth2.py`

Module Python. Nombre de lignes: 605. Elements detectés: class OAuth2PasswordRequestForm:, def login, def __init__

**Classes** : OAuth2PasswordRequestForm, OAuth2PasswordRequestFormStrict, OAuth2, OAuth2PasswordBearer, OAuth2AuthorizationCodeBearer, SecurityScopes
**Fonctions** : login, __init__, make_not_authenticated_error
**Dépendances** : typing, annotated_doc, fastapi.exceptions, fastapi.openapi.models, fastapi.param_functions, fastapi.security.base, fastapi.security.utils, starlette.requests, starlette.status, fastapi, fastapi.security
**API** : /login

### `open_id_connect_url.py`

Module Python. Nombre de lignes: 82. Elements detectés: class OpenIdConnect, def __init__, def make_not_authenticated_error

**Classes** : OpenIdConnect
**Fonctions** : __init__, make_not_authenticated_error
**Dépendances** : typing, annotated_doc, fastapi.openapi.models, fastapi.security.base, starlette.exceptions, starlette.requests, starlette.status
