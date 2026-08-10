# Module : flask/flask_web_service/Chapter06

3 fichier(s), 1 classe(s), 7 fonction(s).

## Vue d'ensemble

- **Classes principales** : DBHelper
- **Fonctions principales** : add, add_input, clear, clear_all, connect, get_all_inputs, home
- **Dépendances** : dbconfig, dbhelper, flask, pymysql
- **Endpoints API** : /, /add, /clear

## Détail des fichiers

### `crimemap.py`

Module Python. Nombre de lignes: 31. Elements detectés: def home, def add, def clear

**Fonctions** : home, add, clear
**Dépendances** : dbhelper, flask
**API** : /, /add, /clear

### `db_setup.py`

Module Python. Nombre de lignes: 23.

**Dépendances** : pymysql, dbconfig

### `dbhelper.py`

Module Python. Nombre de lignes: 35. Elements detectés: class DBHelper:, def connect, def get_all_inputs

**Classes** : DBHelper
**Fonctions** : connect, get_all_inputs, add_input, clear_all
**Dépendances** : pymysql, dbconfig
