# Module : tests/tests_checks

5 fichier(s), 31 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : get_normalized_file_path, test_check_custom_settings, test_check_dir, test_check_err, test_check_err_exp_table, test_check_err_fig, test_check_err_fig_word_cloud, test_check_err_file_area, test_check_err_table, test_check_file_paths_duplicate, test_check_file_paths_empty, test_check_file_paths_unsupported, test_check_new_name, test_check_new_path, test_check_nlp_support
- **Dépendances** : os, shutil, tests, wordless.wl_checks, wordless.wl_utils

## Détail des fichiers

### `test_checks_files.py`

Module Python. Nombre de lignes: 58. Elements detectés: def get_normalized_file_path, def test_check_file_paths_unsupported, def test_check_file_paths_empty

**Fonctions** : get_normalized_file_path, test_check_file_paths_unsupported, test_check_file_paths_empty, test_check_file_paths_duplicate, test_check_err_file_area
**Dépendances** : tests, wordless.wl_checks, wordless.wl_utils

### `test_checks_misc.py`

Module Python. Nombre de lignes: 56. Elements detectés: def test_check_custom_settings, def test_check_dir, def test_check_new_name

**Fonctions** : test_check_custom_settings, test_check_dir, test_check_new_name, test_check_new_path
**Dépendances** : os, shutil, wordless.wl_checks

### `test_checks_tokens.py`

Module Python. Nombre de lignes: 67. Elements detectés: def test_is_word_alphanumeric, def test_is_word_alphabetic, def test_is_num

**Fonctions** : test_is_word_alphanumeric, test_is_word_alphabetic, test_is_num, test_is_punc, test_is_han, test_is_kana, test_is_tibetan, test_has_han, test_has_kana, test_has_tibetan
**Dépendances** : wordless.wl_checks

### `test_checks_work_area.py`

Module Python. Nombre de lignes: 120. Elements detectés: def test_wl_status_bar_missing_search_terms, def test_wl_status_bar_err_fatal, def test_check_search_terms

**Fonctions** : test_wl_status_bar_missing_search_terms, test_wl_status_bar_err_fatal, test_check_search_terms, test_check_nlp_support, test_check_results, test_check_results_download_model, test_check_postprocessing, test_check_err, test_check_err_table, test_check_err_fig, test_check_err_fig_word_cloud, test_check_err_exp_table
**Dépendances** : tests, wordless.wl_checks, wordless.wl_utils
