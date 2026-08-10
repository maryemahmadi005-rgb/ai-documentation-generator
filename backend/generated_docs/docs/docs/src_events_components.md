# Module : src/events/components

6 fichier(s), 28 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : Survey, completeSurvey, fetchCookies, flushQueue, getColorModePreference, getEventData, getIsStaff, getMetaContent, getOctoClientId, getPerformance, getReferrer, getUserEventsId, initPageAndExitEvent, isHeadless, parseUserAgent
- **Dépendances** : ../types, ./Survey.module.scss, ./experiments/experiment, ./hydro-analytics, ./is-headless, ./user-agent, @/events/components/events, @/frame/components/Link, @/frame/components/hooks/useHasAccount, @/frame/components/lib/cookies, @/frame/components/ui/RenderedHTML/RenderedHTML, @/languages/components/useTranslation

## Détail des fichiers

### `Survey.tsx`

**Fonctions** : Survey, vote, submit, completeSurvey, getEventData, trackEvent
**Dépendances** : react, classnames, next/router, @primer/octicons-react, @/languages/components/useTranslation, @/frame/components/Link, @/events/components/events, ../types, ./Survey.module.scss, @/frame/components/ui/RenderedHTML/RenderedHTML

### `dotcom-cookies.ts`

Module TypeScript. Nombre de lignes: 72.

**Fonctions** : fetchCookies, getIsStaff
**Dépendances** : ./is-headless

### `events.ts`

Module TypeScript. Nombre de lignes: 404. Elements detectés: function scheduleNextFlush, function resetPageParams, function getMetaContent

**Fonctions** : scheduleNextFlush, resetPageParams, uuidv4, getUserEventsId, getMetaContent, flushQueue, queueEvent, getReferrer, getColorModePreference, getPerformance, trackScroll, sendPage, sendExit, initPageAndExitEvent, waitForPageReady
**Dépendances** : @/frame/components/lib/cookies, ./user-agent, next/router, @/frame/components/hooks/useHasAccount, ./experiments/experiment, ../types, ./is-headless, ./hydro-analytics

### `hydro-analytics.ts`

Module TypeScript. Nombre de lignes: 101.

**Fonctions** : getOctoClientId, prepareData, sendHydroAnalyticsEvent
**Dépendances** : ../types

### `is-headless.ts`

Module TypeScript. Nombre de lignes: 16.

**Fonctions** : isHeadless

### `user-agent.ts`

Module TypeScript. Nombre de lignes: 29.

**Fonctions** : parseUserAgent
