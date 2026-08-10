# Module : python3_libraries/opencv/opencv3by_example/Chapter11

4 fichier(s), 10 classe(s), 36 fonction(s).

## Vue d'ensemble

- **Classes principales** : ClassifierANN, DenseDetector, FeatureExtractor, ImageClassifier, Quantizer, SIFTExtractor
- **Fonctions principales** : __init__, _get_network_io, _init_confusion_matrix, build_arg_parser, classify, compute, detect, extract_feature_map, extract_image_features, getImageTag, get_centroids, get_confusion_matrix, get_description, get_feature_vector, get_optimized_image
- **Dépendances** : _pickle, argparse, collections, create_features, cv2, json, math, numpy, os, pickle, random, sklearn

## Détail des fichiers

### `classify_data.py`

Module Python. Nombre de lignes: 44. Elements detectés: class ImageClassifier, def __init__, def classify

**Classes** : ImageClassifier
**Fonctions** : __init__, classify, getImageTag, build_arg_parser
**Dépendances** : argparse, _pickle, cv2, numpy, create_features

### `create_features.py`

Module Python. Nombre de lignes: 156. Elements detectés: class DenseDetector, def __init__, def detect

**Classes** : DenseDetector, SIFTExtractor, Quantizer, FeatureExtractor
**Fonctions** : __init__, detect, compute, quantize, normalize, get_feature_vector, extract_image_features, get_centroids, build_arg_parser, load_input_map, extract_feature_map, resize_to_size
**Dépendances** : os, sys, argparse, _pickle, json, cv2, numpy, sklearn.cluster

### `feature_extractor.py`

Module Python. Nombre de lignes: 107. Elements detectés: class DenseDetector, def __init__, def detect

**Classes** : DenseDetector, SIFTExtractor, Quantizer, FeatureExtractor
**Fonctions** : __init__, detect, compute, get_description, quantize, normalize, get_feature_vector, get_centroids, get_optimized_image, build_arg_parser
**Dépendances** : argparse, _pickle, cv2, numpy, sklearn.cluster

### `training.py`

Module Python. Nombre de lignes: 131. Elements detectés: class ClassifierANN, def __init__, def train

**Classes** : ClassifierANN
**Fonctions** : __init__, train, get_confusion_matrix, classify, _get_network_io, _init_confusion_matrix, build_arg_parser, print_confusion_matrix, print_accuracy, split_feature_map
**Dépendances** : argparse, random, cv2, numpy, pickle, math, sklearn, collections
