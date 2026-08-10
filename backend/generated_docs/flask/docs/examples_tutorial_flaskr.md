# Module : examples/tutorial/flaskr

5 fichier(s), 18 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : close_db, create, create_app, delete, get_db, get_post, hello, index, init_app, init_db, init_db_command, load_logged_in_user, login, login_required, logout
- **Dépendances** : ., .auth, .db, click, datetime, flask, functools, os, sqlite3, werkzeug.exceptions, werkzeug.security
- **Endpoints API** : /, /<int:id>/delete, /<int:id>/update, /create, /hello, /login, /logout, /register

## Détail des fichiers

### `__init__.py`

Module Python. Nombre de lignes: 36. Elements detectés: def create_app, def hello

**Fonctions** : create_app, hello
**Dépendances** : os, flask, .
**API** : /hello

### `auth.py`

Module Python. Nombre de lignes: 90. Elements detectés: def login_required, def wrapped_view, def load_logged_in_user

**Fonctions** : login_required, wrapped_view, load_logged_in_user, register, login, logout
**Dépendances** : functools, flask, werkzeug.security, .db
**API** : /register, /login, /logout

### `blog.py`

Module Python. Nombre de lignes: 100. Elements detectés: def index, def get_post, def create

**Fonctions** : index, get_post, create, update, delete
**Dépendances** : flask, werkzeug.exceptions, .auth, .db
**API** : /, /create, /<int:id>/update, /<int:id>/delete

### `db.py`

Module Python. Nombre de lignes: 40. Elements detectés: def get_db, def close_db, def init_db

**Fonctions** : get_db, close_db, init_db, init_db_command, init_app
**Dépendances** : sqlite3, datetime, click, flask

### `schema.sql`

Script SQL. Nombre de lignes: 17.
