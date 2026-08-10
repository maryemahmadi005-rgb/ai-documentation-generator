# Documentation technique - pipeline-calculatrice-Jenkins

## Objectif du projet
Projet basé sur Python. D'après son README, il s'agit de : « Ce dépôt Github contient un programme Python permettant de faire des additions, des soustractions, des multiplications et des divisions pour des entiers ».

## Fonctionnement général
Le projet démarre via sources/prog.py, puis suit une organisation de type **Unknown Architecture**. Se référer au code source pour le détail exact de l'enchaînement entre modules.

## Architecture
Architecture détectée : **Unknown Architecture** 
(confiance estimée : 35%).

Cette détection est basée sur des signaux structurels et doit être validée manuellement.

## Technologies utilisées
Python

## Bases de données
Non déterminé



## Modules principaux
- `sources/calc.py` : Module Python. Nombre de lignes: 36. Elements detectés: def add, def sous, def mult
- `sources/test_calc.py` : Module Python. Nombre de lignes: 83. Elements detectés: class Test, def test_add, def test_add_str
- `sources/prog.py` : Module Python. Nombre de lignes: 12.

## Flux de données
Le point de démarrage identifié est sources/prog.py. Les autres relations entre modules n'ont pas pu être déterminées automatiquement : se référer au code source.

## Points d'entrée
- sources/prog.py

## Dépendances importantes
- calc
- unittest



## Recommandations
- Vérifier les modules principaux manuellement.
- Compléter la documentation avec une analyse approfondie du code source.
