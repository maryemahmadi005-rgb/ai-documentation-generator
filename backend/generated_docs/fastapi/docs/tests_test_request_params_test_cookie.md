# Module : tests/test_request_params/test_cookie

3 fichier(s), 8 classe(s), 30 fonction(s).

## Vue d'ensemble

- **Classes principales** : CookieModelOptionalAlias, CookieModelOptionalAliasAndValidationAlias, CookieModelOptionalStr, CookieModelOptionalValidationAlias, CookieModelRequiredAlias, CookieModelRequiredAliasAndValidationAlias, CookieModelRequiredStr, CookieModelRequiredValidationAlias
- **Fonctions principales** : read_model_optional_alias_and_validation_alias, read_model_optional_validation_alias, read_model_required_alias_and_validation_alias, read_model_required_validation_alias, read_optional_alias_and_validation_alias, read_optional_validation_alias, read_required_alias_and_validation_alias, read_required_validation_alias, test_optional_alias_by_alias, test_optional_alias_by_name, test_optional_alias_missing, test_optional_str, test_optional_str_alias_schema, test_optional_str_missing, test_optional_str_schema
- **Dépendances** : dirty_equals, fastapi, fastapi.testclient, inline_snapshot, pydantic, pytest, typing
- **Endpoints API** : /model-optional-alias, /model-optional-alias-and-validation-alias, /model-optional-str, /model-optional-validation-alias, /model-required-alias, /model-required-alias-and-validation-alias, /model-required-str, /model-required-validation-alias, /optional-alias, /optional-alias-and-validation-alias

## Détail des fichiers

### `test_optional_str.py`

Module Python. Nombre de lignes: 271. Elements detectés: class CookieModelOptionalStr, def test_optional_str_schema, def test_optional_str_missing

**Classes** : CookieModelOptionalStr, CookieModelOptionalAlias, CookieModelOptionalValidationAlias, CookieModelOptionalAliasAndValidationAlias
**Fonctions** : test_optional_str_schema, test_optional_str_missing, test_optional_str, test_optional_str_alias_schema, test_optional_alias_missing, test_optional_alias_by_name, test_optional_alias_by_alias, read_optional_validation_alias, read_model_optional_validation_alias, test_optional_validation_alias_schema, test_optional_validation_alias_missing, test_optional_validation_alias_by_name, test_optional_validation_alias_by_validation_alias, read_optional_alias_and_validation_alias, read_model_optional_alias_and_validation_alias
**Dépendances** : typing, pytest, fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /optional-str, /model-optional-str, /optional-alias, /model-optional-alias, /optional-validation-alias, /model-optional-validation-alias, /optional-alias-and-validation-alias, /model-optional-alias-and-validation-alias

### `test_required_str.py`

Module Python. Nombre de lignes: 352. Elements detectés: class CookieModelRequiredStr, def test_required_str_schema, def test_required_str_missing

**Classes** : CookieModelRequiredStr, CookieModelRequiredAlias, CookieModelRequiredValidationAlias, CookieModelRequiredAliasAndValidationAlias
**Fonctions** : test_required_str_schema, test_required_str_missing, test_required_str, test_required_str_alias_schema, test_required_alias_missing, test_required_alias_by_name, test_required_alias_by_alias, read_required_validation_alias, read_model_required_validation_alias, test_required_validation_alias_schema, test_required_validation_alias_missing, test_required_validation_alias_by_name, test_required_validation_alias_by_validation_alias, read_required_alias_and_validation_alias, read_model_required_alias_and_validation_alias
**Dépendances** : typing, pytest, dirty_equals, fastapi, fastapi.testclient, inline_snapshot, pydantic
**API** : /required-str, /model-required-str, /required-alias, /model-required-alias, /required-validation-alias, /model-required-validation-alias, /required-alias-and-validation-alias, /model-required-alias-and-validation-alias
