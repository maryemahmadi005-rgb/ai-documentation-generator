# Project Documentation

Générer des documents d'analyse à partir de données provenant de diverses sources, en utilisant une plateforme web pour la collecte et le traitement des données.

---

## Fonctionnement général

Le flux opérationnel du projet consiste en la collecte des données via l'interface web, qui sont ensuite traitées par les services backend (Flask) avant d'être stockées dans une base de données. Les utilisateurs peuvent ensuite télécharger leurs documents d'analyse et les envoyer à l'application pour analyse. L'application utilise un modèle Ollama pour analyser les documents et générer des résultats.

---


## Technologies utilisées

- JavaScript
- Python
- Flask
- React

---

## Modules principaux

### Flask
**Fichier :** `backend/app/__init__.py`

**Rôle :** Service backend qui gère les appels HTTP vers l'interface web et la base de données.

**Classes principales :** `Flask`, `Config`
**Dépendances internes :** `Flask`, `Cors`, `JWT`, `Migrate`
**Routes exposées :** `/api/health`
### Frontend
**Fichier :** `front2/src/App.jsx`

**Rôle :** Interface web qui collecte les données des utilisateurs et les envoie à l'application.

**Classes principales :** `App`
**Routes exposées :** `/api/analyses/<int:analysis_id>`

---

## Flux de données

Flux de données : Frontend -> API Backend -> Base de données Ollama -> Résultats

---

## Points d'entrée

- `backend/app/__init__.py`
- `backend/app/routes/analysis_routes.py`
- `backend/app/routes/analyze_routes.py`
- `backend/app/routes/auth_routes.py`
- `backend/app/routes/document_routes.py`
- `backend/app/routes/project_routes.py`
- `backend/app/routes/user_routes.py`
- `backend/run.py`
- `front2/src/App.jsx`
- `front2/src/main.jsx`

---

## Endpoints API

| Méthode(s) | Endpoint | Fichier |
|---|---|---|
| GET | `/api/health` | `backend/app/__init__.py` |
| GET | `/api/analyses/<int:analysis_id>` | `backend/app/routes/analysis_routes.py` |
| POST | `/api/analyses` | `backend/app/routes/analysis_routes.py` |
| PUT | `/api/analyses/<int:analysis_id>` | `backend/app/routes/analysis_routes.py` |
| GET | `/api/analyze/history` | `backend/app/routes/analyze_routes.py` |
| POST | `/api/analyze` | `backend/app/routes/analyze_routes.py` |
| POST | `/api/auth/login` | `backend/app/routes/auth_routes.py` |
| GET | `/api/documents` | `backend/app/routes/document_routes.py` |
| POST | `/api/documents` | `backend/app/routes/document_routes.py` |
| GET | `/api/documents/<int:id>` | `backend/app/routes/document_routes.py` |
| GET | `/api/documents/analysis/<int:analysis_id>` | `backend/app/routes/document_routes.py` |
| DELETE | `/api/documents/<int:id>` | `backend/app/routes/document_routes.py` |
| GET | `/api/documents/<int:id>/download` | `backend/app/routes/document_routes.py` |
| GET | `/api/projects` | `backend/app/routes/project_routes.py` |
| POST | `/api/projects` | `backend/app/routes/project_routes.py` |
| PUT | `/api/projects/<int:id>` | `backend/app/routes/project_routes.py` |
| DELETE | `/api/projects/<int:id>` | `backend/app/routes/project_routes.py` |
| GET | `/api/users` | `backend/app/routes/user_routes.py` |
| POST | `/api/users` | `backend/app/routes/user_routes.py` |
| PUT | `/api/users/<int:id>` | `backend/app/routes/user_routes.py` |
| DELETE | `/api/users/<int:id>` | `backend/app/routes/user_routes.py` |

---

## Dépendances importantes

Aucune dépendance importante détectée.

---

## Installation

**Prérequis**

- Python 3.11+

**Installation backend**

- pip install -r backend/requirements.txt
- python backend/run.py

**Installation frontend**

- npm install
- npm run start

**Services externes**

- Ollama
- Base de données

**Commandes de démarrage**

- python backend/run.py


---

## Usage

**Démarrage de l'application**

- npm run start

**API principale**

- /api/health
- /api/analyses/<int:analysis_id>

**Exemple d'utilisation**

- curl -X GET 'http://localhost:5000/api/analyses/1'

**Flux frontend/backend**

- Frontend -> API Backend -> Service backend


---

## Recommandations

Aucune recommandation spécifique détectée.
