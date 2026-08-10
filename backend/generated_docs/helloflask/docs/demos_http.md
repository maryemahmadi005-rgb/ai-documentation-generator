# Module : demos/http

1 fichier(s), 15 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : admin, bar, foo, go_back, hello, hi, load_post, login, logout, not_found, note, set_cookie, show_post, teapot, three_colors
- **Dépendances** : flask, jinja2.utils, markupsafe, os, urllib.parse, urlparse
- **Endpoints API** : /, /404, /brew/<drink>, /colors/<any(blue, white, red):color>, /goback/<int:year>, /hello, /hi, /note, /note/<content_type>, /set/<name>

## Détail des fichiers

### `app.py`

Module Python. Nombre de lignes: 182. Elements detectés: def hello, def hi, def go_back

**Fonctions** : hello, hi, go_back, three_colors, teapot, not_found, note, set_cookie, login, admin, logout, show_post, load_post, foo, bar
**Dépendances** : os, urlparse, urllib.parse, markupsafe, jinja2.utils, flask
**API** : /, /hello, /hi, /goback/<int:year>, /colors/<any(blue, white, red):color>, /brew/<drink>, /404, /note, /note/<content_type>, /set/<name>
