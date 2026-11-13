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
- 2026-11-13 (suite) : `telephone.md` copié dans `VertIA_v3` via sa session ouverte (version du projet toujours v5.25) ; session « Sécurité » exclue ; dossier de « pilote-74 » à préciser ; 7 projets toujours en attente de `/update`.
- 2026-11-13 : kit v5.43 inchangé — `/insert_template` (registre sans doublon) et `/create_memory` scopé validés en réel sur cibles jetables ; reste la conversion de `/create_agent` ; 7 projets toujours en attente de `/update`.
- 2026-11-12 (suite) : kit v5.43 — `/create_agent` étape 3 : une lecture en échec ne vaut jamais absence ; `_docs/protocole_vibecoding.md` du kit réaligné sur v5.42 ; 7 projets toujours en attente de `/update` (sessions ouvertes).
- 2026-11-12 : 11 projets archivés dans `D:\ServOMorph\archives` (`crea_zik` à archiver à la main) ; 22 des 29 projets non archivés en v5.42 (`SérénIATech_dev` l'était déjà), 7 en attente (sessions ouvertes) ; fusion de `allowed-tools` exercée en réel ; kit v5.42 — `/update` conserve les permissions `allowed-tools` ajoutées par un projet ; v5.41 — `/close` étape 9 : `tests_manuels.md` et `roadmap*.md` exclus du bump ; v5.40 — `/start` : ligne de compteurs dans tous les modes, parties sans objet retirées ; v5.39 : 4b limitée aux `réf:` citées, y compris en `--complet` ; v5.38 : affichage réduit exercé en réel, tous les cas de `tests_manuels.md` conformes.
- 2026-11-10 à 11 : kit v5.34 à v5.37 — `/telephone` copié par défaut dans tout projet créé ou mis à jour ; `parallel_agents` retiré de `/create_projet` ; `/close` étape 14 conditionnelle (pas de push sans remote ni règle projet contraire) ; `llms.txt` aligné.

## Décisions structurantes
_Décisions antérieures au 2026-10-10 archivées dans `_contexte/archive_decisions.md`._
- 2026-11-08 : audit d'un projet suivi : le travail non commité est sauvegardé par un commit par zone (`sauvegarde(<zone>)`, hors `/close`, signals des zones non mis à jour) plutôt qu'en bloc ; un dépôt imbriqué sans `.gitmodules` est détaché et ignoré ; des modifications d'origine inconnue apparues pendant l'audit sont laissées en l'état. Codex n'est joignable que par relais de l'utilisateur.
- 2026-11-09 : analyse fonctionnelle d'un projet suivi menée par inventaire du code en lecture seule (volumes SQLite en mode `ro`, aucune donnée lue), puis tri processus par processus avec l'utilisateur. `SérénIATech_dev` : Indy seul outil de facturation, l'UI ne fait que le suivi ; prospection mail recentrée sur la qualification du pipeline ; une fonctionnalité dite absente est vérifiée dans le code avant d'être classée nouvelle.
- 2026-11-10 : `templates/parallel_agents` n'est pas un template insérable (modèles par agent remplis par `/create_parallel_team`) : exclu de la liste de `/create_projet` plutôt que d'étendre les placeholders d'`/insert_template`.
- 2026-11-11 : `/close` ne pousse jamais sans condition : `git remote` vide ou règle projet (`SPECIFICITES PROJET`, `.claude/memory.md`) = pas de push, rien au bilan ; un projet sans remote voulu n'a pas à personnaliser le corps de `close.md`.

- 2026-11-11 : `/start` (v5.38) n'affiche par défaut que la prochaine étape, la question bloquante et des compteurs (mot pour mot) ; `signals.md` complet sur `--complet` ou si une section manque ; le bloc 4c analyse toujours tout le fichier. La qualité de « Prochaine étape exacte » devient critique.
- 2026-11-11 : `/start` étape 4b (v5.39) : lecture des `réf:` limitée aux actions citées par la prochaine étape, même en `--complet` (lire toutes les `réf:` d'un fichier de 19 actions était trop coûteux en tokens).
- 2026-11-11 : `/start` étape 4 (v5.40) : la ligne de compteurs termine l'affichage dans tous les modes ; une partie sans objet est retirée de la ligne, jamais écrite « omis » (écart constaté au test du repli).
- 2026-11-11 : `/close` étape 9 (v5.41) : `tests_manuels.md` et `roadmap*.md` sont des fichiers de suivi, exclus du déclencheur de bump de version (le statut de roadmap est mis à jour par `/close` lui-même).
- 2026-11-11 : `/update` (v5.42) : `allowed-tools` de `start.md`/`close.md` = liste du kit + ajouts du projet (signalés) ; retraits du projet non conservés ; étape 10 tolère les ajouts en fin de ligne.
- 2026-11-12 : `/create_agent` reste générique : pas de mode « agent client » (besoin couvert par une commande projet), pas d'exception à la règle des MAJUSCULES ; un contrôle en échec ou sans sortie est refait avant toute conclusion d'absence (v5.43).
