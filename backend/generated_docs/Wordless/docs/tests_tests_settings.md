# Module : tests/tests_settings

17 fichier(s), 66 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : add_lang_suffixes, check_invalid_default_lang_utils, check_lang_order, check_missing_extra_langs, check_missing_extra_langs_default, test_dialog_preview_imp, test_settings_default, test_settings_global, test_wl_combo_box_base_log, test_wl_dialog_preview_settings, test_wl_list_stop_words, test_wl_settings, test_wl_settings_dependency_parsing, test_wl_settings_figs_line_charts, test_wl_settings_figs_network_graphs
- **Dépendances** : math, nltk, os, pkgutil, pyphen, re, requests, sacremoses, simplemma, spacy, spacy_lookups_data, tests

## Détail des fichiers

### `test_settings.py`

Module Python. Nombre de lignes: 36. Elements detectés: def test_wl_settings, def test_wl_settings_node

**Fonctions** : test_wl_settings, test_wl_settings_node
**Dépendances** : tests, wordless.wl_settings

### `test_settings_default.py`

Module Python. Nombre de lignes: 28. Elements detectés: def test_settings_default

**Fonctions** : test_settings_default
**Dépendances** : tests, wordless.wl_settings

### `test_settings_dependency_parsing.py`

Module Python. Nombre de lignes: 61. Elements detectés: def test_wl_settings_dependency_parsing, def test_wl_dialog_preview_settings, def test_wl_worker_preview_dependency_parser

**Fonctions** : test_wl_settings_dependency_parsing, test_wl_dialog_preview_settings, test_wl_worker_preview_dependency_parser
**Dépendances** : tests, wordless.wl_nlp, wordless.wl_settings

### `test_settings_figs.py`

Module Python. Nombre de lignes: 58. Elements detectés: def test_wl_settings_figs_line_charts, def test_wl_settings_figs_word_clouds, def test_wl_settings_figs_network_graphs

**Fonctions** : test_wl_settings_figs_line_charts, test_wl_settings_figs_word_clouds, test_wl_settings_figs_network_graphs
**Dépendances** : tests, wordless.wl_settings

### `test_settings_files.py`

Module Python. Nombre de lignes: 64. Elements detectés: def test_wl_settings_files, def test_wl_settings_files_tags, def test_wl_table_tags

**Fonctions** : test_wl_settings_files, test_wl_settings_files_tags, test_wl_table_tags, test_wl_table_tags_header, test_wl_table_tags_body, test_wl_table_tags_xml
**Dépendances** : tests, wordless.wl_settings

### `test_settings_general.py`

Module Python. Nombre de lignes: 58. Elements detectés: def test_wl_settings_general, def test_wl_settings_general_imp, def test_wl_settings_general_exp

**Fonctions** : test_wl_settings_general, test_wl_settings_general_imp, test_wl_settings_general_exp
**Dépendances** : os, tests, wordless.wl_settings

### `test_settings_global.py`

Module Python. Nombre de lignes: 505. Elements detectés: def add_lang_suffixes, def check_missing_extra_langs, def check_missing_extra_langs_default

**Fonctions** : add_lang_suffixes, check_missing_extra_langs, check_missing_extra_langs_default, check_invalid_default_lang_utils, check_lang_order, test_settings_global
**Dépendances** : os, pkgutil, re, nltk, pyphen, requests, sacremoses, simplemma, spacy, spacy_lookups_data, tests, wordless.wl_nlp

### `test_settings_lemmatization.py`

Module Python. Nombre de lignes: 59. Elements detectés: def test_wl_settings_lemmatization, def test_wl_worker_preview_lemmatizer, def update_gui_newlines

**Fonctions** : test_wl_settings_lemmatization, test_wl_worker_preview_lemmatizer, update_gui_newlines
**Dépendances** : tests, wordless.wl_nlp, wordless.wl_settings

### `test_settings_measures.py`

Module Python. Nombre de lignes: 77. Elements detectés: def test_wl_settings_measures_readability, def test_wl_settings_measures_lexical_density_diversity, def test_wl_settings_measures_dispersion

**Fonctions** : test_wl_settings_measures_readability, test_wl_settings_measures_lexical_density_diversity, test_wl_settings_measures_dispersion, test_wl_settings_measures_adjusted_freq, test_wl_settings_measures_statistical_significance, test_wl_settings_measures_bayes_factor, test_wl_combo_box_base_log, test_wl_settings_measures_effect_size
**Dépendances** : math, tests, wordless.wl_settings

### `test_settings_pos_tagging.py`

Module Python. Nombre de lignes: 116. Elements detectés: def test_wl_settings_pos_tagging, def test_wl_worker_preview_pos_tagger, def update_gui_newlines

**Fonctions** : test_wl_settings_pos_tagging, test_wl_worker_preview_pos_tagger, update_gui_newlines, test_wl_settings_pos_tagging_tagsets, test_wl_settings_pos_tagging_tagsets_universal_tagsets, test_wl_worker_fetch_data_tagsets
**Dépendances** : tests, wordless.wl_dialogs, wordless.wl_nlp, wordless.wl_settings, wordless.wl_widgets

### `test_settings_sentence_tokenization.py`

Module Python. Nombre de lignes: 59. Elements detectés: def test_wl_settings_sentence_tokenization, def test_wl_worker_preview_sentence_tokenizer, def update_gui_newlines

**Fonctions** : test_wl_settings_sentence_tokenization, test_wl_worker_preview_sentence_tokenizer, update_gui_newlines
**Dépendances** : tests, wordless.wl_nlp, wordless.wl_settings

### `test_settings_sentiment_analysis.py`

Module Python. Nombre de lignes: 60. Elements detectés: def test_wl_settings_sentiment_analysis, def test_wl_worker_preview_sentiment_analyzer, def update_gui_newlines

**Fonctions** : test_wl_settings_sentiment_analysis, test_wl_worker_preview_sentiment_analyzer, update_gui_newlines
**Dépendances** : tests, wordless.wl_nlp, wordless.wl_settings

### `test_settings_stop_word_lists.py`

Module Python. Nombre de lignes: 53. Elements detectés: def test_dialog_preview_imp, def test_wl_list_stop_words, def test_wl_settings_stop_word_lists

**Fonctions** : test_dialog_preview_imp, test_wl_list_stop_words, test_wl_settings_stop_word_lists
**Dépendances** : tests, wordless.wl_settings

### `test_settings_syl_tokenization.py`

Module Python. Nombre de lignes: 50. Elements detectés: def test_wl_settings_syl_tokenization, def test_wl_worker_preview_syl_tokenizer, def update_gui_newlines

**Fonctions** : test_wl_settings_syl_tokenization, test_wl_worker_preview_syl_tokenizer, update_gui_newlines
**Dépendances** : tests, wordless.wl_settings

### `test_settings_tables.py`

Module Python. Nombre de lignes: 81. Elements detectés: def test_wl_settings_tables, def test_wl_settings_tables_profiler, def test_wl_settings_tables_concordancer

**Fonctions** : test_wl_settings_tables, test_wl_settings_tables_profiler, test_wl_settings_tables_concordancer, test_wl_settings_tables_parallel_concordancer, test_wl_settings_tables_dependency_parser, test_wl_settings_tables_wordlist_generator, test_wl_settings_tables_ngram_generator, test_wl_settings_tables_collocation_extractor, test_wl_settings_tables_colligation_extractor, test_wl_settings_tables_keyword_extractor
**Dépendances** : tests, wordless.wl_settings

### `test_settings_word_tokenization.py`

Module Python. Nombre de lignes: 65. Elements detectés: def test_wl_settings_word_tokenization, def test_wl_worker_preview_word_tokenizer, def update_gui_newlines

**Fonctions** : test_wl_settings_word_tokenization, test_wl_worker_preview_word_tokenizer, update_gui_newlines
**Dépendances** : tests, wordless.wl_nlp, wordless.wl_settings
