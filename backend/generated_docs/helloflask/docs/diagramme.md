# Diagrammes du projet

## Architecture

```mermaid
graph TD
presentation["Presentation / Routes"]
database[("Database")]
presentation --> database
```

## Flux de données

```mermaid
graph TD
user(["User"])
request["Request"]
routes["Routes / API"]
database[("Database")]
response["Response"]
user --> request
request --> routes
routes --> database
database --> response
```

## Dépendances des modules

```mermaid
graph TD
info["Module dependency diagram unavailable"]
```

## Arborescence du projet

```mermaid
graph TD
ROOT["helloflask"]
ROOT_demos["demos/"]
ROOT --> ROOT_demos
ROOT_demos_assets["assets/"]
ROOT_demos --> ROOT_demos_assets
ROOT_demos_cache["cache/"]
ROOT_demos --> ROOT_demos_cache
ROOT_demos_database["database/"]
ROOT_demos --> ROOT_demos_database
ROOT_demos_email["email/"]
ROOT_demos --> ROOT_demos_email
ROOT_demos_form["form/"]
ROOT_demos --> ROOT_demos_form
ROOT_demos_hello["hello/"]
ROOT_demos --> ROOT_demos_hello
ROOT_demos_http["http/"]
ROOT_demos --> ROOT_demos_http
ROOT_demos_template["template/"]
ROOT_demos --> ROOT_demos_template
ROOT_docs["docs/"]
ROOT --> ROOT_docs
ROOT_docs_basics["basics/"]
ROOT_docs --> ROOT_docs_basics
ROOT_docs_book["book/"]
ROOT_docs --> ROOT_docs_book
ROOT_docs_extensions["extensions/"]
ROOT_docs --> ROOT_docs_extensions
ROOT_docs__assets["_assets/"]
ROOT_docs --> ROOT_docs__assets
ROOT_docs__templates["_templates/"]
ROOT_docs --> ROOT_docs__templates
ROOT_examples["examples/"]
ROOT --> ROOT_examples
ROOT_examples_album["album/"]
ROOT_examples --> ROOT_examples_album
ROOT_examples_assets["assets/"]
ROOT_examples --> ROOT_examples_assets
ROOT_examples_c3["c3/"]
ROOT_examples --> ROOT_examples_c3
ROOT_examples_cache["cache/"]
ROOT_examples --> ROOT_examples_cache
ROOT_examples_ch1["ch1/"]
ROOT_examples --> ROOT_examples_ch1
ROOT_examples_ch2["ch2/"]
ROOT_examples --> ROOT_examples_ch2
ROOT_examples_ch3["ch3/"]
ROOT_examples --> ROOT_examples_ch3
ROOT_examples_ch4["ch4/"]
ROOT_examples --> ROOT_examples_ch4
ROOT_examples_ch5["ch5/"]
ROOT_examples --> ROOT_examples_ch5
ROOT_examples_ckeditor["ckeditor/"]
ROOT_examples --> ROOT_examples_ckeditor
ROOT_examples_longtalk["longtalk/"]
ROOT_examples --> ROOT_examples_longtalk
ROOT_examples_notebook["notebook/"]
ROOT_examples --> ROOT_examples_notebook
ROOT_requirements["requirements/"]
ROOT --> ROOT_requirements
ROOT_tests["tests/"]
ROOT --> ROOT_tests
```
