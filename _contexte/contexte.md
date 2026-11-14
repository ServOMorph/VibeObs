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
- 2026-11-14 : kit v6.0 — `/init_projet` propose l'alias par défaut avec le nom du projet et ne demande plus la stack ; `Agent_Trader` créé par `/create_projet` (autre session du kit, commit `7bcd433`) ; v5.44 — journal de session `_contexte/journal_session.md` (gitignoré) écrit au fil de l'eau, intégré puis vidé par `/close`, signalé par `/start` ; 21 projets en v5.44, `SérénIATech_dev` et les projets à session ouverte en attente de `/update`.
- 2026-11-13 (suite) : `telephone.md` copié dans `VertIA_v3` via sa session ouverte ; session « Sécurité » exclue de cette copie.
- 2026-11-13 : kit v5.43 — `/insert_template` (registre sans doublon) et `/create_memory` scopé validés en réel ; reste la conversion de `/create_agent`.
- 2026-11-12 (suite) : kit v5.43 — `/create_agent` étape 3 : une lecture en échec ne vaut jamais absence ; `_docs/protocole_vibecoding.md` du kit réaligné.
- 2026-11-12 : 11 projets archivés dans `D:\ServOMorph\archives` (`crea_zik` à archiver à la main) ; kit v5.38 à v5.42 (`/start` réduit, `allowed-tools` conservés par `/update`).

## Décisions structurantes
_Décisions antérieures au 2026-10-10 archivées dans `_contexte/archive_decisions.md`._
- 2026-11-10 : `templates/parallel_agents` n'est pas un template insérable (modèles par agent remplis par `/create_parallel_team`) : exclu de la liste de `/create_projet` plutôt que d'étendre les placeholders d'`/insert_template`.
- 2026-11-11 : `/close` ne pousse jamais sans condition : `git remote` vide ou règle projet (`SPECIFICITES PROJET`, `.claude/memory.md`) = pas de push, rien au bilan ; un projet sans remote voulu n'a pas à personnaliser le corps de `close.md`.

- 2026-11-11 : `/start` (v5.38) n'affiche par défaut que la prochaine étape, la question bloquante et des compteurs (mot pour mot) ; `signals.md` complet sur `--complet` ou si une section manque ; le bloc 4c analyse toujours tout le fichier. La qualité de « Prochaine étape exacte » devient critique.
- 2026-11-11 : `/start` étape 4b (v5.39) : lecture des `réf:` limitée aux actions citées par la prochaine étape, même en `--complet` (lire toutes les `réf:` d'un fichier de 19 actions était trop coûteux en tokens).
- 2026-11-11 : `/start` étape 4 (v5.40) : la ligne de compteurs termine l'affichage dans tous les modes ; une partie sans objet est retirée de la ligne, jamais écrite « omis » (écart constaté au test du repli).
- 2026-11-11 : `/close` étape 9 (v5.41) : `tests_manuels.md` et `roadmap*.md` sont des fichiers de suivi, exclus du déclencheur de bump de version (le statut de roadmap est mis à jour par `/close` lui-même).
- 2026-11-11 : `/update` (v5.42) : `allowed-tools` de `start.md`/`close.md` = liste du kit + ajouts du projet (signalés) ; retraits du projet non conservés ; étape 10 tolère les ajouts en fin de ligne.
- 2026-11-12 : `/create_agent` reste générique : pas de mode « agent client » (besoin couvert par une commande projet), pas d'exception à la règle des MAJUSCULES ; un contrôle en échec ou sans sortie est refait avant toute conclusion d'absence (v5.43).
- 2026-11-14 : `/init_projet` (v6.0) ne demande plus la stack et propose l'alias par défaut avec le nom du projet ; le champ « Stack » du `contexte.md` d'un projet créé se remplit au fil du travail.
- 2026-11-14 : journal de session (v5.44) gitignoré (un fichier versionné vidé par `/close` laisserait un résidu à chaque clôture et risquerait des données sensibles en dépôt public) ; seul `/close` écrit `signals.md` / `contexte.md`. Règle diffusée aux sessions ouvertes par message unique contrôlé, application validée dans chaque session. Limites assumées : perdu avec le disque, écriture dépendante de la discipline de l'agent (un `/compact` n'est pas détectable sans hook).
