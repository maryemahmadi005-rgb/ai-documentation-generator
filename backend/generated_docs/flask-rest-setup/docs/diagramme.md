# Diagrammes du projet

## Architecture

```mermaid
graph TD
data["Data / Repository Layer"]
```

## Flux de données

```mermaid
graph TD
input(["Input (composants non identifiés)"])
processing["Processing"]
output["Output"]
input --> processing
processing --> output
```

## Dépendances des modules

```mermaid
graph TD
info["Module dependency diagram unavailable"]
```

## Arborescence du projet

```mermaid
graph TD
ROOT["flask-rest-setup"]
ROOT_a_minimal_api["a-minimal-api/"]
ROOT --> ROOT_a_minimal_api
ROOT_notebooks["notebooks/"]
ROOT --> ROOT_notebooks
ROOT_sentiment_clf["sentiment-clf/"]
ROOT --> ROOT_sentiment_clf
ROOT_sentiment_clf_lib["lib/"]
ROOT_sentiment_clf --> ROOT_sentiment_clf_lib
ROOT_to_do_api["to-do-api/"]
ROOT --> ROOT_to_do_api
```
