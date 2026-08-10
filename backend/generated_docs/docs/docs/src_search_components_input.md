# Module : src/search/components/input

7 fichier(s), 21 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : AskAIResults, SearchBarButton, SearchGroups, SearchOverlay, SearchOverlayContainer, aiSearchOptionOnSelect, fetchData, generalSearchResultOnSelect, handleClick, handleKeyDown, handleScroll, handleSearchQueryChange, item, onBackButton, performGeneralSearch
- **Dépendances** : ../helpers/execute-search-actions, ../helpers/fix-incomplete-markdown, ../hooks/useAISearchLocalStorageCache, ../hooks/useMultiQueryParams, ../types, ./AskAIResults, ./AskAIResults.module.scss, ./SearchBarButton.module.scss, ./SearchContext, ./SearchOverlay, ./SearchOverlay.module.scss, @/events/components/event-groups

## Détail des fichiers

### `AskAIResults.tsx`

**Fonctions** : AskAIResults, fetchData, processLine, sendAISearchResultEvent
**Dépendances** : react, lodash-es, ../helpers/execute-search-actions, next/router, @/languages/components/useTranslation, @primer/react, @primer/live-region-element, ../hooks/useAISearchLocalStorageCache, @/frame/components/ui/MarkdownContent/UnrenderedMarkdownContent, ./AskAIResults.module.scss, ../helpers/fix-incomplete-markdown, @/rest/components/useClipboard

### `README.md`

### `SearchBarButton.tsx`

**Fonctions** : SearchBarButton, handleClick, handleKeyDown
**Dépendances** : react, classnames, @primer/react, @primer/octicons-react, @/languages/components/useTranslation, @/search/components/hooks/useMultiQueryParams, ./SearchBarButton.module.scss

### `SearchContext.tsx`

**Fonctions** : useSearchContext
**Dépendances** : react, ../types, @/search/types

### `SearchGroups.tsx`

**Fonctions** : SearchGroups, item
**Dépendances** : @primer/react, ./AskAIResults, ./SearchContext, ./SearchOverlay.module.scss

### `SearchOverlay.tsx`

**Fonctions** : SearchOverlay, handleScroll, handleSearchQueryChange, generalSearchResultOnSelect, aiSearchOptionOnSelect, performGeneralSearch, referenceOnSelect, handleKeyDown, onBackButton, sendKeyboardEvent
**Dépendances** : react, classnames, next/router, @primer/react, @primer/octicons-react, @primer/behaviors, @/languages/components/useTranslation, @/versions/components/useVersion, @/search/components/hooks/useAISearchAutocomplete, @/events/components/events, @/events/types, @/events/components/event-groups

### `SearchOverlayContainer.tsx`

**Fonctions** : SearchOverlayContainer
**Dépendances** : react, ./SearchOverlay, ../hooks/useMultiQueryParams
