# Module : fastapi/dependencies

3 fichier(s), 4 classe(s), 30 fonction(s).

## Vue d'ensemble

- **Classes principales** : Dependant, ParamDetails, SolvedDependency, _CallIdentity
- **Fonctions principales** : __eq__, __hash__, __init__, _get_cache_key, _get_flat_body_params, _get_flat_fields_from_params, _get_oauth_scopes, _get_security_scheme, _get_signature, _impartial, _is_async_gen_callable, _is_async_gen_callable_cached, _is_coroutine_callable_cached, _is_gen_callable, _is_gen_callable_cached
- **Dépendances** : asyncio, collections.abc, contextlib, copy, dataclasses, fastapi, fastapi._compat, fastapi.background, fastapi.concurrency, fastapi.dependencies.models, fastapi.security.base, fastapi.types

## Détail des fichiers

### `models.py`

Module Python. Nombre de lignes: 195. Elements detectés: def _unwrapped_call, def _impartial, class Dependant:

**Classes** : Dependant, _CallIdentity
**Fonctions** : _unwrapped_call, _impartial, __init__, __hash__, __eq__, _get_oauth_scopes, _get_cache_key, _uses_scopes, _is_security_scheme, _get_security_scheme, _is_gen_callable_cached, _is_gen_callable, _is_async_gen_callable_cached, _is_async_gen_callable, _is_coroutine_callable_cached
**Dépendances** : inspect, sys, collections.abc, dataclasses, functools, typing, fastapi._compat, fastapi.security.base, fastapi.types, asyncio

### `utils.py`

Module Python. Nombre de lignes: 961. Elements detectés: def ensure_multipart_is_installed

**Classes** : ParamDetails, SolvedDependency
**Fonctions** : ensure_multipart_is_installed, get_parameterless_sub_dependant, _get_flat_body_params, _get_flat_fields_from_params, get_flat_params, _get_signature, get_typed_signature, get_typed_annotation, get_typed_return_annotation, get_stream_item_type, get_dependant, add_non_field_param_to_dependency, analyze_param, add_param_to_fields, _validate_value_with_model_field
**Dépendances** : dataclasses, inspect, sys, collections.abc, contextlib, copy, typing, fastapi, fastapi._compat, fastapi.background, fastapi.concurrency, fastapi.dependencies.models
