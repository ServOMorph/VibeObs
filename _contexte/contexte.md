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
- 2026-11-14 (suite) : kit v6.2 — `/migration_canva` (manuelle) et `disable-model-invocation` sur les 4 commandes manuelles ; v6.1 — `/delegation` (Codex, OpenCode, Ollama, sous-agents Haiku) avec journal `_codex/journal_delegation.md`, 3 findings du backlog corrigés ; `DOCUMENTATION/` alignée sur v6.0.
- 2026-11-14 : kit v6.0 — `/init_projet` sans question de stack, alias par défaut = nom du projet ; v5.44 — journal de session gitignoré ; 21 projets en v5.44, `SérénIATech_dev` et les projets à session ouverte en attente de `/update`.
- 2026-11-13 : kit v5.43 — `/insert_template` et `/create_memory` scopé validés en réel ; reste la conversion de `/create_agent`.
- 2026-11-12 : 11 projets archivés dans `D:\ServOMorph\archives` (`crea_zik` à archiver à la main) ; kit v5.38 à v5.42.

## Décisions structurantes
_Décisions antérieures au 2026-10-10 archivées dans `_contexte/archive_decisions.md`._

- 2026-11-11 : `/start` (v5.38) n'affiche par défaut que la prochaine étape, la question bloquante et des compteurs (mot pour mot) ; `signals.md` complet sur `--complet` ou si une section manque ; le bloc 4c analyse toujours tout le fichier. La qualité de « Prochaine étape exacte » devient critique.
- 2026-11-11 : `/start` étape 4b (v5.39) : lecture des `réf:` limitée aux actions citées par la prochaine étape, même en `--complet` (lire toutes les `réf:` d'un fichier de 19 actions était trop coûteux en tokens).
- 2026-11-11 : `/start` étape 4 (v5.40) : la ligne de compteurs termine l'affichage dans tous les modes ; une partie sans objet est retirée de la ligne, jamais écrite « omis » (écart constaté au test du repli).
- 2026-11-11 : `/close` étape 9 (v5.41) : `tests_manuels.md` et `roadmap*.md` sont des fichiers de suivi, exclus du déclencheur de bump de version (le statut de roadmap est mis à jour par `/close` lui-même).
- 2026-11-11 : `/update` (v5.42) : `allowed-tools` de `start.md`/`close.md` = liste du kit + ajouts du projet (signalés) ; retraits du projet non conservés ; étape 10 tolère les ajouts en fin de ligne.
- 2026-11-12 : `/create_agent` reste générique : pas de mode « agent client » (besoin couvert par une commande projet), pas d'exception à la règle des MAJUSCULES ; un contrôle en échec ou sans sortie est refait avant toute conclusion d'absence (v5.43).
- 2026-11-14 : `/init_projet` (v6.0) ne demande plus la stack et propose l'alias par défaut avec le nom du projet ; le champ « Stack » du `contexte.md` d'un projet créé se remplit au fil du travail.
- 2026-11-14 : journal de session (v5.44) gitignoré (un fichier versionné vidé par `/close` laisserait un résidu à chaque clôture et risquerait des données sensibles en dépôt public) ; seul `/close` écrit `signals.md` / `contexte.md`. Règle diffusée aux sessions ouvertes par message unique contrôlé, application validée dans chaque session. Limites assumées : perdu avec le disque, écriture dépendante de la discipline de l'agent (un `/compact` n'est pas détectable sans hook).
- 2026-11-14 : `/delegation` — Claude orchestre et délègue selon la tâche : Ollama (texte mécanique fourni, local), OpenCode gratuit (lecture et petite édition dans le dépôt), Codex (correctif multi-fichiers, revue), sous-agent Haiku (web, doc). Écriture dans le kit en worktree, aucun secret vers un exécutant cloud, journal de chaque délégation pour améliorer le routage.
- 2026-11-14 : commandes à lancement manuel marquées `disable-model-invocation: true` (description retirée du contexte, `/nom` conservé) au lieu d'être sorties de `.claude/` ; critère : lancement manuel seulement, appelée par aucune autre commande.
