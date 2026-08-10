# Module : app/auth

2 fichier(s), 6 classe(s), 14 fonction(s).

## Vue d'ensemble

- **Classes principales** : ChangeEmailForm, ChangePasswordForm, LoginForm, PasswordResetForm, PasswordResetRequestForm, RegistrationForm
- **Fonctions principales** : before_request, change_email, change_email_request, change_password, confirm, login, logout, password_reset, password_reset_request, register, resend_confirmation, unconfirmed, validate_email, validate_username
- **Dépendances** : ., .., ..email, ..models, .forms, flask, flask_login, flask_wtf, wtforms, wtforms.validators
- **Endpoints API** : /change-password, /change_email, /confirm, /confirm/<token>, /login, /logout, /register, /reset, /reset/<token>, /unconfirmed

## Détail des fichiers

### `app/auth/forms.py`

Module Python. Nombre de lignes: 53. Elements detectés: class LoginForm, class RegistrationForm, def validate_email

**Classes** : LoginForm, RegistrationForm, ChangePasswordForm, PasswordResetRequestForm, PasswordResetForm, ChangeEmailForm
**Fonctions** : validate_email, validate_username
**Dépendances** : flask_wtf, wtforms, wtforms.validators, ..models

### `app/auth/views.py`

Module Python. Nombre de lignes: 145. Elements detectés: def before_request, def unconfirmed, def login

**Fonctions** : before_request, unconfirmed, login, logout, register, confirm, resend_confirmation, change_password, password_reset_request, password_reset, change_email_request, change_email
**Dépendances** : flask, flask_login, ., .., ..models, ..email, .forms
**API** : /unconfirmed, /login, /logout, /register, /confirm/<token>, /confirm, /change-password, /reset, /reset/<token>, /change_email
