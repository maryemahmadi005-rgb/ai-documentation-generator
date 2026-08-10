# Module : docs_src/stream_data

3 fichier(s), 1 classe(s), 8 fonction(s).

## Vue d'ensemble

- **Classes principales** : PNGStreamingResponse
- **Fonctions principales** : read_image, stream_image_no_async, stream_image_no_async_no_annotation, stream_image_no_async_yield_from, stream_story_no_async, stream_story_no_async_bytes, stream_story_no_async_no_annotation, stream_story_no_async_no_annotation_bytes
- **Dépendances** : base64, collections.abc, fastapi, fastapi.responses, io
- **Endpoints API** : /image/stream, /image/stream-no-annotation, /image/stream-no-async, /image/stream-no-async-no-annotation, /image/stream-no-async-yield-from, /story/stream, /story/stream-bytes, /story/stream-no-annotation, /story/stream-no-annotation-bytes, /story/stream-no-async

## Détail des fichiers

### `tutorial001_py310.py`

Module Python. Nombre de lignes: 45. Elements detectés: def stream_story_no_async, def stream_story_no_async_no_annotation, def stream_story_no_async_bytes

**Fonctions** : stream_story_no_async, stream_story_no_async_no_annotation, stream_story_no_async_bytes, stream_story_no_async_no_annotation_bytes
**Dépendances** : collections.abc, fastapi, fastapi.responses
**API** : /story/stream, /story/stream-no-async, /story/stream-no-annotation, /story/stream-no-async-no-annotation, /story/stream-bytes, /story/stream-no-async-bytes, /story/stream-no-annotation-bytes, /story/stream-no-async-no-annotation-bytes

### `tutorial002_py310.py`

Module Python. Nombre de lignes: 36. Elements detectés: def read_image, class PNGStreamingResponse, def stream_image_no_async

**Classes** : PNGStreamingResponse
**Fonctions** : read_image, stream_image_no_async, stream_image_no_async_yield_from, stream_image_no_async_no_annotation
**Dépendances** : base64, collections.abc, io, fastapi, fastapi.responses
**API** : /image/stream, /image/stream-no-async, /image/stream-no-async-yield-from, /image/stream-no-annotation, /image/stream-no-async-no-annotation
