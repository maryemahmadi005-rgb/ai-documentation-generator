# Objectif du projet

Le but réel du projet est de créer une API RESTful avec Flask et Flask-Restful pour analyser le sentiment des textes. Les technologies détectées sont Python, Flask et Flask-Restful. Le code source fourni inclut les fichiers clés suivants :

- `a-minimal-api/api.py` : Module Python qui définit une API simple pour retourner un message "Hello World".
- `sentiment-clf/app.py` : Module Python qui définit l'API principale pour analyser le sentiment des textes.
- `to-do-api/api.py` : Module Python qui définit une API pour gérer les tâches.

## Fonctionnement général

Le système est composé de plusieurs modules :

- Le module `a-minimal-api` définit une API simple pour retourner un message "Hello World".
- Le module `sentiment-clf` définit l'API principale pour analyser le sentiment des textes. Il utilise la bibliothèque `model` pour effectuer l'analyse.
- Le module `to-do-api` définit une API pour gérer les tâches.

Les interactions entre ces modules sont suivies dans le fichier `app.py` du module `sentiment-clf`.

## Architecture détée

L'architecture détectée est basée sur la structure de projet fournie. Les fichiers clés et les points d'entrée sont utilisés pour comprendre le fonctionnement global du système.

## Technologies utilisées

Les technologies utilisées dans ce projet sont :

- Python : Langage de programmation principal.
- Flask : Framework web utilisé pour créer l'API RESTful.
- Flask-Restful : Bibliothèque pour créer les API RESTful avec Flask.
- model : Bibliothèque spécifique pour analyser le sentiment des textes.

## Modules principaux

Les modules importants sont :

- `a-minimal-api` : Module qui définit une API simple.
- `sentiment-clf` : Module qui définit l'API principale pour analyser le sentiment des textes.
- `to-do-api` : Module qui définit une API pour gérer les tâches.

## Flux de données

Le parcours des données est suivant :

- Les données sont chargées à partir d'un fichier CSV (`train.tsv`) dans le dossier `sentiment_data`.
- Les données sont prétraitées et transformées en utilisant la bibliothèque `model`.
- L'analyse du sentiment est effectuée sur les données prétraitées.
- Le résultat de l'analyse est renvoyé à travers l'API RESTful.

## Points d'entrée

Les points d'entrée sont :

- `sentiment-clf/app.py` : Module qui définit l'API principale pour analyser le sentiment des textes.
- `to-do-api/api.py` : Module qui définit une API pour gérer les tâches.

## Dépendances importantes

Les dépendances principales sont :

- Flask : Framework web utilisé pour créer l'API RESTful.
- Flask-Restful : Bibliothèque pour créer les API RESTful avec Flask.
- model : Bibliothèque spécifique pour analyser le sentiment des textes.

## Recommandations

Il est recommandé de tester l'API RESTful pour analyser le sentiment des textes avant de l'utiliser dans un environnement de production.