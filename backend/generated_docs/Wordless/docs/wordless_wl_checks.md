# Module : wordless/wl_checks

5 fichier(s), 31 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : check_custom_settings, check_dir, check_err, check_err_exp_table, check_err_fig, check_err_fig_word_cloud, check_err_file_area, check_err_table, check_file_paths_dup, check_file_paths_empty, check_file_paths_unsupported, check_new_name, check_new_path, check_nlp_support, check_postprocessing
- **Dépendances** : PyQt5, importlib, os, pathlib, re, traceback, wordless.wl_checks, wordless.wl_dialogs, wordless.wl_utils

## Détail des fichiers

### `wl_checks_files.py`

Module Python. Nombre de lignes: 74. Elements detectés: def check_file_paths_unsupported, def check_file_paths_empty, def check_file_paths_dup

**Fonctions** : check_file_paths_unsupported, check_file_paths_empty, check_file_paths_dup, check_err_file_area
**Dépendances** : os, re, wordless.wl_checks, wordless.wl_dialogs, wordless.wl_utils

### `wl_checks_misc.py`

Module Python. Nombre de lignes: 67. Elements detectés: def check_custom_settings, def get_keys, def check_dir

**Fonctions** : check_custom_settings, get_keys, check_dir, check_new_name, check_new_path
**Dépendances** : os, pathlib

### `wl_checks_tokens.py`

Module Python. Nombre de lignes: 135.

**Fonctions** : is_word_alphanumeric, is_word_alphabetic, is_num, is_punc, is_han, is_kana, is_tibetan, has_han, has_kana, has_tibetan

### `wl_checks_work_area.py`

Module Python. Nombre de lignes: 216. Elements detectés: def wl_status_bar_missing_search_terms, def wl_status_bar_err_fatal, def check_search_terms

**Fonctions** : wl_status_bar_missing_search_terms, wl_status_bar_err_fatal, check_search_terms, check_nlp_support, check_results, check_results_download_model, check_postprocessing, check_err, check_err_table, check_err_fig, check_err_fig_word_cloud, check_err_exp_table
**Dépendances** : importlib, traceback, PyQt5, wordless.wl_dialogs, wordless.wl_utils
