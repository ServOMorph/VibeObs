# Contexte — VibeObs

## Objectif (immuable sauf décision explicite)
Fournir un kit reproductible pour gérer le vibecoding sur des projets multi-sessions, avec contexte persistant via `/start`/`/close` et support multi-zones.

## Stack / contraintes techniques
- **Langage** : Markdown + Bash/PowerShell pour scripts
- **Framework** : Claude Code CLI + Agent SDK
- **Gestion git** : commits automatiques depuis `/close`
- **Modèles recommandés** : Haiku (start), Sonnet (close), Opus (plans/debug)
- **Intégration** : Ollama pour tâches sensibles/templated
- **Déploiement** : copie template vers projets via `/init`, tracking dans DEPLOYMENTS.md

## État actuel
- 2026-09-04 : le kit et son dépôt GitHub sont renommés VibeObs ; chemins locaux, zones, URLs et backup interne alignés. Kit v5.0.
- 2026-09-04 : `/create_projet` remplace `/create_projet_public` : dépôt Git local ou GitHub public/privé, templates optionnels après `/init_projet`.
- 2026-09-04 : `rclone_backup` devient un template avec remote Google Drive explicite ; template `netlify` ajouté.
- 2026-09-04 : le template `discord_com` ne déduplique plus à la seconde ; `notify` attend la prise en charge du bot. Tests isolés passants, test Discord réel en attente d’autorisation système.
- 2026-09-04 : la base `DOCUMENTATION/` dispose d'un contrôle mécanique (`check_docs.py`) exécuté par `/doc_sync`.

## Décisions structurantes
_Décisions antérieures au 2026-08-20 archivées dans `_contexte/archive_decisions.md`._
- 2026-09-04 : `discord_com` ne déduplique pas les sorties sur un timestamp à la seconde ; l’état de la file est l’unique garde contre le renvoi. `notify` attend l’ack du bot afin de sérialiser les notifications consécutives. Le Bot Token reste exclusivement dans `.env` local gitignoré.
- 2026-09-04 : le kit est renommé VibeObs. La commande `/create_projet` remplace `/create_projet_public` et couvre Git local ou GitHub public/privé ; les sauvegardes rclone sont distribuées comme template avec un remote explicite.
- 2026-09-04 : une roadmap achevée déclenche une proposition d'archivage à l'utilisateur ; l'archivage reste soumis à son accord explicite. Règle ajoutée au protocole et à sa documentation de session.
- 2026-09-03 : `/create_agent` propose systématiquement l'insertion du template `discord_com` pour un agent Discord (défaut oui, config renvoyée à `/init_discord_mode`). Le Bot Token (`DISCORD_BOT_TOKEN`) est distingué explicitement de l'Application ID / Public Key / Client Secret partout dans la doc Discord. Correctif du template `discord_com` : `queue.json` repasse à `idle` après un envoi non interactif (fin du bug « un message Discord sur deux avalé »), `WAIT_TIMEOUT` de `discord_loop.py` porté à 110 s (moins de tours de modèle à vide). Non testé en conditions réelles.
- 2026-08-31 : `/create_projet_public` est une commande `.claude/commands/` (pas un skill `skills/`), de la même famille que `/init_projet`/`/create_agent`, invoquée explicitement. Le dossier parent des nouveaux projets vit dans `.env` (`PROJETS_PARENT_DIR`, gitignoré) avec `.env.example` versionné ; la commande s'arrête proprement si `.env` est absent ou la clé vide. Elle crée un dépôt GitHub **public** via `gh` sur le compte connecté, puis enchaîne `/init_projet`.
- 2026-08-31 : `Roberto2` acté définitivement supprimé. `roadmap_com_agents.md` Phase 2 est repointée sur `D:\ServOMorph\Meuniers` (pas de `statut.md` ad hoc à convertir sur ce pilote). `roadmap_messages_zones.md` Phase 1 mise en pause, choix du pilote de remplacement et fusion éventuelle avec `roadmap_com_agents.md` reportés.
- 2026-08-29 : `templates/roberto/` supprimé du kit (plus d'usage identifié, demande explicite utilisateur) — plus aucun template `roberto` disponible pour `/insert_template`. Son launcher `MACROS/`/`UI_WEB/` (pywebview, macros PC, capture écran, communication OpenCode) et `roadmap_workflow_quotidien.md` (Phases 3-5 ouvertes), sans équivalent dans `D:\ServOMorph\Roberto` (source `Roberto2` disparue du disque), déplacés vers ce projet plutôt que perdus — note laissée dans son `_contexte/signals.md`. `roadmap_template_roberto.md` archivée (`_archives/`, 5/5 phases FAIT).
- 2026-08-23 : une équipe d'agents est toujours représentée par un coordinateur dans son propre dossier ; son `team.md` est le manifeste des membres directs et son alias est hiérarchique. Les messages et statuts ne circulent qu'entre un parent et ses enfants directs, sans communication latérale.
- 2026-08-23 : Intercom est indépendant de Claude Code et sert de protocole partagé par Codex, Claude Code ou un autre agent. Les urgences sont relevées aux points de contrôle de l'agent ; un processus externe ne peut pas interrompre un appel d'outil déjà en cours.
