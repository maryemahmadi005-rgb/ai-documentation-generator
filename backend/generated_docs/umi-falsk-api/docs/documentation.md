# Documentation technique - umi-falsk-api

## Objectif du projet
Projet basé sur MySQL, Python, SQLAlchemy ORM, pip (Python). D'après son README, il s'agit de : « > 还是有很细节要优化但是因为我时间不够所以只能先这样（后期优化），如果那位兄台有空可以帮忙优化一下感谢（不过用来练手是够了） ».

## Fonctionnement général
Le projet démarre via run.py, puis suit une organisation de type **Flask Application**. Se référer au code source pour le détail exact de l'enchaînement entre modules.

## Architecture
Architecture détectée : **Flask Application** 
(confiance estimée : 79.2%).

Cette détection est basée sur des signaux structurels et doit être validée manuellement.

## Technologies utilisées
MySQL, Python, SQLAlchemy ORM, pip (Python)

## Bases de données
MySQL, SQLAlchemy ORM



## Modules principaux
- `utils/AlchemyEncoder.py` : Module Python. Nombre de lignes: 17. Elements detectés: class AlchemyEncoder, def default
- `apps/models/weiboUser/index.py` : Module Python. Nombre de lignes: 18. Elements detectés: class WeiboUser
- `apps/models/weiboCaptureRecord/index.py` : Module Python. Nombre de lignes: 16. Elements detectés: class WeiboCaptureRecord
- `routes/index.py` : Module Python. Nombre de lignes: 124. Elements detectés: def testPage, def testCoursePage, def weiboCapture
- `apps/services/WeiboCaptureRecord/index.py` : Module Python. Nombre de lignes: 125. Elements detectés: class WeiboCaptureRecord, def __init__, def __repr__
- `apps/services/testCourse/index.py` : Module Python. Nombre de lignes: 12. Elements detectés: class TestCourse, def __init__, def run
- `config.py` : Module Python. Nombre de lignes: 19.

## Flux de données
Le point de démarrage identifié est run.py. Les autres relations entre modules n'ont pas pu être déterminées automatiquement : se référer au code source.

## Points d'entrée
- run.py

## Dépendances importantes
- apps
- config
- csv
- flask
- flask_sqlalchemy
- multiprocessing
- requests
- sqlalchemy
- utils



## Recommandations
- Vérifier les modules principaux manuellement.
- Compléter la documentation avec une analyse approfondie du code source.
