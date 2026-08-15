# Project Documentation

Générer des documents de documentation automatiquement à partir d'un projet

---

## Fonctionnement général

Le projet utilise une architecture Flask pour gérer les requêtes HTTP et une base de données pour stocker les données. L'analyse de données est effectuée à l'aide de l'API d'analyse, qui utilise l'LLM Ollama pour analyser les documents.

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

**Rôle :** Gère les requêtes HTTP et la configuration de l'application

**Classes principales :** `Flask`, `Config`
**Dépendances internes :** `Flask`, `Cors`, `JWT`
**Routes exposées :** `/api/health`, `/api/analyses/<int:analysis_id>`
### React
**Fichier :** `front2/src/App.jsx`

**Rôle :** Gère la interface utilisateur et la communication avec l'API backend

**Classes principales :** `App`, `BrowserRouter`
**Dépendances internes :** `React`, `Redux`
### Ollama
**Fichier :** `backend/app/models/analysis.py`

**Rôle :** Effectue l'analyse de données à l'aide de l'LLM

**Classes principales :** `Analysis`, `Ollama`
**Dépendances internes :** `Flask`, `Ollama`

---

## Flux de données

Les données sont transmises de l'API backend à l'API d'analyse via l'LLM Ollama. Les données sont ensuite stockées dans la base de données.

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

**Installation frontend**

- npm install

**Configuration**

- backend/app/config.py

**Services externes**

- Ollama
- Base de données

**Commandes de démarrage**

- backend/run.py


---

## Usage

**Démarrage de l'application**

- backend/run.py

**API principale**

- /api/health
- /api/analyses/<int:analysis_id>

**Exemple d'utilisation**

- /api/analyze/history

**Flux frontend/backend**

- Frontend app -> Backend API -> Ollama


---

## Recommandations

Aucune recommandation spécifique détectée.
