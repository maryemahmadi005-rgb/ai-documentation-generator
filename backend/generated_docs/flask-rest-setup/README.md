# flask-rest-setup

# flask-rest-setup

## Description
Le projet Flask-REST-Setup est un exemple de mise en œuvre d'une API REST avec Flask. Il utilise les technologies suivantes :

*   Python 3.x
*   Flask 2.x
*   SQLAlchemy 1.x (pour la gestion des bases de données)
*   JWT ( pour l'authentification)

Le projet fournit une API REST avec les points d'entrée suivants :

*   `/users`: récupération de tous les utilisateurs
*   `/users/<id>`: récupération d'un utilisateur spécifique
*   `/users`: création d'un nouvel utilisateur
*   `/users/<id>`: mise à jour d'un utilisateur spécifique

Le code source fourni dans l'inventaire est une preuve directe de la logique et des fonctionnalités du projet.

Analyse réellement les fonctions, classes et logique présentes :

*   La classe `User` définit les attributs et les méthodes pour gérer les utilisateurs.
*   La fonction `create_user` crée un nouvel utilisateur en base de données.
*   La fonction `get_users` récupère tous les utilisateurs en base de données.

## Features
Le projet présente les fonctionnalités suivantes :

*   Création d'utilisateurs
*   Récupération des utilisateurs
*   Mise à jour des utilisateurs

## Technologies Used
Les technologies utilisées dans le projet sont :

*   Python 3.x
*   Flask 2.x
*   SQLAlchemy 1.x
*   JWT

## Prerequisites
Pour utiliser le projet, vous aurez besoin de :

*   Python 3.x installé sur votre système
*   Les dépendances requises (`Flask`, `SQLAlchemy`, `JWT`) installées via pip

## Installation
Pour installer le projet, suivez les étapes suivantes :

1.  Installez les dépendances requises en exécutant la commande `pip install -r requirements.txt`
2.  Créez un fichier de configuration (`config.py`) avec vos informations de base de données
3.  Exécutez la commande `python app.py` pour démarrer l'application

## Usage
Pour utiliser le projet, suivez les étapes suivantes :

1.  Lancez l'application en exécutant la commande `python app.py`
2.  Utilisez la commande `curl` ou une interface de ligne de commande pour interagir avec l'API REST :
    *   Récupération des utilisateurs : `http://localhost:5000/users`
    *   Création d'un nouvel utilisateur : `http://localhost:5000/users`
    *   Mise à jour d'un utilisateur spécifique : `http://localhost:5000/users/<id>`

Notez que les points d'entrée et les commandes de ligne de commande peuvent varier en fonction des besoins spécifiques de votre projet.
