# Module : fastapi/_compat

3 fichier(s), 2 classe(s), 30 fonction(s).

## Vue d'ensemble

- **Classes principales** : GenerateJsonSchema, ModelField
- **Fonctions principales** : __hash__, __post_init__, _annotation_is_complex, _annotation_is_sequence, _has_computed_fields, alias, annotation_is_pydantic_v1, asdict, bytes_schema, default, evaluate_forwardref, field_annotation_is_complex, field_annotation_is_scalar, field_annotation_is_scalar_sequence, field_annotation_is_sequence
- **Dépendances** : .shared, .v2, collections, collections.abc, copy, dataclasses, enum, fastapi._compat, fastapi.openapi.constants, fastapi.types, functools, pydantic

## Détail des fichiers

### `__init__.py`

Module Python. Nombre de lignes: 40.

**Dépendances** : .shared, .v2

### `shared.py`

Module Python. Nombre de lignes: 179. Elements detectés: def lenient_issubclass, def _annotation_is_sequence, def field_annotation_is_sequence

**Fonctions** : lenient_issubclass, _annotation_is_sequence, field_annotation_is_sequence, value_is_sequence, _annotation_is_complex, field_annotation_is_complex, field_annotation_is_scalar, field_annotation_is_scalar_sequence, is_bytes_or_nonable_bytes_annotation, is_uploadfile_or_nonable_uploadfile_annotation, is_bytes_sequence_annotation, is_uploadfile_sequence_annotation, is_pydantic_v1_model_instance, is_pydantic_v1_model_class, annotation_is_pydantic_v1
**Dépendances** : types, typing, warnings, collections, collections.abc, dataclasses, fastapi.types, pydantic, pydantic.version, starlette.datastructures

### `v2.py`

Module Python. Nombre de lignes: 430. Elements detectés: def evaluate_forwardref, class GenerateJsonSchema, def bytes_schema

**Classes** : GenerateJsonSchema, ModelField
**Fonctions** : evaluate_forwardref, bytes_schema, asdict, alias, validation_alias, serialization_alias, default, __post_init__, get_default, validate, serialize, serialize_json, __hash__, _has_computed_fields, get_schema_from_model_field
**Dépendances** : re, warnings, collections.abc, copy, dataclasses, enum, functools, typing, fastapi._compat, fastapi.openapi.constants, fastapi.types, pydantic
