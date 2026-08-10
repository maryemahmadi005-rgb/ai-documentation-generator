# Module : examples/celery/src/task_app

3 fichier(s), 1 classe(s), 11 fonction(s).

## Vue d'ensemble

- **Classes principales** : FlaskTask
- **Fonctions principales** : __call__, add, block, celery_init_app, create_app, index, process, result
- **Dépendances** : ., celery, celery.result, flask, time
- **Endpoints API** : /, /add, /block, /process, /result/<id>

## Détail des fichiers

### `__init__.py`

Module Python. Nombre de lignes: 31. Elements detectés: def create_app, def index, def celery_init_app

**Classes** : FlaskTask
**Fonctions** : create_app, index, celery_init_app, __call__
**Dépendances** : celery, flask, .
**API** : /

### `tasks.py`

Module Python. Nombre de lignes: 15. Elements detectés: def add, def block, def process

**Fonctions** : add, block, process
**Dépendances** : time, celery

### `views.py`

Module Python. Nombre de lignes: 28. Elements detectés: def result, def add, def block

**Fonctions** : result, add, block, process
**Dépendances** : celery.result, flask, .
**API** : /result/<id>, /add, /block, /process
