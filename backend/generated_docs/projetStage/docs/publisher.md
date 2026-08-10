# Module : publisher

3 fichier(s), 1 classe(s), 14 fonction(s).

## Vue d'ensemble

- **Classes principales** : RepoCreationError
- **Fonctions principales** : _construire_url_pr, _publier_nouveau_depot, _publier_sur_branche, cloner_pour_publication, commit_et_push, creer_branche, creer_repo_documentation, creer_repo_github, creer_repo_gitlab, deposer_doc, inserer_token_dans_url, nettoyer_clone_local, publier_avec_strategie, publier_documentation
- **Dépendances** : architecture.restructeur, git, logging, os, publisher.git_publisher, publisher.repo_creator, requests, shutil, typing, urllib.parse

## Détail des fichiers

### `git_publisher.py`

Module Python. Nombre de lignes: 261. Elements detectés: def inserer_token_dans_url, def cloner_pour_publication

**Fonctions** : inserer_token_dans_url, cloner_pour_publication, deposer_doc, creer_branche, commit_et_push, nettoyer_clone_local, publier_documentation
**Dépendances** : os, shutil, logging, urllib.parse, git, architecture.restructeur

### `repo_creator.py`

Module Python. Nombre de lignes: 149. Elements detectés: class RepoCreationError, def creer_repo_github, def creer_repo_gitlab

**Classes** : RepoCreationError
**Fonctions** : creer_repo_github, creer_repo_gitlab, creer_repo_documentation
**Dépendances** : os, logging, requests, typing

### `strategie.py`

Module Python. Nombre de lignes: 165. Elements detectés: def publier_avec_strategie, def _publier_sur_branche

**Fonctions** : publier_avec_strategie, _publier_sur_branche, _publier_nouveau_depot, _construire_url_pr
**Dépendances** : os, logging, publisher.git_publisher, publisher.repo_creator
