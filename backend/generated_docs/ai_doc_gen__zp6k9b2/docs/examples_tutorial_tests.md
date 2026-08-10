# Module : examples/tutorial/tests

Ce module regroupe 5 fichier(s) source.

## Vue d'ensemble

- **Classes principales** : AuthActions, Recorder
- **Fonctions principales** : __init__, app, auth, client, fake_init_db, login, logout, runner, test_author_required, test_config, test_create, test_create_update_validate, test_delete, test_exists_required, test_get_close_db
- **Dépendances** : flask, flaskr, flaskr.db, os, pytest, sqlite3, tempfile

## Détail des fichiers

### `conftest.py`

Module Python. Nombre de lignes: 44. Elements detectés: def app, def client, def runner

**Classes** : AuthActions
**Fonctions** : app, client, runner, __init__, login, logout, auth
**Dépendances** : os, tempfile, pytest, flaskr, flaskr.db

### `test_auth.py`

Module Python. Nombre de lignes: 53. Elements detectés: def test_register, def test_register_validate_input, def test_login

**Fonctions** : test_register, test_register_validate_input, test_login, test_login_validate_input, test_logout
**Dépendances** : pytest, flask, flaskr.db

### `test_blog.py`

Module Python. Nombre de lignes: 61. Elements detectés: def test_index, def test_login_required, def test_author_required

**Fonctions** : test_index, test_login_required, test_author_required, test_exists_required, test_create, test_update, test_create_update_validate, test_delete
**Dépendances** : pytest, flaskr.db

### `test_db.py`

Module Python. Nombre de lignes: 19. Elements detectés: def test_get_close_db, def test_init_db_command, class Recorder:

**Classes** : Recorder
**Fonctions** : test_get_close_db, test_init_db_command, fake_init_db
**Dépendances** : sqlite3, pytest, flaskr.db

### `test_factory.py`

Module Python. Nombre de lignes: 8. Elements detectés: def test_config, def test_hello

**Fonctions** : test_config, test_hello
**Dépendances** : flaskr
