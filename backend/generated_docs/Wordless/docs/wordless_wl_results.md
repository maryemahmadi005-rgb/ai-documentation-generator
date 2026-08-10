# Module : wordless/wl_results

5 fichier(s), 13 classe(s), 42 fonction(s).

## Vue d'ensemble

- **Classes principales** : Wl_Dialog_Results_Filter, Wl_Dialog_Results_Filter_Collocation_Extractor, Wl_Dialog_Results_Filter_Dependency_Parser, Wl_Dialog_Results_Filter_Wordlist_Generator, Wl_Dialog_Results_Sample, Wl_Dialog_Results_Search, Wl_Dialog_Results_Sort_Concordancer, Wl_Table_Results_Sort_Conordancer, Wl_Worker_Results_Filter_Collocation_Extractor, Wl_Worker_Results_Filter_Dependency_Parser, Wl_Worker_Results_Filter_Wordlist_Generator, Wl_Worker_Results_Search
- **Fonctions principales** : __init__, _add_row, add_layouts_filters, clr_highlights, clr_history, file_to_filter_changed, filter, filter_changed, filters_changed, find_all, find_next, find_prev, get_filter_min_max, item_changed, load_settings
- **Dépendances** : PyQt5, copy, math, numpy, re, traceback, wordless.wl_checks, wordless.wl_dialogs, wordless.wl_nlp, wordless.wl_utils, wordless.wl_widgets

## Détail des fichiers

### `wl_results_filter.py`

Module Python. Nombre de lignes: 763. Elements detectés: def widgets_filter, def load_settings, def filter_changed

**Classes** : Wl_Dialog_Results_Filter, Wl_Dialog_Results_Filter_Dependency_Parser, Wl_Worker_Results_Filter_Dependency_Parser, Wl_Dialog_Results_Filter_Wordlist_Generator, Wl_Worker_Results_Filter_Wordlist_Generator, Wl_Dialog_Results_Filter_Collocation_Extractor, Wl_Worker_Results_Filter_Collocation_Extractor
**Fonctions** : widgets_filter, load_settings, filter_changed, widgets_filter_measures, precision_changed, widgets_filter_p_val, add_layouts_filters, get_filter_min_max, __init__, file_to_filter_changed, filter, update_gui, show, run, filters_changed
**Dépendances** : copy, math, traceback, PyQt5, wordless.wl_checks, wordless.wl_dialogs, wordless.wl_utils, wordless.wl_widgets

### `wl_results_sample.py`

Module Python. Nombre de lignes: 137. Elements detectés: class Wl_Dialog_Results_Sample, def __init__, def load_settings

**Classes** : Wl_Dialog_Results_Sample
**Fonctions** : __init__, load_settings, settings_changed, sample
**Dépendances** : copy, numpy, PyQt5, wordless.wl_dialogs, wordless.wl_widgets

### `wl_results_search.py`

Module Python. Nombre de lignes: 392. Elements detectés: class Wl_Dialog_Results_Search, def __init__

**Classes** : Wl_Dialog_Results_Search, Wl_Worker_Results_Search
**Fonctions** : __init__, load_settings, settings_changed, multi_search_mode_changed, table_item_changed, find_next, find_prev, find_all, update_gui, clr_highlights, clr_history, run
**Dépendances** : copy, traceback, PyQt5, wordless.wl_checks, wordless.wl_dialogs, wordless.wl_nlp, wordless.wl_utils, wordless.wl_widgets

### `wl_results_sort.py`

Module Python. Nombre de lignes: 470. Elements detectés: class Wl_Dialog_Results_Sort_Concordancer, def __init__, def load_settings

**Classes** : Wl_Dialog_Results_Sort_Concordancer, Wl_Table_Results_Sort_Conordancer, Wl_Worker_Results_Sort_Concordancer
**Fonctions** : __init__, load_settings, sort, update_gui, item_changed, selection_changed, table_item_changed, max_left, max_right, _add_row, run
**Dépendances** : copy, re, traceback, PyQt5, wordless.wl_checks, wordless.wl_dialogs, wordless.wl_utils, wordless.wl_widgets
