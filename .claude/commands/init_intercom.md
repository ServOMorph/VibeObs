---
description: Installe une messagerie inter-projets à file d'attente et gestion d'urgence
argument-hint: "<chemin_projet_cible>"
model: sonnet
---

# /init_intercom <chemin_projet_cible>

## Objectif

Installer le mécanisme générique `intercom` dans un projet initialisé. Il emploie des fichiers
append-only locaux : un message normal reste dans la file d'attente ; un message urgent est signalé
par une écoute persistante, sur le modèle du Monitor de `com_telephone`.

## Procédure

1. Résoudre la cible et vérifier `<cible>/.claude/zones.md`. Si `intercom/intercom.py` existe,
   ne rien écraser : proposer uniquement d'ajouter un destinataire absent.
2. Demander, une question à la fois, le nom stable du projet et chaque destinataire (alias + chemin
   absolu). Vérifier les chemins. Présenter le plan et demander une confirmation unique.
3. Copier sans modification `templates/intercom/intercom.py` et `README.md` vers
   `<cible>/intercom/`. Créer `<cible>/.intercom/config.json` depuis l'exemple, avec les valeurs
   validées. Ignorer `.intercom/` dans Git.
4. Ajouter au `AGENTS.md` cible l'obligation d'exécuter `python intercom/intercom.py inbox --urgent`
   avant toute réponse finale, clôture de tâche ou fin de session. Une urgence détectée est traitée
   avant la conclusion, avec `pause`, `ack` et `resume`. Copier ensuite
   `templates/intercom/intercom_listen.md` et `intercom_inbox.md` comme commandes locales.
   L'écoute lance
   `python intercom/intercom.py watch` dans un terminal persistant. Toute urgence impose :
   `pause` avec le travail réel, traitement, `ack`, lecture de `resume`, puis reprise. Un message
   normal reste en attente ou reçoit un `ack` après traitement.
5. Vérifier `python <cible>/intercom/intercom.py --help` et `... inbox`, sans envoyer de message
   de test dans une file réelle. Récapituler les alias et la commande `/intercom_listen`.
