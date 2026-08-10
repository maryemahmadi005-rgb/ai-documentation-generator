# Module : sentiment-clf

5 fichier(s), 2 classe(s), 12 fonction(s).

## Vue d'ensemble

- **Classes principales** : NLPModel, PredictSentiment
- **Fonctions principales** : __init__, build_model, get, pickle_clf, pickle_vectorizer, plot_roc, predict, predict_proba, train, vectorizer_fit, vectorizer_transform
- **Dépendances** : flask, flask_restful, matplotlib.pyplot, model, numpy, pandas, pickle, sklearn.feature_extraction.text, sklearn.metrics, sklearn.model_selection, sklearn.naive_bayes, util

## Détail des fichiers

### `README.md`

Source file. Nombre de lignes: 60.

### `app.py`

Module Python. Nombre de lignes: 41. Elements detectés: class PredictSentiment, def get

**Classes** : PredictSentiment
**Fonctions** : get
**Dépendances** : flask, flask_restful, pickle, numpy, model

### `build_model.py`

Module Python. Nombre de lignes: 27. Elements detectés: def build_model

**Fonctions** : build_model
**Dépendances** : model, pandas, sklearn.model_selection

### `model.py`

Module Python. Nombre de lignes: 58. Elements detectés: class NLPModel, def __init__, def vectorizer_fit

**Classes** : NLPModel
**Fonctions** : __init__, vectorizer_fit, vectorizer_transform, train, predict_proba, predict, pickle_vectorizer, pickle_clf, plot_roc
**Dépendances** : sklearn.naive_bayes, sklearn.feature_extraction.text, pickle, util

### `util.py`

Module Python. Nombre de lignes: 30. Elements detectés: def plot_roc

**Fonctions** : plot_roc
**Dépendances** : sklearn.metrics, matplotlib.pyplot
