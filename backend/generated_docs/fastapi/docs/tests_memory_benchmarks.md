# Module : tests/memory_benchmarks

4 fichier(s), 10 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : _create_app, create_dependency, create_endpoint, dependency, test_dependency_graph, test_openapi_dependency_graph, test_route_dependency_graph
- **Dépendances** : collections.abc, fastapi, fastapi.routing, inspect, pytest, sys, tests.benchmarks.utils, typing

## Détail des fichiers

### `test_dependency_graph.py`

Module Python. Nombre de lignes: 67. Elements detectés: def _create_app, def create_dependency, def dependency

**Fonctions** : _create_app, create_dependency, dependency, create_endpoint, test_dependency_graph
**Dépendances** : inspect, sys, collections.abc, typing, pytest, fastapi, fastapi.routing

### `test_openapi.py`

Module Python. Nombre de lignes: 28. Elements detectés: def test_openapi_dependency_graph

**Fonctions** : test_openapi_dependency_graph
**Dépendances** : sys, pytest, tests.benchmarks.utils

### `test_route_dependency_graph.py`

Module Python. Nombre de lignes: 47. Elements detectés: def _create_app, def create_dependency, def dependency

**Fonctions** : _create_app, create_dependency, dependency, test_route_dependency_graph
**Dépendances** : sys, collections.abc, typing, pytest, fastapi, fastapi.routing
