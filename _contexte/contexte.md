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
- 2026-10-26 : création de `DOCUMENTATION/` pour `SérénIATech_dev` différée ; mécanisme en évaluation dans `Appli_TSA_SDI_TDAH` (0 consultation spontanée mesurée, 3 specs périmées) ; 5 tests actifs en attente dans `tests_manuels.md` d'Appli.
- 2026-10-22 : projet `creation_llm` créé (Git local + GitHub public, kit v5.21, stack à définir) ; écarts de `init_projet.md` étapes 5 et 7 reproduits, toujours à corriger.
- 2026-10-17 : projets `IA_Eco-Responsable` et `REA` créés (kit v5.21, stack à définir) ; mêmes écarts de `init_projet.md` étapes 5 et 7.
- 2026-10-14 : kit v5.21 — `/close` attribue chaque élément à sa zone (3-bis) et contrôle le statut Git des signaux (13), `/start` signale les éléments mal classés (4c) ; déployé dans `SérénIATech_dev`, scénarios réels à rejouer.
- 2026-10-14 : kit v5.20 — `/create_agent` choisit le parent englobant, exclut les données sensibles, migre les actions du parent ; agent `espace_l-invariable` créé, renommage en majuscules en attente.

## Décisions structurantes
_Décisions antérieures au 2026-09-26 archivées dans `_contexte/archive_decisions.md`._
- 2026-10-26 : la consigne « Base de connaissances » de `CLAUDE.md` ne déclenche pas la consultation de `DOCUMENTATION/` (0 cas sur 29 sessions d'Appli) ; création de la zone dans `SérénIATech_dev` subordonnée à l'évaluation dans Appli, et migration de la section Spécificités projet vers l'INDEX déconseillée (les déclencheurs restent dans `CLAUDE.md`).
- 2026-10-14 : `/close` attribue chaque action, décision et point d'attention à sa zone propriétaire avant écriture (la racine ne garde que la coordination transversale) et contrôle le statut Git des signaux avant d'annoncer un commit ; `/start` signale les éléments mal classés sans les déplacer. Limite assumée : 4c ne contrôle pas une roadmap posée à la racine (cas `roadmap_actions_ouvertes_luna.md`, laissée en place sur décision de l'utilisateur).
- 2026-10-14 : `/create_agent` résout le parent par la zone englobante la plus proche (pas seulement la zone racine) et lit les « Données sensibles » du `CLAUDE.md` cible pour les exclure de la lecture étendue de l'agent ; un renommage de casse refusé par le système est reporté et tracé en action P2, sans terminer de processus.
- 2026-10-13 : les règles « installation sur D: » et « `run.py` à la racine » sont posées dans `CLAUDE.md` § Spécificités projet du kit ET du template (miroir exigé par `check_kit.py`), donc déployées dans les futurs projets.
- 2026-10-12 : la substitution des placeholders de `/init_projet` se fait par remplacement littéral Python (UTF-8 sans BOM, LF), jamais par regex/`sed`/`-replace` qui interprètent `\` et `$`.
- 2026-10-12 : `/init_projet` crée ou complète un `.gitignore` de sécurité (motifs ciblés `*token*.json`, `credentials*.json`, jamais `token*` qui masquerait des design tokens). Les données sensibles sont inscrites dans `CLAUDE.md` par remplacement explicite de `Aucun déclaré.`, pas par placeholder : `check_kit.py` retire les lignes à placeholder et un placeholder sans équivalent côté kit décale la comparaison miroir.
- 2026-10-12 : projet `site_internet_ST_v3` = un seul agent (zone racine `site_st`), sert à la fois de refonte de serenia-tech.fr et de banc d'essai VibeObs ; mise à jour automatique du site uniquement via `site_com.md` par projet suivi + brouillon validé ; `creation_superagent.md` écrit après le MVP.
- 2026-10-10 : un agent dont le périmètre d'écriture déborde de son dossier le déclare au minimum (ici `run_jeux.py`) ; le code applicatif (`src/`) reste en lecture seule tant que l'utilisateur n'a pas validé l'intégration.
- 2026-10-08 : agents d'un projet cible qui stockent des modèles lourds hors dépôt suivent la convention `D:\AI\<domaine>\` et le cache `HF_HOME` existant ; un dossier réservé à un autre outil (ex. `tests_ace/`) est exclu du périmètre d'écriture.
- 2026-09-26 : nouveau projet `PromptGuard` (retrait des données sensibles avant envoi à un LLM cloud) créé via `/create_projet`→`/init_projet` ; 3 agents (`securite`, `qa`, `documentation`) créés en lot. Idée de skill de cohérence CLAUDE/AGENTS/GEMINI (tronc commun + section propre par fichier) mémorisée pour expérimentation locale côté PromptGuard, pas de généralisation au kit pour l'instant.
