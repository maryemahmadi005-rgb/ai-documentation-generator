# Diagramme du projet

```mermaid
graph TD
ROOT["ai_doc_gen_awi8ety7"]
ROOT__cache[".cache/"]
ROOT --> ROOT__cache
ROOT__cache_docs["docs/"]
ROOT__cache --> ROOT__cache_docs
ROOT_architecture["architecture/"]
ROOT --> ROOT_architecture
ROOT_generation["generation/"]
ROOT --> ROOT_generation
ROOT_output["output/"]
ROOT --> ROOT_output
ROOT_output_Calculatrice_en_ja["Calculatrice-en-java/"]
ROOT_output --> ROOT_output_Calculatrice_en_ja
ROOT_output_flask["flask/"]
ROOT_output --> ROOT_output_flask
ROOT_output_pluginbase["pluginbase/"]
ROOT_output --> ROOT_output_pluginbase
ROOT_publisher["publisher/"]
ROOT --> ROOT_publisher
ROOT_scanners["scanners/"]
ROOT --> ROOT_scanners
ROOT_static["static/"]
ROOT --> ROOT_static
ROOT_static_css["css/"]
ROOT_static --> ROOT_static_css
ROOT_templates["templates/"]
ROOT --> ROOT_templates
ROOT_temp_repo["temp_repo/"]
ROOT --> ROOT_temp_repo
ROOT_utils["utils/"]
ROOT --> ROOT_utils
```
