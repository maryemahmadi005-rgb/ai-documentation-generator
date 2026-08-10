# Module : docs_src/extra_models

5 fichier(s), 11 classe(s), 4 fonction(s).

## Vue d'ensemble

- **Classes principales** : BaseItem, CarItem, Item, PlaneItem, UserBase, UserIn, UserInDB, UserOut
- **Fonctions principales** : fake_password_hasher, fake_save_user
- **Dépendances** : fastapi, pydantic
- **Endpoints API** : /items/, /items/{item_id}, /user/

## Détail des fichiers

### `tutorial001_py310.py`

Module Python. Nombre de lignes: 28. Elements detectés: class UserIn, class UserOut, class UserInDB

**Classes** : UserIn, UserOut, UserInDB
**Fonctions** : fake_password_hasher, fake_save_user
**Dépendances** : fastapi, pydantic
**API** : /user/

### `tutorial002_py310.py`

Module Python. Nombre de lignes: 24. Elements detectés: class UserBase, class UserIn, class UserOut

**Classes** : UserBase, UserIn, UserOut, UserInDB
**Fonctions** : fake_password_hasher, fake_save_user
**Dépendances** : fastapi, pydantic
**API** : /user/

### `tutorial003_py310.py`

Module Python. Nombre de lignes: 22. Elements detectés: class BaseItem, class CarItem, class PlaneItem

**Classes** : BaseItem, CarItem, PlaneItem
**Dépendances** : fastapi, pydantic
**API** : /items/{item_id}

### `tutorial004_py310.py`

Module Python. Nombre de lignes: 13. Elements detectés: class Item

**Classes** : Item
**Dépendances** : fastapi, pydantic
**API** : /items/
