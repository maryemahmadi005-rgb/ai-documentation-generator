# Diagrammes du projet

## Architecture

```mermaid
graph TD
presentation["Presentation / Routes"]
business["Business / Service Layer"]
data["Data / Repository Layer"]
presentation --> business
business --> data
```

## Flux de données

```mermaid
graph TD
user(["User"])
request["Request"]
routes["Routes / API"]
service["Service Layer"]
response["Response"]
user --> request
request --> routes
routes --> service
service --> response
```

## Dépendances des modules

```mermaid
graph TD
info["Module dependency diagram unavailable"]
```

## Arborescence du projet

```mermaid
graph TD
ROOT["umi-falsk-api"]
ROOT_apps["apps/"]
ROOT --> ROOT_apps
ROOT_apps_models["models/"]
ROOT_apps --> ROOT_apps_models
ROOT_apps_services["services/"]
ROOT_apps --> ROOT_apps_services
ROOT_routes["routes/"]
ROOT --> ROOT_routes
ROOT_utils["utils/"]
ROOT --> ROOT_utils
```
