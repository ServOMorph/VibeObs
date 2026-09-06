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
- 2026-09-06 : le kit VibeObs v5.4 ajoute des hooks de zone opt-in à `/start` et `/close` (`_contexte/on_start.md` / `on_close.md`, sections Pré/Post-synthèse et Fin) ; l'étape 10 de `close.md` (check_kit.py) est conditionnelle à la présence du script.
- 2026-09-06 : `close.md` d'Appli_TSA_SDI_TDAH migré vers le mécanisme SPECIFICITES (corps générique aligné sur `templates/`) ; Phase 3 de `roadmap_migration_close.md` (`/update`) en attente des `/close` des deux repos.
- 2026-09-04 : `discord_com` attend l’ack du bot pour sérialiser les notifications ; sa validation Discord réelle reste ouverte.
- 2026-09-04 : `/create_parallel_team` isole les agents code dans leurs worktrees ; le pilote Appli_TSA_SDI_TDAH attend les cycles `start`/`close` de `ONBOARD` et `RETOURS`.
- 2026-09-04 : les trois fichiers d’instructions d’un projet (`.claude/CLAUDE.md`, `AGENTS.md`, `GEMINI.md`) sont désormais harmonisables à l’identique via le skill local `harmonize-agent-instructions`.

## Décisions structurantes
_Décisions antérieures au 2026-08-31 archivées dans `_contexte/archive_decisions.md`._
- 2026-09-06 : `/start` et `/close` exposent quatre points d'ancrage de hook de zone (`on_start.md` : Pré-synthèse étape 3-bis, Post-synthèse 5-bis ; `on_close.md` : Pré-synthèse 2-bis, Fin 14-ter), opt-in, non bloquants, contrats dans `templates/on_*_TEMPLATE.md`. L'étape 10 de `close.md` (check_kit.py) devient conditionnelle à la présence du script ; corollaire : `close.md` d'un projet déployé peut être migré vers le mécanisme SPECIFICITES sans que `/update` casse la clôture.
- 2026-09-04 : quand un projet utilise les trois fichiers `.claude/CLAUDE.md`, `AGENTS.md` et `GEMINI.md`, ils portent strictement le même contenu ; l’harmonisation attend le choix explicite de la source canonique et se vérifie par hash.
- 2026-09-04 : une équipe à écriture parallèle est créée via `/create_parallel_team`, distinct de `/create_team` ; chaque membre a son worktree et sa branche, sans merge, rebase ou déploiement automatique.
- 2026-09-04 : les aliases de zone destinés à être utilisés par les personnes sont en majuscules (`TESTS`, `ONBOARD`, `RETOURS`) ; les noms de branches Git peuvent rester en minuscules sur Windows.
- 2026-09-04 : `discord_com` ne déduplique pas les sorties sur un timestamp à la seconde ; l’état de la file est l’unique garde contre le renvoi. `notify` attend l’ack du bot afin de sérialiser les notifications consécutives. Le Bot Token reste exclusivement dans `.env` local gitignoré.
- 2026-09-04 : le kit est renommé VibeObs. La commande `/create_projet` remplace `/create_projet_public` et couvre Git local ou GitHub public/privé ; les sauvegardes rclone sont distribuées comme template avec un remote explicite.
- 2026-09-04 : une roadmap achevée déclenche une proposition d'archivage à l'utilisateur ; l'archivage reste soumis à son accord explicite. Règle ajoutée au protocole et à sa documentation de session.
- 2026-09-03 : `/create_agent` propose systématiquement l'insertion du template `discord_com` pour un agent Discord (défaut oui, config renvoyée à `/init_discord_mode`). Le Bot Token (`DISCORD_BOT_TOKEN`) est distingué explicitement de l'Application ID / Public Key / Client Secret partout dans la doc Discord. Correctif du template `discord_com` : `queue.json` repasse à `idle` après un envoi non interactif (fin du bug « un message Discord sur deux avalé »), `WAIT_TIMEOUT` de `discord_loop.py` porté à 110 s (moins de tours de modèle à vide). Non testé en conditions réelles.
- 2026-08-31 : `/create_projet_public` est une commande `.claude/commands/` (pas un skill `skills/`), de la même famille que `/init_projet`/`/create_agent`, invoquée explicitement. Le dossier parent des nouveaux projets vit dans `.env` (`PROJETS_PARENT_DIR`, gitignoré) avec `.env.example` versionné ; la commande s'arrête proprement si `.env` est absent ou la clé vide. Elle crée un dépôt GitHub **public** via `gh` sur le compte connecté, puis enchaîne `/init_projet`.
- 2026-08-31 : `Roberto2` acté définitivement supprimé. `roadmap_com_agents.md` Phase 2 est repointée sur `D:\ServOMorph\Meuniers` (pas de `statut.md` ad hoc à convertir sur ce pilote). `roadmap_messages_zones.md` Phase 1 mise en pause, choix du pilote de remplacement et fusion éventuelle avec `roadmap_com_agents.md` reportés.
