# Module : tests

6 fichier(s), 5 classe(s), 40 fonction(s).

## Vue d'ensemble

- **Classes principales** : APITestCase, BasicsTestCase, FlaskClientTestCase, SeleniumTestCase, UserModelTestCase
- **Fonctions principales** : get_api_headers, setUp, setUpClass, tearDown, tearDownClass, test_404, test_admin_home_page, test_anonymous, test_app_exists, test_app_is_testing, test_bad_auth, test_comments, test_duplicate_email_change_token, test_expired_confirmation_token, test_home_page
- **Dépendances** : app, app.models, base64, datetime, flask, json, logging, re, selenium, threading, time, unittest

## Détail des fichiers

### `tests/test_api.py`

Module Python. Nombre de lignes: 233. Elements detectés: class APITestCase, def setUp, def tearDown

**Classes** : APITestCase
**Fonctions** : setUp, tearDown, get_api_headers, test_404, test_no_auth, test_bad_auth, test_token_auth, test_anonymous, test_unconfirmed_account, test_posts, test_users, test_comments
**Dépendances** : unittest, json, re, base64, app, app.models

### `tests/test_basics.py`

Module Python. Nombre de lignes: 17. Elements detectés: class BasicsTestCase, def setUp, def tearDown

**Classes** : BasicsTestCase
**Fonctions** : setUp, tearDown, test_app_exists, test_app_is_testing
**Dépendances** : unittest, flask, app

### `tests/test_client.py`

Module Python. Nombre de lignes: 55. Elements detectés: class FlaskClientTestCase, def setUp, def tearDown

**Classes** : FlaskClientTestCase
**Fonctions** : setUp, tearDown, test_home_page, test_register_and_login
**Dépendances** : re, unittest, app, app.models

### `tests/test_selenium.py`

Module Python. Nombre de lignes: 80. Elements detectés: class SeleniumTestCase, def setUpClass, def tearDownClass

**Classes** : SeleniumTestCase
**Fonctions** : setUpClass, tearDownClass, setUp, tearDown, test_admin_home_page
**Dépendances** : re, threading, time, unittest, selenium, app, app.models, logging

### `tests/test_user_model.py`

Module Python. Nombre de lignes: 195. Elements detectés: class UserModelTestCase, def setUp, def tearDown

**Classes** : UserModelTestCase
**Fonctions** : setUp, tearDown, test_password_setter, test_no_password_getter, test_password_verification, test_password_salts_are_random, test_valid_confirmation_token, test_invalid_confirmation_token, test_expired_confirmation_token, test_valid_reset_token, test_invalid_reset_token, test_valid_email_change_token, test_invalid_email_change_token, test_duplicate_email_change_token, test_user_role
**Dépendances** : unittest, time, datetime, app, app.models
