# Documentation technique - calculator

## Objectif du projet
Projet basé sur Docker, Express.js, JavaScript, Node.js. D'après son README, il s'agit de : « Calculator.js: a node.js Demonstration Project ».

## Fonctionnement général
Le projet démarre via public/index.html, puis suit une organisation de type **Unknown Architecture**. Se référer au code source pour le détail exact de l'enchaînement entre modules.

## Architecture
Architecture détectée : **Unknown Architecture** 
(confiance estimée : 35%).

Cette détection est basée sur des signaux structurels et doit être validée manuellement.

## Technologies utilisées
Docker, Express.js, JavaScript, Node.js

## Bases de données
Non déterminé


## Modules principaux
- `server.js` : Module JavaScript. Nombre de lignes: 11.
- `package.json` : Fichier JSON. Nombre de lignes: 36.
- `public/default.css` : Style CSS. Nombre de lignes: 129.
- `api/controllers/arithmeticController.js` : Module JavaScript. Nombre de lignes: 38.
- `api/models/arithmeticModel.js` : Impossible de lire le fichier
- `public/index.html` : Page HTML. Nombre de lignes: 229. Elements detectés: function getValue, function setValue, function setError
- `README.md` : Source file. Nombre de lignes: 12.

## Flux de données
Le point de démarrage identifié est public/index.html. Les autres relations entre modules n'ont pas pu être déterminées automatiquement : se référer au code source.

## Points d'entrée
- public/index.html

## Dépendances importantes
- 
- chai@^4.2.0
- express
- express@^4.16.4
- mocha-junit-reporter@^1.18.0
- mocha-multi-reporters@^1.1.7
- mocha@^5.2.0
- nyc@^13.3.0
- supertest@^3.4.2

## Analyse détaillée des fichiers
- `server.js` : Module JavaScript. Nombre de lignes: 11.
- `package.json` : Fichier JSON. Nombre de lignes: 36.
- `public/default.css` : Style CSS. Nombre de lignes: 129.
- `api/controllers/arithmeticController.js` : Module JavaScript. Nombre de lignes: 38.
- `api/models/arithmeticModel.js` : Impossible de lire le fichier
- `public/index.html` : Page HTML. Nombre de lignes: 229. Elements detectés: function getValue, function setValue, function setError
- `README.md` : Source file. Nombre de lignes: 12.

## Recommandations
- Vérifier les modules principaux manuellement.
- Compléter la documentation avec une analyse approfondie du code source.
