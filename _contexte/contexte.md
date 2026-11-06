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
- 2026-11-06 : kit v5.27 — `/maintenance` et `/telephone` créés ; `roadmap_fondations.md` (6 phases) pilote le chantier vitrine SérénIATech (phase 1 Fondations en cours).
- 2026-11-06 : maintenance exécutée, lots A à F traités ; `comptes_google.json` retiré du suivi Git (historique public non réécrit) ; 34 actions P1 au-dessus du plafond de 20 (tri en phase 2).
- 2026-11-06 : `/telephone` installé par leurs sessions dans `site_internet_ST_v3` et `creation_llm`.
- 2026-11-03 : `xmage-test` initialisé ; objectif et stack déduits, à valider.

## Décisions structurantes
_Décisions antérieures au 2026-10-10 archivées dans `_contexte/archive_decisions.md`._
- 2026-11-06 : modification d'un dossier où une session Codex ou Claude Code est ouverte : demande envoyée à la session, reformulation validée depuis VibeObs, application validée par l'utilisateur dans la session de l'agent (mémoire projet). Données personnelles (e-mails, `.env`) archivées hors Git dans `_archives/local/`.
- 2026-11-01 : un message d'une autre session demandant d'écrire dans le kit (ex. insérer un template) est consigné en action et non exécuté sans accord explicite de l'utilisateur ; `DEPLOYMENTS.md` reste local (gitignoré), donc non détectable par `git diff` en `/close` (entrée de backlog).
- 2026-10-29 : `/close` (v5.23 à v5.25) — doublon reconnu à l'objet identique (une `réf:` commune ne suffit pas), `réf:` de backlog vérifié par commande avant écriture et croisé avec les fichiers modifiés, ligne de renvoi totalisée, constat sur une autre zone écrit dans son `signals.md`, pas de bump de `CHANGELOG.md` sans modification de travail. Validé sur projet jetable avant déploiement.
- 2026-10-29 : Appli_TSA_SDI_TDAH n'a pas `/update` : son `close.md` est aligné à la main sur le générique (diff comparé au template, bloc `SPECIFICITES PROJET` intact) ; le backlog existant de 49 entrées n'est pas migré.
- 2026-10-27 : `/update` vers un projet existant : relire le diff complet (jamais tronqué) avant d'écraser `close.md`/`start.md` ; le bloc `SPECIFICITES PROJET` est réinjecté depuis `HEAD`, et toute personnalisation du frontmatter est conservée à la main en attendant la décision sur `update.md`.
- 2026-10-26 : v5.22 (et non v6.0, aucune migration imposée) — les actions ouvertes de `signals.md` sont plafonnées à 20 ; dette, findings et pistes différées vont dans `_contexte/backlog.md` (non chargé par `/start`, entrées traitées supprimées, ligne de renvoi hors plafond). Les findings de revue de code restent une règle spécifique projet (pas d'étape de revue générique dans le kit).
- 2026-10-26 : la consigne « Base de connaissances » de `CLAUDE.md` ne déclenche pas la consultation de `DOCUMENTATION/` (0 cas sur 29 sessions d'Appli) ; création de la zone dans `SérénIATech_dev` subordonnée à l'évaluation dans Appli, et migration de la section Spécificités projet vers l'INDEX déconseillée (les déclencheurs restent dans `CLAUDE.md`).
- 2026-10-14 : `/close` attribue chaque action, décision et point d'attention à sa zone propriétaire avant écriture (la racine ne garde que la coordination transversale) et contrôle le statut Git des signaux avant d'annoncer un commit ; `/start` signale les éléments mal classés sans les déplacer. Limite assumée : 4c ne contrôle pas une roadmap posée à la racine (cas `roadmap_actions_ouvertes_luna.md`, laissée en place sur décision de l'utilisateur).
- 2026-10-14 : `/create_agent` résout le parent par la zone englobante la plus proche (pas seulement la zone racine) et lit les « Données sensibles » du `CLAUDE.md` cible pour les exclure de la lecture étendue de l'agent ; un renommage de casse refusé par le système est reporté et tracé en action P2, sans terminer de processus.
- 2026-10-13 : les règles « installation sur D: » et « `run.py` à la racine » sont posées dans `CLAUDE.md` § Spécificités projet du kit ET du template (miroir exigé par `check_kit.py`), donc déployées dans les futurs projets.
- 2026-10-12 : la substitution des placeholders de `/init_projet` se fait par remplacement littéral Python (UTF-8 sans BOM, LF), jamais par regex/`sed`/`-replace` qui interprètent `\` et `$`.
