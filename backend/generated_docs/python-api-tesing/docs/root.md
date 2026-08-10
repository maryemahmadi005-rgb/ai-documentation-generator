# Module : Racine du projet

20 fichier(s), 1 classe(s), 51 fonction(s).

## Vue d'ensemble

- **Classes principales** : Pinger
- **Fonctions principales** : __init__, bj_sz_photo_compare, build_verify_input, check_directory, check_process, compute_roc_part, concat_excel, copy_files_by_types, count, count_number_by_filetype, count_number_by_filetypes, do_checksum, file2dict, file2dict1, file2html
- **Dépendances** : PIL, argparse, bisect, collections, cv2, data_common, email.mime.application, email.mime.multipart, email.mime.text, glob, hashlib, multiprocessing

## Détail des fichiers

### `README.md`

### `addesss.md`

### `articles.md`

### `books.md`

### `bug_count.py`

Module Python. Nombre de lignes: 26.

**Dépendances** : pathlib, glob, os, pyexcel, pandas

### `count.py`

Module Python. Nombre de lignes: 156. Elements detectés: def compute_roc_part, def roc, def verify_roc

**Fonctions** : compute_roc_part, roc, verify_roc
**Dépendances** : multiprocessing, os, sys, bisect, numpy, sklearn.metrics, data_common

### `count_unqualified_photo_num.py`

Module Python. Nombre de lignes: 33.

**Dépendances** : pandas, pyexcel

### `data_common.py`

Module Python. Nombre de lignes: 575. Elements detectés: def count, def file2html

**Fonctions** : count, file2html, percentage, produce_xls, check_directory, get_labels, get_filelistandlabel, find_files_by_type, copy_files_by_types, count_number_by_filetypes, count_number_by_filetype, concat_excel, file2dict, file2dict1, get_md5
**Dépendances** : os, shutil, traceback, time, pathlib, glob, hashlib, re, collections, pandas

### `datas.py`

Module Python. Nombre de lignes: 48. Elements detectés: def get_verify_server_result

**Fonctions** : get_verify_server_result
**Dépendances** : time, os, pandas

### `excel_summary_demo.py`

Module Python. Nombre de lignes: 28.

**Dépendances** : pandas, data_common

### `far_frr.py`

Module Python. Nombre de lignes: 41.

**Dépendances** : glob, os, pandas, pyexcel, data_common

### `merge_testcase_reports.py`

Module Python. Nombre de lignes: 38. Elements detectés: def sum_report

**Fonctions** : sum_report
**Dépendances** : traceback, re, shutil, os, glob, pandas, data_common

### `others.py`

Module Python. Nombre de lignes: 43. Elements detectés: def send_mail

**Fonctions** : send_mail
**Dépendances** : os, email.mime.text, email.mime.multipart, email.mime.application, smtplib

### `parse_test_cases_data.py`

Module Python. Nombre de lignes: 70. Elements detectés: def get_result, def get_results

**Fonctions** : get_result, get_results
**Dépendances** : traceback, re, shutil, os, pandas, data_common

### `photos.py`

Module Python. Nombre de lignes: 122. Elements detectés: def mark_image, def mark_images, def bj_sz_photo_compare

**Fonctions** : mark_image, mark_images, bj_sz_photo_compare, rotateImage, rotate, rotate2, find_face, raw2jpg, split_raw
**Dépendances** : os, traceback, cv2, numpy, PIL

### `ping.py`

Module Python. Nombre de lignes: 141. Elements detectés: class Pinger, def __init__, def do_checksum

**Classes** : Pinger
**Fonctions** : __init__, do_checksum, receive_pong, send_ping, ping_once, ping
**Dépendances** : os, argparse, socket, struct, select, time

### `servers.py`

Module Python. Nombre de lignes: 300. Elements detectés: def get_live_frr_far, def get_gaze_frr_far, def load_verify_server_result

**Fonctions** : get_live_frr_far, get_gaze_frr_far, load_verify_server_result, get_verify_errors, get_verify_frr_far, get_verify_server_result, check_process, wait_until_stop, get_liveness_server_result, rename, get_gaze_server_result, get_eye_server_result, build_verify_input
**Dépendances** : time, os, subprocess, pathlib, pandas, numpy

### `society_books.md`

### `tips.md`

### `videos.md`
