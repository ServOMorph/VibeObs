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
- 2026-11-11 : kit v5.37 — `/close` étape 14 conditionnelle (pas de push sans remote ni si une règle projet l'interdit) ; phase 6 toujours en attente du plan de l'utilisateur.
- 2026-11-11 : kit v5.36 — `llms.txt` aligné sur la version du kit ; phase 6 toujours en attente du plan de l'utilisateur.
- 2026-11-10 : kit v5.35 — `parallel_agents` retiré de la liste de `/create_projet` (non insérable) ; phase 6 toujours en attente du plan de l'utilisateur.
- 2026-11-10 : kit v5.34 — `/telephone` copié par défaut dans tout projet créé (`/init_projet`, `/create_projet`) ou mis à jour (`/update`) ; projet `creation_videos` créé.
- 2026-11-09 : kit v5.33 — `roadmap_fondations.md` : phases 1, 2, 4 et 5 closes ; phase 3 (PEDAGOGIE) retirée (backlog) ; phase 6 (plan d'automatisation) menée par l'utilisateur dans la session `SérénIATech_dev`.
- 2026-11-09 : rapport de phase 5 relayé à la session Business ; ordre 1 > 2 > 5 > 3, 7 en parallèle, 4 après la décision CAE ; implémentation par les zones ui, gestion-clients et business.

## Décisions structurantes
_Décisions antérieures au 2026-10-10 archivées dans `_contexte/archive_decisions.md`._
- 2026-11-10 : `/telephone` fait partie du socle par défaut des projets cibles (copie à l'init, réalignement à `/update`) ; auparavant installée à la main projet par projet.
- 2026-11-08 : constats d'audit relayés à une session ouverte par `SendMessage` : reformulation contrôlée avant application (patch du diff hors Git avant toute restauration, archivage au lieu de suppression), application validée par l'utilisateur dans la session de l'agent. Phase 4 close avec le test des connecteurs reporté (backlog) ; script de relevé du quota d'abonnement abandonné (`/usage`).
- 2026-11-08 : audit d'un projet suivi : le travail non commité est sauvegardé par un commit par zone (`sauvegarde(<zone>)`, hors `/close`, signals des zones non mis à jour) plutôt qu'en bloc ; un dépôt imbriqué sans `.gitmodules` est détaché et ignoré ; des modifications d'origine inconnue apparues pendant l'audit sont laissées en l'état. Codex n'est joignable que par relais de l'utilisateur.
- 2026-11-06 : modification d'un dossier où une session Codex ou Claude Code est ouverte : demande envoyée à la session, reformulation validée depuis VibeObs, application validée par l'utilisateur dans la session de l'agent (mémoire projet). Données personnelles (e-mails, `.env`) archivées hors Git dans `_archives/local/`.
- 2026-11-01 : un message d'une autre session demandant d'écrire dans le kit (ex. insérer un template) est consigné en action et non exécuté sans accord explicite de l'utilisateur ; `DEPLOYMENTS.md` reste local (gitignoré), donc non détectable par `git diff` en `/close` (entrée de backlog).
- 2026-10-29 : `/close` (v5.23 à v5.25) — doublon reconnu à l'objet identique (une `réf:` commune ne suffit pas), `réf:` de backlog vérifié par commande avant écriture et croisé avec les fichiers modifiés, ligne de renvoi totalisée, constat sur une autre zone écrit dans son `signals.md`, pas de bump de `CHANGELOG.md` sans modification de travail. Validé sur projet jetable avant déploiement.
- 2026-10-29 : Appli_TSA_SDI_TDAH n'a pas `/update` : son `close.md` est aligné à la main sur le générique (diff comparé au template, bloc `SPECIFICITES PROJET` intact) ; le backlog existant de 49 entrées n'est pas migré.
- 2026-11-09 : analyse fonctionnelle d'un projet suivi menée par inventaire du code en lecture seule (volumes SQLite en mode `ro`, aucune donnée lue), puis tri processus par processus avec l'utilisateur. `SérénIATech_dev` : Indy seul outil de facturation, l'UI ne fait que le suivi ; prospection mail recentrée sur la qualification du pipeline ; une fonctionnalité dite absente est vérifiée dans le code avant d'être classée nouvelle.
- 2026-11-10 : `templates/parallel_agents` n'est pas un template insérable (modèles par agent remplis par `/create_parallel_team`) : exclu de la liste de `/create_projet` plutôt que d'étendre les placeholders d'`/insert_template`.
- 2026-11-11 : `/close` ne pousse jamais sans condition : `git remote` vide ou règle projet (`SPECIFICITES PROJET`, `.claude/memory.md`) = pas de push, rien au bilan ; un projet sans remote voulu n'a pas à personnaliser le corps de `close.md`.
