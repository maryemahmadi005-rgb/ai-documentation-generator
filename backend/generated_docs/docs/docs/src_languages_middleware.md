# Module : src/languages/middleware

1 fichier(s), 7 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : detectLanguage, getLanguageCode, getLanguageCodeFromHeader, getLanguageCodeFromPath, getUserLanguage, getUserLanguageFromCookie, translationExists
- **Dépendances** : @/frame/lib/constants, @/languages/lib/languages-server, @/observability/logger/lib/logger-context, @/types, accept-language-parser, express

## Détail des fichiers

### `detect-language.ts`

Module TypeScript. Nombre de lignes: 68. Elements detectés: function translationExists, function getLanguageCode, function getUserLanguage

**Fonctions** : translationExists, getLanguageCode, getUserLanguage, getUserLanguageFromCookie, getLanguageCodeFromPath, getLanguageCodeFromHeader, detectLanguage
**Dépendances** : express, accept-language-parser, @/languages/lib/languages-server, @/frame/lib/constants, @/types, @/observability/logger/lib/logger-context
