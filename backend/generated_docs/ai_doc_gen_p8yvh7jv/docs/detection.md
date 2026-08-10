# Détection automatique

Architecture : **Monolithic**

Confiance : 50%

## Classement

| Architecture | Score | Confiance |
|---|---|---|
| Monolithic | 0 | 50% |

## Analyse IA

Le fichier est un programme JavaFX qui simule une calculatrice simple. L'objectif principal de ce programme est de créer une interface utilisateur graphique (IU) qui permet à l'utilisateur d'entrer des chiffres et des opérations pour effectuer des calculs.

Les classes/fonctions importantes sont :

* La classe `Main` qui étend la classe `Application` de JavaFX. Cette classe contient le code principal du programme, notamment la méthode `start` qui est appelée lorsque l'application est lancée.
* Les boutons (`Button`) qui représentent les chiffres et les opérations mathématiques. Chaque bouton a une action associée qui permet d'afficher le texte correspondant dans le champ de saisie (`TextField`).

Les dépendances sont :

* JavaFX, un framework pour créer des applications graphiques en Java.
* Les bibliothèques standard de Java pour les opérations mathématiques et la manipulation de chaînes de caractères.