# Module : src/flask/sansio

3 fichier(s), 4 classe(s), 45 fonction(s).

## Vue d'ensemble

- **Classes principales** : App, Blueprint, BlueprintSetupState, Scaffold
- **Fonctions principales** : __init__, __repr__, _check_setup_finished, _make_timedelta, _merge_blueprint_funcs, _method_route, add_app_template_filter, add_url_rule, app_template_filter, auto_find_instance_path, create_global_jinja_loader, create_jinja_environment, debug, decorator, delete
- **Dépendances** : .., .app, .scaffold, __future__, collections, datetime, functools, importlib.util, itertools, jinja2, logging, os
- **Endpoints API** : /

## Détail des fichiers

### `app.py`

Module Python. Nombre de lignes: 832. Elements detectés: def _make_timedelta, class App

**Classes** : App
**Fonctions** : _make_timedelta, __init__, _check_setup_finished, name, logger, jinja_env, create_jinja_environment, make_config, make_aborter, auto_find_instance_path, create_global_jinja_loader, select_jinja_autoescape, debug, register_blueprint, iter_blueprints
**Dépendances** : __future__, logging, os, sys, typing, datetime, itertools, werkzeug.exceptions, werkzeug.routing, werkzeug.sansio.response, werkzeug.utils, ..

### `blueprints.py`

Module Python. Nombre de lignes: 572. Elements detectés: class BlueprintSetupState:, def __init__, def add_url_rule

**Classes** : BlueprintSetupState, Blueprint
**Fonctions** : __init__, add_url_rule, _check_setup_finished, record, record_once, wrapper, make_setup_state, register_blueprint, register, _merge_blueprint_funcs, extend, app_template_filter, decorator, add_app_template_filter, register_template_filter
**Dépendances** : __future__, os, typing, collections, functools, .., .scaffold, .app

### `scaffold.py`

Module Python. Nombre de lignes: 641. Elements detectés: def setupmethod, def wrapper_func, class Scaffold:

**Classes** : Scaffold
**Fonctions** : setupmethod, wrapper_func, __init__, __repr__, _check_setup_finished, static_folder, has_static_folder, static_url_path, jinja_loader, _method_route, get, post, put, delete, patch
**Dépendances** : __future__, importlib.util, os, pathlib, sys, typing, collections, functools, jinja2, werkzeug.exceptions, werkzeug.utils, ..
**API** : /
