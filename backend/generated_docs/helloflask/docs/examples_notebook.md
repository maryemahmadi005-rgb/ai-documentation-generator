# Module : examples/notebook

2 fichier(s), 5 classe(s), 20 fonction(s).

## Vue d'ensemble

- **Classes principales** : Base, DeleteNoteForm, Note, NoteForm, NotebookTestCase
- **Fonctions principales** : __repr__, delete_note, edit_note, index, init_command, lorem_command, new_note, setUp, tearDown, test_app_exist, test_app_is_testing, test_create_note, test_delete_note, test_form_validation, test_index_page
- **Dépendances** : app, click, datetime, flask, flask_sqlalchemy, flask_wtf, os, pathlib, sqlalchemy, sqlalchemy.orm, sys, typing
- **Endpoints API** : /, /delete/<int:note_id>, /edit/<int:note_id>, /new

## Détail des fichiers

### `app.py`

Module Python. Nombre de lignes: 119. Elements detectés: class Base, class Note, def __repr__

**Classes** : Base, Note, NoteForm, DeleteNoteForm
**Fonctions** : __repr__, init_command, lorem_command, index, new_note, edit_note, delete_note
**Dépendances** : os, sys, datetime, pathlib, typing, click, flask, flask_sqlalchemy, sqlalchemy, sqlalchemy.orm, flask_wtf, wtforms
**API** : /, /new, /edit/<int:note_id>, /delete/<int:note_id>

### `test_app.py`

Module Python. Nombre de lignes: 93. Elements detectés: class NotebookTestCase, def setUp, def tearDown

**Classes** : NotebookTestCase
**Fonctions** : setUp, tearDown, test_app_exist, test_app_is_testing, test_index_page, test_create_note, test_update_note, test_delete_note, test_form_validation, test_lorem_command, test_lorem_command_with_count, test_init_command, test_init_command_with_drop
**Dépendances** : unittest, os, sqlalchemy, app
