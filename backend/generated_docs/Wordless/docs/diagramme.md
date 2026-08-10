# Diagrammes du projet

## Architecture

```mermaid
graph TD
database[("Database")]
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
ROOT["Wordless"]
ROOT_data["data/"]
ROOT --> ROOT_data
ROOT_doc["doc/"]
ROOT --> ROOT_doc
ROOT_doc_measures["measures/"]
ROOT_doc --> ROOT_doc_measures
ROOT_doc_trs["trs/"]
ROOT_doc --> ROOT_doc_trs
ROOT_imgs["imgs/"]
ROOT --> ROOT_imgs
ROOT_requirements["requirements/"]
ROOT --> ROOT_requirements
ROOT_tests["tests/"]
ROOT --> ROOT_tests
ROOT_tests_tests_checks["tests_checks/"]
ROOT_tests --> ROOT_tests_tests_checks
ROOT_tests_tests_dialogs["tests_dialogs/"]
ROOT_tests --> ROOT_tests_tests_dialogs
ROOT_tests_tests_figs["tests_figs/"]
ROOT_tests --> ROOT_tests_tests_figs
ROOT_tests_tests_file_area["tests_file_area/"]
ROOT_tests --> ROOT_tests_tests_file_area
ROOT_tests_tests_measures["tests_measures/"]
ROOT_tests --> ROOT_tests_tests_measures
ROOT_tests_tests_nlp["tests_nlp/"]
ROOT_tests --> ROOT_tests_tests_nlp
ROOT_tests_tests_results["tests_results/"]
ROOT_tests --> ROOT_tests_tests_results
ROOT_tests_tests_settings["tests_settings/"]
ROOT_tests --> ROOT_tests_tests_settings
ROOT_tests_tests_utils["tests_utils/"]
ROOT_tests --> ROOT_tests_tests_utils
ROOT_tests_tests_widgets["tests_widgets/"]
ROOT_tests --> ROOT_tests_tests_widgets
ROOT_trs["trs/"]
ROOT --> ROOT_trs
ROOT_utils["utils/"]
ROOT --> ROOT_utils
ROOT_wordless["wordless/"]
ROOT --> ROOT_wordless
ROOT_wordless_wl_checks["wl_checks/"]
ROOT_wordless --> ROOT_wordless_wl_checks
ROOT_wordless_wl_dialogs["wl_dialogs/"]
ROOT_wordless --> ROOT_wordless_wl_dialogs
ROOT_wordless_wl_figs["wl_figs/"]
ROOT_wordless --> ROOT_wordless_wl_figs
ROOT_wordless_wl_measures["wl_measures/"]
ROOT_wordless --> ROOT_wordless_wl_measures
ROOT_wordless_wl_nlp["wl_nlp/"]
ROOT_wordless --> ROOT_wordless_wl_nlp
ROOT_wordless_wl_results["wl_results/"]
ROOT_wordless --> ROOT_wordless_wl_results
ROOT_wordless_wl_settings["wl_settings/"]
ROOT_wordless --> ROOT_wordless_wl_settings
ROOT_wordless_wl_tagsets["wl_tagsets/"]
ROOT_wordless --> ROOT_wordless_wl_tagsets
ROOT_wordless_wl_utils["wl_utils/"]
ROOT_wordless --> ROOT_wordless_wl_utils
ROOT_wordless_wl_widgets["wl_widgets/"]
ROOT_wordless --> ROOT_wordless_wl_widgets
```
