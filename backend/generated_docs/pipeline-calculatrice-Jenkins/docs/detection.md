# Détection automatique

Architecture : **Unknown Architecture**

Confiance : 35%

## Classement

| Architecture | Score | Confiance |
|---|---|---|
| Monolithic | 5 | 50.0% |

## Analyse IA

# Objectif du projet

Le projet pipeline-calculatrice-Jenkins est un programme Python qui permet de faire des additions, des soustractions, des multiplications et des divisions pour des entiers. Le code est organisé en trois fichiers principaux : `calc.py`, `prog.py` et `test_calc.py`. Ce dernier contient les tests unitaires pour les fonctions de calcul.

Base-toi principalement sur :

- les points d'entrée
- les classes
- les fonctions
- le code

Le README peut compléter cette description uniquement si les informations sont cohérentes avec le code.

---

# Fonctionnement général

Le projet est composé de trois parties principales :

1.  `calc.py` : Ce fichier contient les fonctions de calcul (addition, soustraction, multiplication et division). Il définit également des classes pour gérer ces opérations.
2.  `prog.py` : Ce fichier contient le programme principal qui lance la calculatrice en utilisant les fonctions de `calc.py`.
3.  `test_calc.py` : Ce fichier contient les tests unitaires pour les fonctions de calcul.

Les interactions entre ces composants sont les suivantes :

-   Le programme principal (`prog.py`) appelle les fonctions de calcul (`calc.py`) pour effectuer les opérations.
-   Les tests unitaires (`test_calc.py`) vérifient que les fonctions de calcul fonctionnent correctement.

---

# Architecture

L'architecture du projet est basée sur le principe de separation des concerns. Chaque fichier a un rôle spécifique :

-   `calc.py` : Contient les fonctions de calcul et les classes pour gérer ces opérations.
-   `prog.py` : Contient le programme principal qui lance la calculatrice en utilisant les fonctions de `calc.py`.
-   `test_calc.py` : Contient les tests unitaires pour les fonctions de calcul.

Cette architecture permet une organisation claire et une maintenance facile du code.

---

# Technologies utilisées

Pour chaque technologie détectée :

*   Python
    *   Rôle dans le projet : Langage de programmation principal.
    *   Où elle est utilisée : Tout le code est écrit en Python.
*   Unittest
    *   Rôle dans le projet : Framework pour les tests unitaires.
    *   Où elle est utilisée : Dans le fichier `test_calc.py`.

---

# Modules principaux

Pour chaque module important :

*   `calc`
    *   Chemin du fichier : `sources/calc.py`.
    *   Rôle : Contient les fonctions de calcul et les classes pour gérer ces opérations.
    *   Classes principales : `Test`, `add`, `sous`, `mult`.
    *   Fonctions importantes : `test_add`, `test_sous`, `test_mult`.
    *   Dépendances : `unittest` (importé dans le fichier).
    *   Interaction avec les autres modules : Le programme principal (`prog.py`) utilise ces fonctions pour effectuer les opérations.
*   `unittest`
    *   Chemin du fichier : `sources/test_calc.py`.
    *   Rôle : Framework pour les tests unitaires.
    *   Utilisation : Dans le fichier `test_calc.py` pour tester les fonctions de calcul.

---

# Flux de données

Entrée

↓

Traitement

↓

Sortie

Le flux réellement observable est :

-   Entrée : Les nombres à calculer (par exemple, 2 et 6).
-   Traitement : Le programme principal (`prog.py`) appelle les fonctions de calcul (`calc.py`) pour effectuer l'opération.
-   Sortie : La réponse à l'