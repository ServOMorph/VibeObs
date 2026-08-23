---
type: guide
description: Messagerie locale Intercom entre projets, avec file d'attente et urgences
tags: guide, communication, urgence, intercom
maj: 2026-08-23
---

# Messagerie inter-projets

`/init_intercom <chemin_projet_cible>` installe Intercom. Chaque projet possède une boîte
append-only `.intercom/inbox.jsonl`; `intercom.py` écrit directement dans celle du destinataire
déclaré dans sa configuration locale.

Les messages `normal` restent en attente. L'écoute `/intercom_listen` reprend le principe du
Monitor de `com_telephone` : surveiller le fichier, pas la mémoire de session. Pour un message
`urgent`, l'agent exécute d'abord `pause`, le traite, fait `ack`, lit `resume`, puis reprend.
L'interruption s'applique au prochain point de contrôle de l'IA : aucun script ne peut interrompre
un appel d'outil déjà lancé.
