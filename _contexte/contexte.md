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
- 2026-09-10 : registre « Templates installés » dans `DEPLOYMENTS.md` (kit, gitignoré) — 1 ligne par couple (projet, template), alimenté par `/insert_template` (`[SORTIE]` 9), `/init_discord_mode`, `/create_projet` (héritage) et `/init_intercom` (étape 6). Rétro-rempli par scan de signature (8 lignes). CHANGELOG v5.8.
- 2026-09-06 : rclone multicompte livré — 1 remote = 1 projet, compte Google dédié. Remotes actifs : `vibeobs_drive` (kit), `sereniatech_drive`, `rayonne_toi_drive` (partagé Rayonne_Toi + Appli_TSA_SDI_TDAH). `insert_template` 7bis : contrôle anti-collision sur le registre. `roadmap_rclone_multicompte.md` archivée (3/3).
- 2026-09-06 : `/update` rejoué sur Appli_TSA_SDI_TDAH (kit v3.1 → v5.4) ; hooks de zone opt-in à `/start`/`/close` (`_contexte/on_start.md` / `on_close.md`) ; étape 10 de `close.md` (check_kit.py) conditionnelle à la présence du script.
- 2026-09-04 : `discord_com` attend l’ack du bot pour sérialiser les notifications ; sa validation Discord réelle reste ouverte.
- 2026-09-04 : `/create_parallel_team` isole les agents code dans leurs worktrees ; le pilote Appli_TSA_SDI_TDAH attend les cycles `start`/`close` de `ONBOARD` et `RETOURS`.

## Décisions structurantes
_Décisions antérieures au 2026-09-03 archivées dans `_contexte/archive_decisions.md`._
- 2026-09-10 : les templates de `templates/<nom>/` insérés dans un projet sont tracés dans une section « Templates installés » de `DEPLOYMENTS.md` (kit, gitignoré, même régime que « Remotes rclone »), une ligne par couple (projet, template) avec destination relative, date et note. `/insert_template` l'écrit à l'étape `[SORTIE]` 9 (si au moins un fichier créé, pas de doublon sur couple existant) ; `/init_discord_mode` et `/create_projet` héritent via délégation à cette procédure ; `/init_intercom` écrit sa ligne à sa nouvelle étape 6. `doc_sync` ne touche pas ce fichier (déjà exclu).
- 2026-09-06 : rclone — un remote est dédié à un seul projet, chaque projet sauvegarde vers un compte Google distinct. Partage entre projets seulement s'il est déclaré explicitement à l'insertion du template et tracé `partagé: A + B` au registre « Remotes rclone » de `DEPLOYMENTS.md`. `/insert_template` 7bis (a→f) lit ce registre, masque et refuse tout remote déjà attribué à un autre projet sauf confirmation de partage ; `/create_projet` et `/init_projet` y délèguent. Backup du kit sur `vibeobs_drive`. `googledrive:` (doublon du compte rayonnetoi) supprimé après repointage de tous les usages et migration/purge des données mal placées.
- 2026-09-06 : `/update` peut légitimement dévier d'une règle générique du kit quand le projet cible a un choix structurant incompatible (ex. helper Ollama dans `scripts/` et non à la racine) : ne pas forcer, documenter l'écart dans `CLAUDE.md` § Spécificités projet, ne pas toucher `AGENTS.md`/`GEMINI.md` déjà présents. `roadmap_migration_close.md` achevée : le corps générique de `start.md`/`close.md` d'un projet déployé peut rester byte-identique au kit, le comportement projet vivant en SPECIFICITES.
- 2026-09-06 : `/start` et `/close` exposent quatre points d'ancrage de hook de zone (`on_start.md` : Pré-synthèse étape 3-bis, Post-synthèse 5-bis ; `on_close.md` : Pré-synthèse 2-bis, Fin 14-ter), opt-in, non bloquants, contrats dans `templates/on_*_TEMPLATE.md`. L'étape 10 de `close.md` (check_kit.py) devient conditionnelle à la présence du script ; corollaire : `close.md` d'un projet déployé peut être migré vers le mécanisme SPECIFICITES sans que `/update` casse la clôture.
- 2026-09-04 : quand un projet utilise les trois fichiers `.claude/CLAUDE.md`, `AGENTS.md` et `GEMINI.md`, ils portent strictement le même contenu ; l’harmonisation attend le choix explicite de la source canonique et se vérifie par hash.
- 2026-09-04 : une équipe à écriture parallèle est créée via `/create_parallel_team`, distinct de `/create_team` ; chaque membre a son worktree et sa branche, sans merge, rebase ou déploiement automatique.
- 2026-09-04 : les aliases de zone destinés à être utilisés par les personnes sont en majuscules (`TESTS`, `ONBOARD`, `RETOURS`) ; les noms de branches Git peuvent rester en minuscules sur Windows.
- 2026-09-04 : `discord_com` ne déduplique pas les sorties sur un timestamp à la seconde ; l’état de la file est l’unique garde contre le renvoi. `notify` attend l’ack du bot afin de sérialiser les notifications consécutives. Le Bot Token reste exclusivement dans `.env` local gitignoré.
- 2026-09-04 : le kit est renommé VibeObs. La commande `/create_projet` remplace `/create_projet_public` et couvre Git local ou GitHub public/privé ; les sauvegardes rclone sont distribuées comme template avec un remote explicite.
- 2026-09-04 : une roadmap achevée déclenche une proposition d'archivage à l'utilisateur ; l'archivage reste soumis à son accord explicite. Règle ajoutée au protocole et à sa documentation de session.
