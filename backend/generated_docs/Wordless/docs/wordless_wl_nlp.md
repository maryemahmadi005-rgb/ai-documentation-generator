# Module : wordless/wl_nlp

14 fichier(s), 6 classe(s), 90 fonction(s).

## Vue d'ensemble

- **Classes principales** : Wl_Text, Wl_Text_Ref, Wl_Text_Total, Wl_Token, Wl_Worker_Download_Model_Spacy, Wl_Worker_Download_Model_Stanza
- **Fonctions principales** : __eq__, __hash__, __init__, __new__, _get_pipelines_to_disable, _to_lang_util_text, check_context, check_models, check_search_settings, check_search_terms, check_text, check_texts, combine_texts_properties, display_text, display_texts_to_tokens
- **Dépendances** : PyQt5, bisect, botok, bs4, collections, copy, html, importlib, itertools, khmernltk, laonlp, nltk

## Détail des fichiers

### `wl_dependency_parsing.py`

Module Python. Nombre de lignes: 538. Elements detectés: def wl_dependency_parse, def wl_dependency_parse_text

**Fonctions** : wl_dependency_parse, wl_dependency_parse_text, wl_dependency_parse_tokens, wl_dependency_parse_fig, _get_pipelines_to_disable, to_displacy_sentence, wl_dependency_parse_fig_text, wl_dependency_parse_fig_tokens, wl_show_dependency_graphs
**Dépendances** : bisect, os, shutil, subprocess, webbrowser, PyQt5, spacy, wordless.wl_checks, wordless.wl_dialogs, wordless.wl_nlp, wordless.wl_settings, wordless.wl_utils

### `wl_lemmatization.py`

Module Python. Nombre de lignes: 309. Elements detectés: def wl_lemmatize, def wl_lemmatize_text

**Fonctions** : wl_lemmatize, wl_lemmatize_text, wl_lemmatize_tokens
**Dépendances** : nltk, PyQt5, simplemma, spacy, wordless.wl_nlp, wordless.wl_utils

### `wl_matching.py`

Module Python. Nombre de lignes: 392. Elements detectés: def split_tag_embedded, def split_tag_nonembedded, def replace_wildcards_in_tag_name

**Fonctions** : split_tag_embedded, split_tag_nonembedded, replace_wildcards_in_tag_name, get_re_tags, get_re_tags_with_tokens, check_search_terms, check_search_settings, match_tokens, match_ngrams, match_search_terms_tokens, match_search_terms_ngrams, match_search_terms_context, check_context
**Dépendances** : copy, itertools, re, PyQt5, wordless.wl_nlp

### `wl_nlp_utils.py`

Module Python. Nombre de lignes: 880. Elements detectés: def to_lang_util_code, def to_lang_util_codes, def _to_lang_util_text

**Classes** : Wl_Worker_Download_Model_Spacy, Wl_Worker_Download_Model_Stanza
**Fonctions** : to_lang_util_code, to_lang_util_codes, _to_lang_util_text, to_lang_util_text, to_lang_util_texts, get_langs_stanza, check_models, update_gui_stanza, __init__, run, init_model_spacy, init_model_stanza, init_sudachipy_word_tokenizer, init_sentence_tokenizers, init_word_tokenizers
**Dépendances** : collections, html, importlib, itertools, os, pathlib, re, shutil, sys, traceback, zipfile, botok

### `wl_pos_tagging.py`

Module Python. Nombre de lignes: 478. Elements detectés: def to_content_function, def wl_pos_tag

**Fonctions** : to_content_function, wl_pos_tag, wl_pos_tag_universal, wl_pos_tag_text, wl_pos_tag_tokens
**Dépendances** : copy, re, khmernltk, laonlp, nltk, PyQt5, pythainlp, spacy, underthesea, wordless.wl_nlp, wordless.wl_utils

### `wl_sentence_tokenization.py`

Module Python. Nombre de lignes: 306. Elements detectés: def wl_sentence_tokenize

**Fonctions** : wl_sentence_tokenize, wl_sentence_split, wl_sentence_seg_tokenize, wl_sentence_seg_tokenize_tokens
**Dépendances** : re, botok, khmernltk, laonlp, nltk, pythainlp, underthesea, wordless.wl_nlp, wordless.wl_utils

### `wl_sentiment_analysis.py`

Module Python. Nombre de lignes: 112. Elements detectés: def wl_sentiment_analyze, def wl_sentiment_analyze_text, def wl_sentiment_analyze_tokens

**Fonctions** : wl_sentiment_analyze, wl_sentiment_analyze_text, wl_sentiment_analyze_tokens
**Dépendances** : collections, underthesea, vaderSentiment.vaderSentiment, wordless.wl_nlp, wordless.wl_utils

### `wl_stop_word_lists.py`

Module Python. Nombre de lignes: 117. Elements detectés: def wl_get_stop_word_list

**Fonctions** : wl_get_stop_word_list, wl_filter_stop_words
**Dépendances** : importlib, laonlp, nltk, opencc, pythainlp, wordless.wl_nlp, wordless.wl_utils

### `wl_syl_tokenization.py`

Module Python. Nombre de lignes: 113. Elements detectés: def wl_syl_tokenize, def wl_syl_tokenize_text, def wl_syl_tokenize_tokens

**Fonctions** : wl_syl_tokenize, wl_syl_tokenize_text, wl_syl_tokenize_tokens
**Dépendances** : re, pythainlp, wordless.wl_nlp, wordless.wl_utils

### `wl_texts.py`

Module Python. Nombre de lignes: 580. Elements detectés: def check_text, def check_texts, class Wl_Token

**Classes** : Wl_Token, Wl_Text, Wl_Text_Ref, Wl_Text_Total
**Fonctions** : check_text, check_texts, __new__, __init__, __hash__, __eq__, display_text, update_properties, to_tokens, display_texts_to_tokens, split_texts_properties, combine_texts_properties, to_token_texts, to_display_texts, set_token_text
**Dépendances** : copy, os, re, bs4, PyQt5, wordless.wl_nlp, wordless.wl_utils

### `wl_token_processing.py`

Module Python. Nombre de lignes: 358. Elements detectés: def text_pos_tag, def text_lemmatize, def text_syl_tokenize

**Fonctions** : text_pos_tag, text_lemmatize, text_syl_tokenize, text_ignore_tags, text_use_tags_only, text_filter_stop_words, remove_empty_tokens, remove_empty_paras, wl_process_tokens, wl_process_tokens_ngram_generator, wl_process_tokens_profiler, wl_process_tokens_wordlist_generator, wl_process_tokens_colligation_extractor, wl_process_tokens_concordancer, wl_process_tokens_dependency_parser
**Dépendances** : copy, wordless.wl_checks, wordless.wl_nlp, wordless.wl_utils

### `wl_word_detokenization.py`

Module Python. Nombre de lignes: 117. Elements detectés: def wl_word_detokenize

**Fonctions** : wl_word_detokenize
**Dépendances** : re, pythainlp, wordless.wl_checks, wordless.wl_nlp, wordless.wl_utils

### `wl_word_tokenization.py`

Module Python. Nombre de lignes: 253. Elements detectés: def wl_word_tokenize

**Fonctions** : wl_word_tokenize, wl_word_tokenize_flat
**Dépendances** : re, botok, khmernltk, laonlp, pythainlp, sudachipy, underthesea, wordless.wl_checks, wordless.wl_nlp, wordless.wl_utils
