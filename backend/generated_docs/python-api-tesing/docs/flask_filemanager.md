# Module : flask/filemanager

5 fichier(s), 6 classe(s), 2 fonction(s).

## Vue d'ensemble

- **Classes principales** : Nodes, NodesSchema, Owners, OwnersSchema, Photos, PhotosSchema
- **Fonctions principales** : __init__, create_app
- **Dépendances** : Model, app, flask, flask_marshmallow, flask_migrate, flask_restful, flask_script, flask_sqlalchemy, marshmallow, os, resources.Photos, run

## Détail des fichiers

### `Model.py`

Module Python. Nombre de lignes: 50. Elements detectés: class Photos, def __init__, class PhotosSchema

**Classes** : Photos, PhotosSchema, Owners, OwnersSchema, Nodes, NodesSchema
**Fonctions** : __init__
**Dépendances** : flask, marshmallow, flask_marshmallow, flask_sqlalchemy

### `app.py`

Module Python. Nombre de lignes: 11.

**Dépendances** : flask, flask_restful, resources.Photos

### `config.py`

Module Python. Nombre de lignes: 10.

**Dépendances** : os

### `migrate.py`

Module Python. Nombre de lignes: 14.

**Dépendances** : flask_script, flask_migrate, Model, run

### `run.py`

Module Python. Nombre de lignes: 16. Elements detectés: def create_app

**Fonctions** : create_app
**Dépendances** : flask, app, Model
