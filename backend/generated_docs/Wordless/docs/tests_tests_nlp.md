# Module : tests/tests_nlp

14 fichier(s), 94 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : compare_context_matched, compare_ngrams_matched, compare_tokens_matched, init_search_settings, init_token_settings, test__get_pipelines_to_disable, test_char_tokenizers, test_check_models, test_check_search_settings, test_check_search_terms, test_check_text, test_check_texts, test_combine_texts_properties, test_dependency_parse, test_display_texts_to_tokens
- **Dépendances** : copy, os, pytest, re, tests, wordless.wl_dialogs, wordless.wl_nlp, wordless.wl_utils

## Détail des fichiers

### `test_dependency_parsing.py`

Module Python. Nombre de lignes: 199. Elements detectés: def test_dependency_parse, def wl_test_dependency_parse_models, def wl_test_dependency_parse_fig_models

**Fonctions** : test_dependency_parse, wl_test_dependency_parse_models, wl_test_dependency_parse_fig_models, test__get_pipelines_to_disable, test_wl_show_dependency_graphs, wl_test_dependency_parse_misc
**Dépendances** : pytest, tests, wordless.wl_nlp

### `test_lemmatization.py`

Module Python. Nombre de lignes: 329. Elements detectés: def test_lemmatize

**Fonctions** : test_lemmatize, wl_test_lemmatize_models, test_lemmatize_misc
**Dépendances** : pytest, tests, wordless.wl_nlp, wordless.wl_utils

### `test_matching.py`

Module Python. Nombre de lignes: 617. Elements detectés: def test_split_tag_embedded, def test_split_tag_nonembedded, def test_replace_wildcards_in_tag_name

**Fonctions** : test_split_tag_embedded, test_split_tag_nonembedded, test_replace_wildcards_in_tag_name, test_get_re_tags, test_get_re_tags_with_tokens, init_token_settings, init_search_settings, test_check_search_terms, test_check_search_settings, compare_tokens_matched, compare_ngrams_matched, compare_context_matched, test_match_tokens, test_match_ngrams, test_match_search_terms_tokens
**Dépendances** : re, tests, wordless.wl_nlp

### `test_nlp_utils.py`

Module Python. Nombre de lignes: 270. Elements detectés: def test_to_lang_util_code, def test_to_lang_util_codes, def test_to_lang_util_text

**Fonctions** : test_to_lang_util_code, test_to_lang_util_codes, test_to_lang_util_text, test_to_lang_util_texts, test_get_langs_stanza, test_check_models, test_wl_worker_download_model_spacy, test_wl_worker_download_model_stanza, test_init_model_spacy, test_init_model_stanza, test_init_sudachipy_word_tokenizer, test_init_sentence_tokenizers, test_init_word_tokenizers, test_init_syl_tokenizers, test_init_word_detokenizers
**Dépendances** : os, tests, wordless.wl_dialogs, wordless.wl_nlp, wordless.wl_utils

### `test_pos_tagging.py`

Module Python. Nombre de lignes: 251. Elements detectés: def test_to_content_function, def test_pos_tag

**Fonctions** : test_to_content_function, test_pos_tag, wl_test_pos_tag_models, test_pos_tag_universal, test_pos_tag_misc
**Dépendances** : copy, pytest, tests, wordless.wl_nlp, wordless.wl_utils

### `test_sentence_tokenization.py`

Module Python. Nombre de lignes: 447. Elements detectés: def test_sentence_tokenize

**Fonctions** : test_sentence_tokenize, wl_test_sentence_tokenize_models, test_sentence_terminators, test_sentence_split, test_sentence_seg_terminators, test_sentence_seg_tokenize, test_sentence_seg_tokenize_tokens, test_sentence_tokenize_misc
**Dépendances** : pytest, tests, wordless.wl_nlp

### `test_sentiment_analysis.py`

Module Python. Nombre de lignes: 101. Elements detectés: def test_sentiment_analyze, def wl_test_sentiment_analyze_models, def test_sentiment_analyze_misc

**Fonctions** : test_sentiment_analyze, wl_test_sentiment_analyze_models, test_sentiment_analyze_misc
**Dépendances** : pytest, tests, wordless.wl_nlp

### `test_stop_word_lists.py`

Module Python. Nombre de lignes: 51. Elements detectés: def test_get_stop_word_list, def test_filter_stop_words, def test_stop_word_lists_misc

**Fonctions** : test_get_stop_word_list, test_filter_stop_words, test_stop_word_lists_misc
**Dépendances** : pytest, tests, wordless.wl_nlp

### `test_syl_tokenization.py`

Module Python. Nombre de lignes: 218. Elements detectés: def test_syl_tokenize

**Fonctions** : test_syl_tokenize, test_syl_tokenize_misc
**Dépendances** : pytest, tests, wordless.wl_nlp

### `test_texts.py`

Module Python. Nombre de lignes: 112. Elements detectés: def test_check_text, def test_check_texts, def test_wl_token

**Fonctions** : test_check_text, test_check_texts, test_wl_token, test_to_tokens, test_display_texts_to_tokens, test_split_texts_properties, test_combine_texts_properties, test_to_token_texts, test_to_display_texts, test_set_token_text, test_set_token_texts, test_has_token_properties, test_get_token_properties, test_set_token_properties, test_update_token_properties
**Dépendances** : copy, tests, wordless.wl_nlp

### `test_token_processing.py`

Module Python. Nombre de lignes: 259. Elements detectés: def text_test, def test_text_pos_tag, def test_text_lemmatize

**Fonctions** : text_test, test_text_pos_tag, test_text_lemmatize, test_text_syl_tokenize, test_text_ignore_tags, test_text_use_tags_only, test_text_filter_stop_words, test_remove_empty_tokens, test_remove_empty_paras, test_wl_process_tokens, test_wl_process_tokens_ngram_generator, test_wl_process_tokens_profiler, test_wl_process_tokens_wordlist_generator, test_wl_process_tokens_colligation_extractor, test_wl_process_tokens_concordancer
**Dépendances** : tests, wordless.wl_nlp

### `test_word_detokenization.py`

Module Python. Nombre de lignes: 73. Elements detectés: def test_word_detokenize

**Fonctions** : test_word_detokenize
**Dépendances** : pytest, tests, wordless.wl_nlp, wordless.wl_utils

### `test_word_tokenization.py`

Module Python. Nombre de lignes: 377. Elements detectés: def test_word_tokenize

**Fonctions** : test_word_tokenize, wl_test_word_tokenize_models, test_char_tokenizers
**Dépendances** : pytest, tests, wordless.wl_nlp, wordless.wl_utils
