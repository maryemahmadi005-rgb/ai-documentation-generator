## Description courte
Ce projet est une application web basée sur Flask, un framework léger et flexible pour les applications Web. Il permet de générer automatiquement des documents à partir d'entrées utilisateur.

## Objectif général
L'objectif principal de ce projet est de fournir une solution simple et efficace pour générer des documents à partir d'entrées utilisateur.

## Technologies principales
- Python (pyproject)
- Flask (framework web léger)

## Utilisation / installation
Pour utiliser ce projet, il suffit d'exécuter les commandes suivantes :
```bash
$ python -m flask run
```
Cela lancerait l'application et la rendra accessible sur `http://127.0.0.1:5000/`.

## Structure générale simple
Le projet est organisé en plusieurs fichiers principaux, notamment :
- `src/flask/app.py` : le fichier principal de l'application.
- `tests/test_apps/cliapp/app.py` : les tests unitaires de l'application.
- `tests/test_apps/helloworld/wsgi.py` : les tests WSGI de l'application.