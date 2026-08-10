# Module : app/api

6 fichier(s), 22 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : auth_error, bad_request, before_request, decorated_function, decorator, edit_post, forbidden, get_comment, get_comments, get_post, get_post_comments, get_posts, get_token, get_user, get_user_followed_posts
- **Dépendances** : ., .., ..models, .decorators, .errors, app.exceptions, flask, flask_httpauth, functools
- **Endpoints API** : /comments/, /comments/<int:id>, /posts/, /posts/<int:id>, /posts/<int:id>/comments/, /tokens/, /users/<int:id>, /users/<int:id>/posts/, /users/<int:id>/timeline/

## Détail des fichiers

### `app/api/authentication.py`

Module Python. Nombre de lignes: 35. Elements detectés: def verify_password, def auth_error, def before_request

**Fonctions** : verify_password, auth_error, before_request, get_token
**Dépendances** : flask, flask_httpauth, ..models, ., .errors
**API** : /tokens/

### `app/api/comments.py`

Module Python. Nombre de lignes: 59. Elements detectés: def get_comments, def get_comment, def get_post_comments

**Fonctions** : get_comments, get_comment, get_post_comments, new_post_comment
**Dépendances** : flask, .., ..models, ., .decorators
**API** : /comments/, /comments/<int:id>, /posts/<int:id>/comments/

### `app/api/decorators.py`

Module Python. Nombre de lignes: 12. Elements detectés: def permission_required, def decorator, def decorated_function

**Fonctions** : permission_required, decorator, decorated_function
**Dépendances** : functools, flask, .errors

### `app/api/errors.py`

Module Python. Nombre de lignes: 18. Elements detectés: def bad_request, def unauthorized, def forbidden

**Fonctions** : bad_request, unauthorized, forbidden, validation_error
**Dépendances** : flask, app.exceptions, .

### `app/api/posts.py`

Module Python. Nombre de lignes: 49. Elements detectés: def get_posts, def get_post, def new_post

**Fonctions** : get_posts, get_post, new_post, edit_post
**Dépendances** : flask, .., ..models, ., .decorators, .errors
**API** : /posts/, /posts/<int:id>

### `app/api/users.py`

Module Python. Nombre de lignes: 47. Elements detectés: def get_user, def get_user_posts, def get_user_followed_posts

**Fonctions** : get_user, get_user_posts, get_user_followed_posts
**Dépendances** : flask, ., ..models
**API** : /users/<int:id>, /users/<int:id>/posts/, /users/<int:id>/timeline/
