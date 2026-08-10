# Module : python3_libraries/pytest_testing/ch7/unittest

5 fichier(s), 3 classe(s), 13 fonction(s).

## Vue d'ensemble

- **Classes principales** : TestNonEmpty
- **Fonctions principales** : db_with_3_tasks, setUp, setUpModule, tasks_db, tasks_db_non_empty, tasks_db_session, tasks_just_a_few, tearDownModule, test_delete_decreases_count
- **Dépendances** : pytest, shutil, tasks, tempfile, unittest

## Détail des fichiers

### `conftest.py`

Module Python. Nombre de lignes: 26. Elements detectés: def tasks_db_session, def tasks_db, def tasks_just_a_few

**Fonctions** : tasks_db_session, tasks_db, tasks_just_a_few, db_with_3_tasks
**Dépendances** : pytest, tasks

### `test_delete_pytest.py`

Module Python. Nombre de lignes: 9. Elements detectés: def test_delete_decreases_count

**Fonctions** : test_delete_decreases_count
**Dépendances** : tasks

### `test_delete_unittest.py`

Module Python. Nombre de lignes: 29. Elements detectés: def setUpModule, def tearDownModule, class TestNonEmpty

**Classes** : TestNonEmpty
**Fonctions** : setUpModule, tearDownModule, setUp, test_delete_decreases_count
**Dépendances** : unittest, shutil, tempfile, tasks

### `test_delete_unittest_fix.py`

Module Python. Nombre de lignes: 20. Elements detectés: class TestNonEmpty, def setUp, def test_delete_decreases_count

**Classes** : TestNonEmpty
**Fonctions** : setUp, test_delete_decreases_count
**Dépendances** : pytest, unittest, tasks

### `test_delete_unittest_fix2.py`

Module Python. Nombre de lignes: 22. Elements detectés: def tasks_db_non_empty, class TestNonEmpty, def test_delete_decreases_count

**Classes** : TestNonEmpty
**Fonctions** : tasks_db_non_empty, test_delete_decreases_count
**Dépendances** : pytest, unittest, tasks
