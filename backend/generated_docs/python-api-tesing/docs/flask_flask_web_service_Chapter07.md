# Module : flask/flask_web_service/Chapter07

4 fichier(s), 2 classe(s), 10 fonction(s).

## Vue d'ensemble

- **Classes principales** : DBHelper, MockDBHelper
- **Fonctions principales** : add_crime, add_input, clear_all, connect, get_all_crimes, home, submitcrime
- **Dépendances** : datetime, dbconfig, dbhelper, flask, json, mockdbhelper, pymysql
- **Endpoints API** : /, /submitcrime

## Détail des fichiers

### `crimemap.py`

Module Python. Nombre de lignes: 27. Elements detectés: def home, def submitcrime

**Fonctions** : home, submitcrime
**Dépendances** : flask, json, dbconfig, mockdbhelper, dbhelper
**API** : /, /submitcrime

### `db_setup.py`

Module Python. Nombre de lignes: 23.

**Dépendances** : pymysql, dbconfig

### `dbhelper.py`

Module Python. Nombre de lignes: 42. Elements detectés: class DBHelper:, def connect, def add_crime

**Classes** : DBHelper
**Fonctions** : connect, add_crime, get_all_crimes
**Dépendances** : datetime, pymysql, dbconfig

### `mockdbhelper.py`

Module Python. Nombre de lignes: 17. Elements detectés: class MockDBHelper:, def connect, def add_crime

**Classes** : MockDBHelper
**Fonctions** : connect, add_crime, get_all_crimes, add_input, clear_all
