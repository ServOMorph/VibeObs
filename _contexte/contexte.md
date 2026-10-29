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
- 2026-10-29 : kit v5.25 — backlog `_contexte/backlog.md` catégorisé (`réf:` vérifié, croisé avec les fichiers modifiés), doublon à objet identique, constat rangé chez sa zone, pas de bump sans modification de travail ; validé sur projet jetable (supprimé), déployé dans `SérénIATech_dev`, `close.md` d'Appli aligné à la main (`d557510`, `start.md` non aligné).
- Non exercé en réel : premier `/close` d'Appli en v5.25 (permissions `ls` / `test -e`, 49 entrées de backlog sans catégorie), backlog créé à la première entrée, backlog vidé.
- 2026-10-27 : `/update` ne protège pas le frontmatter de `close.md` (action P1) ; `signals.md` du kit à 32 actions, au-dessus du plafond de 20 (tri à proposer).
- 2026-10-26 : création de `DOCUMENTATION/` pour `SérénIATech_dev` différée ; évaluation dans Appli (0 consultation spontanée sur 29 sessions, 3 specs périmées).
- 2026-10-17 à 2026-10-22 : projets `IA_Eco-Responsable`, `REA`, `creation_llm` créés (kit v5.21, stack à définir) ; écarts de `init_projet.md` étapes 5 et 7 toujours à corriger.

## Décisions structurantes
_Décisions antérieures au 2026-10-10 archivées dans `_contexte/archive_decisions.md`._
- 2026-10-29 : `/close` (v5.23 à v5.25) — doublon reconnu à l'objet identique (une `réf:` commune ne suffit pas), `réf:` de backlog vérifié par commande avant écriture et croisé avec les fichiers modifiés, ligne de renvoi totalisée, constat sur une autre zone écrit dans son `signals.md`, pas de bump de `CHANGELOG.md` sans modification de travail. Validé sur projet jetable avant déploiement.
- 2026-10-29 : Appli_TSA_SDI_TDAH n'a pas `/update` : son `close.md` est aligné à la main sur le générique (diff comparé au template, bloc `SPECIFICITES PROJET` intact) ; le backlog existant de 49 entrées n'est pas migré.
- 2026-10-27 : `/update` vers un projet existant : relire le diff complet (jamais tronqué) avant d'écraser `close.md`/`start.md` ; le bloc `SPECIFICITES PROJET` est réinjecté depuis `HEAD`, et toute personnalisation du frontmatter est conservée à la main en attendant la décision sur `update.md`.
- 2026-10-26 : v5.22 (et non v6.0, aucune migration imposée) — les actions ouvertes de `signals.md` sont plafonnées à 20 ; dette, findings et pistes différées vont dans `_contexte/backlog.md` (non chargé par `/start`, entrées traitées supprimées, ligne de renvoi hors plafond). Les findings de revue de code restent une règle spécifique projet (pas d'étape de revue générique dans le kit).
- 2026-10-26 : la consigne « Base de connaissances » de `CLAUDE.md` ne déclenche pas la consultation de `DOCUMENTATION/` (0 cas sur 29 sessions d'Appli) ; création de la zone dans `SérénIATech_dev` subordonnée à l'évaluation dans Appli, et migration de la section Spécificités projet vers l'INDEX déconseillée (les déclencheurs restent dans `CLAUDE.md`).
- 2026-10-14 : `/close` attribue chaque action, décision et point d'attention à sa zone propriétaire avant écriture (la racine ne garde que la coordination transversale) et contrôle le statut Git des signaux avant d'annoncer un commit ; `/start` signale les éléments mal classés sans les déplacer. Limite assumée : 4c ne contrôle pas une roadmap posée à la racine (cas `roadmap_actions_ouvertes_luna.md`, laissée en place sur décision de l'utilisateur).
- 2026-10-14 : `/create_agent` résout le parent par la zone englobante la plus proche (pas seulement la zone racine) et lit les « Données sensibles » du `CLAUDE.md` cible pour les exclure de la lecture étendue de l'agent ; un renommage de casse refusé par le système est reporté et tracé en action P2, sans terminer de processus.
- 2026-10-13 : les règles « installation sur D: » et « `run.py` à la racine » sont posées dans `CLAUDE.md` § Spécificités projet du kit ET du template (miroir exigé par `check_kit.py`), donc déployées dans les futurs projets.
- 2026-10-12 : la substitution des placeholders de `/init_projet` se fait par remplacement littéral Python (UTF-8 sans BOM, LF), jamais par regex/`sed`/`-replace` qui interprètent `\` et `$`.
- 2026-10-12 : `/init_projet` crée ou complète un `.gitignore` de sécurité (motifs ciblés `*token*.json`, `credentials*.json`, jamais `token*` qui masquerait des design tokens). Les données sensibles sont inscrites dans `CLAUDE.md` par remplacement explicite de `Aucun déclaré.`, pas par placeholder : `check_kit.py` retire les lignes à placeholder et un placeholder sans équivalent côté kit décale la comparaison miroir.
