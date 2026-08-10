# Module : docs_src/security

15 fichier(s), 22 classe(s), 34 fonction(s).

## Vue d'ensemble

- **Classes principales** : Token, TokenData, User, UserInDB
- **Fonctions principales** : authenticate_user, create_access_token, fake_decode_token, fake_hash_password, get_current_username, get_password_hash, get_user, read_current_user, verify_password
- **Dépendances** : datetime, fastapi, fastapi.security, jwt, jwt.exceptions, pwdlib, pydantic, secrets, typing
- **Endpoints API** : /items/, /status/, /token, /users/me, /users/me/, /users/me/items/

## Détail des fichiers

### `tutorial001_an_py310.py`

Module Python. Nombre de lignes: 8.

**Dépendances** : typing, fastapi, fastapi.security
**API** : /items/

### `tutorial001_py310.py`

Module Python. Nombre de lignes: 7.

**Dépendances** : fastapi, fastapi.security
**API** : /items/

### `tutorial002_an_py310.py`

Module Python. Nombre de lignes: 21. Elements detectés: class User, def fake_decode_token

**Classes** : User
**Fonctions** : fake_decode_token
**Dépendances** : typing, fastapi, fastapi.security, pydantic
**API** : /users/me

### `tutorial002_py310.py`

Module Python. Nombre de lignes: 20. Elements detectés: class User, def fake_decode_token

**Classes** : User
**Fonctions** : fake_decode_token
**Dépendances** : fastapi, fastapi.security, pydantic
**API** : /users/me

### `tutorial003_an_py310.py`

Module Python. Nombre de lignes: 70. Elements detectés: def fake_hash_password, class User, class UserInDB

**Classes** : User, UserInDB
**Fonctions** : fake_hash_password, get_user, fake_decode_token
**Dépendances** : typing, fastapi, fastapi.security, pydantic
**API** : /token, /users/me

### `tutorial003_py310.py`

Module Python. Nombre de lignes: 65. Elements detectés: def fake_hash_password, class User, class UserInDB

**Classes** : User, UserInDB
**Fonctions** : fake_hash_password, get_user, fake_decode_token
**Dépendances** : fastapi, fastapi.security, pydantic
**API** : /token, /users/me

### `tutorial004_an_py310.py`

Module Python. Nombre de lignes: 113. Elements detectés: class Token, class TokenData, class User

**Classes** : Token, TokenData, User, UserInDB
**Fonctions** : verify_password, get_password_hash, get_user, authenticate_user, create_access_token
**Dépendances** : datetime, typing, jwt, fastapi, fastapi.security, jwt.exceptions, pwdlib, pydantic
**API** : /token, /users/me/, /users/me/items/

### `tutorial004_py310.py`

Module Python. Nombre de lignes: 106. Elements detectés: class Token, class TokenData, class User

**Classes** : Token, TokenData, User, UserInDB
**Fonctions** : verify_password, get_password_hash, get_user, authenticate_user, create_access_token
**Dépendances** : datetime, jwt, fastapi, fastapi.security, jwt.exceptions, pwdlib, pydantic
**API** : /token, /users/me/, /users/me/items/

### `tutorial005_an_py310.py`

Module Python. Nombre de lignes: 143. Elements detectés: class Token, class TokenData, class User

**Classes** : Token, TokenData, User, UserInDB
**Fonctions** : verify_password, get_password_hash, get_user, authenticate_user, create_access_token
**Dépendances** : datetime, typing, jwt, fastapi, fastapi.security, jwt.exceptions, pwdlib, pydantic
**API** : /token, /users/me/, /users/me/items/, /status/

### `tutorial005_py310.py`

Module Python. Nombre de lignes: 140. Elements detectés: class Token, class TokenData, class User

**Classes** : Token, TokenData, User, UserInDB
**Fonctions** : verify_password, get_password_hash, get_user, authenticate_user, create_access_token
**Dépendances** : datetime, jwt, fastapi, fastapi.security, jwt.exceptions, pwdlib, pydantic
**API** : /token, /users/me/, /users/me/items/, /status/

### `tutorial006_an_py310.py`

Module Python. Nombre de lignes: 8. Elements detectés: def read_current_user

**Fonctions** : read_current_user
**Dépendances** : typing, fastapi, fastapi.security
**API** : /users/me

### `tutorial006_py310.py`

Module Python. Nombre de lignes: 7. Elements detectés: def read_current_user

**Fonctions** : read_current_user
**Dépendances** : fastapi, fastapi.security
**API** : /users/me

### `tutorial007_an_py310.py`

Module Python. Nombre de lignes: 29. Elements detectés: def get_current_username, def read_current_user

**Fonctions** : get_current_username, read_current_user
**Dépendances** : secrets, typing, fastapi, fastapi.security
**API** : /users/me

### `tutorial007_py310.py`

Module Python. Nombre de lignes: 26. Elements detectés: def get_current_username, def read_current_user

**Fonctions** : get_current_username, read_current_user
**Dépendances** : secrets, fastapi, fastapi.security
**API** : /users/me
