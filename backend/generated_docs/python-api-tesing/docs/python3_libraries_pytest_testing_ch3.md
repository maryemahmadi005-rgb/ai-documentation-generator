# Module : python3_libraries/pytest_testing/ch3

4 fichier(s), 1 classe(s), 20 fonction(s).

## Vue d'ensemble

- **Classes principales** : TestSomething
- **Fonctions principales** : a_tuple, class_scope, footer_function_scope, footer_session_scope, func_scope, mod_scope, sess_scope, some_data, some_other_data, test_1, test_2, test_3, test_4, test_a_tuple, test_everything
- **Dépendances** : pytest, time

## Détail des fichiers

### `test_autouse.py`

Module Python. Nombre de lignes: 25. Elements detectés: def footer_session_scope, def footer_function_scope, def test_1

**Fonctions** : footer_session_scope, footer_function_scope, test_1, test_2
**Dépendances** : pytest, time

### `test_fixtures.py`

Module Python. Nombre de lignes: 25. Elements detectés: def some_data, def test_some_data, def some_other_data

**Fonctions** : some_data, test_some_data, some_other_data, test_other_data, a_tuple, test_a_tuple
**Dépendances** : pytest

### `test_rename_fixture.py`

Module Python. Nombre de lignes: 9. Elements detectés: def ultimate_answer_to_life_the_universe_and_everything, def test_everything

**Fonctions** : ultimate_answer_to_life_the_universe_and_everything, test_everything
**Dépendances** : pytest

### `test_scope.py`

Module Python. Nombre de lignes: 25. Elements detectés: def func_scope, def mod_scope, def sess_scope

**Classes** : TestSomething
**Fonctions** : func_scope, mod_scope, sess_scope, class_scope, test_1, test_2, test_3, test_4
**Dépendances** : pytest
