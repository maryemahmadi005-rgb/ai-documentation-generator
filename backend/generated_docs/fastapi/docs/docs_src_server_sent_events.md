# Module : docs_src/server_sent_events

6 fichier(s), 4 classe(s), 2 fonction(s).

## Vue d'ensemble

- **Classes principales** : Item, Prompt
- **Fonctions principales** : sse_items_no_async, sse_items_no_async_no_annotation
- **Dépendances** : collections.abc, fastapi, fastapi.sse, pydantic, typing
- **Endpoints API** : /chat/stream, /items/stream, /items/stream-no-annotation, /items/stream-no-async, /items/stream-no-async-no-annotation, /logs/stream

## Détail des fichiers

### `tutorial001_py310.py`

Module Python. Nombre de lignes: 29. Elements detectés: class Item, def sse_items_no_async, def sse_items_no_async_no_annotation

**Classes** : Item
**Fonctions** : sse_items_no_async, sse_items_no_async_no_annotation
**Dépendances** : collections.abc, fastapi, fastapi.sse, pydantic
**API** : /items/stream, /items/stream-no-async, /items/stream-no-annotation, /items/stream-no-async-no-annotation

### `tutorial002_py310.py`

Module Python. Nombre de lignes: 18. Elements detectés: class Item

**Classes** : Item
**Dépendances** : collections.abc, fastapi, fastapi.sse, pydantic
**API** : /items/stream

### `tutorial003_py310.py`

Module Python. Nombre de lignes: 13.

**Dépendances** : collections.abc, fastapi, fastapi.sse
**API** : /logs/stream

### `tutorial004_py310.py`

Module Python. Nombre de lignes: 23. Elements detectés: class Item

**Classes** : Item
**Dépendances** : collections.abc, typing, fastapi, fastapi.sse, pydantic
**API** : /items/stream

### `tutorial005_py310.py`

Module Python. Nombre de lignes: 13. Elements detectés: class Prompt

**Classes** : Prompt
**Dépendances** : collections.abc, fastapi, fastapi.sse, pydantic
**API** : /chat/stream
