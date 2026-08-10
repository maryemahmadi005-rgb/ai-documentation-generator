# Module : demos/email

1 fichier(s), 2 classe(s), 8 fonction(s).

## Vue d'ensemble

- **Classes principales** : EmailForm, SubscribeForm
- **Fonctions principales** : _send_async_mail, index, send_api_mail, send_async_mail, send_smtp_mail, send_subscribe_mail, subscribe, unsubscribe
- **Dépendances** : flask, flask_mail, flask_wtf, os, sendgrid, sendgrid.helpers.mail, threading, wtforms, wtforms.validators
- **Endpoints API** : /, /subscribe, /unsubscribe

## Détail des fichiers

### `app.py`

Module Python. Nombre de lignes: 103. Elements detectés: def send_smtp_mail, def send_api_mail, def _send_async_mail

**Classes** : EmailForm, SubscribeForm
**Fonctions** : send_smtp_mail, send_api_mail, _send_async_mail, send_async_mail, send_subscribe_mail, index, subscribe, unsubscribe
**Dépendances** : os, threading, sendgrid, sendgrid.helpers.mail, flask_mail, flask_wtf, wtforms, wtforms.validators, flask
**API** : /, /subscribe, /unsubscribe
