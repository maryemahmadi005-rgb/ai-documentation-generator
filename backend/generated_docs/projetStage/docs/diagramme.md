# Diagrammes du projet

## Architecture

```mermaid
graph TD
presentation["Presentation / Routes"]
```

## Flux de données

```mermaid
graph TD
user(["User"])
request["Request"]
routes["Routes / API"]
response["Response"]
user --> request
request --> routes
routes --> response
```

## Dépendances des modules

```mermaid
graph TD
info["Module dependency diagram unavailable"]
```

## Arborescence du projet

```mermaid
graph TD
ROOT["projetStage"]
ROOT_architecture["architecture/"]
ROOT --> ROOT_architecture
ROOT_generation["generation/"]
ROOT --> ROOT_generation
ROOT_publisher["publisher/"]
ROOT --> ROOT_publisher
ROOT_scanners["scanners/"]
ROOT --> ROOT_scanners
ROOT_templates["templates/"]
ROOT --> ROOT_templates
ROOT_temp_repo["temp_repo/"]
ROOT --> ROOT_temp_repo
ROOT_utils["utils/"]
ROOT --> ROOT_utils
```
