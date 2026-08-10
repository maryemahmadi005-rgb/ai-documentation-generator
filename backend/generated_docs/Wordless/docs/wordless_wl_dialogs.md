# Module : wordless/wl_dialogs

4 fichier(s), 16 classe(s), 17 fonction(s).

## Vue d'ensemble

- **Classes principales** : Wl_Dialog, Wl_Dialog_Err, Wl_Dialog_Err_Download_Model, Wl_Dialog_Err_Fatal, Wl_Dialog_Err_Files, Wl_Dialog_Err_Info_Copy, Wl_Dialog_Frameless, Wl_Dialog_Info, Wl_Dialog_Info_Copy, Wl_Dialog_Info_Simple, Wl_Dialog_Progress, Wl_Dialog_Progress_Download_Model
- **Fonctions principales** : __init__, abort_clicked, adjust_size, copy, exec, get_info, get_msg_box_icon, load, load_settings, move_to_center, open, save_settings, set_info, update_elapsed_time, update_progress
- **Dépendances** : PyQt5, datetime, time, wordless.wl_dialogs, wordless.wl_utils, wordless.wl_widgets

## Détail des fichiers

### `wl_dialogs.py`

Module Python. Nombre de lignes: 272. Elements detectés: def get_msg_box_icon, class Wl_Dialog, def __init__

**Classes** : Wl_Dialog, Wl_Dialog_Frameless, Wl_Dialog_Info, Wl_Dialog_Info_Simple, Wl_Dialog_Info_Copy, Wl_Dialog_Question, Wl_Dialog_Settings
**Fonctions** : get_msg_box_icon, __init__, adjust_size, move_to_center, exec, open, copy, get_info, set_info, load_settings, save_settings, load
**Dépendances** : PyQt5, wordless.wl_utils, wordless.wl_widgets

### `wl_dialogs_errs.py`

Module Python. Nombre de lignes: 88. Elements detectés: class Wl_Dialog_Err, def __init__, class Wl_Dialog_Err_Files

**Classes** : Wl_Dialog_Err, Wl_Dialog_Err_Files, Wl_Dialog_Err_Info_Copy, Wl_Dialog_Err_Fatal, Wl_Dialog_Err_Download_Model
**Fonctions** : __init__
**Dépendances** : PyQt5, wordless.wl_dialogs, wordless.wl_utils, wordless.wl_widgets

### `wl_dialogs_misc.py`

Module Python. Nombre de lignes: 94. Elements detectés: class Wl_Dialog_Progress, def __init__, def abort_clicked

**Classes** : Wl_Dialog_Progress, Wl_Dialog_Progress_Process_Data, Wl_Dialog_Progress_Download_Model, Wl_Dialog_Restart_Required
**Fonctions** : __init__, abort_clicked, update_elapsed_time, update_progress
**Dépendances** : datetime, time, PyQt5, wordless.wl_dialogs, wordless.wl_widgets
