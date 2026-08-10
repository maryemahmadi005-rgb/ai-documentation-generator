# Module : app/main

4 fichier(s), 5 classe(s), 22 fonction(s).

## Vue d'ensemble

- **Classes principales** : CommentForm, EditProfileAdminForm, EditProfileForm, NameForm, PostForm
- **Fonctions principales** : __init__, after_request, edit, edit_profile, edit_profile_admin, follow, followed_by, followers, forbidden, index, inject_permissions, internal_server_error, moderate, page_not_found, post
- **Dépendances** : ., .., ..decorators, ..models, .forms, flask, flask_login, flask_pagedown.fields, flask_sqlalchemy, flask_wtf, wtforms, wtforms.validators
- **Endpoints API** : /, /edit-profile, /edit-profile/<int:id>, /edit/<int:id>, /follow/<username>, /followers/<username>, /post/<int:id>, /shutdown, /unfollow/<username>, /user/<username>

## Détail des fichiers

### `app/main/__init__.py`

Module Python. Nombre de lignes: 7. Elements detectés: def inject_permissions

**Fonctions** : inject_permissions
**Dépendances** : flask, ., ..models

### `app/main/errors.py`

Module Python. Nombre de lignes: 26. Elements detectés: def forbidden, def page_not_found, def internal_server_error

**Fonctions** : forbidden, page_not_found, internal_server_error
**Dépendances** : flask, .

### `app/main/forms.py`

Module Python. Nombre de lignes: 48. Elements detectés: class NameForm, class EditProfileForm, class EditProfileAdminForm

**Classes** : NameForm, EditProfileForm, EditProfileAdminForm, PostForm, CommentForm
**Fonctions** : __init__, validate_email, validate_username
**Dépendances** : flask_wtf, wtforms, wtforms.validators, flask_pagedown.fields, ..models

### `app/main/views.py`

Module Python. Nombre de lignes: 244. Elements detectés: def after_request, def server_shutdown, def index

**Fonctions** : after_request, server_shutdown, index, user, edit_profile, edit_profile_admin, post, edit, follow, unfollow, followers, followed_by, show_all, show_followed, moderate
**Dépendances** : flask, flask_login, flask_sqlalchemy, ., .forms, .., ..models, ..decorators
**API** : /shutdown, /, /user/<username>, /edit-profile, /edit-profile/<int:id>, /post/<int:id>, /edit/<int:id>, /follow/<username>, /unfollow/<username>, /followers/<username>
