# Contexte — claude-vibecoding-kit

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
- 2026-09-03 : correctif template `discord_com` (perte d'un message sur deux + latence à vide du bot) et guidage Bot Token renforcé (`init_discord_mode.md` étape 8 + docs template) ; `/create_agent` propose l'insertion du template pour un agent Discord. Kit v4.3.
- 2026-08-31 : `/create_projet_public` (projet vierge : dossier sous `PROJETS_PARENT_DIR` de `.env` + dépôt GitHub public + `/init_projet`). Premier usage réel : `Stop_Motion_IA`.
- 2026-08-23 : équipes hiérarchiques d'agents (`/create_team`, `parent=<alias>`) et Intercom (`/init_intercom`, `/intercom_inbox`, `/intercom_listen`) — validés sur le seul pilote `Meuniers` (équipe `COMMUNICATION` + agent `DOCUMENTATION`).
- `Roberto2` acté supprimé — `roadmap_com_agents.md` Phase 2 repointée sur `Meuniers`, `roadmap_messages_zones.md` Phase 1 en pause.

## Décisions structurantes
_Décisions antérieures au 2026-08-20 archivées dans `_contexte/archive_decisions.md`._
- 2026-09-03 : `/create_agent` propose systématiquement l'insertion du template `discord_com` pour un agent Discord (défaut oui, config renvoyée à `/init_discord_mode`). Le Bot Token (`DISCORD_BOT_TOKEN`) est distingué explicitement de l'Application ID / Public Key / Client Secret partout dans la doc Discord. Correctif du template `discord_com` : `queue.json` repasse à `idle` après un envoi non interactif (fin du bug « un message Discord sur deux avalé »), `WAIT_TIMEOUT` de `discord_loop.py` porté à 110 s (moins de tours de modèle à vide). Non testé en conditions réelles.
- 2026-08-31 : `/create_projet_public` est une commande `.claude/commands/` (pas un skill `skills/`), de la même famille que `/init_projet`/`/create_agent`, invoquée explicitement. Le dossier parent des nouveaux projets vit dans `.env` (`PROJETS_PARENT_DIR`, gitignoré) avec `.env.example` versionné ; la commande s'arrête proprement si `.env` est absent ou la clé vide. Elle crée un dépôt GitHub **public** via `gh` sur le compte connecté, puis enchaîne `/init_projet`.
- 2026-08-31 : `Roberto2` acté définitivement supprimé. `roadmap_com_agents.md` Phase 2 est repointée sur `D:\ServOMorph\Meuniers` (pas de `statut.md` ad hoc à convertir sur ce pilote). `roadmap_messages_zones.md` Phase 1 mise en pause, choix du pilote de remplacement et fusion éventuelle avec `roadmap_com_agents.md` reportés.
- 2026-08-29 : `templates/roberto/` supprimé du kit (plus d'usage identifié, demande explicite utilisateur) — plus aucun template `roberto` disponible pour `/insert_template`. Son launcher `MACROS/`/`UI_WEB/` (pywebview, macros PC, capture écran, communication OpenCode) et `roadmap_workflow_quotidien.md` (Phases 3-5 ouvertes), sans équivalent dans `D:\ServOMorph\Roberto` (source `Roberto2` disparue du disque), déplacés vers ce projet plutôt que perdus — note laissée dans son `_contexte/signals.md`. `roadmap_template_roberto.md` archivée (`_archives/`, 5/5 phases FAIT).
- 2026-08-23 : une équipe d'agents est toujours représentée par un coordinateur dans son propre dossier ; son `team.md` est le manifeste des membres directs et son alias est hiérarchique. Les messages et statuts ne circulent qu'entre un parent et ses enfants directs, sans communication latérale.
- 2026-08-23 : Intercom est indépendant de Claude Code et sert de protocole partagé par Codex, Claude Code ou un autre agent. Les urgences sont relevées aux points de contrôle de l'agent ; un processus externe ne peut pas interrompre un appel d'outil déjà en cours.
- 2026-08-20 : `templates/roberto/MASCOTTE/` supprimée du kit (extraite par l'utilisateur en projet standalone) ; `UI_WEB/mascotte/` conservé (intégration indépendante). `templates/roberto/AUTOMATISATIONS/` et `templates/roberto/com_telephone/` déplacés vers `D:\ServOMorph\Roberto` (nouveau repo git, premier push). Déplacement bloqué par plusieurs process verrouillant les fichiers (watcher `run.py --watch`, 3 process com_telephone, 2x `node server.js`), arrêtés avec autorisation explicite — à relancer depuis le nouvel emplacement si besoin. Un `rm -rf` intermédiaire a effacé des fichiers déjà déplacés (récupérés via `git checkout HEAD`, rien de non tracké perdu).
- 2026-08-20 : Authentification par token ajoutée à l'UI mobile du prototype "assistant vocal" (`voice-code-bridge/server.js`) — cookie posé via `?token=` en première visite, WebSocket vérifié via `verifyClient`, `/send` (appelé par l'agent local) restreint à `127.0.0.1` sans token. Token stocké dans `server/.env` (gitignoré) plutôt qu'en variable d'environnement système : `setx` s'est révélé peu fiable (ne se propage pas à la session VSCode/Claude Code déjà ouverte, même après reload window). Limite documentée pour l'utilisateur : le token protège l'accès, pas les actions que l'agent exécutera ensuite sur la base des messages reçus.
- 2026-08-20 : `decisions.md` du workflow `quotidien` ne s'archive/réinitialise plus à chaque lancement (roadmap vivante à cases à cocher, cochée seulement après validation explicite de l'utilisateur) — l'ancien mécanisme risquait de perdre des tâches non finies en cas de session interrompue. Réponses vocales (`POST /send`) désormais reformulées courtes/orales (règle ajoutée à `com_telephone/README.md`) et débit TTS ralenti (`length_scale=1.25`), sur demande explicite de l'utilisateur (écoute, pas lecture).
