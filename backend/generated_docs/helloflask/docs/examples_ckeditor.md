# Module : examples/ckeditor

1 fichier(s), 1 classe(s), 6 fonction(s).

## Vue d'ensemble

- **Classes principales** : ArticleForm
- **Fonctions principales** : allowed_file, clean_html, get_image, index, random_filename, upload_image
- **Dépendances** : bleach, flask, flask_ckeditor, flask_wtf, os, pathlib, uuid, wtforms, wtforms.validators
- **Endpoints API** : /, /upload, /uploads/<path:filename>

## Détail des fichiers

### `app.py`

Module Python. Nombre de lignes: 53. Elements detectés: class ArticleForm, def clean_html, def allowed_file

**Classes** : ArticleForm
**Fonctions** : clean_html, allowed_file, random_filename, index, get_image, upload_image
**Dépendances** : os, uuid, pathlib, flask_ckeditor, flask, flask_wtf, wtforms, wtforms.validators, bleach
**API** : /, /uploads/<path:filename>, /upload
