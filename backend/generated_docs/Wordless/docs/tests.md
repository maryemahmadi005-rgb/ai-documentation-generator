# Module : tests

15 fichier(s), 5 classe(s), 54 fonction(s).

## Vue d'ensemble

- **Classes principales** : Wl_Exc_Tests_Lang_Skipped, Wl_Exc_Tests_Lang_Util_Skipped, Wl_Test_Main, Wl_Test_Table, Wl_Test_Text
- **Fonctions principales** : __init__, check_lang_examples, clean_import_caches, filter_table, get_test_file_names, height, open_file, open_file_ref, select_test_files, set_item, set_label, switch_lang_utils_fast, switch_lang_utils_spacy, switch_lang_utils_stanza, test_colligation_extractor
- **Dépendances** : PyQt5, collections, copy, glob, numpy, os, packaging, pickle, random, re, scipy, sys

## Détail des fichiers

### `test_colligation_extractor.py`

Module Python. Nombre de lignes: 121. Elements detectés: def test_colligation_extractor, def update_gui

**Fonctions** : test_colligation_extractor, update_gui
**Dépendances** : random, tests, wordless, wordless.wl_dialogs

### `test_collocation_extractor.py`

Module Python. Nombre de lignes: 118. Elements detectés: def test_collocation_extractor, def update_gui

**Fonctions** : test_collocation_extractor, update_gui
**Dépendances** : random, tests, wordless, wordless.wl_dialogs

### `test_concordancer.py`

Module Python. Nombre de lignes: 124. Elements detectés: def test_concordancer, def update_gui_table

**Fonctions** : test_concordancer, update_gui_table, update_gui_fig
**Dépendances** : tests, wordless, wordless.wl_dialogs

### `test_concordancer_parallel.py`

Module Python. Nombre de lignes: 78. Elements detectés: def test_concordancer_parallel, def update_gui

**Fonctions** : test_concordancer_parallel, update_gui
**Dépendances** : tests, wordless, wordless.wl_dialogs, wordless.wl_nlp

### `test_dependency_parser.py`

Module Python. Nombre de lignes: 85. Elements detectés: def test_dependency_parser, def update_gui

**Fonctions** : test_dependency_parser, update_gui
**Dépendances** : tests, wordless, wordless.wl_dialogs

### `test_keyword_extractor.py`

Module Python. Nombre de lignes: 143. Elements detectés: def test_keyword_extractor, def update_gui

**Fonctions** : test_keyword_extractor, update_gui, test_keyword_extractor_ngram_size, update_gui_ngram_size
**Dépendances** : random, tests, wordless, wordless.wl_dialogs

### `test_main.py`

Module Python. Nombre de lignes: 93. Elements detectés: def test_wl_loading, def test_wl_dialog_confirm_exit, def test_wl_dialog_need_help

**Fonctions** : test_wl_loading, test_wl_dialog_confirm_exit, test_wl_dialog_need_help, test_wl_dialog_citing, test_wl_dialog_donating, test_wl_dialog_acks, test_wl_dialog_check_updates, test_worker_check_updates, test_wl_dialog_changelog, test_wl_dialog_about
**Dépendances** : packaging, tests, wordless

### `test_ngram_generator.py`

Module Python. Nombre de lignes: 144. Elements detectés: def test_ngram_generator, def update_gui

**Fonctions** : test_ngram_generator, update_gui, test_ngram_generator_ngram_size, update_gui_ngram_size, test_get_ngrams_is
**Dépendances** : random, tests, wordless, wordless.wl_dialogs, wordless.wl_nlp

### `test_profiler.py`

Module Python. Nombre de lignes: 259. Elements detectés: def test_profiler, def update_gui

**Fonctions** : test_profiler, update_gui
**Dépendances** : collections, numpy, scipy, tests, wordless, wordless.wl_dialogs, wordless.wl_utils

### `test_wordlist_generator.py`

Module Python. Nombre de lignes: 118. Elements detectés: def test_wordlist_generator, def update_gui

**Fonctions** : test_wordlist_generator, update_gui
**Dépendances** : random, tests, wordless, wordless.wl_dialogs

### `wl_test_doc.py`

Module Python. Nombre de lignes: 110. Elements detectés: def wl_test_supported_langs, def wl_test_supported_encodings

**Fonctions** : wl_test_supported_langs, wl_test_supported_encodings
**Dépendances** : re, tests, utils

### `wl_test_file_area.py`

Module Python. Nombre de lignes: 139. Elements detectés: def wl_test_file_area, def open_file, def open_file_ref

**Fonctions** : wl_test_file_area, open_file, open_file_ref, update_gui, update_gui_ref
**Dépendances** : glob, os, pickle, random, re, time, PyQt5, tests, wordless, wordless.wl_dialogs, wordless.wl_utils

### `wl_test_init.py`

Module Python. Nombre de lignes: 287. Elements detectés: class Wl_Test_Main, def __init__, def height

**Classes** : Wl_Test_Main, Wl_Test_Table, Wl_Test_Text, Wl_Exc_Tests_Lang_Skipped, Wl_Exc_Tests_Lang_Util_Skipped
**Fonctions** : __init__, height, switch_lang_utils_fast, switch_lang_utils_spacy, switch_lang_utils_stanza, set_item, set_label, filter_table, wl_test_index, select_test_files, get_test_file_names, clean_import_caches
**Dépendances** : copy, glob, os, pickle, re, sys, PyQt5, tests, wordless, wordless.wl_checks, wordless.wl_nlp, wordless.wl_settings

### `wl_test_lang_examples.py`

Module Python. Nombre de lignes: 368.

**Fonctions** : check_lang_examples
**Dépendances** : tests
