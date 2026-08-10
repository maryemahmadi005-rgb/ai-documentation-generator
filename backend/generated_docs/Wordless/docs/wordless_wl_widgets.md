# Module : wordless/wl_widgets

10 fichier(s), 46 classe(s), 92 fonction(s).

## Vue d'ensemble

- **Classes principales** : Wl_Button, Wl_Button_Browse, Wl_Button_Color, Wl_Button_Restore_Default_Vals, Wl_Combo_Box, Wl_Combo_Box_Adjustable, Wl_Combo_Box_Encoding, Wl_Combo_Box_Enums, Wl_Combo_Box_File_Fig_Settings, Wl_Combo_Box_File_To_Filter, Wl_Combo_Box_Lang, Wl_Combo_Box_Measure
- **Fonctions principales** : __init__, _add_item, _add_items, addWidget, add_item, assign_pos_tags_changed, browse, clr_list, createEditor, current_changed, data_changed, del_item, dialog_path_confirm, dialog_path_empty, dialog_path_not_dir
- **Dépendances** : PyQt5, bs4, copy, csv, docx, math, openpyxl, os, random, re, traceback, wordless.wl_checks

## Détail des fichiers

### `wl_boxes.py`

Module Python. Nombre de lignes: 357. Elements detectés: class Wl_Combo_Box, def __init__, def wheelEvent

**Classes** : Wl_Combo_Box, Wl_Combo_Box_Adjustable, Wl_Combo_Box_Enums, Wl_Combo_Box_Yes_No, Wl_Combo_Box_Lang, Wl_Combo_Box_Encoding, Wl_Combo_Box_Measure, Wl_Combo_Box_File_To_Filter
**Fonctions** : __init__, wheelEvent, get_val, set_val, get_yes_no, set_yes_no, get_measure, set_measure, table_item_changed, wl_files_changed, get_file, stepBy, value_changed, wl_spin_box_no_limit, no_limit_changed
**Dépendances** : PyQt5, wordless.wl_measures, wordless.wl_utils

### `wl_buttons.py`

Module Python. Nombre de lignes: 97. Elements detectés: class Wl_Button, def __init__, class Wl_Button_Browse

**Classes** : Wl_Button, Wl_Button_Browse, Wl_Button_Color, Wl_Button_Restore_Default_Vals
**Fonctions** : __init__, browse, paintEvent, pick_color, get_color, set_color, wl_button_color_transparent, transparent_changed, restore_default_vals
**Dépendances** : os, PyQt5, wordless.wl_checks, wordless.wl_dialogs, wordless.wl_utils

### `wl_editors.py`

Module Python. Nombre de lignes: 246. Elements detectés: class Wl_Line_Edit_Nonempty, def __init__, def setText

**Classes** : Wl_Line_Edit_Nonempty, Wl_Line_Edit_Re, Wl_Line_Edit_Path, Wl_Line_Edit_Path_File, Wl_Line_Edit_Path_Dir, Wl_Line_Edit_Path_Dir_Confirm, Wl_Text_Browser
**Fonctions** : __init__, setText, text_changed, start_editing, dialog_path_empty, dialog_path_not_found, dialog_path_not_file, validate, dialog_path_not_dir, dialog_path_confirm
**Dépendances** : os, re, PyQt5, wordless.wl_checks, wordless.wl_dialogs, wordless.wl_utils

### `wl_item_delegates.py`

Module Python. Nombre de lignes: 97. Elements detectés: class Wl_Item_Delegate_Uneditable, def createEditor, class Wl_Item_Delegate

**Classes** : Wl_Item_Delegate_Uneditable, Wl_Item_Delegate, Wl_Item_Delegate_Combo_Box, Wl_Item_Delegate_Combo_Box_Custom
**Fonctions** : createEditor, __init__, set_enabled, paint, is_editable
**Dépendances** : math, PyQt5, wordless.wl_utils, wordless.wl_widgets

### `wl_labels.py`

Module Python. Nombre de lignes: 67. Elements detectés: class Wl_Label, def __init__, class Wl_Label_Hint

**Classes** : Wl_Label, Wl_Label_Hint, Wl_Label_Html, Wl_Label_Html_Centered, Wl_Label_Dialog, Wl_Label_Dialog_No_Wrap
**Fonctions** : __init__, set_text
**Dépendances** : PyQt5, wordless.wl_utils

### `wl_layouts.py`

Module Python. Nombre de lignes: 127. Elements detectés: class Wl_Layout, def __init__, class Wl_Wrapper

**Classes** : Wl_Layout, Wl_Wrapper, Wl_Tab_Widget, Wl_Splitter, Wl_Scroll_Area, Wl_Stacked_Widget_Resizable, Wl_Separator
**Fonctions** : __init__, paintEvent, load_settings, eventFilter, current_changed, addWidget
**Dépendances** : PyQt5, wordless.wl_utils, wordless.wl_widgets

### `wl_lists.py`

Module Python. Nombre de lignes: 333. Elements detectés: class Wl_List_Add_Ins_Del_Clr, def __init__, def dropEvent

**Classes** : Wl_List_Add_Ins_Del_Clr, Wl_List_Add_Ins_Del_Clr_Imp_Exp
**Fonctions** : __init__, dropEvent, keyPressEvent, data_changed, selection_changed, get_selected_rows, _add_item, _add_items, add_item, ins_item, del_item, clr_list, load_items, imp_list, exp_list
**Dépendances** : os, PyQt5, wordless.wl_checks, wordless.wl_dialogs, wordless.wl_utils

### `wl_tables.py`

Module Python. Nombre de lignes: 1528. Elements detectés: class Wl_Table, def __init__

**Classes** : Wl_Table, Wl_Worker_Exp_Table, Wl_Table_Add_Ins_Del_Clr, Wl_Table_Item, Wl_Table_Item_Err, Wl_Table_Data
**Fonctions** : __init__, dropEvent, item_changed, selection_changed, disable_updates, enable_updates, is_empty, is_visible, is_selected, get_header_labels_hor, get_header_labels_vert, find_header_hor, find_header_vert, find_headers_hor, find_headers_vert
**Dépendances** : csv, os, random, re, traceback, bs4, docx, openpyxl, PyQt5, wordless.wl_checks, wordless.wl_dialogs, wordless.wl_nlp

### `wl_widgets.py`

Module Python. Nombre de lignes: 797. Elements detectés: class Wl_Dialog_Context_Settings, def __init__

**Classes** : Wl_Dialog_Context_Settings, Wl_Combo_Box_File_Fig_Settings
**Fonctions** : __init__, multi_search_mode_changed, token_settings_changed, load_settings, save_settings, wl_widgets_token_settings, words_changed, assign_pos_tags_changed, ignore_tags_changed, use_tags_changed, wl_widgets_token_settings_concordancer, wl_widgets_search_settings, match_without_tags_changed, match_tags_changed, wl_widgets_search_settings_tokens
**Dépendances** : copy, PyQt5, wordless.wl_dialogs, wordless.wl_measures, wordless.wl_utils, wordless.wl_widgets
