# Module : flask/flask_web_service/Chapter09

4 fichier(s), 3 classe(s), 16 fonction(s).

## Vue d'ensemble

- **Classes principales** : MockDBHelper, PasswordHelper, User
- **Fonctions principales** : __init__, account, add_user, get_hash, get_id, get_salt, get_user, home, is_active, is_anonymous, is_authenticated, load_user, login, logout, register
- **Dépendances** : base64, flask, flask_login, hashlib, mockdbhelper, os, passwordhelper, user
- **Endpoints API** : /, /account, /login, /logout, /register

## Détail des fichiers

### `mockdbhelper.py`

Module Python. Nombre de lignes: 10. Elements detectés: class MockDBHelper:, def get_user, def add_user

**Classes** : MockDBHelper
**Fonctions** : get_user, add_user

### `passwordhelper.py`

Module Python. Nombre de lignes: 10. Elements detectés: class PasswordHelper:, def get_hash, def get_salt

**Classes** : PasswordHelper
**Fonctions** : get_hash, get_salt, validate_password
**Dépendances** : hashlib, os, base64

### `user.py`

Module Python. Nombre de lignes: 11. Elements detectés: class User:, def __init__, def get_id

**Classes** : User
**Fonctions** : __init__, get_id, is_active, is_anonymous, is_authenticated

### `waitercaller.py`

Module Python. Nombre de lignes: 58. Elements detectés: def load_user, def login, def register

**Fonctions** : load_user, login, register, logout, home, account
**Dépendances** : flask, flask_login, mockdbhelper, passwordhelper, user
**API** : /login, /register, /logout, /, /account
