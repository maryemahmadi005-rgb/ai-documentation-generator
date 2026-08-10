# Module : utils

14 fichier(s), 8 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : convert_readme_zho_tw, convert_to_zho_tw, del_obsolete_trans, download_modern_botok, download_pkuseg, fix_ts_format, print_with_elapsed_time, release_trs
- **Dépendances** : botok, bs4, collections, datetime, glob, nltk, opencc, os, pathlib, pip, re, requests

## Détail des fichiers

### `data_luong_nguyen_dinh_freq_syls_easy_1000.py`

Module Python. Nombre de lignes: 35.

**Dépendances** : collections, glob

### `linux_compile_py_from_src.sh`

### `linux_create_shortcut.py`

Module Python. Nombre de lignes: 40.

**Dépendances** : os, subprocess, wordless.wl_utils

### `wl_download_ci.py`

Module Python. Nombre de lignes: 33.

**Dépendances** : nltk, spacy, stanza

### `wl_download_modern_botok.py`

Module Python. Nombre de lignes: 56. Elements detectés: def download_modern_botok

**Fonctions** : download_modern_botok
**Dépendances** : os, shutil, botok, pip, requests

### `wl_download_pkuseg.py`

Module Python. Nombre de lignes: 46. Elements detectés: def download_pkuseg

**Fonctions** : download_pkuseg
**Dépendances** : os, shutil, zipfile, spacy_pkuseg, requests

### `wl_generate_acks.py`

Module Python. Nombre de lignes: 230.

**Dépendances** : utils

### `wl_generate_readme_zho_tw.py`

Module Python. Nombre de lignes: 62. Elements detectés: def convert_to_zho_tw, def convert_readme_zho_tw

**Fonctions** : convert_to_zho_tw, convert_readme_zho_tw
**Dépendances** : opencc

### `wl_packaging.py`

Module Python. Nombre de lignes: 97. Elements detectés: def print_with_elapsed_time

**Fonctions** : print_with_elapsed_time
**Dépendances** : datetime, os, shutil, subprocess, time, wordless.wl_utils

### `wl_trs_generate_ts_files.py`

Module Python. Nombre de lignes: 34.

**Dépendances** : pathlib, re, subprocess

### `wl_trs_translate.py`

Module Python. Nombre de lignes: 414.

**Dépendances** : re, bs4, utils

### `wl_trs_utils.py`

Module Python. Nombre de lignes: 49. Elements detectés: def fix_ts_format, def del_obsolete_trans, def release_trs

**Fonctions** : fix_ts_format, del_obsolete_trans, release_trs
**Dépendances** : glob, subprocess, bs4

### `wl_trs_zho_tw.py`

Module Python. Nombre de lignes: 44.

**Dépendances** : bs4, opencc, utils
