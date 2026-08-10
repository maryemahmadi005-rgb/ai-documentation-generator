# Module : python3_libraries/opencv/opencv3by_example/Chapter09

4 fichier(s), 8 classe(s), 22 fonction(s).

## Vue d'ensemble

- **Classes principales** : ClassifierTrainer, DenseDetector, FeatureExtractor, ImageClassifier, Quantizer, SIFTDetector, SIFTExtractor
- **Fonctions principales** : __init__, _encodeLabels, _fit, build_arg_parser, classify, compute, detect, extract_feature_map, extract_image_features, getImageTag, get_centroids, get_feature_vector, load_input_map, normalize, quantize
- **Dépendances** : _pickle, argparse, create_features, cv2, json, numpy, os, sklearn, sklearn.cluster, sklearn.multiclass, sklearn.svm, sys

## Détail des fichiers

### `classify_data.py`

Module Python. Nombre de lignes: 42. Elements detectés: class ImageClassifier, def __init__, def getImageTag

**Classes** : ImageClassifier
**Fonctions** : __init__, getImageTag, build_arg_parser
**Dépendances** : os, sys, argparse, _pickle, cv2, numpy, create_features, training

### `create_features.py`

Module Python. Nombre de lignes: 158. Elements detectés: class DenseDetector, def __init__, def detect

**Classes** : DenseDetector, SIFTExtractor, Quantizer, FeatureExtractor
**Fonctions** : __init__, detect, compute, quantize, normalize, get_feature_vector, extract_image_features, get_centroids, build_arg_parser, load_input_map, extract_feature_map, resize_to_size
**Dépendances** : os, sys, argparse, _pickle, json, cv2, numpy, sklearn.cluster

### `feature_detector.py`

Module Python. Nombre de lignes: 40. Elements detectés: class DenseDetector, def __init__, def detect

**Classes** : DenseDetector, SIFTDetector
**Fonctions** : __init__, detect
**Dépendances** : sys, cv2, numpy

### `training.py`

Module Python. Nombre de lignes: 60. Elements detectés: class ClassifierTrainer, def __init__, def _fit

**Classes** : ClassifierTrainer
**Fonctions** : __init__, _fit, _encodeLabels, classify, build_arg_parser
**Dépendances** : os, sys, argparse, _pickle, numpy, sklearn.multiclass, sklearn.svm, sklearn
