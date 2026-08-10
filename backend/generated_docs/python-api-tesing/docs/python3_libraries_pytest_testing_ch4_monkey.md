# Module : python3_libraries/pytest_testing/ch4/monkey

3 fichier(s), 1 classe(s), 16 fonction(s).

## Vue d'ensemble

- **Classes principales** : Point
- **Fonctions principales** : __init__, __repr__, __str__, point_fixture, read_cheese_preferences, test_def_prefs_change_defaults, test_def_prefs_change_expanduser, test_def_prefs_change_home, test_def_prefs_full, test_env, test_point_missing_x, test_point_repr, test_point_str, test_prepend, write_cheese_preferences
- **Dépendances** : cheese, copy, json, os, pytest

## Détail des fichiers

### `cheese.py`

Module Python. Nombre de lignes: 21. Elements detectés: def read_cheese_preferences, def write_cheese_preferences, def write_default_cheese_preferences

**Fonctions** : read_cheese_preferences, write_cheese_preferences, write_default_cheese_preferences
**Dépendances** : os, json

### `test_cheese.py`

Module Python. Nombre de lignes: 39. Elements detectés: def test_def_prefs_full, def test_def_prefs_change_home, def test_def_prefs_change_expanduser

**Fonctions** : test_def_prefs_full, test_def_prefs_change_home, test_def_prefs_change_expanduser, test_def_prefs_change_defaults
**Dépendances** : copy, cheese

### `test_monkey.py`

Module Python. Nombre de lignes: 30. Elements detectés: class Point, def __init__, def __repr__

**Classes** : Point
**Fonctions** : __init__, __repr__, __str__, point_fixture, test_point_repr, test_point_str, test_point_missing_x, test_env, test_prepend
**Dépendances** : pytest, os
