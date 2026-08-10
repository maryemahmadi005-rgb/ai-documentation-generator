# Module : src/flask

Ce module regroupe 17 fichier(s) source.

## Vue d'ensemble

- **Classes principales** : AppContext, AppContextProxy, AppGroup, Blueprint, CertParamType, Config, ConfigAttribute, CounterAPI, CustomClient, DebugFilesKeyError, DispatchingJinjaLoader, EnvironBuilder
- **Fonctions principales** : __contains__, __delattr__, __enter__, __exit__, __get__, __getattr__, __getitem__, __init__, __init_subclass__, __iter__, __repr__, __set__, __setattr__, __str__, _called_with_wrong_args
- **Dépendances** : ., .app, .blueprints, .cli, .config, .ctx, .debughelpers, .globals, .helpers, .json, .json.tag, .sansio.app
- **Endpoints API** : /, /stream, /uploads/<path:name>

## Détail des fichiers

### `__init__.py`

Module Python. Nombre de lignes: 39.

**Dépendances** : ., .app, .blueprints, .config, .ctx, .globals, .helpers, .json, .signals, .templating, .wrappers

### `app.py`

Module Python. Nombre de lignes: 1325. Elements detectés: def _make_timedelta, def remove_ctx, def wrapper

**Classes** : Flask, CustomClient
**Fonctions** : _make_timedelta, remove_ctx, wrapper, add_ctx, __init_subclass__, __init__, get_send_file_max_age, send_static_file, open_resource, open_instance_resource, create_jinja_environment, create_url_adapter, raise_routing_exception, update_template_context, make_shell_context
**Dépendances** : __future__, collections.abc, inspect, os, sys, typing, weakref, datetime, functools, itertools, types, urllib.parse

### `blueprints.py`

Module Python. Nombre de lignes: 102. Elements detectés: class Blueprint, def __init__, def get_send_file_max_age

**Classes** : Blueprint
**Fonctions** : __init__, get_send_file_max_age, send_static_file, open_resource
**Dépendances** : __future__, os, typing, datetime, .cli, .globals, .helpers, .sansio.blueprints, .sansio.scaffold, .wrappers

### `cli.py`

Module Python. Nombre de lignes: 899. Elements detectés: class NoAppException, def find_best_app, def _called_with_wrong_args

**Classes** : NoAppException, ScriptInfo, AppGroup, FlaskGroup, CertParamType, SeparatedPathType
**Fonctions** : find_best_app, _called_with_wrong_args, find_app_by_string, prepare_import, locate_app, get_version, __init__, load_app, with_appcontext, decorator, command, group, _set_app, _set_debug, _env_file_callback
**Dépendances** : __future__, ast, collections.abc, importlib.metadata, inspect, os, platform, re, sys, traceback, typing, functools

### `config.py`

Module Python. Nombre de lignes: 286. Elements detectés: class ConfigAttribute, def __init__, def __get__

**Classes** : ConfigAttribute, Config, and
**Fonctions** : __init__, __get__, __set__, from_envvar, from_prefixed_env, from_pyfile, from_object, from_file, from_mapping, get_namespace, __repr__
**Dépendances** : __future__, errno, json, os, types, typing, werkzeug.utils, typing_extensions, .sansio.app, yourapplication, tomllib

### `ctx.py`

Module Python. Nombre de lignes: 404. Elements detectés: class _AppCtxGlobals:, def __getattr__, def __setattr__

**Classes** : _AppCtxGlobals, AppContext
**Fonctions** : __getattr__, __setattr__, __delattr__, get, pop, setdefault, __contains__, __iter__, __repr__, after_this_request, index, add_header, copy_current_request_context, do_some_work, wrapper
**Dépendances** : __future__, contextvars, typing, functools, types, werkzeug.exceptions, werkzeug.routing, ., .globals, .helpers, .signals, typing_extensions
**API** : /

### `debughelpers.py`

Module Python. Nombre de lignes: 146. Elements detectés: class UnexpectedUnicodeError, class DebugFilesKeyError, def __init__

**Classes** : UnexpectedUnicodeError, DebugFilesKeyError, FormDataRoutingRedirect, newcls
**Fonctions** : __init__, __str__, attach_enctype_error_multidict, __getitem__, _dump_loader_info, explain_template_loading_attempts
**Dépendances** : __future__, typing, jinja2.loaders, werkzeug.routing, .blueprints, .globals, .sansio.app, .sansio.scaffold, .wrappers

### `globals.py`

Module Python. Nombre de lignes: 58. Elements detectés: class ProxyMixin, def _get_current_object, class FlaskProxy

**Classes** : ProxyMixin, FlaskProxy, AppContextProxy, _AppCtxGlobalsProxy, RequestProxy, SessionMixinProxy
**Fonctions** : _get_current_object, __getattr__
**Dépendances** : __future__, typing, contextvars, werkzeug.local, .app, .ctx, .sessions, .wrappers, warnings

### `helpers.py`

Module Python. Nombre de lignes: 534. Elements detectés: def get_debug_flag, def get_load_dotenv, def stream_with_context

**Classes** : _CollectErrors
**Fonctions** : get_debug_flag, get_load_dotenv, stream_with_context, streamed_response, generate, decorator, generator, make_response, index, url_for, redirect, abort, get_template_attribute, flash, get_flashed_messages
**Dépendances** : __future__, importlib.util, os, sys, typing, datetime, functools, types, werkzeug.utils, werkzeug.exceptions, werkzeug.wrappers, .globals
**API** : /stream, /uploads/<path:name>

### `logging.py`

Module Python. Nombre de lignes: 55. Elements detectés: def wsgi_errors_stream, def has_level_handler, def create_logger

**Fonctions** : wsgi_errors_stream, has_level_handler, create_logger
**Dépendances** : __future__, logging, sys, typing, werkzeug.local, .globals, .sansio.app

### `sessions.py`

Module Python. Nombre de lignes: 310. Elements detectés: class SessionMixin, def permanent, def permanent

**Classes** : SessionMixin, SecureCookieSession, NullSession, SessionInterface, Session, SecureCookieSessionInterface
**Fonctions** : permanent, __init__, on_update, _fail, make_null_session, is_null_session, get_cookie_name, get_cookie_domain, get_cookie_path, get_cookie_httponly, get_cookie_secure, get_cookie_samesite, get_cookie_partitioned, get_expiration_time, should_set_cookie
**Dépendances** : __future__, collections.abc, hashlib, typing, datetime, itsdangerous, werkzeug.datastructures, .json.tag, typing_extensions, .app, .wrappers

### `signals.py`

Module Python. Nombre de lignes: 14.

**Dépendances** : __future__, blinker

### `templating.py`

Module Python. Nombre de lignes: 166. Elements detectés: def _default_template_ctx_processor, class Environment, def __init__

**Classes** : Environment, DispatchingJinjaLoader
**Fonctions** : _default_template_ctx_processor, __init__, get_source, _get_source_explained, _get_source_fast, _iter_loaders, list_templates, _render, render_template, render_template_string, _stream, generate, stream_template, stream_template_string
**Dépendances** : __future__, typing, jinja2, .ctx, .globals, .helpers, .signals, .sansio.app, .sansio.scaffold, .debughelpers

### `testing.py`

Module Python. Nombre de lignes: 237. Elements detectés: class EnvironBuilder, def __init__, def json_dumps

**Classes** : EnvironBuilder, FlaskClient, FlaskCliRunner
**Fonctions** : __init__, json_dumps, _get_werkzeug_version, session_transaction, _copy_environ, _request_from_builder_args, open, __enter__, __exit__, invoke
**Dépendances** : __future__, importlib.metadata, typing, contextlib, copy, types, urllib.parse, werkzeug.test, click.testing, werkzeug.wrappers, .cli, .sessions

### `typing.py`

Module Python. Nombre de lignes: 77.

**Dépendances** : __future__, collections.abc, typing, _typeshed.wsgi, werkzeug.datastructures, werkzeug.sansio.response

### `views.py`

Module Python. Nombre de lignes: 146. Elements detectés: class View:, class Hello, def dispatch_request

**Classes** : View, Hello, MethodView, CounterAPI
**Fonctions** : dispatch_request, as_view, view, get, post, __init_subclass__
**Dépendances** : __future__, typing, ., .globals

### `wrappers.py`

Module Python. Nombre de lignes: 194. Elements detectés: class Request, def max_content_length, def max_content_length

**Classes** : Request, Response
**Fonctions** : max_content_length, max_form_memory_size, max_form_parts, endpoint, blueprint, blueprints, _load_form_data, on_json_loading_failed, max_cookie_size
**Dépendances** : __future__, typing, werkzeug.exceptions, werkzeug.wrappers, ., .globals, .helpers, werkzeug.routing, .debughelpers
