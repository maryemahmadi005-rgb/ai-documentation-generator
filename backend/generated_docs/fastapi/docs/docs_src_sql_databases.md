# Module : docs_src/sql_databases

5 fichier(s), 12 classe(s), 30 fonction(s).

## Vue d'ensemble

- **Classes principales** : Hero, HeroBase, HeroCreate, HeroPublic, HeroUpdate
- **Fonctions principales** : create_db_and_tables, create_hero, delete_hero, get_session, on_startup, read_hero, read_heroes, update_hero
- **Dépendances** : fastapi, sqlmodel, typing
- **Endpoints API** : /heroes/, /heroes/{hero_id}

## Détail des fichiers

### `tutorial001_an_py310.py`

Module Python. Nombre de lignes: 50. Elements detectés: class Hero, def create_db_and_tables, def get_session

**Classes** : Hero
**Fonctions** : create_db_and_tables, get_session, on_startup, create_hero, read_heroes, read_hero, delete_hero
**Dépendances** : typing, fastapi, sqlmodel
**API** : /heroes/, /heroes/{hero_id}

### `tutorial001_py310.py`

Module Python. Nombre de lignes: 48. Elements detectés: class Hero, def create_db_and_tables, def get_session

**Classes** : Hero
**Fonctions** : create_db_and_tables, get_session, on_startup, create_hero, read_heroes, read_hero, delete_hero
**Dépendances** : fastapi, sqlmodel
**API** : /heroes/, /heroes/{hero_id}

### `tutorial002_an_py310.py`

Module Python. Nombre de lignes: 71. Elements detectés: class HeroBase, class Hero, class HeroPublic

**Classes** : HeroBase, Hero, HeroPublic, HeroCreate, HeroUpdate
**Fonctions** : create_db_and_tables, get_session, on_startup, create_hero, read_heroes, read_hero, update_hero, delete_hero
**Dépendances** : typing, fastapi, sqlmodel
**API** : /heroes/, /heroes/{hero_id}

### `tutorial002_py310.py`

Module Python. Nombre de lignes: 71. Elements detectés: class HeroBase, class Hero, class HeroPublic

**Classes** : HeroBase, Hero, HeroPublic, HeroCreate, HeroUpdate
**Fonctions** : create_db_and_tables, get_session, on_startup, create_hero, read_heroes, read_hero, update_hero, delete_hero
**Dépendances** : fastapi, sqlmodel
**API** : /heroes/, /heroes/{hero_id}
