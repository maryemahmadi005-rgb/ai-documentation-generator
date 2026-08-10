# Module : Racine du projet

5 fichier(s), 7 classe(s), 5 fonction(s).

## Vue d'ensemble

- **Classes principales** : Config, DevelopmentConfig, DockerConfig, HerokuConfig, ProductionConfig, TestingConfig, UnixConfig
- **Fonctions principales** : deploy, init_app, make_shell_context, profile, test
- **Dépendances** : app, app.models, click, coverage, dotenv, flask_migrate, logging, logging.handlers, os, subprocess, sys, unittest

## Détail des fichiers

### `README.md`

Source file. Nombre de lignes: 7.

### `boot.sh`

Source file. Nombre de lignes: 11.

### `config.py`

Module Python. Nombre de lignes: 103. Elements detectés: class Config:, def init_app, class DevelopmentConfig

**Classes** : Config, DevelopmentConfig, TestingConfig, ProductionConfig, HerokuConfig, DockerConfig, UnixConfig
**Fonctions** : init_app
**Dépendances** : os, logging, logging.handlers, werkzeug.middleware.proxy_fix, werkzeug.contrib.fixers

### `docker-compose.yml`

Source file. Nombre de lignes: 14.

### `flasky.py`

Module Python. Nombre de lignes: 67. Elements detectés: def make_shell_context, def test, def profile

**Fonctions** : make_shell_context, test, profile, deploy
**Dépendances** : os, dotenv, coverage, sys, click, flask_migrate, app, app.models, subprocess, unittest, werkzeug.contrib.profiler
