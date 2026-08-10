# Module : tests/tests_utils

8 fichier(s), 1 classe(s), 50 fonction(s).

## Vue d'ensemble

- **Classes principales** : Widget
- **Fonctions principales** : check_encodings_detected, parent, test_change_file_owner_to_user, test_check_noun_number, test_check_os, test_detection_encoding, test_detection_lang, test_find_wl_main, test_flatten_list, test_get_linux_distro, test_get_normalized_dir, test_get_normalized_path, test_get_path_data, test_get_path_file, test_get_path_img
- **Dépendances** : charset_normalizer, lingua, os, platform, pytest, re, shutil, sys, tests, wordless.wl_dialogs, wordless.wl_utils

## Détail des fichiers

### `test_conversion.py`

Module Python. Nombre de lignes: 124. Elements detectés: def test_normalize_lang_code, def test_to_lang_code, def test_to_lang_codes

**Fonctions** : test_normalize_lang_code, test_to_lang_code, test_to_lang_codes, test_to_lang_text, test_to_lang_texts, test_to_iso_639_3, test_to_iso_639_1, test_remove_lang_code_suffixes, test_to_encoding_code, test_to_encoding_text, test_to_yes_no_code, test_to_yes_no_text
**Dépendances** : pytest, tests, wordless.wl_utils

### `test_detection.py`

Module Python. Nombre de lignes: 351. Elements detectés: def check_encodings_detected, def test_detection_encoding

**Fonctions** : check_encodings_detected, test_detection_encoding, test_lingua, test_detection_lang
**Dépendances** : os, re, shutil, charset_normalizer, lingua, tests, wordless.wl_utils

### `test_excs.py`

Module Python. Nombre de lignes: 66. Elements detectés: def test_wl_exc, def test_wl_exc_aborted, def test_wl_exc_word_cloud

**Fonctions** : test_wl_exc, test_wl_exc_aborted, test_wl_exc_word_cloud, test_wl_exc_word_cloud_font, test_wl_exc_word_cloud_font_nonexistent, test_wl_exc_word_cloud_font_is_dir, test_wl_exc_word_cloud_font_unsupported, test_wl_exc_word_cloud_mask, test_wl_exc_word_cloud_mask_nonexistent, test_wl_exc_word_cloud_mask_is_dir, test_wl_exc_word_cloud_mask_unsupported
**Dépendances** : pytest, tests, wordless.wl_utils

### `test_misc.py`

Module Python. Nombre de lignes: 106. Elements detectés: def test_check_os, def test_get_linux_distro, def test_change_file_owner_to_user

**Classes** : Widget
**Fonctions** : test_check_os, test_get_linux_distro, test_change_file_owner_to_user, test_find_wl_main, parent, test_get_wl_ver, test_wl_get_proxies, test_wl_download, test_wl_download_file_size, test_flatten_list, test_merge_dicts, test_normalize_nums, test_check_noun_number
**Dépendances** : os, platform, re, tests, wordless.wl_utils

### `test_paths.py`

Module Python. Nombre de lignes: 55. Elements detectés: def test_get_normalized_path, def test_get_normalized_dir, def test_get_path_file

**Fonctions** : test_get_normalized_path, test_get_normalized_dir, test_get_path_file, test_get_path_data, test_get_path_img
**Dépendances** : os, sys, wordless.wl_utils

### `test_sorting.py`

Module Python. Nombre de lignes: 70. Elements detectés: def test_sorted_freq_files_items, def test_sorted_freq_files_items_keyword_extractor, def test_sorted_stats_files_items

**Fonctions** : test_sorted_freq_files_items, test_sorted_freq_files_items_keyword_extractor, test_sorted_stats_files_items
**Dépendances** : wordless.wl_utils

### `test_threading.py`

Module Python. Nombre de lignes: 30. Elements detectés: def test_wl_worker, def test_wl_worker_no_progress

**Fonctions** : test_wl_worker, test_wl_worker_no_progress
**Dépendances** : tests, wordless.wl_dialogs, wordless.wl_utils
