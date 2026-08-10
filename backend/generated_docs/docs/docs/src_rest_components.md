# Module : src/rest/components

15 fichier(s), 33 fonction(s).

## Vue d'ensemble

- **Fonctions principales** : ApiVersionPicker, ClientSideRedirectExceptions, ClientSideRedirects, FineGrainedAccess, NoFineGrainedAccess, RestAuth, RestBanner, RestCodeSamples, RestMethod, RestOperation, RestPreviewNotice, RestRedirect, RestReferencePage, RestStatusCodes, arrayTransform
- **Dépendances** : ./RestAuth, ./RestCodeSamples, ./RestCodeSamples.module.scss, ./RestOperation, ./RestPreviewNotice, ./RestStatusCodes, ./types, @/automated-pipelines/components/AutomatedPageContext, @/automated-pipelines/components/parameter-table/ParameterTable, @/frame/components/DefaultLayout, @/frame/components/HighlightedCode, @/frame/components/Link

## Détail des fichiers

### `ApiVersionPicker.tsx`

**Fonctions** : rememberApiVersion, ApiVersionPicker
**Dépendances** : next/router, @/frame/components/lib/cookies, @primer/octicons-react, @/frame/components/context/MainContext, @/versions/components/useVersion, @/tools/components/Picker, @/languages/components/useTranslation, @/frame/lib/constants, @/rest/lib/config

### `ClientSideRedirectExceptions.tsx`

**Fonctions** : ClientSideRedirectExceptions, getRedirect
**Dépendances** : react, next/router

### `ClientSideRedirects.tsx`

**Fonctions** : ClientSideRedirects
**Dépendances** : react, next/dynamic, next/router

### `RestAuth.tsx`

**Fonctions** : RestAuth, NoFineGrainedAccess, FineGrainedAccess
**Dépendances** : next/router, @/languages/components/useTranslation, @/versions/components/useVersion, @/frame/components/Link, ./types, @/frame/components/ui/RenderedHTML/RenderedHTML

### `RestBanner.tsx`

**Fonctions** : RestBanner
**Dépendances** : react, @primer/react, next/router, @/versions/components/useVersion, @/frame/components/Link, @/frame/components/context/MainContext, @/languages/components/useTranslation, @/frame/components/ui/RenderedHTML/RenderedHTML

### `RestCodeSamples.tsx`

**Fonctions** : getLanguageHighlight, RestCodeSamples, handleExampleSelection, handleResponseSelection, handleLanguageSelection
**Dépendances** : react, @primer/react, @primer/octicons-react, @primer/live-region-element, @/frame/components/lib/cookies, classnames, @/rest/lib/code-example-utils, @/languages/components/useTranslation, @/rest/components/useClipboard, @/frame/lib/constants, @/frame/components/HighlightedCode, ./RestCodeSamples.module.scss

### `RestMethod.tsx`

**Fonctions** : RestMethod
**Dépendances** : classnames, ./RestCodeSamples.module.scss, @/frame/components/ui/RenderedHTML/RenderedHTML

### `RestOperation.tsx`

**Fonctions** : RestOperation
**Dépendances** : react, next/router, github-slugger, classnames, @/frame/components/article/HeadingLink, @/languages/components/useTranslation, ./RestPreviewNotice, @/automated-pipelines/components/parameter-table/ParameterTable, ./RestCodeSamples, ./RestStatusCodes, ./RestAuth, ./types

### `RestPreviewNotice.tsx`

**Fonctions** : RestPreviewNotice
**Dépendances** : @/frame/components/ui/Alert

### `RestRedirect.tsx`

**Fonctions** : RestRedirect
**Dépendances** : react, next/router, @/frame/components/lib/cookies, @/versions/components/useVersion, @/frame/components/context/MainContext, @/frame/lib/constants

### `RestReferencePage.tsx`

**Fonctions** : RestReferencePage
**Dépendances** : react, @/frame/components/DefaultLayout, @/frame/components/ui/MarkdownContent, @/frame/components/ui/Lead, @/frame/components/ui/PermissionsStatement, ./RestOperation, @/automated-pipelines/components/AutomatedPageContext, ./types, @/rest/components/ClientSideRedirects, @/rest/components/RestRedirect

### `RestStatusCodes.tsx`

**Fonctions** : RestStatusCodes
**Dépendances** : @/languages/components/useTranslation, ./types, @/frame/components/ui/RenderedHTML/RenderedHTML

### `get-rest-code-samples.ts`

Module TypeScript. Nombre de lignes: 458. Elements detectés: function shouldOmitAuthentication, function escapeShellValue

**Fonctions** : shouldOmitAuthentication, escapeShellValue, getShellExample, getGHExample, hasNestedArrays, handleSingleParameter, arrayTransform, handleObjectParameter, getJSExample, findMatchingQueryKey, getRequiredQueryParamsPath, getAcceptHeader
**Dépendances** : url-template, javascript-stringify, @/rest/components/types, @/frame/components/context/MainContext, @octokit/auth-oauth-app

### `types.ts`

Module TypeScript. Nombre de lignes: 99.

### `useClipboard.ts`

Module TypeScript. Nombre de lignes: 36.

**Fonctions** : useCopyClipboard
**Dépendances** : react
