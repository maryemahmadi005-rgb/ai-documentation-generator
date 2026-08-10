# Module : fastapi/openapi

4 fichier(s), 9 classe(s), 20 fonction(s).

## Vue d'ensemble

- **Classes principales** : BaseModelWithConfig, Contact, EmailStr, Info, License, Reference, Server, ServerVariable, _OpenAPIDependencyData
- **Fonctions principales** : __get_pydantic_core_schema__, __get_pydantic_json_schema__, __get_validators__, _get_api_route_for_openapi, _get_openapi_dependency_data, _get_openapi_operation_parameters, _get_openapi_security_definitions, _html_safe_json, _validate, generate_operation_id, generate_operation_summary, get_fields_from_routes, get_openapi, get_openapi_operation_metadata, get_openapi_operation_request_body
- **Dépendances** : annotated_doc, collections.abc, copy, dataclasses, email_validator, enum, fastapi, fastapi._compat, fastapi.datastructures, fastapi.dependencies.models, fastapi.dependencies.utils, fastapi.encoders

## Détail des fichiers

### `docs.py`

Module Python. Nombre de lignes: 342. Elements detectés: def _html_safe_json, def get_swagger_ui_html

**Fonctions** : _html_safe_json, get_swagger_ui_html, get_redoc_html, get_swagger_ui_oauth2_redirect_html
**Dépendances** : json, typing, annotated_doc, fastapi.encoders, starlette.responses

### `models.py`

Module Python. Nombre de lignes: 338. Elements detectés: class EmailStr, def __get_validators__, def validate

**Classes** : EmailStr, BaseModelWithConfig, Contact, License, Info, ServerVariable, Server, Reference
**Fonctions** : __get_validators__, validate, _validate, __get_pydantic_json_schema__, __get_pydantic_core_schema__
**Dépendances** : collections.abc, enum, typing, fastapi._compat, fastapi.logger, pydantic, typing_extensions, email_validator

### `utils.py`

Module Python. Nombre de lignes: 649. Elements detectés: class _OpenAPIDependencyData:, def _get_openapi_dependency_data

**Classes** : _OpenAPIDependencyData
**Fonctions** : _get_openapi_dependency_data, _get_openapi_security_definitions, _get_openapi_operation_parameters, get_openapi_operation_request_body, generate_operation_id, generate_operation_summary, get_openapi_operation_metadata, get_openapi_path, _get_api_route_for_openapi, get_fields_from_routes, get_openapi
**Dépendances** : copy, http.client, inspect, warnings, collections.abc, dataclasses, typing, fastapi, fastapi._compat, fastapi.datastructures, fastapi.dependencies.models, fastapi.dependencies.utils
