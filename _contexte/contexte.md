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
- 2026-10-12 : projet test `site_internet_ST_v3` (zone `site_st`, refonte serenia-tech.fr) créé via `/create_projet` + `/init_projet`, roadmap 8 phases ; premier `/start site_st` à faire.
- 2026-10-12 : kit v5.17 — `/init_projet` pose un `.gitignore` et inscrit les données sensibles, `/close` crée `CHANGELOG.md` absent, template `signals.md` conforme à l'invariant.
- 2026-10-10 : agent `jeux` créé dans `Appli_TSA_SDI_TDAH/JEUX` ; premier `/start jeux` à faire.
- 2026-10-08 : agents `textes` et `modeles_llm` créés dans `CreaZik_V3` ; premiers `/start` à faire.
- 2026-09-16 : harmonisation `CLAUDE.md`/`AGENTS.md`/`GEMINI.md` reportée en P1 sur ordre utilisateur.

## Décisions structurantes
_Décisions antérieures au 2026-09-10 archivées dans `_contexte/archive_decisions.md`._
- 2026-10-12 : `/init_projet` crée ou complète un `.gitignore` de sécurité (motifs ciblés `*token*.json`, `credentials*.json`, jamais `token*` qui masquerait des design tokens). Les données sensibles sont inscrites dans `CLAUDE.md` par remplacement explicite de `Aucun déclaré.`, pas par placeholder : `check_kit.py` retire les lignes à placeholder et un placeholder sans équivalent côté kit décale la comparaison miroir.
- 2026-10-12 : projet `site_internet_ST_v3` = un seul agent (zone racine `site_st`), sert à la fois de refonte de serenia-tech.fr et de banc d'essai VibeObs ; mise à jour automatique du site uniquement via `site_com.md` par projet suivi + brouillon validé ; `creation_superagent.md` écrit après le MVP.
- 2026-10-10 : un agent dont le périmètre d'écriture déborde de son dossier le déclare au minimum (ici `run_jeux.py`) ; le code applicatif (`src/`) reste en lecture seule tant que l'utilisateur n'a pas validé l'intégration.
- 2026-10-08 : agents d'un projet cible qui stockent des modèles lourds hors dépôt suivent la convention `D:\AI\<domaine>\` et le cache `HF_HOME` existant ; un dossier réservé à un autre outil (ex. `tests_ace/`) est exclu du périmètre d'écriture.
- 2026-09-26 : nouveau projet `PromptGuard` (retrait des données sensibles avant envoi à un LLM cloud) créé via `/create_projet`→`/init_projet` ; 3 agents (`securite`, `qa`, `documentation`) créés en lot. Idée de skill de cohérence CLAUDE/AGENTS/GEMINI (tronc commun + section propre par fichier) mémorisée pour expérimentation locale côté PromptGuard, pas de généralisation au kit pour l'instant.
- 2026-09-16 : `agent_role_TEMPLATE.md` § Invariants réutilise `{{ECRITURE_ETENDUE}}` (P14) pour rester cohérent avec le Périmètre de tout agent à écriture étendue, sans changement de `create_agent.md`.
- 2026-09-13 : `/create_projet` place `0. Aucun template` en tête de la liste de sélection des templates (jamais en dernier) — les rendus Markdown fixent le numéro de départ d'une liste ordonnée sur son premier élément et ignorent les valeurs explicites suivantes, ce qui provoquait un décalage d'affichage (`0` rendu comme le chiffre suivant, ex. `8`).
- 2026-09-13 : `rclone_backup.json` porte `remote` et `folder` ; le dossier Drive ne dépend plus de la casse du chemin local. Le script exclut `.env*`, clés, certificats, credentials, tokens, configurations rclone et paramètres locaux ; `--check` réalise un contrôle rclone à sens unique.
- 2026-09-10 : le hook « Fin » de `/close` ne tente plus d'upload cloud sous auto-mode — le classifieur de sécurité refuse systématiquement `rclone copy` de secrets, sans être contournable par `permissions.allow` ni un réglage local. Le hook se limite à `--refresh-list` (manifeste tenu à jour), l'upload Drive devient une action manuelle hors session, tracée dans `tests_manuels.md` du projet. Correctifs `backup_project.py` (template kit + copie vendored Appli) : exclusion élargie des artefacts régénérables (match sur segment de chemin) et sorties robustes à l'encodage — `sys.stdout/stderr.reconfigure(encoding="utf-8", errors="replace")` + `subprocess.run(..., encoding="utf-8", errors="replace")` — pour ne plus crasher sur un nom de fichier non-ASCII (Windows cp1252).
- 2026-09-10 : les templates de `templates/<nom>/` insérés dans un projet sont tracés dans une section « Templates installés » de `DEPLOYMENTS.md` (kit, gitignoré, même régime que « Remotes rclone »), une ligne par couple (projet, template) avec destination relative, date et note. `/insert_template` l'écrit à l'étape `[SORTIE]` 9 (si au moins un fichier créé, pas de doublon sur couple existant) ; `/init_discord_mode` et `/create_projet` héritent via délégation à cette procédure ; `/init_intercom` écrit sa ligne à sa nouvelle étape 6. `doc_sync` ne touche pas ce fichier (déjà exclu).
