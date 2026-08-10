# Module : demos/database

1 fichier(s), 8 classe(s), 8 fonction(s).

## Vue d'ensemble

- **Classes principales** : Article, Author, Citizen, City, DeleteNoteForm, EditNoteForm, NewNoteForm, Note
- **Fonctions principales** : __repr__, delete_note, edit_note, increment_edit_time, index, initdb, make_shell_context, new_note
- **Dépendances** : click, flask, flask_sqlalchemy, flask_wtf, os, sys, wtforms, wtforms.validators
- **Endpoints API** : /, /delete/<int:note_id>, /edit/<int:note_id>, /new

## Détail des fichiers

### `app.py`

Module Python. Nombre de lignes: 214. Elements detectés: def make_shell_context, def initdb, class NewNoteForm

**Classes** : NewNoteForm, EditNoteForm, DeleteNoteForm, Note, Author, Article, Citizen, City
**Fonctions** : make_shell_context, initdb, __repr__, index, new_note, edit_note, delete_note, increment_edit_time
**Dépendances** : os, sys, click, flask, flask_sqlalchemy, flask_wtf, wtforms, wtforms.validators
**API** : /, /new, /edit/<int:note_id>, /delete/<int:note_id>
