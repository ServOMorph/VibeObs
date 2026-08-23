# Intercom

Messagerie locale inter-projets : `.intercom/inbox.jsonl` est une file append-only. Les messages
normaux attendent ; les urgences exigent un `pause` avant traitement, puis `ack` et `resume`.

L'installation doit aussi ajouter à `AGENTS.md` une règle de contrôle `inbox --urgent` avant chaque
réponse finale ou clôture de tâche. Ainsi une urgence est traitée automatiquement dès la fin de la
tâche active, sans tenter d'interrompre un appel d'outil en cours.
