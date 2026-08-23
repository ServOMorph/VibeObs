---
description: Surveille les messages inter-projets entrants
model: haiku
---

# /intercom_listen

Lancer `python intercom/intercom.py watch` dans un terminal persistant et surveiller sa sortie.
À chaque `NOUVEAU_MESSAGE`, lire `python intercom/intercom.py inbox`.

- Message `normal` : le laisser dans la file ou le traiter ; une fois traité, exécuter `ack <id>`.
- Message `urgent` : avant toute autre action, exécuter `pause` avec la tâche, sa prochaine action
  et le contexte réellement en cours. Traiter l'urgence, faire `ack <id>`, lire `resume` et reprendre.
