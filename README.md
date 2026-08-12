# Project Documentation

Générer des documents d'analyse pour les projets

---

## Fonctionnement général

Le flux réel fonctionne comme suit : une requête HTTP est envoyée à l'endpoint /api/analyze, qui appelle le service AnalyserService pour traiter la demande. Ce service utilise ensuite le module CodeAnalyzer pour analyser le code source du projet et générer un document d'analyse.

---


## Technologies utilisées

- JavaScript
- Python
- Flask
- React

---

## Modules principaux

### CodeAnalyzer
**Fichier :** `backend/services/analyzers/code_analyzer.py`

**Rôle :** Gère les appels HTTP vers Ollama et la validation du JSON retourné pour analyser le code source des projets.

**Classes principales :** `CodeAnalyzer`, `Analysis`
**Dépendances internes :** `Flask`, `requests`, `Ollama`
### AnalyserService
**Fichier :** `backend/services/analysis_service.py`

**Rôle :** Traite les demandes d'analyse et appelle le module CodeAnalyzer.

**Classes principales :** `Analysis`, `ProjectNotFoundError`
**Dépendances internes :** `Flask`, `requests`
### DocumentService
**Fichier :** `backend/services/document_service.py`

**Rôle :** Gère la génération des documents d'analyse.

**Classes principales :** `Document`, `DocumentationPipelineError`
**Dépendances internes :** `Flask`, `requests`

---

## Flux de données

Les données de code source sont envoyées à l'endpoint /api/analyze, qui appelle le service AnalyserService pour traiter la demande. Ce service utilise ensuite le module CodeAnalyzer pour analyser le code source et générer un document d'analyse.

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

## Recommandations

- {'type': "absence de gestion d'erreur", 'description': "L'endpoint /api/analyze ne gère pas les erreurs de manière efficace."}
