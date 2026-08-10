# Module : src/tools/components

7 fichier(s), 2 classe(s), 16 fonction(s).

## Vue d'ensemble

- **Classes principales** : is, never
- **Fonctions principales** : Fields, InArticlePicker, Picker, PlatformPicker, SelectionProvider, ToggleableContent, ToolPicker, classifyToggleClass, getDefaultTool, isContentVisible, isToggleClass, noop, onClickChoice, toClassList, toggleVisibility
- **Dépendances** : ./Fields, ./Fields.module.scss, ./InArticlePicker, ./InArticlePicker.module.scss, ./Picker, ./Picker.module.scss, ./SelectionContext, @/events/components/events, @/events/components/user-agent, @/events/types, @/frame/components/context/ArticleContext, @/frame/components/lib/cookies

## Détail des fichiers

### `Fields.tsx`

**Fonctions** : Fields
**Dépendances** : @primer/react, react, classnames, ./Picker, ./Fields.module.scss

### `InArticlePicker.tsx`

**Fonctions** : InArticlePicker, toggleVisibility, onClickChoice
**Dépendances** : react, @/frame/components/lib/cookies, @primer/react, @/events/components/events, @/events/types, next/router, ./InArticlePicker.module.scss

### `Picker.tsx`

**Fonctions** : Picker
**Dépendances** : react, @primer/react, @primer/behaviors, ./Fields, ./Picker.module.scss

### `PlatformPicker.tsx`

**Fonctions** : PlatformPicker
**Dépendances** : react, @/frame/components/context/ArticleContext, @/events/components/user-agent, ./InArticlePicker, ./SelectionContext, @/frame/lib/constants

### `SelectionContext.tsx`

**Classes** : is, never
**Fonctions** : noop, SelectionProvider, useSelection, toClassList, classifyToggleClass, isToggleClass, isContentVisible
**Dépendances** : react, @/tools/lib/all-platforms, @/tools/lib/all-tools

### `ToggleableContent.tsx`

**Fonctions** : ToggleableContent
**Dépendances** : react

### `ToolPicker.tsx`

**Fonctions** : getDefaultTool, ToolPicker
**Dépendances** : @/frame/components/context/ArticleContext, ./InArticlePicker, ./SelectionContext, @/frame/lib/constants
