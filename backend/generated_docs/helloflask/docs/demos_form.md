# Module : demos/form

2 fichier(s), 8 classe(s), 16 fonction(s).

## Vue d'ensemble

- **Classes principales** : FortyTwoForm, LoginForm, MultiUploadForm, NewPostForm, RegisterForm, SigninForm, SigninForm2, UploadForm
- **Fonctions principales** : allowed_file, basic, bootstrap, custom_validator, dropzone_upload, get_file, html, index, multi_form, multi_form_multi_view, multi_upload, random_filename, show_images, two_submits, upload
- **Dépendances** : flask, flask_ckeditor, flask_dropzone, flask_wtf, flask_wtf.csrf, flask_wtf.file, forms, os, uuid, wtforms, wtforms.validators
- **Endpoints API** : /, /basic, /bootstrap, /custom-validator, /dropzone-upload, /html, /multi-upload, /upload, /uploaded-images, /uploads/<path:filename>

## Détail des fichiers

### `app.py`

Module Python. Nombre de lignes: 208. Elements detectés: def index, def html, def basic

**Fonctions** : index, html, basic, bootstrap, custom_validator, get_file, show_images, allowed_file, random_filename, upload, multi_upload, dropzone_upload, two_submits, multi_form, multi_form_multi_view
**Dépendances** : os, uuid, flask, flask_ckeditor, flask_dropzone, flask_wtf.csrf, wtforms, forms
**API** : /, /html, /basic, /bootstrap, /custom-validator, /uploads/<path:filename>, /uploaded-images, /upload, /multi-upload, /dropzone-upload

### `forms.py`

Module Python. Nombre de lignes: 63. Elements detectés: class LoginForm, class FortyTwoForm, def validate_answer

**Classes** : LoginForm, FortyTwoForm, UploadForm, MultiUploadForm, NewPostForm, SigninForm, RegisterForm, SigninForm2
**Fonctions** : validate_answer
**Dépendances** : flask_ckeditor, flask_wtf, flask_wtf.file, wtforms, wtforms.validators
