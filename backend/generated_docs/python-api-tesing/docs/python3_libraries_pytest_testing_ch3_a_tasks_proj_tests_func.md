# Module : python3_libraries/pytest_testing/ch3/a/tasks_proj/tests/func

5 fichier(s), 2 classe(s), 20 fonction(s).

## Vue d'ensemble

- **Classes principales** : TestAdd, TestUpdate
- **Fonctions principales** : equivalent, test_add_1, test_add_2, test_add_3, test_add_4, test_add_5, test_add_6, test_add_increases_count, test_add_raises, test_add_returns_valid_id, test_added_task_has_id_set, test_bad_id, test_bad_task, test_delete_raises, test_equivalent
- **Dépendances** : pytest, tasks

## Détail des fichiers

### `__init__.py`

Module Python. Nombre de lignes: 8.

### `test_add.py`

Module Python. Nombre de lignes: 33. Elements detectés: def test_add_returns_valid_id, def test_added_task_has_id_set, def test_add_increases_count

**Fonctions** : test_add_returns_valid_id, test_added_task_has_id_set, test_add_increases_count
**Dépendances** : pytest, tasks

### `test_add_variety.py`

Module Python. Nombre de lignes: 79. Elements detectés: def test_add_1, def equivalent, def test_add_2

**Classes** : TestAdd
**Fonctions** : test_add_1, equivalent, test_add_2, test_add_3, test_add_4, test_add_5, test_add_6, test_equivalent, test_valid_id
**Dépendances** : pytest, tasks

### `test_api_exceptions.py`

Module Python. Nombre de lignes: 39. Elements detectés: def test_add_raises, def test_list_raises, def test_get_raises

**Classes** : TestUpdate
**Fonctions** : test_add_raises, test_list_raises, test_get_raises, test_bad_id, test_bad_task, test_delete_raises, test_start_tasks_db_raises
**Dépendances** : pytest, tasks

### `test_unique_id.py`

Module Python. Nombre de lignes: 8. Elements detectés: def test_unique_id

**Fonctions** : test_unique_id
**Dépendances** : tasks
