# Module : python3_libraries/pytest_testing/tasks_proj/src/tasks

6 fichier(s), 4 classe(s), 44 fonction(s).

## Vue d'ensemble

- **Classes principales** : TasksDB_MongoDB, TasksDB_TinyDB, TasksException, UninitializedDatabase
- **Fonctions principales** : __init__, _connect, _disconnect, _start_mongod, _stop_mongod, _tasks_db, add, count, delete, delete_all, get, get_config, list_tasks, start_tasks_db, stop_tasks_db
- **Dépendances** : .api, ConfigParser, __future__, bson.objectid, click, collections, configparser, contextlib, os, pymongo, six, subprocess

## Détail des fichiers

### `__init__.py`

Module Python. Nombre de lignes: 16.

**Dépendances** : .api

### `api.py`

Module Python. Nombre de lignes: 101. Elements detectés: class TasksException, class UninitializedDatabase, def add

**Classes** : TasksException, UninitializedDatabase
**Fonctions** : add, get, list_tasks, count, update, delete, delete_all, unique_id, start_tasks_db, stop_tasks_db
**Dépendances** : collections, six, tasks.tasksdb_tinydb, tasks.tasksdb_pymongo

### `cli.py`

Module Python. Nombre de lignes: 69. Elements detectés: def tasks_cli, def add, def delete

**Fonctions** : tasks_cli, add, delete, list_tasks, update, count, _tasks_db
**Dépendances** : __future__, click, tasks.config, contextlib, tasks.api

### `config.py`

Module Python. Nombre de lignes: 21. Elements detectés: def get_config

**Fonctions** : get_config
**Dépendances** : collections, configparser, ConfigParser, os

### `tasksdb_pymongo.py`

Module Python. Nombre de lignes: 77. Elements detectés: class TasksDB_MongoDB, def __init__, def add

**Classes** : TasksDB_MongoDB
**Fonctions** : __init__, add, get, list_tasks, count, update, delete, unique_id, delete_all, stop_tasks_db, _start_mongod, _stop_mongod, _connect, _disconnect, start_tasks_db
**Dépendances** : os, pymongo, subprocess, time, bson.objectid

### `tasksdb_tinydb.py`

Module Python. Nombre de lignes: 52. Elements detectés: class TasksDB_TinyDB, def __init__, def add

**Classes** : TasksDB_TinyDB
**Fonctions** : __init__, add, get, list_tasks, count, update, delete, delete_all, unique_id, stop_tasks_db, start_tasks_db
**Dépendances** : tinydb
