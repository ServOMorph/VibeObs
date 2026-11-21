---
type: guide
description: Initialiser le protocole vibecoding dans un projet avec /init_projet
tags: guide, init, init_projet
maj: 2026-11-21
---

# Initialiser un projet

Commande : `/init_projet <chemin vers le projet>` — s'exécute depuis le kit. Références : [`../../README.md`](../../README.md) (démarrage rapide) et [`../../_docs/protocole_vibecoding.md`](../../_docs/protocole_vibecoding.md) (section /init).

## Déroulé

1. Claude pose les questions d'initialisation : alias (le nom du dossier projet est proposé par
   défaut), objectif, git, première zone ou zone supplémentaire, données sensibles, AGENTS.md,
   GEMINI.md, puis ajout éventuel d'agents. La stack n'est plus demandée (v6.0) : le champ « Stack »
   de `contexte.md` s'initialise à « Non définie à la création » et se complète au fil du projet
2. Projet sans git : question complémentaire sur le backup miroir Google Drive (rclone) à chaque /close ;
   si oui, choix ou connexion du remote (un remote dédié par projet par défaut, contrôle anti-collision
   sur le registre « Remotes rclone » de `DEPLOYMENTS.md`)
3. Copie les templates, crée ou complète le `.gitignore` de sécurité, remplace les placeholders
   (remplacement littéral par script Python, jamais par regex), contrôle qu'aucun `{{` ne subsiste et
   que `{{RACINE}}` est un chemin Windows valide
4. Si backup rclone : branche `backup_project.py` dans le bloc `SPECIFICITES PROJET` de `close.md`
5. Projet sous git : commit initial `init: protocole vibecoding — zone <alias>` (`git init` d'abord si
   le dépôt est absent)
6. Si l'utilisateur le demande (Q9), enchaîne dans la même exécution sur `/create_agent`, après
   l'initialisation complète du projet (seule commande d'agents proposée : `/create_team` a été supprimé)
7. Enregistre le déploiement dans `DEPLOYMENTS.md` (registre hors git), puis liste les fichiers écrits

La racine du projet cible est l'argument — jamais demandée.

## Placeholders remplacés

| Placeholder | Valeur |
|---|---|
| `{{ALIAS}}` | Alias court de la zone |
| `{{RACINE}}` | Chemin absolu de la racine du projet |
| `{{OBJECTIF}}` | Objectif du projet, 1-2 phrases |
| `{{DATE}}` | Date du jour, AAAA-MM-JJ |
| `{{RCLONE_REMOTE}}`, `{{NOM_PROJET}}` | Remote retenu et nom du dossier projet, seulement dans `rclone_backup.json` |

## Fichiers déployés

Depuis `templates/` : `.claude/CLAUDE.md`, `zones.md`, commands/ (start, close, create_memory, telephone), `_contexte/` (contexte.md, signals.md), `ollama_call.py` ; avec backup rclone : `backup_project.py` et `rclone_backup.json`. Depuis le kit : `Protocole_start_close_context.md` → `_docs/protocole_vibecoding.md`. Sur confirmation : `AGENTS.md`, `GEMINI.md` (agents non-Claude). `.gitignore` créé ou complété (`.env`, `.env.*` sauf `.env.example`, `*.key`, `*.pem`, `credentials*.json`, `*token*.json`, `*.token`, `.claude/settings.local.json`, `**/_contexte/journal_session.md`). `roadmap_TEMPLATE.md` et `agent_role_TEMPLATE.md` ne sont pas copiés à l'init.

La réponse sur les données sensibles remplace `Aucun déclaré.` dans `CLAUDE.md` § Données sensibles ; si elle est négative, la ligne reste.

## Cas particuliers

- **Projet sans git** : pas de commit ; la traçabilité repose sur la section "Dernière session" de signals.md
- **Multi-zones** : start.md, close.md, zones.md partagés — une ligne par zone, pas de duplication de fichiers
- **Init d'une zone supplémentaire** : ajout d'une ligne dans zones.md, pas de re-copie du protocole

## Mise à jour ultérieure

`/update <chemin>` ou `/update all` : met à jour les fichiers de protocole d'un projet déjà initialisé sans toucher `_contexte/`, `zones.md`, ni la section "Spécificités projet" de CLAUDE.md. `init_projet.md` et `update.md` ne sont pas déployés dans les projets — ils restent dans le kit.
