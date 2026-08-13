# Project Documentation

Générer des documents d'analyse à partir de données provenant de diverses sources

---

## Fonctionnement général

Le projet utilise une architecture Flask pour gérer les requêtes HTTP et les interactions avec les bases de données. Les données sont traitées par l'AnalyserService, qui utilise des modèles Ollama pour analyser les documents texte.

---


## Technologies utilisées

- JavaScript
- Python
- Flask
- React

---

## Modules principaux

### app
**Fichier :** `backend/app/__init__.py`

**Rôle :** Gère les appels HTTP vers Ollama et la validation du JSON retourné

**Classes principales :** `Flask`, `Config`
**Dépendances internes :** `flask`, `python`
**Routes exposées :** `/api/health`
### analysis_routes
**Fichier :** `backend/app/routes/analysis_routes.py`

**Rôle :** Gère les requêtes d'analyse et les interactions avec Ollama

**Classes principales :** `Flask`, `db`
**Dépendances internes :** `flask`, `db`
**Routes exposées :** `/api/analyses/<int:analysis_id>`, `/api/analyses`
### document_routes
**Fichier :** `backend/app/routes/document_routes.py`

**Rôle :** Gère les requêtes de document et les interactions avec la base de données

**Classes principales :** `Flask`, `db`
**Dépendances internes :** `flask`, `db`
**Routes exposées :** `/api/documents/<int:document_id>`

---

## Flux de données

Les données sont traitées par l'AnalyserService, qui utilise des modèles Ollama pour analyser les documents texte. Les résultats sont ensuite envoyés à la base de données pour stockage.

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

**Configuration**

- .env.example

**Services externes**

- Ollama
- base de données

**Commandes de démarrage**

- backend/run.py


---

## Usage

**Démarrage de l'application**

- python backend/run.py
- npm run start

**API principale**

- /api/health
- /api/analyses/<int:analysis_id>
- /api/documents/<int:document_id>

**Exemple d'utilisation**

- python backend/app/routes/document_routes.py /api/documents/1


---

## Recommandations

Aucune recommandation spécifique détectée.
