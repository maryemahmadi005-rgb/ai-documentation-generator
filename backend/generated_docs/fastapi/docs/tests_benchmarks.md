# Module : tests/benchmarks

4 fichier(s), 4 classe(s), 20 fonction(s).

## Vue d'ensemble

- **Classes principales** : ItemIn, ItemOut, LargeIn, LargeOut
- **Fonctions principales** : _bench_get, client, create_dependency, create_openapi_app, dep_a, dep_b, dependency, do_request, generate_openapi, sync_dict_no_response_model, sync_dict_with_response_model, sync_large_dict_no_response_model, sync_large_dict_with_response_model, sync_large_model_no_response_model, sync_large_model_with_response_model
- **Dépendances** : collections.abc, fastapi, fastapi.testclient, json, pydantic, pytest, sys, tests.benchmarks.utils, typing
- **Endpoints API** : /async/large-receive, /async/validated, /sync/dict-no-response-model, /sync/dict-with-response-model, /sync/large-dict-no-response-model, /sync/large-dict-with-response-model, /sync/large-receive, /sync/model-no-response-model, /sync/model-with-response-model, /sync/validated

## Détail des fichiers

### `test_general_performance.py`

Module Python. Nombre de lignes: 288. Elements detectés: def dep_a, def dep_b, class ItemIn

**Classes** : ItemIn, ItemOut, LargeIn, LargeOut
**Fonctions** : dep_a, dep_b, sync_validated, sync_dict_no_response_model, sync_dict_with_response_model, sync_model_no_response_model, sync_model_with_response_model, sync_large_receive, sync_large_dict_no_response_model, sync_large_dict_with_response_model, sync_large_model_no_response_model, sync_large_model_with_response_model, client, _bench_get, do_request
**Dépendances** : json, sys, collections.abc, typing, pytest, fastapi, fastapi.testclient, pydantic
**API** : /sync/validated, /sync/dict-no-response-model, /sync/dict-with-response-model, /sync/model-no-response-model, /sync/model-with-response-model, /async/validated, /sync/large-receive, /async/large-receive, /sync/large-dict-no-response-model, /sync/large-dict-with-response-model

### `test_openapi.py`

Module Python. Nombre de lignes: 28. Elements detectés: def test_openapi_dependency_graph

**Fonctions** : test_openapi_dependency_graph
**Dépendances** : sys, pytest, tests.benchmarks.utils

### `utils.py`

Module Python. Nombre de lignes: 35. Elements detectés: def create_openapi_app, def create_dependency, def dependency

**Fonctions** : create_openapi_app, create_dependency, dependency, generate_openapi
**Dépendances** : collections.abc, typing, fastapi
