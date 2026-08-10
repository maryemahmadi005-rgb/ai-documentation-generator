# Module : tests/type_check

3 fichier(s), 2 classe(s), 22 fonction(s).

## Vue d'ensemble

- **Classes principales** : RenderTemplateView, StatusJSON
- **Fonctions principales** : after_sync, before_sync, handle_400, handle_accept_base, handle_custom, handle_multiple, hello_bytes, hello_generator, hello_generator_expression, hello_iterator, hello_json, hello_json_dict, hello_json_list, hello_str, return_template
- **Dépendances** : __future__, flask, flask.templating, flask.views, flask.wrappers, http, typing, werkzeug.exceptions
- **Endpoints API** : /bytes, /generator, /generator-expression, /iterator, /json, /json/dict, /status, /status/<int:code>, /str, /typed-dict

## Détail des fichiers

### `typing_app_decorators.py`

Module Python. Nombre de lignes: 18. Elements detectés: def after_sync, def before_sync, def teardown_sync

**Fonctions** : after_sync, before_sync, teardown_sync
**Dépendances** : __future__, flask

### `typing_error_handler.py`

Module Python. Nombre de lignes: 21. Elements detectés: def handle_400, def handle_custom, def handle_accept_base

**Fonctions** : handle_400, handle_custom, handle_accept_base, handle_multiple
**Dépendances** : __future__, http, werkzeug.exceptions, flask

### `typing_route.py`

Module Python. Nombre de lignes: 71. Elements detectés: def hello_str, def hello_bytes, def hello_json

**Classes** : StatusJSON, RenderTemplateView
**Fonctions** : hello_str, hello_bytes, hello_json, hello_json_dict, hello_json_list, typed_dict, hello_generator, show, hello_generator_expression, hello_iterator, tuple_status, tuple_status_enum, tuple_headers, return_template, return_template_stream
**Dépendances** : __future__, typing, http, flask, flask.templating, flask.views, flask.wrappers
**API** : /str, /bytes, /json, /json/dict, /typed-dict, /generator, /generator-expression, /iterator, /status, /status/<int:code>
