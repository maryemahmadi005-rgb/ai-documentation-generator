# Module : app

5 fichier(s), 7 classe(s), 24 fonction(s).

## Vue d'ensemble

- **Classes principales** : AnonymousUser, Comment, Follow, Permission, Post, Role, User
- **Fonctions principales** : __init__, __repr__, add_permission, add_self_follows, admin_required, confirm, create_app, decorated_function, decorator, generate_confirmation_token, generate_email_change_token, generate_reset_token, has_permission, insert_roles, password
- **Dépendances** : ., .api, .auth, .main, .models, app.exceptions, bleach, config, datetime, faker, flask, flask_bootstrap

## Détail des fichiers

### `app/__init__.py`

Module Python. Nombre de lignes: 35. Elements detectés: def create_app

**Fonctions** : create_app
**Dépendances** : flask, flask_bootstrap, flask_mail, flask_moment, flask_sqlalchemy, flask_login, flask_pagedown, config, flask_sslify, .main, .auth, .api

### `app/decorators.py`

Module Python. Nombre de lignes: 15. Elements detectés: def permission_required, def decorator, def decorated_function

**Fonctions** : permission_required, decorator, decorated_function, admin_required
**Dépendances** : functools, flask, flask_login, .models

### `app/email.py`

Module Python. Nombre de lignes: 16. Elements detectés: def send_async_email, def send_email

**Fonctions** : send_async_email, send_email
**Dépendances** : threading, flask, flask_mail, .

### `app/fake.py`

Module Python. Nombre de lignes: 33. Elements detectés: def users, def posts

**Fonctions** : users, posts
**Dépendances** : random, sqlalchemy.exc, faker, ., .models

### `app/models.py`

Module Python. Nombre de lignes: 307. Elements detectés: class Permission:, class Role, def __init__

**Classes** : Permission, Role, Follow, User, AnonymousUser, Post, Comment
**Fonctions** : __init__, insert_roles, add_permission, remove_permission, reset_permissions, has_permission, __repr__, add_self_follows, password, verify_password, generate_confirmation_token, confirm, generate_reset_token, reset_password, generate_email_change_token
**Dépendances** : datetime, hashlib, werkzeug.security, itsdangerous, markdown, bleach, flask, flask_login, app.exceptions, .
