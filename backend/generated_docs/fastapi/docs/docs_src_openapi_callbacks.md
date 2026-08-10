# Module : docs_src/openapi_callbacks

2 fichier(s), 3 classe(s), 2 fonction(s).

## Vue d'ensemble

- **Classes principales** : Invoice, InvoiceEvent, InvoiceEventReceived
- **Fonctions principales** : create_invoice, invoice_notification
- **Dépendances** : fastapi, pydantic
- **Endpoints API** : /invoices/, {$callback_url}/invoices/{$request.body.id}

## Détail des fichiers

### `tutorial001_py310.py`

Module Python. Nombre de lignes: 35. Elements detectés: class Invoice, class InvoiceEvent, class InvoiceEventReceived

**Classes** : Invoice, InvoiceEvent, InvoiceEventReceived
**Fonctions** : invoice_notification, create_invoice
**Dépendances** : fastapi, pydantic
**API** : {$callback_url}/invoices/{$request.body.id}, /invoices/
