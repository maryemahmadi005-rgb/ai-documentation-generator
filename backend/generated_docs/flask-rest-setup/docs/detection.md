# Détection automatique

Architecture : **Unknown Architecture**

Confiance : 33.3%

## Classement

| Architecture | Score | Confiance |
|---|---|---|
| Flask Application | 8 | 33.3% |

## Analyse IA

# Objectif du projet
L'objectif principal du projet est de créer une API RESTful pour analyser le sentiment des textes à l'aide d'un modèle de classification basé sur le Naïve Bayes.

## Fonctionnement général
Le flux de travail se déroule comme suit :
- L'utilisateur envoie un texte à analyser à l'API.
- L'API traite le texte et utilise le modèle de classification pour préparer les données.
- Le modèle de classification est utilisé pour prédire le sentiment du texte (positif ou négatif).
- La réponse est renvoyée à l'utilisateur sous forme de JSON.

## Architecture
L'architecture du projet a été détectée comme une architecture RESTful, avec un serveur Flask en tant que point de départ. Les classes principales sont les suivantes :
- `HelloWorld` : une classe qui représente la fonctionnalité principale de l'API.
- `PredictSentiment` : une classe qui utilise le modèle de classification pour analyser le sentiment des textes.

Cependant, il est important de noter que cette détection n'est pas 100% fiable et qu'il y a des limites à cette analyse. La confiance dans cette détection est de 33.3%.

## Technologies utilisées
- Python : langue de programmation principale.
- Flask : framework web utilisé pour créer l'API RESTful.
- Flask-Restful : bibliothèque qui facilite la création d'API RESTful avec Flask.
- Matplotlib : bibliothèque graphique utilisée pour visualiser les résultats du modèle de classification.
- Model : module Python qui contient le modèle de classification utilisé pour analyser le sentiment des textes.

## Modules principaux
### `sentiment-clf/app.py`
- Rôle : point d'entrée de l'API RESTful.
- Classes principales :
  - `PredictSentiment` : classe qui utilise le modèle de classification pour analyser le sentiment des textes.
- Fonctions importantes :
  - `get` : fonction qui renvoie la réponse du modèle de classification.
- Dépendances :
  - Flask-Restful
  - Matplotlib

### `sentiment-clf/build_model.py`
- Rôle : construction du modèle de classification.
- Classes principales :
  - `NLPModel` : classe qui contient le modèle de classification utilisé pour analyser le sentiment des textes.
- Fonctions importantes :
  - `build_model` : fonction qui construit le modèle de classification à partir des données.
- Dépendances :
  - Model
  - Pandas
  - Scikit-learn

### `sentiment-clf/model.py`
- Rôle : contient le modèle de classification utilisé pour analyser le sentiment des textes.
- Classes principales :
  - `NLPModel` : classe qui contient le modèle de classification utilisé pour analyser le sentiment des textes.
- Fonctions importantes :
  - `__init__` : fonction qui initialise le modèle de classification.
  - `vectorizer_fit` : fonction qui ajuste le vectoriseur du modèle de classification.
- Dépendances :
  - Scikit-learn
  - Pickle

### `sentiment-clf/util.py`
- Rôle : contient des fonctions utiles pour l'analyse du sentiment.
- Classes principales :
  - `plot_roc` : fonction qui affiche un graphique ROC pour le modèle de classification.
- Fonctions importantes :
  - `plot_roc` : fonction qui affiche un graphique ROC pour le modèle de classification.
- Dépendances :
  - Matplotlib
  - Scikit-learn

## Flux de données
Le flux de données se déroule comme suit :
- L'utilisateur