# Module : wordless/wl_settings

17 fichier(s), 50 classe(s), 125 fonction(s).

## Vue d'ensemble

- **Classes principales** : Dialog_Preview_Imp, Wl_Combo_Box_Base_Log, Wl_Dialog_Preview_Settings, Wl_List_Stop_Words, Wl_Settings, Wl_Settings_Dependency_Parsing, Wl_Settings_Figs_Line_Charts, Wl_Settings_Figs_Network_Graphs, Wl_Settings_Figs_Word_Clouds, Wl_Settings_Files, Wl_Settings_Files_Tags, Wl_Settings_General
- **Fonctions principales** : __init__, _add_row, abort, apply_settings, browse_files, browse_search_terms, browse_stop_words, browse_tables, browse_temp_files, change_fonts, check_empty_duplicate_tags, check_invalid_tags, check_invalid_tags_xml, check_path, data_changed_default
- **Dépendances** : PyQt5, copy, math, matplotlib, matplotlib.backends.backend_qtagg, matplotlib.pyplot, networkx, os, re, traceback, wordless.wl_checks, wordless.wl_dialogs

## Détail des fichiers

### `wl_settings.py`

Module Python. Nombre de lignes: 288. Elements detectés: class Wl_Settings, def __init__

**Classes** : Wl_Settings, Wl_Settings_Node
**Fonctions** : __init__, selection_changed, load_settings, validate_settings, reset_all_settings, save_settings, apply_settings, load
**Dépendances** : traceback, PyQt5, wordless.wl_checks, wordless.wl_dialogs, wordless.wl_widgets, wordless.wl_settings

### `wl_settings_default.py`

Module Python. Nombre de lignes: 2366. Elements detectés: def init_settings_default

**Fonctions** : init_settings_default
**Dépendances** : copy, math, networkx, PyQt5, wordless.wl_nlp, wordless.wl_tagsets, wordless.wl_utils

### `wl_settings_dependency_parsing.py`

Module Python. Nombre de lignes: 251. Elements detectés: class Wl_Settings_Dependency_Parsing, def __init__

**Classes** : Wl_Settings_Dependency_Parsing, Wl_Dialog_Preview_Settings, Wl_Worker_Preview_Dependency_Parser
**Fonctions** : __init__, preview_changed, preview_results_changed, update_gui, update_gui_err, load_settings, apply_settings, save_settings, run
**Dépendances** : copy, PyQt5, wordless.wl_dialogs, wordless.wl_nlp, wordless.wl_settings, wordless.wl_utils, wordless.wl_widgets

### `wl_settings_figs.py`

Module Python. Nombre de lignes: 615.

**Classes** : Wl_Settings_Figs_Line_Charts, Wl_Settings_Figs_Word_Clouds, Wl_Settings_Figs_Network_Graphs
**Fonctions** : __init__, change_fonts, load_settings, apply_settings, font_settings_changed, validate_settings, settings_changed
**Dépendances** : copy, os, matplotlib, matplotlib.backends.backend_qtagg, matplotlib.pyplot, networkx, PyQt5, wordless.wl_settings, wordless.wl_utils, wordless.wl_widgets

### `wl_settings_files.py`

Module Python. Nombre de lignes: 482. Elements detectés: class Wl_Settings_Files, def __init__

**Classes** : Wl_Settings_Files, Wl_Settings_Files_Tags, Wl_Table_Tags, Wl_Table_Tags_Header, Wl_Table_Tags_Body, Wl_Table_Tags_Xml
**Fonctions** : __init__, load_settings, apply_settings, check_empty_duplicate_tags, check_invalid_tags, check_invalid_tags_xml, update_tags, _add_row, reset_table, get_tags, item_changed
**Dépendances** : copy, re, PyQt5, wordless.wl_checks, wordless.wl_dialogs, wordless.wl_nlp, wordless.wl_settings, wordless.wl_utils, wordless.wl_widgets

### `wl_settings_general.py`

Module Python. Nombre de lignes: 459. Elements detectés: class Wl_Settings_General, def __init__, def proxy_settings_changed

**Classes** : Wl_Settings_General, Wl_Settings_General_Imp, Wl_Settings_General_Exp
**Fonctions** : __init__, proxy_settings_changed, load_settings, apply_settings, browse_files, browse_search_terms, browse_stop_words, browse_temp_files, detect_encodings_changed, check_path, validate_settings, tables_default_type_changed, browse_tables
**Dépendances** : copy, os, PyQt5, wordless.wl_dialogs, wordless.wl_settings, wordless.wl_utils, wordless.wl_widgets

### `wl_settings_global.py`

Module Python. Nombre de lignes: 3669. Elements detectés: def init_settings_global

**Fonctions** : init_settings_global
**Dépendances** : PyQt5, wordless.wl_measures

### `wl_settings_lemmatization.py`

Module Python. Nombre de lignes: 193. Elements detectés: class Wl_Settings_Lemmatization, def __init__, def preview_changed

**Classes** : Wl_Settings_Lemmatization, Wl_Worker_Preview_Lemmatizer
**Fonctions** : __init__, preview_changed, preview_results_changed, update_gui, update_gui_err, load_settings, apply_settings, run
**Dépendances** : copy, PyQt5, wordless.wl_nlp, wordless.wl_settings, wordless.wl_utils, wordless.wl_widgets

### `wl_settings_measures.py`

Module Python. Nombre de lignes: 814. Elements detectés: class Wl_Settings_Measures_Readability, def __init__

**Classes** : Wl_Settings_Measures_Readability, Wl_Settings_Measures_Lexical_Density_Diversity, Wl_Settings_Measures_Dispersion, Wl_Settings_Measures_Adjusted_Freq, Wl_Settings_Measures_Statistical_Significance, Wl_Settings_Measures_Bayes_Factor, Wl_Combo_Box_Base_Log, Wl_Settings_Measures_Effect_Size
**Fonctions** : __init__, re_changed, load_settings, apply_settings, get_base_log, set_base_log
**Dépendances** : copy, math, PyQt5, wordless.wl_settings, wordless.wl_widgets

### `wl_settings_pos_tagging.py`

Module Python. Nombre de lignes: 477. Elements detectés: class Wl_Settings_Pos_Tagging, def __init__

**Classes** : Wl_Settings_Pos_Tagging, Wl_Worker_Preview_Pos_Tagger, Wl_Settings_Pos_Tagging_Tagsets, Wl_Worker_Fetch_Data_Tagsets
**Fonctions** : __init__, preview_changed, preview_results_changed, update_gui, update_gui_err, load_settings, apply_settings, run, preview_lang_changed, preview_pos_tagger_changed, reset_currently_shown_table, reset_mappings, reset_all_mappings
**Dépendances** : copy, re, PyQt5, wordless.wl_dialogs, wordless.wl_nlp, wordless.wl_settings, wordless.wl_utils, wordless.wl_widgets

### `wl_settings_sentence_tokenization.py`

Module Python. Nombre de lignes: 190. Elements detectés: class Wl_Settings_Sentence_Tokenization, def __init__, def preview_changed

**Classes** : Wl_Settings_Sentence_Tokenization, Wl_Worker_Preview_Sentence_Tokenizer
**Fonctions** : __init__, preview_changed, preview_results_changed, update_gui, update_gui_err, load_settings, apply_settings, run
**Dépendances** : copy, PyQt5, wordless.wl_nlp, wordless.wl_settings, wordless.wl_utils, wordless.wl_widgets

### `wl_settings_sentiment_analysis.py`

Module Python. Nombre de lignes: 197. Elements detectés: class Wl_Settings_Sentiment_Analysis, def __init__, def preview_changed

**Classes** : Wl_Settings_Sentiment_Analysis, Wl_Worker_Preview_Sentiment_Analyzer
**Fonctions** : __init__, preview_changed, preview_results_changed, update_gui, update_gui_err, load_settings, apply_settings, run
**Dépendances** : copy, PyQt5, wordless.wl_nlp, wordless.wl_settings, wordless.wl_utils, wordless.wl_widgets

### `wl_settings_stop_word_lists.py`

Module Python. Nombre de lignes: 257. Elements detectés: class Dialog_Preview_Imp, def __init__, def load_settings

**Classes** : Dialog_Preview_Imp, Wl_List_Stop_Words, Wl_Settings_Stop_Word_Lists
**Fonctions** : __init__, load_settings, save_settings, data_changed_default, selection_changed_default, switch_to_custom, switch_to_default, imp_list, stop_word_list_changed, preview_settings_changed, preview_results_changed, apply_settings
**Dépendances** : copy, PyQt5, wordless.wl_dialogs, wordless.wl_nlp, wordless.wl_settings, wordless.wl_utils, wordless.wl_widgets

### `wl_settings_syl_tokenization.py`

Module Python. Nombre de lignes: 188. Elements detectés: class Wl_Settings_Syl_Tokenization, def __init__, def preview_changed

**Classes** : Wl_Settings_Syl_Tokenization, Wl_Worker_Preview_Syl_Tokenizer
**Fonctions** : __init__, preview_changed, preview_results_changed, update_gui, update_gui_err, load_settings, apply_settings, run
**Dépendances** : copy, PyQt5, wordless.wl_nlp, wordless.wl_settings, wordless.wl_utils, wordless.wl_widgets

### `wl_settings_tables.py`

Module Python. Nombre de lignes: 351. Elements detectés: class Wl_Settings_Tables, def __init__, def load_settings

**Classes** : Wl_Settings_Tables, Wl_Settings_Tables_Profiler, Wl_Settings_Tables_Concordancer, Wl_Settings_Tables_Parallel_Concordancer, Wl_Settings_Tables_Dependency_Parser, Wl_Settings_Tables_Wordlist_Generator, Wl_Settings_Tables_Ngram_Generator, Wl_Settings_Tables_Collocation_Extractor
**Fonctions** : __init__, load_settings, apply_settings
**Dépendances** : copy, PyQt5, wordless.wl_settings, wordless.wl_widgets

### `wl_settings_word_tokenization.py`

Module Python. Nombre de lignes: 222. Elements detectés: class Wl_Settings_Word_Tokenization, def __init__

**Classes** : Wl_Settings_Word_Tokenization, Wl_Worker_Preview_Word_Tokenizer
**Fonctions** : __init__, preview_changed, preview_results_changed, abort, update_gui, update_gui_err, load_settings, apply_settings, run
**Dépendances** : copy, re, PyQt5, wordless.wl_nlp, wordless.wl_settings, wordless.wl_utils, wordless.wl_widgets
