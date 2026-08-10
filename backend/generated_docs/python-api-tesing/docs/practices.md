# Module : practices

9 fichier(s), 4 classe(s), 38 fonction(s).

## Vue d'ensemble

- **Classes principales** : Pinger, flushfile
- **Fonctions principales** : __init__, checksum, doOnePing, do_checksum, draw_cloud, draw_house, draw_tree, draw_window, main, ping, ping_once, print_part, receiveOnePing, receive_pong, sendOnePing
- **Dépendances** : PIL, __future__, argparse, io, math, os, pygame, select, socket, struct, sys, time

## Détail des fichiers

### `TTS.py`

Module Python. Nombre de lignes: 27. Elements detectés: def text2Speech

**Fonctions** : text2Speech
**Dépendances** : win32com.client, tkinter

### `pil_merge.py`

Module Python. Nombre de lignes: 26.

**Dépendances** : math, PIL

### `ping.py`

Module Python. Nombre de lignes: 125. Elements detectés: class Pinger, def __init__, def do_checksum

**Classes** : Pinger
**Fonctions** : __init__, do_checksum, receive_pong, send_ping, ping_once, ping
**Dépendances** : os, argparse, socket, struct, select, time

### `ping2.py`

Module Python. Nombre de lignes: 141. Elements detectés: class Pinger, def __init__, def do_checksum

**Classes** : Pinger
**Fonctions** : __init__, do_checksum, receive_pong, send_ping, ping_once, ping
**Dépendances** : os, argparse, socket, struct, select, time

### `ping3.py`

Module Python. Nombre de lignes: 141. Elements detectés: class Pinger, def __init__, def do_checksum

**Classes** : Pinger
**Fonctions** : __init__, do_checksum, receive_pong, send_ping, ping_once, ping
**Dépendances** : os, argparse, socket, struct, select, time

### `pygame_house.py`

Module Python. Nombre de lignes: 58. Elements detectés: def draw_tree, def draw_house, def draw_window

**Fonctions** : draw_tree, draw_house, draw_window, draw_cloud
**Dépendances** : pygame

### `traceroute.py`

Module Python. Nombre de lignes: 62. Elements detectés: class flushfile, def __init__, def write

**Classes** : flushfile
**Fonctions** : __init__, write, main
**Dépendances** : socket, io, struct, sys

### `traceroute2.py`

Module Python. Nombre de lignes: 119. Elements detectés: def checksum, def receiveOnePing, def sendOnePing

**Fonctions** : checksum, receiveOnePing, sendOnePing, doOnePing, print_part, traceroute
**Dépendances** : __future__, socket, os, sys, struct, time, argparse

### `traceroute3.py`

Module Python. Nombre de lignes: 118. Elements detectés: def checksum, def receiveOnePing, def sendOnePing

**Fonctions** : checksum, receiveOnePing, sendOnePing, doOnePing, print_part, traceroute
**Dépendances** : __future__, socket, os, sys, struct, time, argparse
