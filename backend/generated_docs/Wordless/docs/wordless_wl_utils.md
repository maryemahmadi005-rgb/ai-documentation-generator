# Module : wordless/wl_utils

8 fichier(s), 10 classe(s), 42 fonction(s).

## Vue d'ensemble

- **Classes principales** : Wl_Exc, Wl_Exc_Aborted, Wl_Exc_Word_Cloud, Wl_Exc_Word_Cloud_Font, Wl_Exc_Word_Cloud_Font_Is_Dir, Wl_Exc_Word_Cloud_Font_Nonexistent, Wl_Exc_Word_Cloud_Font_Unsupported, Wl_Exc_Word_Cloud_Mask, Wl_Worker, Wl_Worker_No_Progress
- **Fonctions principales** : __init__, change_file_owner_to_user, check_noun_number, check_os, detect_encoding, detect_lang_file, detect_lang_text, find_wl_main, flatten_list, get_linux_distro, get_normalized_dir, get_normalized_path, get_path_data, get_path_file, get_path_img
- **Dépendances** : PyQt5, charset_normalizer, collections, copy, lingua, numpy, opencc, os, packaging.version, platform, re, requests

## Détail des fichiers

### `wl_conversion.py`

Module Python. Nombre de lignes: 102. Elements detectés: def normalize_lang_code, def to_lang_code, def to_lang_codes

**Fonctions** : normalize_lang_code, to_lang_code, to_lang_codes, to_lang_text, to_lang_texts, to_iso_639_3, to_iso_639_1, remove_lang_code_suffixes, to_encoding_code, to_encoding_text, to_yes_no_code, to_yes_no_text
**Dépendances** : PyQt5

### `wl_detection.py`

Module Python. Nombre de lignes: 98. Elements detectés: def detect_encoding, def detect_lang_text, def detect_lang_file

**Fonctions** : detect_encoding, detect_lang_text, detect_lang_file
**Dépendances** : charset_normalizer, lingua, opencc

### `wl_excs.py`

Module Python. Nombre de lignes: 43. Elements detectés: class Wl_Exc, class Wl_Exc_Aborted, def __init__

**Classes** : Wl_Exc, Wl_Exc_Aborted, Wl_Exc_Word_Cloud, Wl_Exc_Word_Cloud_Font, Wl_Exc_Word_Cloud_Font_Nonexistent, Wl_Exc_Word_Cloud_Font_Is_Dir, Wl_Exc_Word_Cloud_Font_Unsupported, Wl_Exc_Word_Cloud_Mask
**Fonctions** : __init__
**Dépendances** : PyQt5

### `wl_misc.py`

Module Python. Nombre de lignes: 181. Elements detectés: def check_os, def get_linux_distro, def change_file_owner_to_user

**Fonctions** : check_os, get_linux_distro, change_file_owner_to_user, find_wl_main, get_wl_ver, wl_get_proxies, wl_download, wl_download_file_size, log_time, wrapper, flatten_list, merge_dicts, normalize_nums, check_noun_number
**Dépendances** : collections, copy, os, platform, re, time, traceback, urllib, numpy, packaging.version, PyQt5, requests

### `wl_paths.py`

Module Python. Nombre de lignes: 44. Elements detectés: def get_normalized_path, def get_normalized_dir, def get_path_file

**Fonctions** : get_normalized_path, get_normalized_dir, get_path_file, get_path_data, get_path_img
**Dépendances** : os, sys, wordless.wl_utils

### `wl_sorting.py`

Module Python. Nombre de lignes: 70. Elements detectés: def sorted_freq_files_items, def key, def sorted_freq_files_items_keyword_extractor

**Fonctions** : sorted_freq_files_items, key, sorted_freq_files_items_keyword_extractor, sorted_stats_files_items

### `wl_threading.py`

Module Python. Nombre de lignes: 62. Elements detectés: class Wl_Worker, def __init__, def stop

**Classes** : Wl_Worker, Wl_Worker_No_Progress
**Fonctions** : __init__, stop, start_worker_in_thread
**Dépendances** : time, PyQt5
