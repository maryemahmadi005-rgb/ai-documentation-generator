# Module : fastapi

16 fichier(s), 30 classe(s), 59 fonction(s).

## Vue d'ensemble

- **Classes principales** : BackgroundTasks, Body, Color, Cookie, DefaultPlaceholder, DependencyScopeError, EndpointContext, EventSourceResponse, FastAPI, FastAPIError, Form, HTTPException
- **Fonctions principales** : Body, Cookie, Default, Depends, File, Form, Header, Path, Query, Security, __bool__, __eq__, __get_pydantic_core_schema__, __get_pydantic_json_schema__, __init__
- **Dépendances** : ._compat, ._compat.v2, .applications, .background, .datastructures, .db, .exceptions, .param_functions, .requests, .responses, .routing, .security
- **Endpoints API** : /files/, /items/, /items/{item_id}, /send-notification/{email}, /uploadfile/, /users/, /users/me/items/

## Détail des fichiers

### `__init__.py`

Module Python. Nombre de lignes: 22.

**Dépendances** : starlette, .applications, .background, .datastructures, .exceptions, .param_functions, .requests, .responses, .routing, .websockets

### `applications.py`

Module Python. Nombre de lignes: 4112. Elements detectés: class FastAPI, def __init__

**Classes** : FastAPI, Item, UnicornException
**Fonctions** : __init__, build_middleware_stack, openapi, setup, add_api_route, frontend, api_route, decorator, add_api_websocket_route, websocket, include_router, get, read_items, put, replace_item
**Dépendances** : os, collections.abc, enum, typing, annotated_doc, fastapi, fastapi.datastructures, fastapi.exception_handlers, fastapi.exceptions, fastapi.logger, fastapi.middleware.asyncexitstack, fastapi.openapi.docs
**API** : /users/, /items/, /items/{item_id}

### `background.py`

Module Python. Nombre de lignes: 46. Elements detectés: class BackgroundTasks, def write_notification, def add_task

**Classes** : BackgroundTasks
**Fonctions** : write_notification, add_task
**Dépendances** : collections.abc, typing, annotated_doc, starlette.background, typing_extensions, fastapi
**API** : /send-notification/{email}

### `cli.py`

Module Python. Nombre de lignes: 10. Elements detectés: def main

**Fonctions** : main
**Dépendances** : fastapi_cli.cli

### `concurrency.py`

Module Python. Nombre de lignes: 37.

**Dépendances** : collections.abc, contextlib, typing, anyio.to_thread, anyio, starlette.concurrency

### `datastructures.py`

Module Python. Nombre de lignes: 144. Elements detectés: class UploadFile

**Classes** : UploadFile, DefaultPlaceholder
**Fonctions** : _validate, __get_pydantic_json_schema__, __get_pydantic_core_schema__, __init__, __bool__, __eq__, Default
**Dépendances** : collections.abc, typing, annotated_doc, pydantic, starlette.datastructures, fastapi, ._compat.v2
**API** : /files/, /uploadfile/

### `encoders.py`

Module Python. Nombre de lignes: 338. Elements detectés: class Color:  # type: ignore[no-redef], class PyExtraColor:  # type: ignore[no-redef], def isoformat

**Classes** : Color, PyExtraColor
**Fonctions** : isoformat, decimal_encoder, generate_encoders_by_class_tuples, jsonable_encoder
**Dépendances** : dataclasses, datetime, collections, collections.abc, decimal, enum, ipaddress, pathlib, re, types, typing, uuid

### `exception_handlers.py`

Module Python. Nombre de lignes: 28.

**Dépendances** : fastapi.encoders, fastapi.exceptions, fastapi.utils, fastapi.websockets, starlette.exceptions, starlette.requests, starlette.responses, starlette.status

### `exceptions.py`

Module Python. Nombre de lignes: 203. Elements detectés: class EndpointContext, class HTTPException, def __init__

**Classes** : EndpointContext, HTTPException, WebSocketException, FastAPIError, DependencyScopeError, ValidationException, RequestValidationError, WebSocketRequestValidationError
**Fonctions** : __init__, errors, _format_endpoint_context, __str__
**Dépendances** : collections.abc, typing, annotated_doc, pydantic, starlette.exceptions, fastapi
**API** : /items/{item_id}

### `param_functions.py`

Module Python. Nombre de lignes: 2323. Elements detectés: def Path

**Fonctions** : Path, Query, Header, Cookie, Body, Form, File, Depends, Security
**Dépendances** : collections.abc, typing, annotated_doc, fastapi, fastapi._compat, fastapi.datastructures, fastapi.openapi.models, pydantic, typing_extensions, .db, .security
**API** : /items/{item_id}, /items/, /users/me/items/

### `params.py`

Module Python. Nombre de lignes: 718. Elements detectés: class ParamTypes, class Param, def __init__

**Classes** : ParamTypes, Param, Path, Query, Header, Cookie, Body, Form
**Fonctions** : __init__, __repr__
**Dépendances** : warnings, collections.abc, dataclasses, enum, typing, fastapi.exceptions, fastapi.openapi.models, pydantic, pydantic.fields, typing_extensions, ._compat, .datastructures

### `responses.py`

Module Python. Nombre de lignes: 76. Elements detectés: class _UjsonModule, def dumps, class _OrjsonModule

**Classes** : _UjsonModule, _OrjsonModule, UJSONResponse, ORJSONResponse
**Fonctions** : dumps, render
**Dépendances** : importlib, typing, fastapi.exceptions, fastapi.sse, starlette.responses, typing_extensions

### `sse.py`

Module Python. Nombre de lignes: 197. Elements detectés: class EventSourceResponse, def _check_single_line, def _check_event_single_line

**Classes** : EventSourceResponse, ServerSentEvent
**Fonctions** : _check_single_line, _check_event_single_line, _check_id_valid, _check_data_exclusive, _split_sse_lines, format_sse_event
**Dépendances** : typing, annotated_doc, pydantic, starlette.responses

### `types.py`

Module Python. Nombre de lignes: 10.

**Dépendances** : types, collections.abc, enum, typing, pydantic, pydantic.main

### `utils.py`

Module Python. Nombre de lignes: 115. Elements detectés: def is_body_allowed_for_status_code, def get_path_param_names, def create_model_field

**Fonctions** : is_body_allowed_for_status_code, get_path_param_names, create_model_field, generate_operation_id_for_path, generate_unique_id, deep_dict_update, get_value_or_default
**Dépendances** : re, warnings, typing, fastapi, fastapi._compat, fastapi.datastructures, fastapi.exceptions, pydantic.fields, ._compat, .routing
