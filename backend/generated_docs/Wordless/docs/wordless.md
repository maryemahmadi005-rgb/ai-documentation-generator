# Module : wordless

12 fichier(s), 59 classe(s), 141 fonction(s).

## Vue d'ensemble

- **Classes principales** : Table_Open_Files, Wl_Dialog_Acks, Wl_Dialog_Check_Updates, Wl_Dialog_Citing, Wl_Dialog_Confirm_Exit, Wl_Dialog_Donating, Wl_Dialog_Need_Help, Wl_Dialog_Open_Corpora, Wl_Dialog_Opening_Nontext_Files, Wl_Loading, Wl_Main, Wl_Table_Colligation_Extractor
- **Fonctions principales** : __init__, always_confirm_on_exit_changed, closeEvent, clr_all_tables, clr_table, copy_worksheet, deselect_all, edit_results_filter, edit_results_sample, edit_results_search, exp_all_tables, fade_in, fade_out, fig_settings_changed, file_area_changed
- **Dépendances** : PyQt5, bisect, botok, bs4, collections, copy, csv, docx, glob, itertools, matplotlib, matplotlib.pyplot

## Détail des fichiers

### `wl_colligation_extractor.py`

Module Python. Nombre de lignes: 1091. Elements detectés: class Wrapper_Colligation_Extractor, def __init__

**Classes** : Wrapper_Colligation_Extractor, Wl_Table_Colligation_Extractor, Wl_Worker_Colligation_Extractor, Wl_Worker_Colligation_Extractor_Table, Wl_Worker_Colligation_Extractor_Fig
**Fonctions** : __init__, load_settings, token_settings_changed, search_settings_changed, generation_settings_changed, table_settings_changed, fig_settings_changed, generate_table, update_gui_table, generate_fig, update_gui_fig, run
**Dépendances** : bisect, collections, copy, re, traceback, numpy, PyQt5, wordless.wl_checks, wordless.wl_dialogs, wordless.wl_figs, wordless.wl_nlp, wordless.wl_utils

### `wl_collocation_extractor.py`

Module Python. Nombre de lignes: 1092. Elements detectés: class Wrapper_Collocation_Extractor, def __init__

**Classes** : Wrapper_Collocation_Extractor, Wl_Table_Collocation_Extractor, Wl_Worker_Collocation_Extractor, Wl_Worker_Collocation_Extractor_Table, Wl_Worker_Collocation_Extractor_Fig
**Fonctions** : __init__, load_settings, token_settings_changed, search_settings_changed, generation_settings_changed, table_settings_changed, fig_settings_changed, generate_table, update_gui_table, generate_fig, update_gui_fig, run
**Dépendances** : bisect, collections, copy, re, traceback, numpy, PyQt5, wordless.wl_checks, wordless.wl_dialogs, wordless.wl_figs, wordless.wl_nlp, wordless.wl_utils

### `wl_concordancer.py`

Module Python. Nombre de lignes: 914. Elements detectés: class Wrapper_Concordancer, def __init__

**Classes** : Wrapper_Concordancer, Wl_Table_Concordancer, Wl_Worker_Concordancer_Table, Wl_Worker_Concordancer_Fig
**Fonctions** : __init__, load_settings, token_settings_changed, search_settings_changed, generation_settings_changed, table_settings_changed, fig_settings_changed, zapping_settings_changed, generate_table, update_gui_table, generate_fig, update_gui_fig, run
**Dépendances** : bisect, copy, traceback, matplotlib, matplotlib.pyplot, numpy, PyQt5, wordless.wl_checks, wordless.wl_dialogs, wordless.wl_figs, wordless.wl_nlp, wordless.wl_utils

### `wl_concordancer_parallel.py`

Module Python. Nombre de lignes: 408. Elements detectés: class Wrapper_Concordancer_Parallel, def __init__

**Classes** : Wrapper_Concordancer_Parallel, Wl_Table_Concordancer_Parallel, Wl_Worker_Concordancer_Parallel_Table
**Fonctions** : __init__, load_settings, token_settings_changed, search_settings_changed, table_settings_changed, generate_table, update_gui_table, run
**Dépendances** : bisect, copy, itertools, traceback, PyQt5, wordless.wl_checks, wordless.wl_dialogs, wordless.wl_nlp, wordless.wl_utils, wordless.wl_widgets

### `wl_dependency_parser.py`

Module Python. Nombre de lignes: 549. Elements detectés: class Wrapper_Dependency_Parser, def __init__

**Classes** : Wrapper_Dependency_Parser, Wl_Table_Dependency_Parser, Wl_Worker_Dependency_Parser
**Fonctions** : __init__, load_settings, token_settings_changed, search_settings_changed, table_settings_changed, fig_settings_changed, selection_changed_generate_fig, file_changed, generate_table, update_gui_table, generate_fig, run
**Dépendances** : bisect, copy, traceback, numpy, PyQt5, wordless.wl_checks, wordless.wl_dialogs, wordless.wl_nlp, wordless.wl_utils, wordless.wl_widgets

### `wl_file_area.py`

Module Python. Nombre de lignes: 1010. Elements detectés: class Wrapper_File_Area, def __init__, def get_files

**Classes** : Wrapper_File_Area, Wl_Table_Header_Files, Wl_Table_Files, Wl_Dialog_Open_Corpora, Table_Open_Files, Wl_Dialog_Opening_Nontext_Files, Wl_Worker_Add_Files, Wl_Worker_Open_Files
**Fonctions** : __init__, get_files, get_file_names, get_selected_files, get_selected_file_names, find_file_by_name, find_files_by_name, paintSection, section_clicked, select_all, deselect_all, invert_selection, item_changed, item_clicked, selection_changed
**Dépendances** : copy, csv, os, re, traceback, bs4, docx, openpyxl, pptx, pypdf, PyQt5, wordless.wl_checks

### `wl_keyword_extractor.py`

Module Python. Nombre de lignes: 864. Elements detectés: class Wrapper_Keyword_Extractor, def __init__

**Classes** : Wrapper_Keyword_Extractor, Wl_Table_Keyword_Extractor, Wl_Worker_Keyword_Extractor, Wl_Worker_Keyword_Extractor_Table, Wl_Worker_Keyword_Extractor_Fig
**Fonctions** : __init__, load_settings, token_settings_changed, generation_settings_changed, table_settings_changed, fig_settings_changed, file_changed, wl_dialog_missing_corpus_observed, wl_dialog_missing_corpus_ref, wl_status_bar_msg_missing_corpus_observed, wl_status_bar_msg_missing_corpus_ref, generate_table, update_gui_table, generate_fig, update_gui_fig
**Dépendances** : collections, copy, traceback, numpy, PyQt5, wordless.wl_checks, wordless.wl_dialogs, wordless.wl_figs, wordless.wl_measures, wordless.wl_nlp, wordless.wl_utils, wordless.wl_widgets

### `wl_main.py`

Module Python. Nombre de lignes: 1197.

**Classes** : Wl_Loading, Wl_Dialog_Confirm_Exit, Wl_Main, Wl_Dialog_Need_Help, Wl_Dialog_Citing, Wl_Dialog_Donating, Wl_Dialog_Acks, Wl_Dialog_Check_Updates
**Fonctions** : __init__, show_message, fade_in, fade_out, load_settings, always_confirm_on_exit_changed, closeEvent, init_menu, init_central_widget, init_work_area, file_area_changed, work_area_changed, edit_results_search, edit_results_filter, edit_results_sample
**Dépendances** : multiprocessing, copy, glob, os, pickle, platform, re, subprocess, sys, time, botok, matplotlib

### `wl_ngram_generator.py`

Module Python. Nombre de lignes: 865. Elements detectés: class Wrapper_Ngram_Generator, def __init__

**Classes** : Wrapper_Ngram_Generator, Wl_Table_Ngram_Generator, Wl_Worker_Ngram_Generator, Wl_Worker_Ngram_Generator_Table, Wl_Worker_Ngram_Generator_Fig
**Fonctions** : __init__, load_settings, token_settings_changed, search_settings_changed, generation_settings_changed, table_settings_changed, fig_settings_changed, generate_table, update_gui_table, generate_fig, update_gui_fig, get_ngrams_is, run
**Dépendances** : collections, copy, traceback, numpy, PyQt5, wordless.wl_checks, wordless.wl_dialogs, wordless.wl_figs, wordless.wl_measures, wordless.wl_nlp, wordless.wl_utils, wordless.wl_widgets

### `wl_profiler.py`

Module Python. Nombre de lignes: 1519. Elements detectés: def copy_worksheet, class Wrapper_Profiler, def __init__

**Classes** : Wrapper_Profiler, Wl_Table_Profiler, Wl_Table_Profiler_Readability, Wl_Table_Profiler_Counts, Wl_Table_Profiler_Lexical_Density_Diversity, Wl_Table_Profiler_Syntactic_Complexity, Wl_Table_Profiler_Lens, Wl_Table_Profiler_Len_Breakdown
**Fonctions** : copy_worksheet, __init__, load_settings, tabs_changed, item_changed, token_settings_changed, table_settings_changed, file_changed, generate_all_tables, update_gui_table, exp_all_tables, update_gui_exp_all_tables, clr_all_tables, clr_table, generate_table
**Dépendances** : collections, copy, csv, os, re, traceback, numpy, openpyxl, PyQt5, scipy, wordless.wl_checks, wordless.wl_dialogs

### `wl_wordlist_generator.py`

Module Python. Nombre de lignes: 664. Elements detectés: class Wrapper_Wordlist_Generator, def __init__

**Classes** : Wrapper_Wordlist_Generator, Wl_Table_Wordlist_Generator, Wl_Worker_Wordlist_Generator, Wl_Worker_Wordlist_Generator_Table, Wl_Worker_Wordlist_Generator_Fig
**Fonctions** : __init__, load_settings, token_settings_changed, generation_settings_changed, table_settings_changed, fig_settings_changed, generate_table, update_gui_table, generate_fig, update_gui_fig, run
**Dépendances** : collections, copy, traceback, numpy, PyQt5, wordless.wl_checks, wordless.wl_dialogs, wordless.wl_figs, wordless.wl_measures, wordless.wl_nlp, wordless.wl_utils, wordless.wl_widgets
