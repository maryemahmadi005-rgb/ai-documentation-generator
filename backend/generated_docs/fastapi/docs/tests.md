# Module : tests

211 fichier(s), 212 classe(s), 1259 fonction(s).

## Vue d'ensemble

- **Classes principales** : A, APIRouteA, APIRouteB, APIRouteC, Address, AsyncCallableDependency, AsyncCallableGenDependency, AsyncDependencyError, AuthHeaders, B, BaseUser, CallableDependency
- **Fonctions principales** : __bool__, __call__, __class__, __dict__, __eq__, __hash__, __init__, __iter__, __str__, _get_client_key, _get_client_tag, _make_orjson_app, _make_ujson_app, acquire_session, add_background_task
- **Dépendances** : .forward_reference_type, .main, .utils, __future__, anyio, asyncio, base64, collections, collections.abc, contextlib, contextvars, dataclasses
- **Endpoints API** : /, /a, /a/{id}, /admin, /api, /api/, /api/users, /app, /app-scope-function, /app-scope-request

## Détail des fichiers

### `forward_reference_type.py`

Module Python. Nombre de lignes: 5. Elements detectés: def forwardref_method, class ForwardRefModel

**Classes** : ForwardRefModel
**Fonctions** : forwardref_method
**Dépendances** : pydantic

### `main.py`

Module Python. Nombre de lignes: 127. Elements detectés: def non_operation, def non_decorated_route, def get_text

**Fonctions** : non_operation, non_decorated_route, get_text, get_id, get_str_id, get_int_id, get_float_id, get_bool_id, get_path_param_id, get_path_param_min_length, get_path_param_max_length, get_path_param_min_max_length, get_path_param_gt, get_path_param_gt0, get_path_param_ge
**Dépendances** : http, fastapi
**API** : /text, /path/{item_id}, /path/str/{item_id}, /path/int/{item_id}, /path/float/{item_id}, /path/bool/{item_id}, /path/param/{item_id}, /path/param-minlength/{item_id}, /path/param-maxlength/{item_id}, /path/param-min_maxlength/{item_id}

### `test_additional_properties.py`

Module Python. Nombre de lignes: 103. Elements detectés: class Items, def foo, def test_additional_properties_post

**Classes** : Items
**Fonctions** : foo, test_additional_properties_post, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /foo

### `test_additional_properties_bool.py`

Module Python. Nombre de lignes: 109. Elements detectés: class FooBaseModel, class Foo, def test_call_invalid

**Classes** : FooBaseModel, Foo
**Fonctions** : test_call_invalid, test_call_valid, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /

### `test_additional_response_extra.py`

Module Python. Nombre de lignes: 39. Elements detectés: def read_item, def test_path_operation, def test_openapi_schema

**Fonctions** : read_item, test_path_operation, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot
**API** : /

### `test_additional_responses_bad.py`

Module Python. Nombre de lignes: 32. Elements detectés: def test_openapi_schema

**Fonctions** : test_openapi_schema
**Dépendances** : pytest, fastapi, fastapi.testclient
**API** : /a

### `test_additional_responses_custom_model_in_callback.py`

Module Python. Nombre de lignes: 134. Elements detectés: class CustomModel, def callback_route, def main_route

**Classes** : CustomModel
**Fonctions** : callback_route, main_route, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot, pydantic, starlette.responses
**API** : {$callback_url}/callback/, /

### `test_additional_responses_custom_validationerror.py`

Module Python. Nombre de lignes: 87. Elements detectés: class JsonApiResponse, class Error, class JsonApiError

**Classes** : JsonApiResponse, Error, JsonApiError
**Fonctions** : test_openapi_schema
**Dépendances** : fastapi, fastapi.responses, fastapi.testclient, inline_snapshot, pydantic
**API** : /a/{id}

### `test_additional_responses_default_validationerror.py`

Module Python. Nombre de lignes: 84. Elements detectés: def test_openapi_schema

**Fonctions** : test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot
**API** : /a/{id}

### `test_additional_responses_response_class.py`

Module Python. Nombre de lignes: 102. Elements detectés: class JsonApiResponse, class Error, class JsonApiError

**Classes** : JsonApiResponse, Error, JsonApiError
**Fonctions** : test_openapi_schema
**Dépendances** : fastapi, fastapi.responses, fastapi.testclient, inline_snapshot, pydantic
**API** : /a, /b

### `test_additional_responses_router.py`

Module Python. Nombre de lignes: 156. Elements detectés: class ResponseModel, def test_a, def test_b

**Classes** : ResponseModel
**Fonctions** : test_a, test_b, test_c, test_d, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /a, /b, /c, /d

### `test_additional_responses_union_duplicate_anyof.py`

Module Python. Nombre de lignes: 109. Elements detectés: class ModelA, class ModelB, def test_openapi_schema

**Classes** : ModelA, ModelB
**Fonctions** : test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /route1, /route2

### `test_allow_inf_nan_in_enforcing.py`

Module Python. Nombre de lignes: 70. Elements detectés: def test_allow_inf_nan_param_true, def test_allow_inf_nan_param_false, def test_allow_inf_nan_param_default

**Fonctions** : test_allow_inf_nan_param_true, test_allow_inf_nan_param_false, test_allow_inf_nan_param_default, test_allow_inf_nan_body
**Dépendances** : typing, pytest, fastapi, fastapi.testclient
**API** : /

### `test_ambiguous_params.py`

Module Python. Nombre de lignes: 57. Elements detectés: def test_no_annotated_defaults, def test_multiple_annotations

**Fonctions** : test_no_annotated_defaults, test_multiple_annotations
**Dépendances** : typing, pytest, fastapi, fastapi.param_functions, fastapi.testclient
**API** : /items/{item_id}/, /, /multi-query

### `test_annotated.py`

Module Python. Nombre de lignes: 267. Elements detectés: def test_get, def test_multiple_path, def test_nested_router

**Fonctions** : test_get, test_multiple_path, test_nested_router, test_openapi_schema
**Dépendances** : typing, pytest, fastapi, fastapi.testclient, inline_snapshot
**API** : /default, /required, /multiple, /unrelated, /test1, /test2, /test

### `test_application.py`

Module Python. Nombre de lignes: 1271. Elements detectés: def test_get_path, def test_swagger_ui, def test_swagger_ui_oauth2_redirect

**Fonctions** : test_get_path, test_swagger_ui, test_swagger_ui_oauth2_redirect, test_redoc, test_enum_status_code_response, test_openapi_schema
**Dépendances** : pytest, fastapi.testclient, inline_snapshot, .main

### `test_arbitrary_types.py`

Module Python. Nombre de lignes: 116. Elements detectés: def get_client, class FakeNumpyArray:, def __init__

**Classes** : FakeNumpyArray, MyModel
**Fonctions** : get_client, __init__, test, test_get, test_typeadapter, test_openapi_schema
**Dépendances** : typing, pytest, fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /

### `test_callable_endpoint.py`

Module Python. Nombre de lignes: 13. Elements detectés: def main, def test_partial

**Fonctions** : main, test_partial
**Dépendances** : functools, fastapi, fastapi.testclient

### `test_compat.py`

Module Python. Nombre de lignes: 107. Elements detectés: def test_model_field_default_required, def test_complex, def foo

**Classes** : Missing, EmbeddedModel, Model
**Fonctions** : test_model_field_default_required, test_complex, foo, test_propagates_pydantic2_model_config, __bool__, test_is_bytes_sequence_annotation_union, test_is_uploadfile_sequence_annotation, test_serialize_sequence_value_with_optional_list, test_serialize_sequence_value_with_optional_list_pipe_union, test_serialize_sequence_value_with_none_first_in_union
**Dépendances** : typing, fastapi, fastapi._compat, fastapi._compat.shared, fastapi.testclient, pydantic, pydantic.fields
**API** : /

### `test_computed_fields.py`

Module Python. Nombre de lignes: 96. Elements detectés: def get_client, class Rectangle, def area

**Classes** : Rectangle
**Fonctions** : get_client, area, read_root, read_responses, test_get, test_openapi_schema
**Dépendances** : pytest, fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /, /responses

### `test_custom_middleware_exception.py`

Module Python. Nombre de lignes: 72. Elements detectés: class ContentSizeLimitMiddleware:, def __init__, def receive_wrapper

**Classes** : ContentSizeLimitMiddleware
**Fonctions** : __init__, receive_wrapper, run_middleware, test_custom_middleware_exception, test_custom_middleware_exception_not_raised
**Dépendances** : pathlib, fastapi, fastapi.exceptions, fastapi.testclient, starlette.types
**API** : /middleware

### `test_custom_route_class.py`

Module Python. Nombre de lignes: 91. Elements detectés: class APIRouteA, class APIRouteB, class APIRouteC

**Classes** : APIRouteA, APIRouteB, APIRouteC
**Fonctions** : get_a, get_b, get_c, test_get_path, test_route_classes, test_openapi_schema
**Dépendances** : pytest, fastapi, fastapi.routing, fastapi.testclient, inline_snapshot
**API** : /

### `test_custom_schema_fields.py`

Module Python. Nombre de lignes: 46. Elements detectés: class Item, def foo, def test_custom_response_schema

**Classes** : Item
**Fonctions** : foo, test_custom_response_schema, test_response
**Dépendances** : typing, fastapi, fastapi.testclient, pydantic
**API** : /foo

### `test_custom_swagger_ui_redirect.py`

Module Python. Nombre de lignes: 26. Elements detectés: def test_swagger_ui, def test_swagger_ui_oauth2_redirect, def test_response

**Fonctions** : test_swagger_ui, test_swagger_ui_oauth2_redirect, test_response
**Dépendances** : fastapi, fastapi.testclient
**API** : /items/

### `test_datastructures.py`

Module Python. Nombre de lignes: 49. Elements detectés: def test_upload_file_invalid_pydantic_v2, def test_default_placeholder_equals, def test_default_placeholder_bool

**Fonctions** : test_upload_file_invalid_pydantic_v2, test_default_placeholder_equals, test_default_placeholder_bool, test_upload_file_is_closed, create_upload_file
**Dépendances** : io, pathlib, typing, pytest, fastapi, fastapi.datastructures, fastapi.testclient
**API** : /uploadfile/

### `test_datetime_custom_encoder.py`

Module Python. Nombre de lignes: 20. Elements detectés: def test_pydanticv2, class ModelWithDatetimeField, def serialize_datetime

**Classes** : ModelWithDatetimeField
**Fonctions** : test_pydanticv2, serialize_datetime, get_model
**Dépendances** : datetime, fastapi, fastapi.testclient, pydantic
**API** : /model

### `test_default_response_class.py`

Module Python. Nombre de lignes: 151. Elements detectés: class ORJSONResponse, def render, class OverrideResponse

**Classes** : ORJSONResponse, OverrideResponse
**Fonctions** : render, get_root, get_path_override, get_a, get_a_path_override, get_a_a, get_a_a_path_override, get_a_b, get_a_b_path_override, get_b, get_b_path_override, get_b_a, get_b_a_path_override, get_b_a_c, get_b_a_c_path_override
**Dépendances** : typing, fastapi, fastapi.responses, fastapi.testclient, tests.utils, orjson
**API** : /, /override

### `test_default_response_class_router.py`

Module Python. Nombre de lignes: 141. Elements detectés: class OverrideResponse, def get_root, def get_path_override

**Classes** : OverrideResponse
**Fonctions** : get_root, get_path_override, get_a, get_a_path_override, get_a_a, get_a_a_path_override, get_a_b, get_a_b_path_override, get_b, get_b_path_override, get_b_a, get_b_a_path_override, get_b_a_c, get_b_a_c_path_override, test_app
**Dépendances** : fastapi, fastapi.responses, fastapi.testclient
**API** : /, /override

### `test_dependency_after_yield_raise.py`

Module Python. Nombre de lignes: 45. Elements detectés: class CustomError, def catching_dep, def broken_dep

**Classes** : CustomError
**Fonctions** : catching_dep, broken_dep, catching, broken, test_catching, test_broken_raise, test_broken_no_raise, test_broken_return_finishes
**Dépendances** : typing, pytest, fastapi, fastapi.testclient
**API** : /catching, /broken

### `test_dependency_after_yield_streaming.py`

Module Python. Nombre de lignes: 88. Elements detectés: class Session:, def __init__, def __iter__

**Classes** : Session
**Fonctions** : __init__, __iter__, acquire_session, dep_session, broken_dep_session, get_data, get_stream_simple, iter_data, get_stream_session, get_broken_session_data, get_broken_session_stream, test_regular_no_stream, test_stream_simple, test_stream_session, test_broken_session_data
**Dépendances** : collections.abc, contextlib, typing, pytest, fastapi, fastapi.responses, fastapi.testclient
**API** : /data, /stream-simple, /stream-session, /broken-session-data, /broken-session-stream

### `test_dependency_after_yield_websockets.py`

Module Python. Nombre de lignes: 56. Elements detectés: class Session:, def __init__, def __iter__

**Classes** : Session
**Fonctions** : __init__, __iter__, acquire_session, dep_session, broken_dep_session, test_websocket_dependency_after_yield, test_websocket_dependency_after_yield_broken
**Dépendances** : collections.abc, contextlib, typing, pytest, fastapi, fastapi.testclient

### `test_dependency_cache.py`

Module Python. Nombre de lignes: 67. Elements detectés: def test_normal_counter, def test_sub_counter, def test_sub_counter_no_cache

**Fonctions** : test_normal_counter, test_sub_counter, test_sub_counter_no_cache, test_security_cache
**Dépendances** : fastapi, fastapi.testclient
**API** : /counter/, /sub-counter/, /sub-counter-no-cache/, /scope-counter

### `test_dependency_class.py`

Module Python. Nombre de lignes: 109. Elements detectés: class CallableDependency:, def __call__, class CallableGenDependency:

**Classes** : CallableDependency, CallableGenDependency, AsyncCallableDependency, AsyncCallableGenDependency, MethodsDependency
**Fonctions** : __call__, synchronous, synchronous_gen, test_class_dependency
**Dépendances** : collections.abc, pytest, fastapi, fastapi.testclient
**API** : /callable-dependency-class, /callable-gen-dependency-class, /async-callable-dependency-class, /async-callable-gen-dependency-class, /callable-dependency, /callable-gen-dependency, /async-callable-dependency, /async-callable-gen-dependency, /synchronous-method-dependency, /synchronous-method-gen-dependency

### `test_dependency_contextmanager.py`

Module Python. Nombre de lignes: 288. Elements detectés: class AsyncDependencyError, class SyncDependencyError, class OtherDependencyError

**Classes** : AsyncDependencyError, SyncDependencyError, OtherDependencyError
**Fonctions** : generator_state, generator_state_try, get_sync_async, get_sync_sync, get_sync_async_raise, get_sync_sync_raise, get_sync_async_raise_other, get_sync_sync_raise_other, get_sync_context_b, get_sync_context_b_raise, test_async_state, test_sync_state, test_async_raise_other, test_sync_raise_other, test_async_raise_raises
**Dépendances** : json, pytest, fastapi, fastapi.responses, fastapi.testclient
**API** : /async, /sync, /async_raise, /sync_raise, /async_raise_other, /sync_raise_other, /context_b, /context_b_raise, /context_b_bg, /sync_async

### `test_dependency_contextvars.py`

Module Python. Nombre de lignes: 37. Elements detectés: def get_user, def test_dependency_contextvars

**Fonctions** : get_user, test_dependency_contextvars
**Dépendances** : collections.abc, contextvars, typing, fastapi, fastapi.testclient
**API** : /user

### `test_dependency_duplicates.py`

Module Python. Nombre de lignes: 211. Elements detectés: class Item, def duplicate_dependency, def dependency

**Classes** : Item
**Fonctions** : duplicate_dependency, dependency, sub_duplicate_dependency, test_no_duplicates_invalid, test_no_duplicates, test_duplicates, test_sub_duplicates, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /with-duplicates, /no-duplicates, /with-duplicates-sub

### `test_dependency_models.py`

Module Python. Nombre de lignes: 145. Elements detectés: def sync_dependency, def generator_dependency, class UnhashableCallable:

**Classes** : UnhashableCallable, UnhashableGeneratorCallable, UnhashableAsyncGeneratorCallable, EqualCallable, EqualAsyncCallable, EqualSyncCallable, CallableWithUnhashableReturn
**Fonctions** : sync_dependency, generator_dependency, __call__, __eq__, __hash__, test_callable_classification_is_shared_by_call, test_callable_classification_cache_supports_large_apps, test_unhashable_callable_classification, test_equal_callable_instances_are_cached_by_identity, test_callable_classification, test_derived_values_are_not_stored_on_dependant, test_security_scheme_helpers, test_derived_values_follow_dependency_state, test_explicit_and_generator_scopes, test_callable_return_annotations_are_not_used
**Dépendances** : collections.abc, typing, fastapi.dependencies.models, fastapi.security

### `test_dependency_overrides.py`

Module Python. Nombre de lignes: 310. Elements detectés: def test_main_depends, def test_main_depends_q_foo, def test_main_depends_q_foo_skip_100_limit_200

**Fonctions** : test_main_depends, test_main_depends_q_foo, test_main_depends_q_foo_skip_100_limit_200, test_decorator_depends, test_decorator_depends_q_foo, test_decorator_depends_q_foo_skip_100_limit_200, test_router_depends, test_router_depends_q_foo, test_router_depends_q_foo_skip_100_limit_200, test_router_decorator_depends, test_router_decorator_depends_q_foo, test_router_decorator_depends_q_foo_skip_100_limit_200, test_override_simple, test_override_with_sub_main_depends, test_override_with_sub__main_depends_q_foo
**Dépendances** : pytest, fastapi, fastapi.testclient
**API** : /main-depends/, /decorator-depends/, /router-depends/, /router-decorator-depends/

### `test_dependency_paramless.py`

Module Python. Nombre de lignes: 56. Elements detectés: def process_auth, def get_credentials, def get_parameterless_with_scopes

**Fonctions** : process_auth, get_credentials, get_parameterless_with_scopes, get_parameterless_without_scopes, test_get_credentials, test_parameterless_with_scopes, test_parameterless_without_scopes, test_call_get_parameterless_without_scopes_for_coverage
**Dépendances** : typing, fastapi, fastapi.security, fastapi.testclient
**API** : /get-credentials, /parameterless-with-scopes, /parameterless-without-scopes

### `test_dependency_partial.py`

Module Python. Nombre de lignes: 198. Elements detectés: def function_dependency, def gen_dependency, class CallableDependency:

**Classes** : CallableDependency, CallableGenDependency, AsyncCallableDependency, AsyncCallableGenDependency, MethodsDependency
**Fonctions** : function_dependency, gen_dependency, __call__, synchronous, synchronous_gen, test_dependency_types_with_partial
**Dépendances** : collections.abc, functools, typing, pytest, fastapi, fastapi.testclient
**API** : /partial-function-dependency, /partial-async-function-dependency, /partial-gen-dependency, /partial-async-gen-dependency, /partial-callable-dependency, /partial-callable-gen-dependency, /partial-async-callable-dependency, /partial-async-callable-gen-dependency, /partial-synchronous-method-dependency, /partial-synchronous-method-gen-dependency

### `test_dependency_pep695.py`

Module Python. Nombre de lignes: 18. Elements detectés: def test_pep695_type_dependencies

**Fonctions** : test_pep695_type_dependencies
**Dépendances** : typing, fastapi, fastapi.testclient, typing_extensions
**API** : /

### `test_dependency_security_overrides.py`

Module Python. Nombre de lignes: 44. Elements detectés: def get_user, def get_user_override, def get_data

**Fonctions** : get_user, get_user_override, get_data, get_data_override, read_user, test_normal, test_override_data, test_override_security
**Dépendances** : fastapi, fastapi.security, fastapi.testclient
**API** : /user

### `test_dependency_wrapped.py`

Module Python. Nombre de lignes: 303. Elements detectés: def noop_wrap, def wrapper, def noop_wrap_async

**Classes** : ClassInstanceDep, ClassInstanceGenDep, ClassInstanceWrappedDep, ClassInstanceWrappedAsyncDep, ClassInstanceWrappedGenDep, ClassInstanceWrappedAsyncGenDep, ClassDep, ClassInstanceAsyncDep
**Fonctions** : noop_wrap, wrapper, noop_wrap_async, __call__, __init__, wrapped_dependency, wrapped_gen_dependency, get_wrapped_endpoint, wrapped_dependency_async_wrapper, wrapped_gen_dependency_async_wrapper, get_wrapped_endpoint_async_wrapper, test_class_dependency
**Dépendances** : inspect, sys, collections.abc, functools, pytest, fastapi, fastapi.concurrency, fastapi.testclient, asyncio
**API** : /wrapped-dependency/, /wrapped-gen-dependency/, /async-wrapped-dependency/, /async-wrapped-gen-dependency/, /wrapped-class-instance-dependency/, /wrapped-class-instance-async-dependency/, /wrapped-class-instance-gen-dependency/, /wrapped-class-instance-async-gen-dependency/, /class-instance-wrapped-dependency/, /class-instance-wrapped-async-dependency/

### `test_dependency_yield_except_httpexception.py`

Module Python. Nombre de lignes: 53. Elements detectés: def put_invalid_user, def put_user, def reset_state_and_db

**Fonctions** : put_invalid_user, put_user, reset_state_and_db, test_dependency_gets_exception, test_dependency_no_exception
**Dépendances** : pytest, fastapi, fastapi.testclient
**API** : /invalid-user/{user_id}, /user/{user_id}

### `test_dependency_yield_scope.py`

Module Python. Nombre de lignes: 171. Elements detectés: class Session:, def __init__, def dep_session

**Classes** : Session, NamedSession
**Fonctions** : __init__, dep_session, raise_after_yield, get_named_session, get_named_func_session, get_named_regular_func_session, get_index, function_scope, iter_data, request_scope, get_stream_session, get_sub, get_named_function_scope, get_regular_function_scope, test_function_scope
**Dépendances** : json, typing, pytest, fastapi, fastapi.exceptions, fastapi.responses, fastapi.testclient
**API** : /, /function-scope, /request-scope, /two-scopes, /sub, /named-function-scope, /regular-function-scope, /broken-scope, /app-scope-function, /app-scope-request

### `test_dependency_yield_scope_websockets.py`

Module Python. Nombre de lignes: 149. Elements detectés: class Session:, def __init__, class NamedSession:

**Classes** : Session, NamedSession
**Fonctions** : __init__, get_named_session, get_named_func_session, get_named_regular_func_session, test_function_scope, test_request_scope, test_two_scopes, test_sub, test_broken_scope, test_named_function_scope, test_regular_function_scope
**Dépendances** : contextvars, typing, pytest, fastapi, fastapi.exceptions, fastapi.testclient

### `test_depends_hashable.py`

Module Python. Nombre de lignes: 18. Elements detectés: def dep, def test_depends_hashable

**Fonctions** : dep, test_depends_hashable
**Dépendances** : fastapi

### `test_deprecated_openapi_prefix.py`

Module Python. Nombre de lignes: 36. Elements detectés: def read_main, def test_main, def test_openapi

**Fonctions** : read_main, test_main, test_openapi
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot
**API** : /app

### `test_deprecated_responses.py`

Module Python. Nombre de lignes: 55. Elements detectés: class Item, def _make_orjson_app, def get_items

**Classes** : Item
**Fonctions** : _make_orjson_app, get_items, test_orjson_response_returns_correct_data, test_orjson_response_emits_deprecation_warning, _make_ujson_app, test_ujson_response_returns_correct_data, test_ujson_response_emits_deprecation_warning
**Dépendances** : warnings, pytest, fastapi, fastapi.exceptions, fastapi.responses, fastapi.testclient, pydantic, tests.utils
**API** : /items

### `test_dump_json_fast_path.py`

Module Python. Nombre de lignes: 36. Elements detectés: class Item, def get_default, def get_explicit

**Classes** : Item
**Fonctions** : get_default, get_explicit, test_default_response_class_skips_json_dumps, test_explicit_response_class_uses_json_dumps
**Dépendances** : unittest.mock, fastapi, fastapi.responses, fastapi.testclient, pydantic
**API** : /default, /explicit

### `test_duplicate_models_openapi.py`

Module Python. Nombre de lignes: 69. Elements detectés: class Model, class Model2, class Model3

**Classes** : Model, Model2, Model3
**Fonctions** : f, test_get_api_route, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /

### `test_empty_router.py`

Module Python. Nombre de lignes: 23. Elements detectés: def get_empty, def test_use_empty, def test_include_empty

**Fonctions** : get_empty, test_use_empty, test_include_empty
**Dépendances** : pytest, fastapi, fastapi.exceptions, fastapi.testclient

### `test_enforce_once_required_parameter.py`

Module Python. Nombre de lignes: 100. Elements detectés: def _get_client_key, def _get_client_tag, def foo_handler

**Fonctions** : _get_client_key, _get_client_tag, foo_handler, test_get_invalid, test_get_valid, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot
**API** : /foo

### `test_exception_handlers.py`

Module Python. Nombre de lignes: 57. Elements detectés: def http_exception_handler, def request_validation_exception_handler, def server_error_exception_handler

**Fonctions** : http_exception_handler, request_validation_exception_handler, server_error_exception_handler, raise_value_error, dependency_with_yield, with_yield, route_with_http_exception, route_with_request_validation_exception, route_with_server_error, test_override_http_exception, test_override_request_validation_exception, test_override_server_error_exception_raises, test_override_server_error_exception_response, test_traceback_for_dependency_with_yield
**Dépendances** : pytest, fastapi, fastapi.exceptions, fastapi.testclient, starlette.responses
**API** : /dependency-with-yield, /http-exception, /request-validation/{param}/, /server-error

### `test_extra_routes.py`

Module Python. Nombre de lignes: 333. Elements detectés: class Item, def get_items, def get_not_decorated

**Classes** : Item
**Fonctions** : get_items, get_not_decorated, delete_item, head_item, options_item, patch_item, trace_item, test_get_api_route, test_get_api_route_not_decorated, test_delete, test_head, test_options, test_patch, test_trace, test_openapi_schema
**Dépendances** : fastapi, fastapi.responses, fastapi.testclient, inline_snapshot, pydantic
**API** : /items/{item_id}

### `test_fastapi_cli.py`

Module Python. Nombre de lignes: 29. Elements detectés: def test_fastapi_cli, def test_fastapi_cli_not_installed

**Fonctions** : test_fastapi_cli, test_fastapi_cli_not_installed
**Dépendances** : os, subprocess, sys, unittest.mock, fastapi.cli, pytest

### `test_file_and_form_order_issue_9116.py`

Module Python. Nombre de lignes: 68. Elements detectés: def file_before_form, def file_after_form, def file_list_before_form

**Fonctions** : file_before_form, file_after_form, file_list_before_form, file_list_after_form, tmp_file_1, tmp_file_2, test_file_form_order, test_file_list_form_order
**Dépendances** : pathlib, typing, pytest, fastapi, fastapi.testclient
**API** : /file_before_form, /file_after_form, /file_list_before_form, /file_list_after_form

### `test_filter_pydantic_sub_model_pv2.py`

Module Python. Nombre de lignes: 166. Elements detectés: def get_client, class ModelB, class ModelC

**Classes** : ModelB, ModelC, ModelA
**Fonctions** : get_client, lower_username, test_filter_sub_model, test_validator_is_cloned, test_openapi_schema
**Dépendances** : pytest, dirty_equals, fastapi, fastapi.exceptions, fastapi.testclient, inline_snapshot, pydantic
**API** : /model/{name}

### `test_form_default.py`

Module Python. Nombre de lignes: 22. Elements detectés: def test_form_default_url_encoded, def test_form_default_multi_part

**Fonctions** : test_form_default_url_encoded, test_form_default_multi_part
**Dépendances** : typing, fastapi, starlette.testclient
**API** : /urlencoded, /multipart

### `test_forms_from_non_typing_sequences.py`

Module Python. Nombre de lignes: 31. Elements detectés: def post_form_param_list, def post_form_param_set, def post_form_param_tuple

**Fonctions** : post_form_param_list, post_form_param_set, post_form_param_tuple, test_python_list_param_as_form, test_python_set_param_as_form, test_python_tuple_param_as_form
**Dépendances** : fastapi, fastapi.testclient
**API** : /form/python-list, /form/python-set, /form/python-tuple

### `test_forms_single_model.py`

Module Python. Nombre de lignes: 116. Elements detectés: class FormModel, class FormModelExtraAllow, def post_form

**Classes** : FormModel, FormModelExtraAllow
**Fonctions** : post_form, post_form_extra_allow, test_send_all_data, test_defaults, test_invalid_data, test_no_data, test_extra_param_single, test_extra_param_list
**Dépendances** : typing, fastapi, fastapi.testclient, pydantic
**API** : /form/, /form-extra-allow/

### `test_forms_single_param.py`

Module Python. Nombre de lignes: 99. Elements detectés: def post_form, def test_single_form_field, def test_openapi_schema

**Fonctions** : post_form, test_single_form_field, test_openapi_schema
**Dépendances** : typing, fastapi, fastapi.testclient, inline_snapshot
**API** : /form/

### `test_frontend.py`

Module Python. Nombre de lignes: 1051. Elements detectés: def write_file, def record_dependency, def dependency

**Classes** : PartialRoute
**Fonctions** : write_file, record_dependency, dependency, test_frontend_exact_prefix_path_serves_index, test_apirouter_frontend_with_router_prefix_and_frontend_subpath, test_frontend_fallback_rejects_invalid_fallback, test_index_fallback_ignores_invalid_q_value, test_frontend_static_files_lookup_errors, raise_permission_error, raise_value_error, raise_name_too_long, raise_os_error, test_frontend_route_group_helpers, test_included_low_priority_routes_cache_is_reused, test_low_priority_api_route_handles_with_context
**Dépendances** : errno, os, runpy, contextlib, pathlib, typing, anyio, pytest, fastapi, fastapi.testclient, starlette.exceptions, starlette.responses
**API** : /api, /api/users, /dashboard, /api/

### `test_generate_unique_id_function.py`

Module Python. Nombre de lignes: 1644. Elements detectés: def custom_generate_unique_id, def custom_generate_unique_id2, def custom_generate_unique_id3

**Classes** : Item, Message
**Fonctions** : custom_generate_unique_id, custom_generate_unique_id2, custom_generate_unique_id3, test_top_level_generate_unique_id, post_root, post_router, test_router_overrides_generate_unique_id, test_router_include_overrides_generate_unique_id, test_subrouter_top_level_include_overrides_generate_unique_id, post_subrouter, test_router_path_operation_overrides_generate_unique_id, test_app_path_operation_overrides_generate_unique_id, test_callback_override_generate_unique_id, post_callback, post_with_callback
**Dépendances** : warnings, fastapi, fastapi.routing, fastapi.testclient, inline_snapshot, pydantic
**API** : /, /router, /subrouter, /post-callback, /tocallback, /second, /third

### `test_generic_parameterless_depends.py`

Module Python. Nombre de lignes: 60. Elements detectés: class A:, class B:, def test_generic_parameterless_depends

**Classes** : A, B
**Fonctions** : test_generic_parameterless_depends, test_openapi_schema
**Dépendances** : typing, fastapi, fastapi.testclient, inline_snapshot
**API** : /a, /b

### `test_get_model_definitions_formfeed_escape.py`

Module Python. Nombre de lignes: 148. Elements detectés: def client_fixture, class Address, class Facility

**Classes** : Address, Facility
**Fonctions** : client_fixture, get_facility, test_get, test_openapi_schema
**Dépendances** : pytest, fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /facilities/{facility_id}

### `test_get_request_body.py`

Module Python. Nombre de lignes: 103. Elements detectés: class Product, def test_get_with_body, def test_openapi_schema

**Classes** : Product
**Fonctions** : test_get_with_body, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /product

### `test_http_connection_injection.py`

Module Python. Nombre de lignes: 26. Elements detectés: def test_value_extracting_by_http, def test_value_extracting_by_ws

**Fonctions** : test_value_extracting_by_http, test_value_extracting_by_ws
**Dépendances** : fastapi, fastapi.requests, fastapi.testclient, starlette.websockets
**API** : /http

### `test_include_route.py`

Module Python. Nombre de lignes: 14. Elements detectés: def read_items, def test_sub_router

**Fonctions** : read_items, test_sub_router
**Dépendances** : fastapi, fastapi.responses, fastapi.testclient
**API** : /items/

### `test_infer_param_optionality.py`

Module Python. Nombre de lignes: 303. Elements detectés: def get_users, def get_user, def get_items

**Fonctions** : get_users, get_user, get_items, get_item, test_get_users, test_get_user, test_get_items_1, test_get_items_2, test_get_item_1, test_get_item_2, test_get_users_items, test_get_users_item, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot
**API** : /, /{user_id}, /{item_id}

### `test_inherited_custom_class.py`

Module Python. Nombre de lignes: 49. Elements detectés: class MyUuid:, def __init__, def __str__

**Classes** : MyUuid, SomeCustomClass
**Fonctions** : __init__, __str__, __class__, __dict__, test_pydanticv2, return_fast_uuid, serialize_a_uuid, return_some_user
**Dépendances** : uuid, pytest, fastapi, fastapi.testclient, pydantic
**API** : /fast_uuid, /get_custom_class

### `test_invalid_path_param.py`

Module Python. Nombre de lignes: 51. Elements detectés: def test_invalid_sequence, class Item, def read_items

**Classes** : Item
**Fonctions** : test_invalid_sequence, read_items, test_invalid_tuple, test_invalid_dict, test_invalid_simple_list, test_invalid_simple_tuple, test_invalid_simple_set, test_invalid_simple_dict
**Dépendances** : pytest, fastapi, pydantic
**API** : /items/{id}

### `test_invalid_sequence_param.py`

Module Python. Nombre de lignes: 47. Elements detectés: def test_invalid_sequence, class Item, def read_items

**Classes** : Item
**Fonctions** : test_invalid_sequence, read_items, test_invalid_tuple, test_invalid_dict, test_invalid_simple_dict
**Dépendances** : pytest, fastapi, pydantic
**API** : /items/

### `test_json_type.py`

Module Python. Nombre de lignes: 43. Elements detectés: def form_json_list, def query_json_list, def header_json_list

**Fonctions** : form_json_list, query_json_list, header_json_list, cookie_json_list, test_form_json_list, test_query_json_list, test_header_json_list, test_cookie_json_list
**Dépendances** : json, typing, fastapi, fastapi.testclient, pydantic
**API** : /form-json-list, /query-json-list, /header-json-list, /cookie-json-list

### `test_jsonable_encoder.py`

Module Python. Nombre de lignes: 246. Elements detectés: class Person:, def __init__, class Pet:

**Classes** : Person, Pet, Item, DictablePerson, DictablePet, Unserializable, RoleEnum, ModelWithConfig
**Fonctions** : __init__, __iter__, __dict__, test_encode_dict, test_encode_dict_include_exclude_list, test_encode_class, test_encode_dictable, test_encode_dataclass, test_encode_unsupported, test_encode_custom_json_encoders_model_pydanticv2, serialize_dt_field, test_json_encoder_error_with_pydanticv1, test_encode_model_with_config, test_encode_model_with_alias_raises, test_encode_model_with_alias
**Dépendances** : warnings, collections, dataclasses, datetime, decimal, enum, math, pathlib, typing, pytest, fastapi._compat, fastapi.encoders

### `test_list_bytes_file_order_preserved_issue_14811.py`

Module Python. Nombre de lignes: 35. Elements detectés: def test_list_bytes_file_preserves_order

**Fonctions** : test_list_bytes_file_preserves_order
**Dépendances** : typing, anyio, pytest, fastapi, fastapi.testclient, starlette.datastructures
**API** : /upload

### `test_local_docs.py`

Module Python. Nombre de lignes: 56. Elements detectés: def test_strings_in_generated_swagger, def test_strings_in_custom_swagger, def test_strings_in_generated_redoc

**Fonctions** : test_strings_in_generated_swagger, test_strings_in_custom_swagger, test_strings_in_generated_redoc, test_strings_in_custom_redoc, test_google_fonts_in_generated_redoc
**Dépendances** : inspect, fastapi.openapi.docs

### `test_multi_body_errors.py`

Module Python. Nombre de lignes: 175. Elements detectés: class Item, def save_item_no_body, def test_put_correct_body

**Classes** : Item
**Fonctions** : save_item_no_body, test_put_correct_body, test_jsonable_encoder_requiring_error, test_put_incorrect_body_multiple, test_openapi_schema
**Dépendances** : decimal, dirty_equals, fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /items/

### `test_multi_query_errors.py`

Module Python. Nombre de lignes: 111. Elements detectés: def read_items, def test_multi_query, def test_multi_query_incorrect

**Fonctions** : read_items, test_multi_query, test_multi_query_incorrect, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot
**API** : /items/

### `test_multipart_installation.py`

Module Python. Nombre de lignes: 115. Elements detectés: def test_incorrect_multipart_installed_form, def test_incorrect_multipart_installed_file_upload, def test_incorrect_multipart_installed_file_bytes

**Fonctions** : test_incorrect_multipart_installed_form, test_incorrect_multipart_installed_file_upload, test_incorrect_multipart_installed_file_bytes, test_incorrect_multipart_installed_multi_form, test_incorrect_multipart_installed_form_file, test_no_multipart_installed, test_no_multipart_installed_file, test_no_multipart_installed_file_bytes, test_no_multipart_installed_multi_form, test_no_multipart_installed_form_file, test_old_multipart_installed
**Dépendances** : warnings, pytest, fastapi, fastapi.dependencies.utils
**API** : /

### `test_nested_annotated_in_sequence.py`

Module Python. Nombre de lignes: 128. Elements detectés: def read_root, def test_endpoint_none, def test_endpoint_valid

**Fonctions** : read_root, test_endpoint_none, test_endpoint_valid, test_endpoint_too_long, test_openapi
**Dépendances** : typing, dirty_equals, fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /

### `test_no_schema_split.py`

Module Python. Nombre de lignes: 157. Elements detectés: class MessageEventType, class MessageEvent, class MessageOutput

**Classes** : MessageEventType, MessageEvent, MessageOutput, Message
**Fonctions** : test_create_message, test_openapi_schema
**Dépendances** : enum, fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /messages

### `test_no_swagger_ui_redirect.py`

Module Python. Nombre de lignes: 20. Elements detectés: def test_swagger_ui, def test_swagger_ui_no_oauth2_redirect, def test_response

**Fonctions** : test_swagger_ui, test_swagger_ui_no_oauth2_redirect, test_response
**Dépendances** : fastapi, fastapi.testclient
**API** : /items/

### `test_openapi_cache_root_path.py`

Module Python. Nombre de lignes: 56. Elements detectés: def test_root_path_does_not_persist_across_requests, def read_root, def test_multiple_different_root_paths_do_not_accumulate

**Fonctions** : test_root_path_does_not_persist_across_requests, read_root, test_multiple_different_root_paths_do_not_accumulate, test_legitimate_root_path_still_appears, test_configured_servers_not_mutated
**Dépendances** : fastapi, fastapi.testclient
**API** : /

### `test_openapi_examples.py`

Module Python. Nombre de lignes: 399. Elements detectés: class Item, def examples, def path_examples

**Classes** : Item
**Fonctions** : examples, path_examples, query_examples, header_examples, cookie_examples, test_call_api, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /examples/, /path_examples/{item_id}, /query_examples/, /header_examples/, /cookie_examples/

### `test_openapi_model_description_trim_on_formfeed.py`

Module Python. Nombre de lignes: 21. Elements detectés: class MyModel, def foo, def test_openapi

**Classes** : MyModel
**Fonctions** : foo, test_openapi
**Dépendances** : fastapi, fastapi.testclient, pydantic
**API** : /foo

### `test_openapi_query_parameter_extension.py`

Module Python. Nombre de lignes: 122. Elements detectés: def route_with_extra_query_parameters, def test_get_route, def test_openapi

**Fonctions** : route_with_extra_query_parameters, test_get_route, test_openapi
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot
**API** : /

### `test_openapi_route_extensions.py`

Module Python. Nombre de lignes: 36. Elements detectés: def route_with_extras, def test_get_route, def test_openapi_schema

**Fonctions** : route_with_extras, test_get_route, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot
**API** : /

### `test_openapi_schema_type.py`

Module Python. Nombre de lignes: 20. Elements detectés: def test_allowed_schema_type, def test_invalid_type_value

**Fonctions** : test_allowed_schema_type, test_invalid_type_value
**Dépendances** : pytest, fastapi.openapi.models

### `test_openapi_separate_input_output_schemas.py`

Module Python. Nombre de lignes: 648. Elements detectés: class SubItem, class Item, class WithComputedField

**Classes** : SubItem, Item, WithComputedField
**Fonctions** : computed_field, get_app_client, create_item, create_item_list, read_items, create_with_computed_field, test_create_item, test_create_item_with_sub, test_create_item_list, test_read_items, test_with_computed_field, test_openapi_schema, test_openapi_schema_no_separate
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /items/, /items-list/, /with-computed-field/

### `test_openapi_servers.py`

Module Python. Nombre de lignes: 51. Elements detectés: def foo, def test_app, def test_openapi_schema

**Fonctions** : foo, test_app, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot
**API** : /foo

### `test_operations_signatures.py`

Module Python. Nombre de lignes: 18. Elements detectés: def test_signatures_consistency

**Fonctions** : test_signatures_consistency
**Dépendances** : inspect, fastapi

### `test_optional_file_list.py`

Module Python. Nombre de lignes: 21. Elements detectés: def test_optional_bytes_list, def test_optional_bytes_list_no_files

**Fonctions** : test_optional_bytes_list, test_optional_bytes_list_no_files
**Dépendances** : fastapi, fastapi.testclient
**API** : /files

### `test_orjson_response_class.py`

Module Python. Nombre de lignes: 22. Elements detectés: def get_orjson_non_str_keys, def test_orjson_non_str_keys

**Fonctions** : get_orjson_non_str_keys, test_orjson_non_str_keys
**Dépendances** : warnings, pytest, fastapi, fastapi.exceptions, fastapi.responses, fastapi.testclient, sqlalchemy.sql.elements
**API** : /orjson_non_str_keys

### `test_param_class.py`

Module Python. Nombre de lignes: 16. Elements detectés: def read_items, def test_default_param_query_none, def test_default_param_query

**Fonctions** : read_items, test_default_param_query_none, test_default_param_query
**Dépendances** : fastapi, fastapi.params, fastapi.testclient
**API** : /items/

### `test_param_in_path_and_dependency.py`

Module Python. Nombre de lignes: 88. Elements detectés: def test_read_users, def test_openapi_schema

**Fonctions** : test_read_users, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot
**API** : /users/{user_id}

### `test_param_include_in_schema.py`

Module Python. Nombre de lignes: 227. Elements detectés: def test_hidden_cookie, def test_hidden_header, def test_hidden_path

**Fonctions** : test_hidden_cookie, test_hidden_header, test_hidden_path, test_hidden_query, test_openapi_schema
**Dépendances** : pytest, fastapi, fastapi.testclient, inline_snapshot
**API** : /hidden_cookie, /hidden_header, /hidden_path/{hidden_path}, /hidden_query

### `test_params_repr.py`

Module Python. Nombre de lignes: 58. Elements detectés: def get_user, def test_param_repr_str, def test_param_repr_none

**Fonctions** : get_user, test_param_repr_str, test_param_repr_none, test_param_repr_ellipsis, test_param_repr_number, test_param_repr_list, test_path_repr, test_query_repr_str, test_query_repr_none, test_query_repr_ellipsis, test_query_repr_number, test_query_repr_list, test_header_repr_str, test_header_repr_none, test_header_repr_ellipsis
**Dépendances** : typing, fastapi.params

### `test_path.py`

Module Python. Nombre de lignes: 628. Elements detectés: def test_text_get, def test_nonexistent, def test_path_foobar

**Fonctions** : test_text_get, test_nonexistent, test_path_foobar, test_path_str_foobar, test_path_str_42, test_path_str_True, test_path_int_foobar, test_path_int_True, test_path_int_42, test_path_int_42_5, test_path_float_foobar, test_path_float_True, test_path_float_42, test_path_float_42_5, test_path_bool_foobar
**Dépendances** : fastapi.testclient, .main

### `test_prepare_release.py`

Module Python. Nombre de lignes: 218. Elements detectés: def release_notes_content, def test_bump_version, def test_update_version_file

**Fonctions** : release_notes_content, test_bump_version, test_update_version_file, test_update_version_file_requires_newer_version, test_update_release_notes, test_update_release_notes_rejects_existing_version, test_get_release_notes_body_with_dated_heading, test_get_release_notes_body_with_plain_heading, test_get_release_notes_body_allows_non_version_h2_content, test_get_release_notes_body_requires_version_section, test_get_release_notes_body_requires_non_empty_section, test_cli_updates_configured_files, test_cli_accepts_env_vars, test_cli_prints_current_version, test_cli_prints_release_notes
**Dépendances** : datetime, pathlib, pytest, typer.testing, scripts.prepare_release

### `test_put_no_body.py`

Module Python. Nombre de lignes: 92. Elements detectés: def save_item_no_body, def test_put_no_body, def test_put_no_body_with_body

**Fonctions** : save_item_no_body, test_put_no_body, test_put_no_body_with_body, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot
**API** : /items/{item_id}

### `test_pydantic_v1_error.py`

Module Python. Nombre de lignes: 61. Elements detectés: def test_raises_pydantic_v1_model_in_endpoint_param, class ParamModelV1, def endpoint

**Classes** : ParamModelV1, ReturnModelV1, ResponseModelV1, ErrorModelV1, ModelV1A
**Fonctions** : test_raises_pydantic_v1_model_in_endpoint_param, endpoint, test_raises_pydantic_v1_model_in_return_type, test_raises_pydantic_v1_model_in_response_model, test_raises_pydantic_v1_model_in_additional_responses_model, test_raises_pydantic_v1_model_in_union, test_raises_pydantic_v1_model_in_sequence
**Dépendances** : sys, warnings, pytest, tests.utils, fastapi, fastapi.exceptions, pydantic.v1
**API** : /param, /return, /response-model, /responses, /union, /sequence

### `test_pydanticv2_dataclasses_uuid_stringified_annotations.py`

Module Python. Nombre de lignes: 39. Elements detectés: class Item:, def test_annotations

**Classes** : Item
**Fonctions** : test_annotations
**Dépendances** : __future__, uuid, dataclasses, dirty_equals, fastapi, fastapi.testclient, inline_snapshot
**API** : /item

### `test_query.py`

Module Python. Nombre de lignes: 217. Elements detectés: def test_query, def test_query_query_baz, def test_query_not_declared_baz

**Fonctions** : test_query, test_query_query_baz, test_query_not_declared_baz, test_query_optional, test_query_optional_query_baz, test_query_optional_not_declared_baz, test_query_int, test_query_int_query_42, test_query_int_query_42_5, test_query_int_query_baz, test_query_int_not_declared_baz, test_query_int_optional, test_query_int_optional_query_50, test_query_int_optional_query_foo, test_query_int_default
**Dépendances** : fastapi.testclient, .main

### `test_query_cookie_header_model_extra_params.py`

Module Python. Nombre de lignes: 106. Elements detectés: class Model, class AuthHeaders, def test_query_pass_extra_list

**Classes** : Model, AuthHeaders
**Fonctions** : test_query_pass_extra_list, test_query_pass_extra_single, test_header_pass_extra_list, test_header_pass_extra_single, test_header_model_prefers_hyphenated_header_with_convert_underscores, test_header_model_rejects_underscore_header_with_convert_underscores, test_cookie_pass_extra_list
**Dépendances** : fastapi, fastapi.testclient, pydantic
**API** : /query, /header, /cookie, /header-requires-hyphen

### `test_read_with_orm_mode.py`

Module Python. Nombre de lignes: 31. Elements detectés: def test_read_with_orm_mode, class PersonBase, class Person

**Classes** : PersonBase, Person, PersonCreate, PersonRead
**Fonctions** : test_read_with_orm_mode, full_name, create_person
**Dépendances** : typing, fastapi, fastapi.testclient, pydantic
**API** : /people/

### `test_regex_deprecated_body.py`

Module Python. Nombre de lignes: 140. Elements detectés: def get_client, def test_no_query, def test_q_fixedquery

**Fonctions** : get_client, test_no_query, test_q_fixedquery, test_query_nonregexquery, test_openapi_schema
**Dépendances** : typing, pytest, fastapi, fastapi.exceptions, fastapi.testclient, inline_snapshot, .utils
**API** : /items/

### `test_regex_deprecated_params.py`

Module Python. Nombre de lignes: 132. Elements detectés: def get_client, def test_query_params_str_validations_no_query, def test_query_params_str_validations_q_fixedquery

**Fonctions** : get_client, test_query_params_str_validations_no_query, test_query_params_str_validations_q_fixedquery, test_query_params_str_validations_item_query_nonregexquery, test_openapi_schema
**Dépendances** : typing, pytest, fastapi, fastapi.exceptions, fastapi.testclient, inline_snapshot, .utils
**API** : /items/

### `test_repeated_cookie_headers.py`

Module Python. Nombre de lignes: 21. Elements detectés: def set_cookie, def set_indirect_cookie, def get_direct_cookie

**Fonctions** : set_cookie, set_indirect_cookie, get_direct_cookie, get_indirect_cookie, test_cookie_is_set_once
**Dépendances** : fastapi, fastapi.testclient
**API** : /directCookie, /indirectCookie

### `test_repeated_dependency_schema.py`

Module Python. Nombre de lignes: 96. Elements detectés: def get_header, def get_something_else, def get_deps

**Fonctions** : get_header, get_something_else, get_deps, test_response, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot
**API** : /

### `test_repeated_parameter_alias.py`

Module Python. Nombre de lignes: 97. Elements detectés: def get_parameters_with_repeated_aliases, def test_get_parameters, def test_openapi_schema

**Fonctions** : get_parameters_with_repeated_aliases, test_get_parameters, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot
**API** : /{repeated_alias}

### `test_request_body_parameters_media_type.py`

Module Python. Nombre de lignes: 170. Elements detectés: class Product, class Shop, def test_openapi_schema

**Classes** : Product, Shop
**Fonctions** : test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /products, /shops

### `test_request_param_model_by_alias.py`

Module Python. Nombre de lignes: 51. Elements detectés: class Model, def test_query_model_with_alias, def test_header_model_with_alias

**Classes** : Model
**Fonctions** : test_query_model_with_alias, test_header_model_with_alias, test_cookie_model_with_alias, test_query_model_with_alias_by_name, test_header_model_with_alias_by_name, test_cookie_model_with_alias_by_name
**Dépendances** : dirty_equals, fastapi, fastapi.testclient, pydantic
**API** : /query, /header, /cookie

### `test_required_noneable.py`

Module Python. Nombre de lignes: 37. Elements detectés: def read_query, def read_explicit_query, def send_body_embed

**Fonctions** : read_query, read_explicit_query, send_body_embed, test_required_nonable_query_invalid, test_required_noneable_query_value, test_required_nonable_explicit_query_invalid, test_required_nonable_explicit_query_value, test_required_nonable_body_embed_no_content, test_required_nonable_body_embed_invalid, test_required_noneable_body_embed_value
**Dépendances** : fastapi, fastapi.testclient
**API** : /query, /explicit-query, /body-embed

### `test_response_by_alias.py`

Module Python. Nombre de lignes: 284. Elements detectés: class Model, class ModelNoAlias, def read_dict

**Classes** : Model, ModelNoAlias
**Fonctions** : read_dict, read_model, read_list, by_alias_dict, by_alias_model, by_alias_list, no_alias_dict, no_alias_model, no_alias_list, test_read_dict, test_read_model, test_read_list, test_read_dict_by_alias, test_read_model_by_alias, test_read_list_by_alias
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /dict, /model, /list, /by-alias/dict, /by-alias/model, /by-alias/list, /no-alias/dict, /no-alias/model, /no-alias/list

### `test_response_change_status_code.py`

Module Python. Nombre de lignes: 15. Elements detectés: def test_dependency_set_status_code

**Fonctions** : test_dependency_set_status_code
**Dépendances** : fastapi, fastapi.testclient
**API** : /

### `test_response_class_no_mediatype.py`

Module Python. Nombre de lignes: 99. Elements detectés: class JsonApiResponse, class Error, class JsonApiError

**Classes** : JsonApiResponse, Error, JsonApiError
**Fonctions** : test_openapi_schema
**Dépendances** : fastapi, fastapi.responses, fastapi.testclient, inline_snapshot, pydantic
**API** : /a, /b

### `test_response_code_no_body.py`

Module Python. Nombre de lignes: 98. Elements detectés: class JsonApiResponse, class Error, class JsonApiError

**Classes** : JsonApiResponse, Error, JsonApiError
**Fonctions** : test_get_response, test_openapi_schema
**Dépendances** : fastapi, fastapi.responses, fastapi.testclient, inline_snapshot, pydantic
**API** : /a, /b

### `test_response_dependency.py`

Module Python. Nombre de lignes: 126. Elements detectés: def test_response_with_depends_annotated, def modify_response, def endpoint

**Fonctions** : test_response_with_depends_annotated, modify_response, endpoint, test_response_with_depends_default, test_response_without_depends, test_response_dependency_chain, first_modifier, second_modifier, test_response_dependency_returns_different_response_instance, default_response, test_request_with_depends_annotated, extract_request_info, test_background_tasks_with_depends_annotated, background_task, add_background_task
**Dépendances** : typing, fastapi, fastapi.responses, fastapi.testclient
**API** : /

### `test_response_model_as_return_annotation.py`

Module Python. Nombre de lignes: 959. Elements detectés: class BaseUser, class User, class DBUser

**Classes** : BaseUser, User, DBUser, Item
**Fonctions** : no_response_model_no_annotation_return_model, no_response_model_no_annotation_return_dict, response_model_no_annotation_return_same_model, response_model_no_annotation_return_exact_dict, response_model_no_annotation_return_invalid_dict, response_model_no_annotation_return_invalid_model, response_model_no_annotation_return_dict_with_extra_data, response_model_no_annotation_return_submodel_with_extra_data, no_response_model_annotation_return_same_model, no_response_model_annotation_return_exact_dict, no_response_model_annotation_return_invalid_dict, no_response_model_annotation_return_invalid_model, no_response_model_annotation_return_dict_with_extra_data, no_response_model_annotation_return_submodel_with_extra_data, response_model_none_annotation_return_same_model
**Dépendances** : pytest, fastapi, fastapi.exceptions, fastapi.responses, fastapi.testclient, inline_snapshot, pydantic
**API** : /no_response_model-no_annotation-return_model, /no_response_model-no_annotation-return_dict, /response_model-no_annotation-return_same_model, /response_model-no_annotation-return_exact_dict, /response_model-no_annotation-return_invalid_dict, /response_model-no_annotation-return_invalid_model, /response_model-no_annotation-return_dict_with_extra_data, /response_model-no_annotation-return_submodel_with_extra_data, /no_response_model-annotation-return_same_model, /no_response_model-annotation-return_exact_dict

### `test_response_model_data_filter.py`

Module Python. Nombre de lignes: 54. Elements detectés: class UserBase, class UserCreate, class UserDB

**Classes** : UserBase, UserCreate, UserDB, PetDB, PetOut
**Fonctions** : test_filter_top_level_model, test_filter_second_level_model, test_list_of_models
**Dépendances** : fastapi, fastapi.testclient, pydantic
**API** : /users/, /pets/{pet_id}, /pets/

### `test_response_model_data_filter_no_inheritance.py`

Module Python. Nombre de lignes: 56. Elements detectés: class UserCreate, class UserDB, class User

**Classes** : UserCreate, UserDB, User, PetDB, PetOut
**Fonctions** : test_filter_top_level_model, test_filter_second_level_model, test_list_of_models
**Dépendances** : fastapi, fastapi.testclient, pydantic
**API** : /users/, /pets/{pet_id}, /pets/

### `test_response_model_default_factory.py`

Module Python. Nombre de lignes: 30. Elements detectés: class ResponseModel, def test_response_model_has_default_factory_return_dict, def test_response_model_has_default_factory_return_model

**Classes** : ResponseModel
**Fonctions** : test_response_model_has_default_factory_return_dict, test_response_model_has_default_factory_return_model
**Dépendances** : fastapi, fastapi.testclient, pydantic
**API** : /response_model_has_default_factory_return_dict, /response_model_has_default_factory_return_model

### `test_response_model_include_exclude.py`

Module Python. Nombre de lignes: 137. Elements detectés: class Model1, class Model2, class Model3

**Classes** : Model1, Model2, Model3
**Fonctions** : simple_include, simple_include_dict, simple_exclude, simple_exclude_dict, mixed, mixed_dict, test_nested_include_simple, test_nested_include_simple_dict, test_nested_exclude_simple, test_nested_exclude_simple_dict, test_nested_include_mixed, test_nested_include_mixed_dict
**Dépendances** : fastapi, fastapi.testclient, pydantic
**API** : /simple_include, /simple_include_dict, /simple_exclude, /simple_exclude_dict, /mixed, /mixed_dict

### `test_response_model_invalid.py`

Module Python. Nombre de lignes: 29. Elements detectés: class NonPydanticModel:, def test_invalid_response_model_raises, def read_root

**Classes** : NonPydanticModel
**Fonctions** : test_invalid_response_model_raises, read_root, test_invalid_response_model_sub_type_raises, test_invalid_response_model_in_responses_raises, test_invalid_response_model_sub_type_in_responses_raises
**Dépendances** : pytest, fastapi, fastapi.exceptions
**API** : /

### `test_response_model_sub_types.py`

Module Python. Nombre de lignes: 143. Elements detectés: class Model, def valid1, def valid2

**Classes** : Model
**Fonctions** : valid1, valid2, valid3, valid4, test_path_operations, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /valid1, /valid2, /valid3, /valid4

### `test_response_set_response_code_empty.py`

Module Python. Nombre de lignes: 94. Elements detectés: def test_dependency_set_status_code, def test_openapi_schema

**Fonctions** : test_dependency_set_status_code, test_openapi_schema
**Dépendances** : typing, fastapi, fastapi.testclient, inline_snapshot
**API** : /{id}

### `test_return_none_stringified_annotations.py`

Module Python. Nombre de lignes: 12. Elements detectés: def test_no_content, def return_no_content

**Fonctions** : test_no_content, return_no_content
**Dépendances** : http, fastapi, fastapi.testclient
**API** : /no-content

### `test_route_scope.py`

Module Python. Nombre de lignes: 33. Elements detectés: def test_get, def test_invalid_method_doesnt_match, def test_invalid_path_doesnt_match

**Fonctions** : test_get, test_invalid_method_doesnt_match, test_invalid_path_doesnt_match, test_websocket, test_websocket_invalid_path_doesnt_match
**Dépendances** : pytest, fastapi, fastapi.routing, fastapi.testclient
**API** : /users/{user_id}

### `test_router_circular_import.py`

Module Python. Nombre de lignes: 9. Elements detectés: def test_router_circular_import

**Fonctions** : test_router_circular_import
**Dépendances** : pytest, fastapi

### `test_router_events.py`

Module Python. Nombre de lignes: 297. Elements detectés: class State, def state, def test_router_events

**Classes** : State
**Fonctions** : state, test_router_events, main, app_startup, app_shutdown, router_startup, router_shutdown, sub_router_startup, sub_router_shutdown, test_app_lifespan_state, test_router_nested_lifespan_state, test_router_nested_lifespan_state_overriding_by_parent, test_merged_no_return_lifespans_return_none, test_merged_mixed_state_lifespans, test_router_async_shutdown_handler
**Dépendances** : collections.abc, contextlib, pytest, fastapi, fastapi.testclient, pydantic
**API** : /

### `test_router_include_context.py`

Module Python. Nombre de lignes: 794. Elements detectés: def dependency_a, def dependency_b, def dependency_c

**Classes** : Subscription, TrackingRoute, HeaderRoute, HeaderRouter, TrackingRouter, RejectingRoute, UnknownRoute
**Fonctions** : dependency_a, dependency_b, dependency_c, unique_id_b, test_iter_route_contexts_returns_direct_route_context, read_item, test_iter_route_contexts_supports_nested_conflict_detection, read_user, read_user_again, test_get_openapi_accepts_filtered_route_contexts_with_effective_paths, read_public, read_private, test_get_openapi_accepts_webhook_route_contexts, new_subscription, test_router_include_context_matches_flattened_include_metadata
**Dépendances** : threading, collections.abc, typing, pytest, fastapi, fastapi.exceptions, fastapi.openapi.utils, fastapi.responses, fastapi.routing, fastapi.security, fastapi.testclient, pydantic
**API** : /items/{item_id}, /{username}, /auth/user/{username}, /public, /private, /callback, /{item_id}, /later, /items, /items/

### `test_router_prefix_with_template.py`

Module Python. Nombre de lignes: 13. Elements detectés: def read_user, def test_get

**Fonctions** : read_user, test_get
**Dépendances** : fastapi, fastapi.testclient
**API** : /users/{id}

### `test_router_redirect_slashes.py`

Module Python. Nombre de lignes: 26. Elements detectés: def test_redirect_slashes_enabled, def hello_page, def test_redirect_slashes_disabled

**Fonctions** : test_redirect_slashes_enabled, hello_page, test_redirect_slashes_disabled
**Dépendances** : fastapi, fastapi.testclient
**API** : /hello/

### `test_schema_compat_pydantic_v2.py`

Module Python. Nombre de lignes: 108. Elements detectés: def get_client, class PlatformRole, class OtherRole

**Classes** : PlatformRole, OtherRole, User
**Fonctions** : get_client, test_get, test_openapi_schema
**Dépendances** : pytest, dirty_equals, fastapi, fastapi.testclient, inline_snapshot, pydantic, tests.utils, enum
**API** : /users

### `test_schema_extra_examples.py`

Module Python. Nombre de lignes: 818. Elements detectés: def create_app, class Item, def schema_extra

**Classes** : Item
**Fonctions** : create_app, schema_extra, example, examples, example_examples, path_example, path_examples, path_example_examples, query_example, query_examples, query_example_examples, header_example, header_examples, header_example_examples, cookie_example
**Dépendances** : pytest, fastapi, fastapi.exceptions, fastapi.testclient, inline_snapshot, pydantic
**API** : /schema_extra/, /example/, /examples/, /example_examples/, /form_example, /form_examples, /form_example_examples, /path_example/{item_id}, /path_examples/{item_id}, /path_example_examples/{item_id}

### `test_schema_ref_pydantic_v2.py`

Module Python. Nombre de lignes: 58. Elements detectés: def get_client, class ModelWithRef, def test_get

**Classes** : ModelWithRef
**Fonctions** : get_client, test_get, test_openapi_schema
**Dépendances** : typing, pytest, fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /

### `test_security_api_key_cookie.py`

Module Python. Nombre de lignes: 56. Elements detectés: class User, def get_current_user, def read_current_user

**Classes** : User
**Fonctions** : get_current_user, read_current_user, test_security_api_key, test_security_api_key_no_key, test_openapi_schema
**Dépendances** : fastapi, fastapi.security, fastapi.testclient, inline_snapshot, pydantic
**API** : /users/me

### `test_security_api_key_cookie_description.py`

Module Python. Nombre de lignes: 61. Elements detectés: class User, def get_current_user, def read_current_user

**Classes** : User
**Fonctions** : get_current_user, read_current_user, test_security_api_key, test_security_api_key_no_key, test_openapi_schema
**Dépendances** : fastapi, fastapi.security, fastapi.testclient, inline_snapshot, pydantic
**API** : /users/me

### `test_security_api_key_cookie_optional.py`

Module Python. Nombre de lignes: 60. Elements detectés: class User, def get_current_user, def read_current_user

**Classes** : User
**Fonctions** : get_current_user, read_current_user, test_security_api_key, test_security_api_key_no_key, test_openapi_schema
**Dépendances** : fastapi, fastapi.security, fastapi.testclient, inline_snapshot, pydantic
**API** : /users/me

### `test_security_api_key_header.py`

Module Python. Nombre de lignes: 54. Elements detectés: class User, def get_current_user, def read_current_user

**Classes** : User
**Fonctions** : get_current_user, read_current_user, test_security_api_key, test_security_api_key_no_key, test_openapi_schema
**Dépendances** : fastapi, fastapi.security, fastapi.testclient, inline_snapshot, pydantic
**API** : /users/me

### `test_security_api_key_header_description.py`

Module Python. Nombre de lignes: 59. Elements detectés: class User, def get_current_user, def read_current_user

**Classes** : User
**Fonctions** : get_current_user, read_current_user, test_security_api_key, test_security_api_key_no_key, test_openapi_schema
**Dépendances** : fastapi, fastapi.security, fastapi.testclient, inline_snapshot, pydantic
**API** : /users/me

### `test_security_api_key_header_optional.py`

Module Python. Nombre de lignes: 57. Elements detectés: class User, def get_current_user, def read_current_user

**Classes** : User
**Fonctions** : get_current_user, read_current_user, test_security_api_key, test_security_api_key_no_key, test_openapi_schema
**Dépendances** : fastapi, fastapi.security, fastapi.testclient, inline_snapshot, pydantic
**API** : /users/me

### `test_security_api_key_query.py`

Module Python. Nombre de lignes: 54. Elements detectés: class User, def get_current_user, def read_current_user

**Classes** : User
**Fonctions** : get_current_user, read_current_user, test_security_api_key, test_security_api_key_no_key, test_openapi_schema
**Dépendances** : fastapi, fastapi.security, fastapi.testclient, inline_snapshot, pydantic
**API** : /users/me

### `test_security_api_key_query_description.py`

Module Python. Nombre de lignes: 59. Elements detectés: class User, def get_current_user, def read_current_user

**Classes** : User
**Fonctions** : get_current_user, read_current_user, test_security_api_key, test_security_api_key_no_key, test_openapi_schema
**Dépendances** : fastapi, fastapi.security, fastapi.testclient, inline_snapshot, pydantic
**API** : /users/me

### `test_security_api_key_query_optional.py`

Module Python. Nombre de lignes: 57. Elements detectés: class User, def get_current_user, def read_current_user

**Classes** : User
**Fonctions** : get_current_user, read_current_user, test_security_api_key, test_security_api_key_no_key, test_openapi_schema
**Dépendances** : fastapi, fastapi.security, fastapi.testclient, inline_snapshot, pydantic
**API** : /users/me

### `test_security_http_base.py`

Module Python. Nombre de lignes: 50. Elements detectés: def read_current_user, def test_security_http_base, def test_security_http_base_with_whitespaces

**Fonctions** : read_current_user, test_security_http_base, test_security_http_base_with_whitespaces, test_security_http_base_no_credentials, test_openapi_schema
**Dépendances** : fastapi, fastapi.security.http, fastapi.testclient, inline_snapshot
**API** : /users/me

### `test_security_http_base_description.py`

Module Python. Nombre de lignes: 52. Elements detectés: def read_current_user, def test_security_http_base, def test_security_http_base_no_credentials

**Fonctions** : read_current_user, test_security_http_base, test_security_http_base_no_credentials, test_openapi_schema
**Dépendances** : fastapi, fastapi.security.http, fastapi.testclient, inline_snapshot
**API** : /users/me

### `test_security_http_base_optional.py`

Module Python. Nombre de lignes: 49. Elements detectés: def read_current_user, def test_security_http_base, def test_security_http_base_no_credentials

**Fonctions** : read_current_user, test_security_http_base, test_security_http_base_no_credentials, test_openapi_schema
**Dépendances** : fastapi, fastapi.security.http, fastapi.testclient, inline_snapshot
**API** : /users/me

### `test_security_http_basic_optional.py`

Module Python. Nombre de lignes: 62. Elements detectés: def read_current_user, def test_security_http_basic, def test_security_http_basic_no_credentials

**Fonctions** : read_current_user, test_security_http_basic, test_security_http_basic_no_credentials, test_security_http_basic_invalid_credentials, test_security_http_basic_non_basic_credentials, test_openapi_schema
**Dépendances** : base64, fastapi, fastapi.security, fastapi.testclient, inline_snapshot
**API** : /users/me

### `test_security_http_basic_realm.py`

Module Python. Nombre de lignes: 61. Elements detectés: def read_current_user, def test_security_http_basic, def test_security_http_basic_no_credentials

**Fonctions** : read_current_user, test_security_http_basic, test_security_http_basic_no_credentials, test_security_http_basic_invalid_credentials, test_security_http_basic_non_basic_credentials, test_openapi_schema
**Dépendances** : base64, fastapi, fastapi.security, fastapi.testclient, inline_snapshot
**API** : /users/me

### `test_security_http_basic_realm_description.py`

Module Python. Nombre de lignes: 67. Elements detectés: def read_current_user, def test_security_http_basic, def test_security_http_basic_no_credentials

**Fonctions** : read_current_user, test_security_http_basic, test_security_http_basic_no_credentials, test_security_http_basic_invalid_credentials, test_security_http_basic_non_basic_credentials, test_openapi_schema
**Dépendances** : base64, fastapi, fastapi.security, fastapi.testclient, inline_snapshot
**API** : /users/me

### `test_security_http_bearer.py`

Module Python. Nombre de lignes: 51. Elements detectés: def read_current_user, def test_security_http_bearer, def test_security_http_bearer_no_credentials

**Fonctions** : read_current_user, test_security_http_bearer, test_security_http_bearer_no_credentials, test_security_http_bearer_incorrect_scheme_credentials, test_openapi_schema
**Dépendances** : fastapi, fastapi.security, fastapi.testclient, inline_snapshot
**API** : /users/me

### `test_security_http_bearer_description.py`

Module Python. Nombre de lignes: 57. Elements detectés: def read_current_user, def test_security_http_bearer, def test_security_http_bearer_no_credentials

**Fonctions** : read_current_user, test_security_http_bearer, test_security_http_bearer_no_credentials, test_security_http_bearer_incorrect_scheme_credentials, test_openapi_schema
**Dépendances** : fastapi, fastapi.security, fastapi.testclient, inline_snapshot
**API** : /users/me

### `test_security_http_bearer_optional.py`

Module Python. Nombre de lignes: 53. Elements detectés: def read_current_user, def test_security_http_bearer, def test_security_http_bearer_no_credentials

**Fonctions** : read_current_user, test_security_http_bearer, test_security_http_bearer_no_credentials, test_security_http_bearer_incorrect_scheme_credentials, test_openapi_schema
**Dépendances** : fastapi, fastapi.security, fastapi.testclient, inline_snapshot
**API** : /users/me

### `test_security_http_digest.py`

Module Python. Nombre de lignes: 53. Elements detectés: def read_current_user, def test_security_http_digest, def test_security_http_digest_no_credentials

**Fonctions** : read_current_user, test_security_http_digest, test_security_http_digest_no_credentials, test_security_http_digest_incorrect_scheme_credentials, test_openapi_schema
**Dépendances** : fastapi, fastapi.security, fastapi.testclient, inline_snapshot
**API** : /users/me

### `test_security_http_digest_description.py`

Module Python. Nombre de lignes: 59. Elements detectés: def read_current_user, def test_security_http_digest, def test_security_http_digest_no_credentials

**Fonctions** : read_current_user, test_security_http_digest, test_security_http_digest_no_credentials, test_security_http_digest_incorrect_scheme_credentials, test_openapi_schema
**Dépendances** : fastapi, fastapi.security, fastapi.testclient, inline_snapshot
**API** : /users/me

### `test_security_http_digest_optional.py`

Module Python. Nombre de lignes: 55. Elements detectés: def read_current_user, def test_security_http_digest, def test_security_http_digest_no_credentials

**Fonctions** : read_current_user, test_security_http_digest, test_security_http_digest_no_credentials, test_security_http_digest_incorrect_scheme_credentials, test_openapi_schema
**Dépendances** : fastapi, fastapi.security, fastapi.testclient, inline_snapshot
**API** : /users/me

### `test_security_oauth2.py`

Module Python. Nombre de lignes: 252. Elements detectés: class User, def get_current_user, def login

**Classes** : User
**Fonctions** : get_current_user, login, read_current_user, test_security_oauth2, test_security_oauth2_password_other_header, test_security_oauth2_password_bearer_no_header, test_strict_login_no_data, test_strict_login_no_grant_type, test_strict_login_incorrect_grant_type, test_strict_login_correct_grant_type, test_openapi_schema
**Dépendances** : pytest, fastapi, fastapi.security, fastapi.testclient, inline_snapshot, pydantic
**API** : /login, /users/me

### `test_security_oauth2_authorization_code_bearer.py`

Module Python. Nombre de lignes: 66. Elements detectés: def test_no_token, def test_incorrect_token, def test_token

**Fonctions** : test_no_token, test_incorrect_token, test_token, test_token_with_whitespaces, test_openapi_schema
**Dépendances** : fastapi, fastapi.security, fastapi.testclient, inline_snapshot
**API** : /items/

### `test_security_oauth2_authorization_code_bearer_description.py`

Module Python. Nombre de lignes: 66. Elements detectés: def test_no_token, def test_incorrect_token, def test_token

**Fonctions** : test_no_token, test_incorrect_token, test_token, test_openapi_schema
**Dépendances** : fastapi, fastapi.security, fastapi.testclient, inline_snapshot
**API** : /items/

### `test_security_oauth2_authorization_code_bearer_scopes_openapi.py`

Module Python. Nombre de lignes: 163. Elements detectés: def test_root, def test_read_with_oauth2_scheme, def test_read_with_get_token

**Fonctions** : test_root, test_read_with_oauth2_scheme, test_read_with_get_token, test_read_token, test_create_token, test_openapi_schema
**Dépendances** : typing, fastapi, fastapi.security, fastapi.testclient, inline_snapshot
**API** : /, /with-oauth2-scheme, /with-get-token, /items/

### `test_security_oauth2_authorization_code_bearer_scopes_openapi_simple.py`

Module Python. Nombre de lignes: 65. Elements detectés: def test_read_admin, def test_openapi_schema

**Fonctions** : test_read_admin, test_openapi_schema
**Dépendances** : typing, fastapi, fastapi.security, fastapi.testclient, inline_snapshot
**API** : /admin

### `test_security_oauth2_optional.py`

Module Python. Nombre de lignes: 253. Elements detectés: class User, def get_current_user, def login

**Classes** : User
**Fonctions** : get_current_user, login, read_users_me, test_security_oauth2, test_security_oauth2_password_other_header, test_security_oauth2_password_bearer_no_header, test_strict_login_no_data, test_strict_login_no_grant_type, test_strict_login_incorrect_grant_type, test_strict_login_correct_data, test_openapi_schema
**Dépendances** : pytest, fastapi, fastapi.security, fastapi.testclient, inline_snapshot, pydantic
**API** : /login, /users/me

### `test_security_oauth2_optional_description.py`

Module Python. Nombre de lignes: 255. Elements detectés: class User, def get_current_user, def login

**Classes** : User
**Fonctions** : get_current_user, login, read_users_me, test_security_oauth2, test_security_oauth2_password_other_header, test_security_oauth2_password_bearer_no_header, test_strict_login_None, test_strict_login_no_grant_type, test_strict_login_incorrect_grant_type, test_strict_login_correct_correct_grant_type, test_openapi_schema
**Dépendances** : pytest, fastapi, fastapi.security, fastapi.testclient, inline_snapshot, pydantic
**API** : /login, /users/me

### `test_security_oauth2_password_bearer_optional.py`

Module Python. Nombre de lignes: 56. Elements detectés: def test_no_token, def test_token, def test_incorrect_token

**Fonctions** : test_no_token, test_token, test_incorrect_token, test_openapi_schema
**Dépendances** : fastapi, fastapi.security, fastapi.testclient, inline_snapshot
**API** : /items/

### `test_security_oauth2_password_bearer_optional_description.py`

Module Python. Nombre de lignes: 61. Elements detectés: def test_no_token, def test_token, def test_incorrect_token

**Fonctions** : test_no_token, test_token, test_incorrect_token, test_openapi_schema
**Dépendances** : fastapi, fastapi.security, fastapi.testclient, inline_snapshot
**API** : /items/

### `test_security_openid_connect.py`

Module Python. Nombre de lignes: 61. Elements detectés: class User, def get_current_user, def read_current_user

**Classes** : User
**Fonctions** : get_current_user, read_current_user, test_security_oauth2, test_security_oauth2_password_other_header, test_security_oauth2_password_bearer_no_header, test_openapi_schema
**Dépendances** : fastapi, fastapi.security.open_id_connect_url, fastapi.testclient, inline_snapshot, pydantic
**API** : /users/me

### `test_security_openid_connect_description.py`

Module Python. Nombre de lignes: 64. Elements detectés: class User, def get_current_user, def read_current_user

**Classes** : User
**Fonctions** : get_current_user, read_current_user, test_security_oauth2, test_security_oauth2_password_other_header, test_security_oauth2_password_bearer_no_header, test_openapi_schema
**Dépendances** : fastapi, fastapi.security.open_id_connect_url, fastapi.testclient, inline_snapshot, pydantic
**API** : /users/me

### `test_security_openid_connect_optional.py`

Module Python. Nombre de lignes: 64. Elements detectés: class User, def get_current_user, def read_current_user

**Classes** : User
**Fonctions** : get_current_user, read_current_user, test_security_oauth2, test_security_oauth2_password_other_header, test_security_oauth2_password_bearer_no_header, test_openapi_schema
**Dépendances** : fastapi, fastapi.security.open_id_connect_url, fastapi.testclient, inline_snapshot, pydantic
**API** : /users/me

### `test_security_scopes.py`

Module Python. Nombre de lignes: 31. Elements detectés: def call_counter_fixture, def app_fixture, def get_db

**Fonctions** : call_counter_fixture, app_fixture, get_db, get_user, endpoint, client_fixture, test_security_scopes_dependency_called_once
**Dépendances** : typing, pytest, fastapi, fastapi.testclient
**API** : /

### `test_security_scopes_dont_propagate.py`

Module Python. Nombre de lignes: 28. Elements detectés: def get_scopes, def test_security_scopes_dont_propagate

**Fonctions** : get_scopes, test_security_scopes_dont_propagate
**Dépendances** : typing, fastapi, fastapi.security, fastapi.testclient
**API** : /scopes

### `test_security_scopes_sub_dependency.py`

Module Python. Nombre de lignes: 89. Elements detectés: def call_counts_fixture, def app_fixture, def get_db_session

**Fonctions** : call_counts_fixture, app_fixture, get_db_session, get_current_user, get_user_me, get_user_items, path_operation, client_fixture, test_security_scopes_sub_dependency_caching
**Dépendances** : typing, pytest, fastapi, fastapi.security, fastapi.testclient
**API** : /

### `test_serialize_response.py`

Module Python. Nombre de lignes: 38. Elements detectés: class Item, def get_valid, def get_coerce

**Classes** : Item
**Fonctions** : get_valid, get_coerce, get_validlist, test_valid, test_coerce, test_validlist
**Dépendances** : fastapi, fastapi.testclient, pydantic
**API** : /items/valid, /items/coerce, /items/validlist

### `test_serialize_response_dataclass.py`

Module Python. Nombre de lignes: 159. Elements detectés: class Item:, def get_valid, def get_object

**Classes** : Item
**Fonctions** : get_valid, get_object, get_coerce, get_validlist, get_objectlist, get_no_response_model_object, get_no_response_model_objectlist, test_valid, test_object, test_coerce, test_validlist, test_objectlist, test_no_response_model_object, test_no_response_model_objectlist
**Dépendances** : dataclasses, datetime, fastapi, fastapi.testclient
**API** : /items/valid, /items/object, /items/coerce, /items/validlist, /items/objectlist, /items/no-response-model/object, /items/no-response-model/objectlist

### `test_serialize_response_model.py`

Module Python. Nombre de lignes: 115. Elements detectés: class Item, def get_valid, def get_coerce

**Classes** : Item
**Fonctions** : get_valid, get_coerce, get_validlist, get_validdict, get_valid_exclude_unset, get_coerce_exclude_unset, get_validlist_exclude_unset, get_validdict_exclude_unset, test_valid, test_coerce, test_validlist, test_validdict, test_valid_exclude_unset, test_coerce_exclude_unset, test_validlist_exclude_unset
**Dépendances** : fastapi, pydantic, starlette.testclient
**API** : /items/valid, /items/coerce, /items/validlist, /items/validdict, /items/valid-exclude-unset, /items/coerce-exclude-unset, /items/validlist-exclude-unset, /items/validdict-exclude-unset

### `test_skip_defaults.py`

Module Python. Nombre de lignes: 81. Elements detectés: class SubModel, class Model, class ModelSubclass

**Classes** : SubModel, Model, ModelSubclass, ModelDefaults
**Fonctions** : get_root, get_exclude_unset, get_exclude_defaults, get_exclude_none, get_exclude_unset_none, get_iterable_exclude_unset, get_iterable_exclude_defaults, get_iterable_exclude_none, test_return_defaults, test_return_exclude_unset, test_return_exclude_defaults, test_return_exclude_none, test_return_exclude_unset_none, test_return_iterable_exclude_unset, test_return_iterable_exclude_defaults
**Dépendances** : collections.abc, fastapi, fastapi.testclient, pydantic
**API** : /, /exclude_unset, /exclude_defaults, /exclude_none, /exclude_unset_none, /iterable_exclude_unset, /iterable_exclude_defaults, /iterable_exclude_none

### `test_sse.py`

Module Python. Nombre de lignes: 361. Elements detectés: class Item, def sse_items_sync, def sse_items_sync_no_annotation

**Classes** : Item
**Fonctions** : sse_items_sync, sse_items_sync_no_annotation, client_fixture, test_async_generator_with_model, test_sync_generator_with_model, test_async_generator_no_annotation, test_sync_generator_no_annotation, test_dict_items, test_post_method_sse, test_sse_events_with_fields, test_mixed_plain_and_sse_events, test_string_data_json_encoded, test_server_sent_event_null_id_rejected, test_server_sent_event_single_line_fields_reject_newlines, test_server_sent_event_negative_retry_rejected
**Dépendances** : asyncio, time, collections.abc, fastapi.routing, pytest, fastapi, fastapi.responses, fastapi.sse, fastapi.testclient, pydantic
**API** : /items/stream, /items/stream-sync, /items/stream-no-annotation, /items/stream-sync-no-annotation, /items/stream-dict, /items/stream-sse-event, /items/stream-mixed, /items/stream-string, /items/stream-post, /items/stream-raw

### `test_starlette_exception.py`

Module Python. Nombre de lignes: 183. Elements detectés: def test_get_item, def test_get_item_not_found, def test_get_starlette_item

**Fonctions** : test_get_item, test_get_item_not_found, test_get_starlette_item, test_get_starlette_item_not_found, test_no_body_status_code_exception_handlers, test_no_body_status_code_with_detail_exception_handlers, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot, starlette.exceptions
**API** : /items/{item_id}, /http-no-body-statuscode-exception, /http-no-body-statuscode-with-detail-exception, /starlette-items/{item_id}

### `test_starlette_urlconvertors.py`

Module Python. Nombre de lignes: 42. Elements detectés: def int_convertor, def float_convertor, def path_convertor

**Fonctions** : int_convertor, float_convertor, path_convertor, query_convertor, test_route_converters_int, test_route_converters_float, test_route_converters_path, test_route_converters_query, test_url_path_for_path_convertor
**Dépendances** : fastapi, fastapi.testclient
**API** : /int/{param:int}, /float/{param:float}, /path/{param:path}, /query/

### `test_stream_bare_type.py`

Module Python. Nombre de lignes: 50. Elements detectés: class Item, def stream_bare_sync, def test_stream_bare_async_iterable

**Classes** : Item
**Fonctions** : stream_bare_sync, test_stream_bare_async_iterable, test_stream_bare_sync_iterable, test_jsonl_router_typed_stream, test_jsonl_router_typed_openapi_schema
**Dépendances** : json, typing, fastapi, fastapi.testclient, pydantic
**API** : /items/stream-bare-async, /items/stream-bare-sync, /events-jsonl

### `test_stream_cancellation.py`

Module Python. Nombre de lignes: 67.

**Dépendances** : collections.abc, anyio, pytest, fastapi, fastapi.responses, starlette.types
**API** : /stream-raw, /stream-jsonl

### `test_stream_json_validation_error.py`

Module Python. Nombre de lignes: 25. Elements detectés: class Item, def stream_items_invalid_sync, def test_stream_json_validation_error_async

**Classes** : Item
**Fonctions** : stream_items_invalid_sync, test_stream_json_validation_error_async, test_stream_json_validation_error_sync
**Dépendances** : collections.abc, pytest, fastapi, fastapi.exceptions, fastapi.testclient, pydantic
**API** : /items/stream-invalid, /items/stream-invalid-sync

### `test_stream_status_code.py`

Module Python. Nombre de lignes: 420. Elements detectés: def set_accepted

**Fonctions** : set_accepted, test_status_code, test_openapi
**Dépendances** : collections.abc, pytest, fastapi, fastapi.responses, fastapi.testclient, inline_snapshot
**API** : /sse, /jsonl, /raw, /sse-dependency, /jsonl-dependency, /raw-dependency, /sse-dependency-override, /jsonl-dependency-override, /raw-dependency-override

### `test_strict_content_type_app_level.py`

Module Python. Nombre de lignes: 27. Elements detectés: def test_default_strict_rejects_no_content_type, def test_default_strict_accepts_json_content_type, def test_lax_accepts_no_content_type

**Fonctions** : test_default_strict_rejects_no_content_type, test_default_strict_accepts_json_content_type, test_lax_accepts_no_content_type, test_lax_accepts_json_content_type
**Dépendances** : fastapi, fastapi.testclient
**API** : /items/

### `test_strict_content_type_nested.py`

Module Python. Nombre de lignes: 56. Elements detectés: def test_strict_inner_on_lax_app_rejects_no_content_type, def test_default_inner_inherits_lax_from_app, def test_strict_inner_accepts_json_content_type

**Fonctions** : test_strict_inner_on_lax_app_rejects_no_content_type, test_default_inner_inherits_lax_from_app, test_strict_inner_accepts_json_content_type, test_default_inner_accepts_json_content_type, test_lax_outer_on_strict_app_accepts_no_content_type, test_strict_inner_on_lax_outer_rejects_no_content_type, test_lax_outer_accepts_json_content_type, test_strict_inner_on_lax_outer_accepts_json_content_type
**Dépendances** : fastapi, fastapi.testclient
**API** : /items/

### `test_strict_content_type_router_level.py`

Module Python. Nombre de lignes: 38. Elements detectés: def test_lax_router_on_strict_app_accepts_no_content_type, def test_strict_router_on_strict_app_rejects_no_content_type, def test_default_router_inherits_strict_from_app

**Fonctions** : test_lax_router_on_strict_app_accepts_no_content_type, test_strict_router_on_strict_app_rejects_no_content_type, test_default_router_inherits_strict_from_app, test_lax_router_accepts_json_content_type, test_strict_router_accepts_json_content_type, test_default_router_accepts_json_content_type
**Dépendances** : fastapi, fastapi.testclient
**API** : /items/

### `test_stringified_annotation_dependency.py`

Module Python. Nombre de lignes: 61. Elements detectés: class DummyClient:, def client_fixture, def test_get

**Classes** : DummyClient
**Fonctions** : client_fixture, test_get, test_openapi_schema
**Dépendances** : __future__, typing, pytest, fastapi, fastapi.testclient, inline_snapshot, collections.abc
**API** : /

### `test_stringified_annotation_dependency_py314.py`

Module Python. Nombre de lignes: 20. Elements detectés: class DummyUser: ..., def test_stringified_annotation

**Classes** : DummyUser
**Fonctions** : test_stringified_annotation
**Dépendances** : typing, fastapi, fastapi.testclient, .utils
**API** : /

### `test_stringified_annotations_simple.py`

Module Python. Nombre de lignes: 17. Elements detectés: class Dep:, def __call__, def test_stringified_annotations

**Classes** : Dep
**Fonctions** : __call__, test_stringified_annotations, call
**Dépendances** : __future__, typing, fastapi, fastapi.testclient, .utils
**API** : /test/

### `test_sub_callbacks.py`

Module Python. Nombre de lignes: 275. Elements detectés: class Invoice, class InvoiceEvent, class InvoiceEventReceived

**Classes** : Invoice, InvoiceEvent, InvoiceEventReceived, Event
**Fonctions** : invoice_notification, event_callback, create_invoice, test_get, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : {$callback_url}/invoices/{$request.body.id}, {$callback_url}/events/{$request.body.title}, /invoices/

### `test_swagger_ui_escape.py`

Module Python. Nombre de lignes: 30. Elements detectés: def test_init_oauth_html_chars_are_escaped, def test_swagger_ui_parameters_html_chars_are_escaped, def test_normal_init_oauth_still_works

**Fonctions** : test_init_oauth_html_chars_are_escaped, test_swagger_ui_parameters_html_chars_are_escaped, test_normal_init_oauth_still_works
**Dépendances** : fastapi.openapi.docs

### `test_swagger_ui_init_oauth.py`

Module Python. Nombre de lignes: 18. Elements detectés: def test_swagger_ui, def test_response

**Fonctions** : test_swagger_ui, test_response
**Dépendances** : fastapi, fastapi.testclient
**API** : /items/

### `test_top_level_security_scheme_in_openapi.py`

Module Python. Nombre de lignes: 48. Elements detectés: def test_get_root, def test_get_root_no_token, def test_openapi_schema

**Fonctions** : test_get_root, test_get_root_no_token, test_openapi_schema
**Dépendances** : fastapi, fastapi.security, fastapi.testclient, inline_snapshot
**API** : /

### `test_tuples.py`

Module Python. Nombre de lignes: 246. Elements detectés: class ItemGroup, class Coordinate, def post_model_with_tuple

**Classes** : ItemGroup, Coordinate
**Fonctions** : post_model_with_tuple, post_tuple_of_models, hello, test_model_with_tuple_valid, test_model_with_tuple_invalid, test_tuple_with_model_valid, test_tuple_with_model_invalid, test_tuple_form_valid, test_tuple_form_invalid, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /model-with-tuple/, /tuple-of-models/, /tuple-form/

### `test_typing_python39.py`

Module Python. Nombre de lignes: 19. Elements detectés: def test_typing, def post_endpoint

**Fonctions** : test_typing, post_endpoint
**Dépendances** : fastapi, fastapi.testclient, .utils
**API** : /

### `test_union_body.py`

Module Python. Nombre de lignes: 119. Elements detectés: class Item, class OtherItem, def save_union_body

**Classes** : Item, OtherItem
**Fonctions** : save_union_body, test_post_other_item, test_post_item, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /items/

### `test_union_body_discriminator.py`

Module Python. Nombre de lignes: 193. Elements detectés: def test_discriminator_pydantic_v2, class FirstItem, class OtherItem

**Classes** : FirstItem, OtherItem
**Fonctions** : test_discriminator_pydantic_v2, save_union_body_discriminator
**Dépendances** : typing, dirty_equals, fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /items/

### `test_union_body_discriminator_annotated.py`

Module Python. Nombre de lignes: 185. Elements detectés: def client_fixture, class Cat, class Dog

**Classes** : Cat, Dog
**Fonctions** : client_fixture, get_pet_type, test_union_body_discriminator_assignment, test_union_body_discriminator_annotated, test_openapi_schema
**Dépendances** : typing, pytest, fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /pet/assignment, /pet/annotated

### `test_union_forms.py`

Module Python. Nombre de lignes: 143. Elements detectés: class UserForm, class CompanyForm, def post_union_form

**Classes** : UserForm, CompanyForm
**Fonctions** : post_union_form, test_post_user_form, test_post_company_form, test_invalid_form_data, test_empty_form, test_openapi_schema
**Dépendances** : typing, fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /form-union/

### `test_union_inherited_body.py`

Module Python. Nombre de lignes: 127. Elements detectés: class Item, class ExtendedItem, def save_union_different_body

**Classes** : Item, ExtendedItem
**Fonctions** : save_union_different_body, test_post_extended_item, test_post_item, test_openapi_schema
**Dépendances** : fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /items/

### `test_validate_response.py`

Module Python. Nombre de lignes: 55. Elements detectés: class Item, def get_invalid, def get_invalid_none

**Classes** : Item
**Fonctions** : get_invalid, get_invalid_none, get_valid_none, get_innerinvalid, get_invalidlist, test_invalid, test_invalid_none, test_valid_none_data, test_valid_none_none, test_double_invalid, test_invalid_list
**Dépendances** : pytest, fastapi, fastapi.exceptions, fastapi.testclient, pydantic
**API** : /items/invalid, /items/invalidnone, /items/validnone, /items/innerinvalid, /items/invalidlist

### `test_validate_response_dataclass.py`

Module Python. Nombre de lignes: 34. Elements detectés: class Item:, def get_invalid, def get_innerinvalid

**Classes** : Item
**Fonctions** : get_invalid, get_innerinvalid, get_invalidlist, test_invalid, test_double_invalid, test_invalid_list
**Dépendances** : pytest, fastapi, fastapi.exceptions, fastapi.testclient, pydantic.dataclasses
**API** : /items/invalid, /items/innerinvalid, /items/invalidlist

### `test_validation_error_context.py`

Module Python. Nombre de lignes: 123. Elements detectés: class Item, class ExceptionCapture:, def __init__

**Classes** : Item, ExceptionCapture
**Fonctions** : __init__, capture, get_user, get_item, get_sub_item, test_request_validation_error_includes_endpoint_context, test_response_validation_error_includes_endpoint_context, test_websocket_validation_error_includes_endpoint_context, test_subapp_request_validation_error_includes_endpoint_context, test_subapp_websocket_validation_error_includes_endpoint_context, test_validation_error_with_only_path, test_validation_error_with_no_context
**Dépendances** : fastapi, fastapi.exceptions, fastapi.testclient, pydantic
**API** : /users/{user_id}, /items/

### `test_webhooks_security.py`

Module Python. Nombre de lignes: 124. Elements detectés: class Subscription, def new_subscription, def test_dummy_webhook

**Classes** : Subscription
**Fonctions** : new_subscription, test_dummy_webhook, test_openapi_schema
**Dépendances** : datetime, typing, fastapi, fastapi.security, fastapi.testclient, inline_snapshot, pydantic

### `test_wrapped_method_forward_reference.py`

Module Python. Nombre de lignes: 24. Elements detectés: def passthrough, def method, def test_wrapped_method_type_inference

**Fonctions** : passthrough, method, test_wrapped_method_type_inference
**Dépendances** : functools, fastapi, fastapi.testclient, .forward_reference_type

### `test_ws_dependencies.py`

Module Python. Nombre de lignes: 48. Elements detectés: def dependency_list, def create_dependency, def fun

**Fonctions** : dependency_list, create_dependency, fun, test_index, test_routerindex, test_routerprefixindex
**Dépendances** : json, typing, fastapi, fastapi.testclient

### `test_ws_router.py`

Module Python. Nombre de lignes: 199. Elements detectés: class CustomError, def make_app, def test_app

**Classes** : CustomError
**Fonctions** : make_app, test_app, test_router, test_prefix_router, test_native_prefix_router, test_router2, test_router_ws_depends, test_router_ws_depends_with_override, test_router_with_params, test_wrong_uri, websocket_middleware, middleware_constructor, test_depend_validation, test_depend_err_middleware, test_depend_err_handler
**Dépendances** : functools, pytest, fastapi, fastapi.middleware, fastapi.testclient

### `utils.py`

Module Python. Nombre de lignes: 22. Elements detectés: def skip_module_if_py_gte_314

**Fonctions** : skip_module_if_py_gte_314
**Dépendances** : sys, importlib.util, pytest
