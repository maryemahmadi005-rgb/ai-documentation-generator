# Module : tests

23 fichier(s), 71 classe(s), 259 fonction(s).

## Vue d'ensemble

- **Classes principales** : AppError, AsyncMethodView, AsyncView, Base, BaseView, BetterIndex, BlueprintError, ChildExceptionRegistered, ChildExceptionUnregistered, ChildView, Config, ContextConverter
- **Fonctions principales** : __fspath__, __getattr__, __init__, _async_app, _param_cb, _standard_os_environ, add_x_parachute, after_request_handler, after_request_signal, app, app_ctx, app_forbidden, backend_forbidden, backend_no, before_request_handler
- **Dépendances** : __future__, asyncio, blueprintapp, click, click.testing, codecs, collections.abc, concurrent, config_module_app, config_package_app, contextlib, datetime
- **Endpoints API** : /, /<company_id>, /<ctx:name>, /<list:args>, /<self>, /abort, /action, /add, /args_unpack, /array

## Détail des fichiers

### `conftest.py`

Module Python. Nombre de lignes: 82. Elements detectés: def _standard_os_environ, def app, def app_ctx

**Fonctions** : _standard_os_environ, app, app_ctx, req_ctx, client, test_apps, leak_detector, modules_tmp_path, modules_tmp_path_prefix, site_packages, purge_module, inner
**Dépendances** : os, sys, pytest, flask, flask.globals

### `test_appctx.py`

Module Python. Nombre de lignes: 194. Elements detectés: def test_basic_url_generation, def index, def test_url_generation_requires_server_name

**Classes** : CustomRequestGlobals
**Fonctions** : test_basic_url_generation, index, test_url_generation_requires_server_name, test_url_generation_without_context_fails, test_request_context_means_app_context, test_app_context_provides_current_app, test_app_tearing_down, cleanup, test_app_tearing_down_with_previous_exception, test_app_tearing_down_with_handled_exception_by_except_block, test_app_tearing_down_with_handled_exception_by_app_handler, handler, test_app_tearing_down_with_unhandled_exception, test_app_ctx_globals_methods, test_custom_app_ctx_globals_class
**Dépendances** : sys, pytest, flask, flask.globals, flask.testing
**API** : /

### `test_async.py`

Module Python. Nombre de lignes: 104. Elements detectés: class AppError, class BlueprintError, class AsyncView

**Classes** : AppError, BlueprintError, AsyncView, AsyncMethodView
**Fonctions** : _async_app, test_async_route, test_async_error_handler, test_async_before_after_request, index, bp_index
**Dépendances** : asyncio, pytest, flask, flask.views
**API** : /, /home, /error

### `test_basic.py`

Module Python. Nombre de lignes: 1483. Elements detectés: def test_options_work, def index, def test_options_on_multiple_rules

**Classes** : PrefixPathMiddleware, MyException, ForbiddenSubclass, E1, E2, E3, View
**Fonctions** : test_options_work, index, test_options_on_multiple_rules, index_put, test_method_route, hello, test_method_route_no_methods, test_provide_automatic_options_attr_disable, test_provide_automatic_options_attr_enable, test_provide_automatic_options_arg_disable, test_provide_automatic_options_method_disable, test_request_dispatching, more, test_disallow_string_for_allowed_methods, test_url_mapping
**Dépendances** : gc, importlib.metadata, re, typing, uuid, weakref, contextlib, datetime, platform, pytest, werkzeug.serving, markupsafe
**API** : /, /more, /nothing, /clear, /test, /bump, /read, /set, /get, /getitem

### `test_blueprints.py`

Module Python. Nombre de lignes: 793. Elements detectés: def test_blueprint_specific_error_handling, def frontend_forbidden, def frontend_no

**Classes** : MyDecoratorException, MyFunctionException, MyBlueprint
**Fonctions** : test_blueprint_specific_error_handling, frontend_forbidden, frontend_no, backend_forbidden, backend_no, sideend_no, app_forbidden, test_blueprint_specific_user_error_handling, my_decorator_exception_handler, my_function_exception_handler, blue_deco_test, blue_func_test, test_blueprint_app_error_handling, forbidden_handler, bp_forbidden
**Dépendances** : pytest, jinja2, werkzeug.http, flask, blueprintapp, werkzeug.routing
**API** : /frontend-no, /backend-no, /what-is-a-sideend, /decorator, /function, /forbidden, /nope, /foo, /bar, /

### `test_cli.py`

Module Python. Nombre de lignes: 536. Elements detectés: def runner, def test_cli_name, def test_find_best_app

**Classes** : Module, MockCtx, TestRoutes
**Fonctions** : runner, test_cli_name, test_find_best_app, create_app, make_app, test_prepare_import, reset_path, test_locate_app, test_locate_app_raises, test_locate_app_suppress_raise, test_get_version, exit, test_scriptinfo, test_app_cli_has_app_context, _param_cb
**Dépendances** : importlib.metadata, os, platform, ssl, sys, types, functools, pathlib, click, pytest, click.testing, flask

### `test_config.py`

Module Python. Nombre de lignes: 193. Elements detectés: def common_object_test, def test_config_from_pyfile, def test_config_from_object

**Classes** : Base, Test, Config, Flask
**Fonctions** : common_object_test, test_config_from_pyfile, test_config_from_object, test_config_from_file_json, test_config_from_file_toml, test_from_prefixed_env, test_from_prefixed_env_custom_prefix, test_from_prefixed_env_nested, test_config_from_mapping, test_config_from_class, test_config_from_envvar, test_config_from_envvar_missing, test_config_missing, test_config_missing_file, test_custom_config_class
**Dépendances** : json, os, pytest, flask

### `test_converters.py`

Module Python. Nombre de lignes: 29. Elements detectés: def test_custom_converters, class ListConverter, def to_python

**Classes** : ListConverter, ContextConverter
**Fonctions** : test_custom_converters, to_python, to_url, index, test_context_available
**Dépendances** : werkzeug.routing, flask
**API** : /<list:args>, /<ctx:name>

### `test_helpers.py`

Module Python. Nombre de lignes: 273. Elements detectés: class FakePath:, def __init__, def __fspath__

**Classes** : FakePath, PyBytesIO, TestSendfile, StaticFileApp, TestUrlFor, MyView, MyAborter, MyFlask
**Fonctions** : __init__, __fspath__, __getattr__, test_send_file, test_static_file, get_send_file_max_age, test_send_from_directory, test_url_for_with_anchor, index, test_url_for_with_scheme, test_url_for_with_scheme_not_external, test_url_for_with_alternating_schemes, test_url_with_method, get, post
**Dépendances** : io, os, pytest, werkzeug.exceptions, flask, flask.helpers, flask.views
**API** : /, /<self>

### `test_instance_config.py`

Module Python. Nombre de lignes: 80. Elements detectés: def test_explicit_instance_paths, def test_uninstalled_module_paths, def test_uninstalled_package_paths

**Fonctions** : test_explicit_instance_paths, test_uninstalled_module_paths, test_uninstalled_package_paths, test_uninstalled_namespace_paths, create_namespace, test_installed_module_paths, test_installed_package_paths, test_prefix_package_paths
**Dépendances** : os, pytest, flask, config_module_app, config_package_app, namespace.package2, site_app, installed_package, site_package

### `test_json.py`

Module Python. Nombre de lignes: 272. Elements detectés: def test_bad_request_debug_message, def post_json, def test_json_bad_requests

**Classes** : FixedOffset, X, CustomProvider, ObjectWithHTML
**Fonctions** : test_bad_request_debug_message, post_json, test_json_bad_requests, return_json, test_json_custom_mimetypes, test_json_as_unicode, test_json_dump_to_file, test_jsonify_basic_types, test_jsonify_dicts, return_kwargs, return_dict, test_jsonify_arrays, return_args_unpack, return_array, test_jsonify_datetime
**Dépendances** : datetime, decimal, io, uuid, pytest, werkzeug.http, flask, flask.json.provider, codecs
**API** : /json, /kw, /dict, /args_unpack, /array, /, /add

### `test_json_tag.py`

Module Python. Nombre de lignes: 64. Elements detectés: def test_dump_load_unchanged, def test_duplicate_tag, class TagDict

**Classes** : TagDict, Foo, TagFoo, Tag1, Tag2
**Fonctions** : test_dump_load_unchanged, test_duplicate_tag, test_custom_tag, __init__, check, to_json, to_python, test_tag_interface, test_tag_order
**Dépendances** : datetime, uuid, pytest, markupsafe, flask.json.tag

### `test_logging.py`

Module Python. Nombre de lignes: 69. Elements detectés: def reset_logging, def test_logger, def test_logger_debug

**Fonctions** : reset_logging, test_logger, test_logger_debug, test_existing_handler, test_wsgi_errors_stream, index, test_has_level_handler, test_log_view_exception
**Dépendances** : logging, sys, io, pytest, flask.logging
**API** : /

### `test_regression.py`

Module Python. Nombre de lignes: 22. Elements detectés: def test_aborting, class Foo, def handle_foo

**Classes** : Foo
**Fonctions** : test_aborting, handle_foo, index, test
**Dépendances** : flask
**API** : /, /test

### `test_reqctx.py`

Module Python. Nombre de lignes: 190. Elements detectés: def test_teardown_on_pop, def end_of_request, def test_teardown_with_previous_exception

**Classes** : SessionError, FailingSessionInterface, CustomFlask, PathAwareSessionInterface
**Fonctions** : test_teardown_on_pop, end_of_request, test_teardown_with_previous_exception, test_teardown_with_handled_exception, test_proper_test_request_context, index, sub, test_context_binding, meh, test_context_test, test_manual_context_binding, test_copy_context_thread, work, test_session_error_pops_context, open_session
**Dépendances** : __future__, collections.abc, warnings, concurrent, pytest, flask, flask.sessions, flask.testing
**API** : /, /meh, /set, /get, /set_dynamic_cookie, /get_dynamic_cookie

### `test_request.py`

Module Python. Nombre de lignes: 53. Elements detectés: def test_max_content_length, def index, def catcher

**Fonctions** : test_max_content_length, index, catcher, test_limit_config, test_trusted_hosts_config
**Dépendances** : __future__, flask, flask.testing
**API** : /

### `test_session_interface.py`

Module Python. Nombre de lignes: 21. Elements detectés: def test_open_session_with_endpoint, class MySessionInterface, def save_session

**Classes** : MySessionInterface
**Fonctions** : test_open_session_with_endpoint, save_session, open_session, index
**Dépendances** : flask, flask.globals, flask.sessions
**API** : /

### `test_signals.py`

Module Python. Nombre de lignes: 139. Elements detectés: def test_template_rendered, def index, def record

**Fonctions** : test_template_rendered, index, record, test_before_render_template, test_request_signals, before_request_signal, after_request_signal, before_request_handler, after_request_handler, test_request_exception_signal, test_appcontext_signals, record_push, record_pop, test_flash_signal, test_appcontext_tearing_down_signal
**Dépendances** : flask
**API** : /

### `test_subclassing.py`

Module Python. Nombre de lignes: 15. Elements detectés: def test_suppressed_exception_logging, class SuppressedFlask, def log_exception

**Classes** : SuppressedFlask
**Fonctions** : test_suppressed_exception_logging, log_exception, index
**Dépendances** : io, flask
**API** : /

### `test_templating.py`

Module Python. Nombre de lignes: 387. Elements detectés: def test_context_processing, def context_processor, def index

**Classes** : MyFlask, _TestHandler, CustomEnvironment, CustomFlask
**Fonctions** : test_context_processing, context_processor, index, test_original_win, test_simple_stream, test_request_less_rendering, test_standard_context, test_escaping, test_no_escaping, test_escaping_without_template_filename, test_macros, test_template_filter, my_reverse, my_reverse_2, my_reverse_3
**Dépendances** : logging, pytest, werkzeug.serving, jinja2, markupsafe, flask, blueprintapp
**API** : /

### `test_testing.py`

Module Python. Nombre de lignes: 277. Elements detectés: def test_environ_defaults_from_config, def index, def test_environ_defaults

**Classes** : Namespace, SubRunner, NS
**Fonctions** : test_environ_defaults_from_config, index, test_environ_defaults, test_environ_base_default, test_environ_base_modified, test_client_open_environ, test_specify_url_scheme, test_path_is_url, test_environbuilder_json_dumps, test_blueprint_with_subdomain, test_redirect_session, get_session, test_session_transactions, test_session_transactions_no_null_sessions, test_session_transactions_keep_context
**Dépendances** : importlib.metadata, click, pytest, flask, flask.cli, flask.globals, flask.json, flask.testing
**API** : /, /index, /redirect, /target, /other, /action, /echo, /hello, /<company_id>

### `test_user_error_handler.py`

Module Python. Nombre de lignes: 215. Elements detectés: def test_error_handler_no_match, class CustomException, def custom_exception_handler

**Classes** : CustomException, ParentException, ChildExceptionUnregistered, ChildExceptionRegistered, ForbiddenSubclassRegistered, ForbiddenSubclassUnregistered, TestGenericHandlers, Custom
**Fonctions** : test_error_handler_no_match, custom_exception_handler, handle_500, custom_test, key_error, do_abort, test_error_handler_subclass, parent_exception_handler, child_exception_handler, parent_test, unregistered_test, registered_test, test_error_handler_http_subclass, code_exception_handler, subclass_exception_handler
**Dépendances** : pytest, werkzeug.exceptions, flask
**API** : /custom, /keyerror, /abort, /parent, /child-unregistered, /child-registered, /forbidden, /forbidden-registered, /forbidden-unregistered, /error

### `test_views.py`

Module Python. Nombre de lignes: 188. Elements detectés: def common_test, def test_basic_view, class Index

**Classes** : Index, Other, BetterIndex, BaseView, ChildView, GetView, DeleteView, GetDeleteView
**Fonctions** : common_test, test_basic_view, dispatch_request, test_method_based_view, get, post, test_view_patching, test_view_inheritance, delete, test_view_decorators, add_x_parachute, new_function, test_view_provide_automatic_options_attr_disable, test_view_provide_automatic_options_attr_enable, test_provide_automatic_options_method_disable
**Dépendances** : pytest, werkzeug.http, flask.views, flask.testing
