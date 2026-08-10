# Diagrammes du projet

## Architecture

```mermaid
graph TD
presentation["Presentation / Routes"]
data["Data / Repository Layer"]
presentation --> data
```

## Flux de données

```mermaid
graph TD
user(["User"])
request["Request"]
controller["Controller"]
response["Response"]
user --> request
request --> controller
controller --> response
```

## Dépendances des modules

```mermaid
graph TD
info["Module dependency diagram unavailable"]
```

## Arborescence du projet

```mermaid
graph TD
ROOT["calculator"]
ROOT_api["api/"]
ROOT --> ROOT_api
ROOT_api_controllers["controllers/"]
ROOT_api --> ROOT_api_controllers
ROOT_api_models["models/"]
ROOT_api --> ROOT_api_models
ROOT_public["public/"]
ROOT --> ROOT_public
ROOT_test["test/"]
ROOT --> ROOT_test
```
