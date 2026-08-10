# Module : scripts

13 fichier(s), 29 classe(s), 75 fonction(s).

## Vue d'ensemble

- **Classes principales** : AddCommentData, AddCommentResponse, AddDiscussionComment, CodeIncludeInfo, Comment, CommentsEdge, HTMLLinkAttribute, HeaderPermalinkInfo, HtmlLinkInfo, LabelSettings, LinkData, MarkdownLinkInfo
- **Fonctions principales** : __init__, _add_lang_code_to_url, _construct_html_link, _construct_markdown_link, add_markdown_notice, build_lang, bump_version, callback, commands_json, complete_existing_lang, create_comment, current_version, extract_code_includes, extract_header_permalinks, extract_html_links
- **Dépendances** : collections, collections.abc, datetime, doc_parsing_utils, functools, git, github, github.PullRequestReview, html.parser, http.server, httpx, json

## Détail des fichiers

### `add_latest_release_date.py`

Module Python. Nombre de lignes: 28. Elements detectés: def main

**Fonctions** : main
**Dépendances** : re, sys, datetime

### `deploy_docs_status.py`

Module Python. Nombre de lignes: 131. Elements detectés: class Settings, class LinkData, def main

**Classes** : Settings, LinkData
**Fonctions** : main
**Dépendances** : logging, re, typing, github, pydantic, pydantic_settings

### `doc_parsing_utils.py`

Module Python. Nombre de lignes: 595. Elements detectés: class CodeIncludeInfo, class HeaderPermalinkInfo, class MarkdownLinkInfo

**Classes** : CodeIncludeInfo, HeaderPermalinkInfo, MarkdownLinkInfo, HTMLLinkAttribute, HtmlLinkInfo, MultilineCodeBlockInfo
**Fonctions** : extract_code_includes, replace_code_includes_with_placeholders, replace_placeholders_with_code_includes, extract_header_permalinks, remove_header_permalinks, replace_header_permalinks, extract_markdown_links, _add_lang_code_to_url, _construct_markdown_link, replace_markdown_links, extract_html_links, _construct_html_link, replace_html_links, get_code_block_lang, extract_multiline_code_blocks
**Dépendances** : re, typing

### `docs.py`

Module Python. Nombre de lignes: 795. Elements detectés: def strip_markdown_links, class VisibleTextExtractor, def __init__

**Classes** : VisibleTextExtractor
**Fonctions** : strip_markdown_links, __init__, handle_data, extract_visible_text, slugify, get_en_config, get_lang_paths, lang_callback, complete_existing_lang, callback, new_lang, build_lang, split_markdown_header, add_markdown_notice, is_non_translated_path
**Dépendances** : json, logging, os, re, shutil, subprocess, html.parser, http.server, multiprocessing, pathlib, typing, typer

### `general-llm-prompt.md`

Source file. Nombre de lignes: 340.

### `label_approved.py`

Module Python. Nombre de lignes: 51. Elements detectés: class LabelSettings, class Settings

**Classes** : LabelSettings, Settings
**Dépendances** : logging, typing, github, github.PullRequestReview, pydantic, pydantic_settings

### `lint.sh`

Source file. Nombre de lignes: 7.

### `notify_translations.py`

Module Python. Nombre de lignes: 351. Elements detectés: class Comment, class UpdateDiscussionComment, class UpdateCommentData

**Classes** : Comment, UpdateDiscussionComment, UpdateCommentData, UpdateCommentResponse, AddDiscussionComment, AddCommentData, AddCommentResponse, CommentsEdge
**Fonctions** : get_graphql_response, get_graphql_translation_discussions, get_graphql_translation_discussion_comments_edges, get_graphql_translation_discussion_comments, create_comment, update_comment, main
**Dépendances** : logging, random, sys, time, pathlib, typing, httpx, github, pydantic, pydantic_settings

### `prepare_release.py`

Module Python. Nombre de lignes: 184. Elements detectés: def parse_version, def get_current_version, def bump_version

**Fonctions** : parse_version, get_current_version, bump_version, update_version_file, update_release_notes, get_release_notes_body, prepare, current_version, release_notes
**Dépendances** : re, datetime, pathlib, typing, typer

### `sponsors.py`

Module Python. Nombre de lignes: 181. Elements detectés: class SponsorEntity, class Tier, class SponsorshipAsMaintainerNode

**Classes** : SponsorEntity, Tier, SponsorshipAsMaintainerNode, SponsorshipAsMaintainerEdge, SponsorshipAsMaintainer, SponsorsUser, SponsorsResponseData, SponsorsResponse
**Fonctions** : get_graphql_response, get_graphql_sponsor_edges, get_individual_sponsors, update_content, main
**Dépendances** : logging, secrets, subprocess, collections, pathlib, typing, httpx, yaml, github, pydantic, pydantic_settings

### `topic_repos.py`

Module Python. Nombre de lignes: 70. Elements detectés: class Settings, class Repo, def main

**Classes** : Settings, Repo
**Fonctions** : main
**Dépendances** : logging, secrets, subprocess, pathlib, yaml, github, pydantic, pydantic_settings

### `translate.py`

Module Python. Nombre de lignes: 430. Elements detectés: def get_langs, def generate_lang_path, def generate_en_path

**Fonctions** : get_langs, generate_lang_path, generate_en_path, get_prompt, translate_page, iter_all_en_paths, iter_en_paths_to_translate, translate_lang, get_llm_translatable, list_llm_translatable, llm_translatable_json, commands_json, list_removable, list_all_removable, remove_removable
**Dépendances** : json, secrets, subprocess, collections.abc, functools, os, pathlib, typing, git, typer, yaml, doc_parsing_utils

### `translation_fixer.py`

Module Python. Nombre de lignes: 103. Elements detectés: def callback, def iter_all_lang_paths, def get_all_paths

**Fonctions** : callback, iter_all_lang_paths, get_all_paths, process_one_page, fix_all, fix_pages
**Dépendances** : os, collections.abc, pathlib, typing, typer, scripts.doc_parsing_utils
