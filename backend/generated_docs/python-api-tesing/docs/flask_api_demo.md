# Module : flask/api_demo

5 fichier(s), 4 classe(s), 2 fonction(s).

## Vue d'ensemble

- **Classes principales** : Category, CategorySchema, Comment, CommentSchema
- **Fonctions principales** : __init__, create_app
- **Dépendances** : Model, app, flask, flask_marshmallow, flask_migrate, flask_restful, flask_script, flask_sqlalchemy, marshmallow, os, resources.Category, resources.Comment

## Détail des fichiers

### `Model.py`

Module Python. Nombre de lignes: 37. Elements detectés: class Comment, def __init__, class Category

**Classes** : Comment, Category, CategorySchema, CommentSchema
**Fonctions** : __init__
**Dépendances** : flask, marshmallow, flask_marshmallow, flask_sqlalchemy

### `app.py`

Module Python. Nombre de lignes: 15.

**Dépendances** : flask, flask_restful, resources.Hello, resources.Category, resources.Comment

### `config.py`

Module Python. Nombre de lignes: 10.

**Dépendances** : os

### `migrate.py`

Module Python. Nombre de lignes: 10.

**Dépendances** : flask_script, flask_migrate, Model, run

### `run.py`

Module Python. Nombre de lignes: 16. Elements detectés: def create_app

**Fonctions** : create_app
**Dépendances** : flask, app, Model
