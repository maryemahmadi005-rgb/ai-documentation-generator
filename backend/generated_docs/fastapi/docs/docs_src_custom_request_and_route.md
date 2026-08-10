# Module : docs_src/custom_request_and_route

6 fichier(s), 7 classe(s), 5 fonction(s).

## Vue d'ensemble

- **Classes principales** : GzipRequest, GzipRoute, TimedRoute, ValidationErrorLoggingRoute
- **Fonctions principales** : get_route_handler
- **Dépendances** : collections.abc, fastapi, fastapi.exceptions, fastapi.routing, gzip, time, typing
- **Endpoints API** : /, /sum, /timed

## Détail des fichiers

### `tutorial001_an_py310.py`

Module Python. Nombre de lignes: 25. Elements detectés: class GzipRequest, class GzipRoute, def get_route_handler

**Classes** : GzipRequest, GzipRoute
**Fonctions** : get_route_handler
**Dépendances** : gzip, collections.abc, typing, fastapi, fastapi.routing
**API** : /sum

### `tutorial001_py310.py`

Module Python. Nombre de lignes: 24. Elements detectés: class GzipRequest, class GzipRoute, def get_route_handler

**Classes** : GzipRequest, GzipRoute
**Fonctions** : get_route_handler
**Dépendances** : gzip, collections.abc, fastapi, fastapi.routing
**API** : /sum

### `tutorial002_an_py310.py`

Module Python. Nombre de lignes: 21. Elements detectés: class ValidationErrorLoggingRoute, def get_route_handler

**Classes** : ValidationErrorLoggingRoute
**Fonctions** : get_route_handler
**Dépendances** : collections.abc, typing, fastapi, fastapi.exceptions, fastapi.routing
**API** : /

### `tutorial002_py310.py`

Module Python. Nombre de lignes: 20. Elements detectés: class ValidationErrorLoggingRoute, def get_route_handler

**Classes** : ValidationErrorLoggingRoute
**Fonctions** : get_route_handler
**Dépendances** : collections.abc, fastapi, fastapi.exceptions, fastapi.routing
**API** : /

### `tutorial003_py310.py`

Module Python. Nombre de lignes: 26. Elements detectés: class TimedRoute, def get_route_handler

**Classes** : TimedRoute
**Fonctions** : get_route_handler
**Dépendances** : time, collections.abc, fastapi, fastapi.routing
**API** : /, /timed
