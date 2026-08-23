---
description: Lit et traite la boîte intercom
model: haiku
---

# /intercom_inbox

Exécuter `python intercom/intercom.py inbox`. Les messages normaux restent en attente ou reçoivent
`ack <id>` après traitement. Pour toute urgence : `pause`, traitement, `ack <id>`, puis `resume` et
reprise du travail mémorisé.
