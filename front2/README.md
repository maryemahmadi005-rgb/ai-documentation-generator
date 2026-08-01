# DocGen AI — Frontend

Frontend React (Vite + JavaScript) pour le Générateur Automatique de
Documentation Technique. Design "AI SaaS" premium inspiré de l'expérience
d'outils comme Repowise, avec une identité visuelle originale (voir section
Design ci-dessous).

Pipeline backend inchangé : GitHub URL → Clone → Analyse code → Résumé IA
(Ollama) → Détection architecture → Génération documentation → Sauvegarde.
Aucune route Flask n'a été modifiée ; seule la couche frontend a été revue.

## Installation

```bash
npm install
npm run dev
```

L'application démarre sur `http://localhost:5173`.
Le backend Flask doit tourner sur `http://127.0.0.1:5000` (voir `src/api/axios.js`).

## Design system

- **Couleurs** : bleu primaire `#2e5eff` / `#1d3fd1`, dégradés bleu/violet doux
  (`#7c8fff`) sur fond blanc, textes ardoise (`#0f1626` → `#9aa4b5`).
- **Typographie** : titres en `Space Grotesk`, texte courant en `Inter`,
  code/monospace en `JetBrains Mono` (chargées via Google Fonts dans
  `src/styles/global.css`).
- **Forme** : cartes à coins arrondis 16–20px, ombres douces, transitions
  `cubic-bezier` sur hover.
- **Signature visuelle** : un motif de "pipeline animé" (dépôt → moteur IA →
  documentation) relié par un trait en pointillés animé. Il apparaît en grand
  dans le hero (`PipelineSignature.jsx`) et se retrouve, sous forme d'étapes
  cochées une à une, dans le composant de progression pendant l'analyse
  (`PipelineProgress.jsx`) — pour une identité cohérente entre les deux
  moments clés du produit.

## Design system

- **Thème** : sombre par défaut ("dark developer theme"), avec bascule
  claire disponible via `ThemeToggle` (`[data-theme="light"]` dans
  `global.css`).
- **Couleurs** : accent bleu/indigo `#5b7dff` → `#4361ee`, touches violettes
  (`#a78bfa`) et sarcelle (`#2dd4bf`), fonds ardoise très sombres
  (`#0d1122` → `#171e38`).
- **Typographie** : titres en `Space Grotesk`, texte courant en `Inter`,
  code/monospace en `JetBrains Mono`.
- **Forme** : cartes à coins arrondis 16–20px, ombres douces + halo bleu
  (`--shadow-glow`), transitions `cubic-bezier` sur hover.
- **Icônes** : `lucide-react` (Github, GitBranch, Layers, FileText, Sparkles,
  CheckCircle2, Loader2, ...).
- **Animations** : `framer-motion` pour les apparitions au scroll (hero,
  How it works, Feature cards, sections de la page d'analyse).
- **Visuel signature** : `GithubVisual.jsx` — une fenêtre de code façon
  éditeur avec balayage animé et badges flottants (architecture, fichiers,
  résumé IA), pour une identité "outil développeur" originale.

## Dépendances ajoutées

- `lucide-react` — icônes.
- `framer-motion` — animations d'apparition (hero, sections, cartes).
- `mermaid` — rendu du diagramme d'architecture (chargé dynamiquement,
  uniquement si un diagramme est présent).

## Pages et routes

| Route             | Page                | Description                                   |
|--------------------|----------------------|------------------------------------------------|
| `/login`           | `Login.jsx`          | Connexion                                      |
| `/register`         | `Register.jsx`        | Création de compte                             |
| `/home`             | `Home.jsx`            | Hero + formulaire de génération de documentation |
| `/analysis/:id`     | `AnalysisResult.jsx`  | Résultat détaillé d'une analyse (2 colonnes)   |
| `/history`          | `History.jsx`         | Historique des analyses (cartes)              |

Après `Generate Documentation`, l'utilisateur est automatiquement redirigé
vers `/analysis/:id` (les données de l'analyse sont transmises via l'état de
navigation `location.state.analysis`, et re-synchronisées via l'API si la
page est rechargée directement).

## Structure

```
src/
 ├── api/axios.js
 ├── components/
 │    ├── Navbar.jsx / .css          # Logo, Home / History, ThemeToggle, Logout
 │    ├── Sidebar.jsx / .css         # navigation fixe de la page Analysis (scrollspy)
 │    ├── SectionCard.jsx / .css     # wrapper de section (ancre + titre + carte)
 │    ├── Hero.jsx / .css            # copie + illustration du hero (Home)
 │    ├── GenerateForm.jsx / .css    # input GitHub URL + bouton + progression
 │    ├── SearchBar.jsx / .css       # recherche (page History)
 │    ├── ThemeToggle.jsx / .css     # bascule Dark / Light
 │    ├── Footer.jsx / .css
 │    ├── PipelineSignature.jsx / .css  # illustration animée (utilisée par Hero)
 │    ├── HistoryCard.jsx / .css     # carte d'historique (page History)
 │    ├── Overview/
 │    │    ├── StatCard.jsx / .css
 │    │    └── ProjectInfo.jsx / .css
 │    ├── Architecture/
 │    │    ├── ArchitectureCard.jsx / .css
 │    │    ├── MermaidDiagram.jsx / .css
 │    │    └── PipelineProgress.jsx / .css
 │    ├── Repository/
 │    │    ├── RepoTree.jsx / .css
 │    │    └── FileViewer.jsx / .css
 │    ├── Documentation/
 │    │    ├── MarkdownViewer.jsx / .css
 │    │    └── DownloadButtons.jsx / .css
 │    ├── Summary/
 │    │    └── AISummary.jsx / .css
 │    └── Common/
 │         ├── Loader.jsx / .css
 │         ├── EmptyState.jsx / .css
 │         └── ErrorMessage.jsx
 ├── pages/
 │    ├── Login.jsx, Register.jsx, Auth.css
 │    ├── Home.jsx / .css            # assemble Hero + GenerateForm
 │    ├── AnalysisResult.jsx / .css  # assemble Sidebar + toutes les sections
 │    └── History.jsx / .css         # assemble SearchBar + HistoryCard
 ├── routes/AppRoutes.jsx
 ├── styles/global.css               # design tokens (+ overrides [data-theme="dark"])
 ├── App.jsx
 └── main.jsx
```

Les pages ne contiennent plus que la logique (état, appels API) ; chaque
domaine fonctionnel (Overview, Architecture, Repository, Documentation,
Summary) a son propre dossier de composants de présentation.

### Dark / Light mode

`ThemeToggle` bascule l'attribut `data-theme` sur `<html>` et persiste le
choix dans `localStorage`. Les couleurs sombres sont définies comme des
overrides de variables CSS dans `styles/global.css` (`[data-theme="dark"]`),
donc tous les composants existants héritent automatiquement du thème sans
code supplémentaire.

### Aperçu de fichier (Repository)

`RepoTree` accepte un callback `onFileSelect` déclenché au clic sur un
fichier ; `FileViewer` affiche `node.content` s'il est présent dans la
réponse de l'API. Aucun endpoint de contenu de fichier n'étant listé dans le
backend fourni, un état vide explicite s'affiche si ce champ est absent.

## Endpoints utilisés (inchangés)

| Méthode | Endpoint             | Usage                                          |
|---------|-----------------------|--------------------------------------------------|
| POST    | `/api/login`          | Connexion (nom d'endpoint supposé, à adapter)   |
| POST    | `/api/users`          | Création de compte                              |
| POST    | `/api/projects`       | Création du projet — requiert `user_id`, `name`, `github_url` |
| POST    | `/api/analyze`        | Lancement de l'analyse — requiert `project_id` et `github_url` |
| GET     | `/api/analyze/history`| Historique des analyses (⚠️ pas `/api/analyses`) |
| GET     | `/api/documents`      | Secours si le contenu du document est absent (par `analysis_id`) |

### Flux de génération (Home.jsx)

1. `POST /projects` avec `{ user_id, name, github_url }` → l'API renvoie `{ project: { id, ... } }`.
2. `POST /analyze` avec `{ project_id, github_url }` → l'API renvoie :
   ```json
   {
     "analysis": {
       "id": 1,
       "status": "completed",
       "architecture": "MVC",
       "architecture_score": 0.82,
       "architecture_confidence": 0.91,
       "ai_summary": "...",
       "document": { "id": 1, "content": "...", "format": "markdown", "file_path": "..." }
     }
   }
   ```
   Cette réponse **ne contient ni `project_name` ni `github_url`** : le
   frontend les réinjecte lui-même (`extractProjectName(githubUrl)` +
   `github_url`) avant de naviguer vers `/analysis/:id`.
3. Redirection vers `/analysis/:id` avec le résultat enrichi.

`user_id` est lu depuis `localStorage.getItem("user")` (stocké au login) —
suppose que `POST /api/login` renvoie `{ user: { id, ... } }`.

### Mapping utilisé dans AnalysisResult.jsx

- Architecture : `analysis.architecture` (string), `analysis.architecture_score`, `analysis.architecture_confidence`
- README / Documentation : `analysis.document.content` (un seul document markdown généré par analyse — README et Documentation affichent donc le même contenu)
- Bouton "Open Generated Documentation" : `analysis.document.file_path` — c'est un **chemin serveur**, pas forcément une URL ouvrable directement dans le navigateur ; à adapter si une route statique/de téléchargement existe côté Flask.
- Repository tree, Mermaid diagram, files/directories analysées : **non renvoyés** par ce backend actuellement → ces sections affichent un état vide tant que ces champs ne sont pas ajoutés côté API.

⚠️ La forme exacte de la réponse de `/projects` (`{ id }`, `{ project_id }` ou
`{ project: { id } }`) n'était pas spécifiée : le code lit les trois
variantes avec fallback (`src/pages/Home.jsx`), à ajuster si besoin une fois
testé contre la vraie réponse Flask.

## Hypothèses de structure de données

Les champs suivants ne sont pas garantis dans la liste d'endpoints fournie ;
le code lit plusieurs variantes de clés avec fallback, à ajuster une fois
l'API testée en conditions réelles :

- `analysis.id` (ou `project_id`) : identifiant utilisé dans `/analysis/:id`.
- `analysis.file_structure` / `tree` / `repository_tree` : tableau récursif
  `{ name, type: 'file' | 'folder', children? }` pour la section Repository.
- `analysis.architecture.diagram` / `mermaid_diagram` : code Mermaid (chaîne
  de caractères) pour le diagramme d'architecture (optionnel, la carte ne
  s'affiche que si ce champ est présent).
- `analysis.readme_content` vs `analysis.documentation_content` : le README
  brut et la documentation complète sont traités comme deux contenus
  distincts (sections "README" et "Documentation" séparées, comme demandé).

## Dépendance ajoutée

`mermaid` (chargée dynamiquement, uniquement si un diagramme est présent)
pour le rendu du diagramme d'architecture dans `AnalysisResult`.
