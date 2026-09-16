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
- 2026-09-16 : étude harmonisation `CLAUDE.md`/`AGENTS.md`/`GEMINI.md` (contradiction templates minimaux vs identité v5.3, `/update` fige la dérive) ; mise en œuvre reportée en P1 sur ordre utilisateur.
- 2026-09-16 : `/create_agent` a créé l'agent DOCUMENTATION du projet `Appli_TSA_SDI_TDAH` ; friction P14 tranchée et corrigée dans `agent_role_TEMPLATE.md`.
- 2026-09-13 : `/create_projet` place `0. Aucun template` en tête de liste ; vérification réelle restant à faire.
- 2026-09-13 : `rclone_backup` définit son dossier Drive canonique, exclut les secrets et propose `--check`.
- 2026-09-10 : le hook « Fin » de `/close` d'Appli_TSA_SDI_TDAH se limite à `--refresh-list` ; upload Drive manuel hors session.

## Décisions structurantes
_Décisions antérieures au 2026-09-04 archivées dans `_contexte/archive_decisions.md`._
- 2026-09-16 : `agent_role_TEMPLATE.md` § Invariants réutilise `{{ECRITURE_ETENDUE}}` (P14) pour rester cohérent avec le Périmètre de tout agent à écriture étendue, sans changement de `create_agent.md`.
- 2026-09-13 : `/create_projet` place `0. Aucun template` en tête de la liste de sélection des templates (jamais en dernier) — les rendus Markdown fixent le numéro de départ d'une liste ordonnée sur son premier élément et ignorent les valeurs explicites suivantes, ce qui provoquait un décalage d'affichage (`0` rendu comme le chiffre suivant, ex. `8`).
- 2026-09-13 : `rclone_backup.json` porte `remote` et `folder` ; le dossier Drive ne dépend plus de la casse du chemin local. Le script exclut `.env*`, clés, certificats, credentials, tokens, configurations rclone et paramètres locaux ; `--check` réalise un contrôle rclone à sens unique.
- 2026-09-10 : le hook « Fin » de `/close` ne tente plus d'upload cloud sous auto-mode — le classifieur de sécurité refuse systématiquement `rclone copy` de secrets, sans être contournable par `permissions.allow` ni un réglage local. Le hook se limite à `--refresh-list` (manifeste tenu à jour), l'upload Drive devient une action manuelle hors session, tracée dans `tests_manuels.md` du projet. Correctifs `backup_project.py` (template kit + copie vendored Appli) : exclusion élargie des artefacts régénérables (match sur segment de chemin) et sorties robustes à l'encodage — `sys.stdout/stderr.reconfigure(encoding="utf-8", errors="replace")` + `subprocess.run(..., encoding="utf-8", errors="replace")` — pour ne plus crasher sur un nom de fichier non-ASCII (Windows cp1252).
- 2026-09-10 : les templates de `templates/<nom>/` insérés dans un projet sont tracés dans une section « Templates installés » de `DEPLOYMENTS.md` (kit, gitignoré, même régime que « Remotes rclone »), une ligne par couple (projet, template) avec destination relative, date et note. `/insert_template` l'écrit à l'étape `[SORTIE]` 9 (si au moins un fichier créé, pas de doublon sur couple existant) ; `/init_discord_mode` et `/create_projet` héritent via délégation à cette procédure ; `/init_intercom` écrit sa ligne à sa nouvelle étape 6. `doc_sync` ne touche pas ce fichier (déjà exclu).
- 2026-09-06 : rclone — un remote est dédié à un seul projet, chaque projet sauvegarde vers un compte Google distinct. Partage entre projets seulement s'il est déclaré explicitement à l'insertion du template et tracé `partagé: A + B` au registre « Remotes rclone » de `DEPLOYMENTS.md`. `/insert_template` 7bis (a→f) lit ce registre, masque et refuse tout remote déjà attribué à un autre projet sauf confirmation de partage ; `/create_projet` et `/init_projet` y délèguent. Backup du kit sur `vibeobs_drive`. `googledrive:` (doublon du compte rayonnetoi) supprimé après repointage de tous les usages et migration/purge des données mal placées.
- 2026-09-06 : `/update` peut légitimement dévier d'une règle générique du kit quand le projet cible a un choix structurant incompatible (ex. helper Ollama dans `scripts/` et non à la racine) : ne pas forcer, documenter l'écart dans `CLAUDE.md` § Spécificités projet, ne pas toucher `AGENTS.md`/`GEMINI.md` déjà présents. `roadmap_migration_close.md` achevée : le corps générique de `start.md`/`close.md` d'un projet déployé peut rester byte-identique au kit, le comportement projet vivant en SPECIFICITES.
- 2026-09-06 : `/start` et `/close` exposent quatre points d'ancrage de hook de zone (`on_start.md` : Pré-synthèse étape 3-bis, Post-synthèse 5-bis ; `on_close.md` : Pré-synthèse 2-bis, Fin 14-ter), opt-in, non bloquants, contrats dans `templates/on_*_TEMPLATE.md`. L'étape 10 de `close.md` (check_kit.py) devient conditionnelle à la présence du script ; corollaire : `close.md` d'un projet déployé peut être migré vers le mécanisme SPECIFICITES sans que `/update` casse la clôture.
- 2026-09-04 : quand un projet utilise les trois fichiers `.claude/CLAUDE.md`, `AGENTS.md` et `GEMINI.md`, ils portent strictement le même contenu ; l’harmonisation attend le choix explicite de la source canonique et se vérifie par hash.
- 2026-09-04 : une équipe à écriture parallèle est créée via `/create_parallel_team`, distinct de `/create_team` ; chaque membre a son worktree et sa branche, sans merge, rebase ou déploiement automatique.
