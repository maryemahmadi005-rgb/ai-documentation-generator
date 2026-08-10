# Module : examples/ch2

1 fichier(s), 15 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : admin, bar, do_something, foo, hello, hi, is_safe_url, login, logout, note, set_cookie, teapot, the_answer, three_colors, time_machine
- **Dépendances** : flask, markupsafe, os, urllib.parse
- **Endpoints API** : /, /answer, /back/<int:year>, /brew/<drink>, /colors/<any(blue, white, red):color>, /hello, /hi, /note, /note/<content_type>, /set/<name>

## Détail des fichiers

### `app.py`

Module Python. Nombre de lignes: 147. Elements detectés: def hello, def hi, def time_machine

**Fonctions** : hello, hi, time_machine, three_colors, teapot, the_answer, note, set_cookie, login, admin, logout, foo, bar, do_something, is_safe_url
**Dépendances** : os, urllib.parse, markupsafe, flask
**API** : /, /hello, /hi, /back/<int:year>, /colors/<any(blue, white, red):color>, /brew/<drink>, /answer, /note, /note/<content_type>, /set/<name>
