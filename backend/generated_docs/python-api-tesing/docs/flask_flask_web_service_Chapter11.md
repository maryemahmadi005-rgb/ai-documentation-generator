# Module : flask/flask_web_service/Chapter11

7 fichier(s), 8 classe(s), 41 fonction(s).

## Vue d'ensemble

- **Classes principales** : BitlyHelper, CreateTableForm, DBHelper, LoginForm, MockDBHelper, PasswordHelper, RegistrationForm, User
- **Fonctions principales** : __init__, account, account_createtable, account_deletetable, add_request, add_table, add_user, dashboard, dashboard_resolve, delete_request, delete_table, get_hash, get_id, get_requests, get_salt
- **Dépendances** : base64, bitlyhelper, bson, config, datetime, dbhelper, flask, flask_login, flask_wtf, forms, hashlib, json
- **Endpoints API** : /, /account, /account/createtable, /account/deletetable, /dashboard, /dashboard/resolve, /login, /logout, /newrequest/<tid>, /register

## Détail des fichiers

### `bitlyhelper.py`

Module Python. Nombre de lignes: 14. Elements detectés: class BitlyHelper:, def shorten_url

**Classes** : BitlyHelper
**Fonctions** : shorten_url
**Dépendances** : urllib, json

### `dbhelper.py`

Module Python. Nombre de lignes: 34. Elements detectés: class DBHelper:, def __init__, def get_user

**Classes** : DBHelper
**Fonctions** : __init__, get_user, add_user, add_table, update_table, get_tables, get_table, delete_table, add_request, get_requests, delete_request
**Dépendances** : pymongo, bson

### `forms.py`

Module Python. Nombre de lignes: 20. Elements detectés: class RegistrationForm, class LoginForm, class CreateTableForm

**Classes** : RegistrationForm, LoginForm, CreateTableForm
**Dépendances** : flask_wtf, wtforms, wtforms.fields.html5

### `mockdbhelper.py`

Module Python. Nombre de lignes: 45. Elements detectés: class MockDBHelper:, def get_user, def add_user

**Classes** : MockDBHelper
**Fonctions** : get_user, add_user, add_table, update_table, get_tables, get_table, delete_table, add_request, get_requests, delete_request
**Dépendances** : datetime

### `passwordhelper.py`

Module Python. Nombre de lignes: 12. Elements detectés: class PasswordHelper:, def get_hash, def get_salt

**Classes** : PasswordHelper
**Fonctions** : get_hash, get_salt, validate_password
**Dépendances** : hashlib, os, base64

### `user.py`

Module Python. Nombre de lignes: 11. Elements detectés: class User:, def __init__, def get_id

**Classes** : User
**Fonctions** : __init__, get_id, is_active, is_anonymous, is_authenticated

### `waitercaller.py`

Module Python. Nombre de lignes: 109. Elements detectés: def load_user, def login, def register

**Fonctions** : load_user, login, register, logout, home, dashboard, dashboard_resolve, account, account_createtable, account_deletetable, new_request
**Dépendances** : datetime, flask, flask_login, config, mockdbhelper, dbhelper, passwordhelper, bitlyhelper, user, forms
**API** : /login, /register, /logout, /, /dashboard, /dashboard/resolve, /account, /account/createtable, /account/deletetable, /newrequest/<tid>
