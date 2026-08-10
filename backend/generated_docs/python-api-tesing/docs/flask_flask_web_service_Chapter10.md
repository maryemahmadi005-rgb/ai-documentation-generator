# Module : flask/flask_web_service/Chapter10

6 fichier(s), 7 classe(s), 30 fonction(s).

## Vue d'ensemble

- **Classes principales** : BitlyHelper, CreateTableForm, LoginForm, MockDBHelper, PasswordHelper, RegistrationForm, User
- **Fonctions principales** : __init__, account, account_createtable, account_deletetable, add_request, add_table, add_user, dashboard, dashboard_resolve, delete_request, delete_table, get_hash, get_id, get_requests, get_salt
- **Dépendances** : base64, bitlyhelper, config, datetime, dbhelper, flask, flask_login, flask_wtf, forms, hashlib, json, mockdbhelper
- **Endpoints API** : /, /account, /account/createtable, /account/deletetable, /dashboard, /dashboard/resolve, /login, /logout, /newrequest/<tid>, /register

## Détail des fichiers

### `bitlyhelper.py`

Module Python. Nombre de lignes: 14. Elements detectés: class BitlyHelper:, def shorten_url

**Classes** : BitlyHelper
**Fonctions** : shorten_url
**Dépendances** : urllib, json

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

Module Python. Nombre de lignes: 10. Elements detectés: class PasswordHelper:, def get_hash, def get_salt

**Classes** : PasswordHelper
**Fonctions** : get_hash, get_salt, validate_password
**Dépendances** : hashlib, os, base64

### `user.py`

Module Python. Nombre de lignes: 11. Elements detectés: class User:, def __init__, def get_id

**Classes** : User
**Fonctions** : __init__, get_id, is_active, is_anonymous, is_authenticated

### `waitercaller.py`

Module Python. Nombre de lignes: 105. Elements detectés: def load_user, def login, def register

**Fonctions** : load_user, login, register, logout, home, dashboard, dashboard_resolve, account, account_createtable, account_deletetable, new_request
**Dépendances** : datetime, flask, flask_login, passwordhelper, bitlyhelper, user, forms, config, mockdbhelper, dbhelper
**API** : /login, /register, /logout, /, /dashboard, /dashboard/resolve, /account, /account/createtable, /account/deletetable, /newrequest/<tid>
