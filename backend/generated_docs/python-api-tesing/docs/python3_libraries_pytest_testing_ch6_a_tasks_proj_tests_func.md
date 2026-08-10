# Module : python3_libraries/pytest_testing/ch6/a/tasks_proj/tests/func

6 fichier(s), 3 classe(s), 30 fonction(s).

## Vue d'ensemble

- **Classes principales** : TestAdd, TestUpdate
- **Fonctions principales** : a_task, b_task, c_task, equivalent, id_func, test_add_1, test_add_2, test_add_3, test_add_4, test_add_5, test_add_6, test_add_a, test_add_b, test_add_c, test_add_increases_count
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

### `test_add_variety2.py`

Module Python. Nombre de lignes: 46. Elements detectés: def equivalent, def a_task, def test_add_a

**Fonctions** : equivalent, a_task, test_add_a, b_task, test_add_b, id_func, c_task, test_add_c
**Dépendances** : pytest, tasks

### `test_api_exceptions.py`

Module Python. Nombre de lignes: 51. Elements detectés: class TestAdd, def test_missing_summary, def test_done_not_bool

**Classes** : TestAdd, TestUpdate
**Fonctions** : test_missing_summary, test_done_not_bool, test_add_raises, test_list_raises, test_get_raises, test_bad_id, test_bad_task, test_delete_raises, test_start_tasks_db_raises
**Dépendances** : pytest, tasks

### `test_unique_id.py`

Module Python. Nombre de lignes: 8. Elements detectés: def test_unique_id

**Fonctions** : test_unique_id
**Dépendances** : tasks
