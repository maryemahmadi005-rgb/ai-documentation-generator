# Module : src/flask/json

Ce module regroupe 3 fichier(s) source.

## Vue d'ensemble

- **Classes principales** : DefaultJSONProvider, JSONProvider, JSONTag, PassDict, PassList, TagBytes, TagDict, TagMarkup, TagOrderedDict, TagTuple, and
- **Fonctions principales** : __init__, _default, _prepare_response_obj, _untag_scan, check, dump, dumps, jsonify, load, loads, register, response, tag, to_json, to_python
- **Dépendances** : ..globals, ..json, ..sansio.app, ..wrappers, .provider, __future__, base64, dataclasses, datetime, decimal, flask.json.tag, json

## Détail des fichiers

### `__init__.py`

Module Python. Nombre de lignes: 122. Elements detectés: def dumps, def dump, def loads

**Fonctions** : dumps, dump, loads, load, jsonify
**Dépendances** : __future__, json, typing, ..globals, .provider, ..wrappers

### `provider.py`

Module Python. Nombre de lignes: 163. Elements detectés: class JSONProvider:, class and implement at least :meth:`dumps` and :meth:`loads`. All, def __init__

**Classes** : JSONProvider, and, DefaultJSONProvider
**Fonctions** : __init__, dumps, dump, loads, load, _prepare_response_obj, response, _default
**Dépendances** : __future__, dataclasses, decimal, json, typing, uuid, weakref, datetime, werkzeug.http, werkzeug.sansio.response, ..sansio.app

### `tag.py`

Module Python. Nombre de lignes: 236. Elements detectés: class TagOrderedDict, def check, def to_json

**Classes** : TagOrderedDict, JSONTag, TagDict, PassDict, TagTuple, PassList, TagBytes, TagMarkup
**Fonctions** : check, to_json, to_python, __init__, tag, register, untag, _untag_scan, dumps, loads
**Dépendances** : flask.json.tag, __future__, typing, base64, datetime, uuid, markupsafe, werkzeug.http, ..json
