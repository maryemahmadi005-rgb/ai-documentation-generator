# Module : flask/flask_web_service/Chapter08

4 fichier(s), 2 classe(s), 12 fonction(s).

## Vue d'ensemble

- **Classes principales** : DBHelper, MockDBHelper
- **Fonctions principales** : add_crime, add_input, clear_all, connect, format_date, get_all_crimes, home, sanitize_string, submitcrime
- **Dépendances** : dateparser, datetime, dbconfig, dbhelper, flask, json, mockdbhelper, pymysql, string
- **Endpoints API** : /, /submitcrime

## Détail des fichiers

### `crimemap.py`

Module Python. Nombre de lignes: 52. Elements detectés: def sanitize_string, def format_date, def home

**Fonctions** : sanitize_string, format_date, home, submitcrime
**Dépendances** : flask, json, dateparser, datetime, string, dbconfig, mockdbhelper, dbhelper
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
