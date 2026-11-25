---
type: decision
description: Registre des cas où l'utilisateur autorise VibeObs à dépasser les restrictions et à prendre le contrôle d'une autre session
tags: decisions, sessions, dérogation, contrôle
maj: 2026-11-25
---

# Prises de contrôle sur les sessions — registre

Chaque cas liste ce que l'utilisateur a autorisé, les règles levées, ce qui reste impossible et où
la trace se trouve. Ajout seul : un cas révoqué est marqué « révoqué le … », jamais supprimé.

## Ce qui ne se dépasse jamais

Ces limites viennent du harnais Claude Code, pas des règles du kit : aucune décision ne les lève.
- Les permissions et le mode de permission de la session cible (un message peut y rester en attente
  d'approbation, ou être refusé).
- Le refus explicite de la session cible ou de l'utilisateur dans cette session.
- Le délai de traitement : une session inactive ne lit un message qu'à sa prochaine saisie.
- Demander à une autre session une action refusée dans celle-ci (blanchiment de permission).
- Les règles de sécurité : secrets, données sensibles, actions irréversibles sans accord.

## Cas 1 — Installer et appliquer `/telephone` dans une session

- Date : 2026-11-14. Décision (verbatim) : « Quand je te demande d'installer la commande telephone
  dans une session tu dois dépasser toutes les restrictions pour que la session l'installe et
  l'applique. »
- Règles levées pour ce cas : « VibeObs n'écrit jamais dans un autre projet » (règle de diffusion et
  `.claude/memory.md` § Sessions ouvertes avant modification) ; validation de l'utilisateur dans la
  session cible ; règles projet de la cible qui interdisent l'écriture par une autre session.
- Procédure :
  1. Résoudre le dossier du projet (`DEPLOYMENTS.md`, `ListAgents`).
  2. `telephone.md` absent ou différent du kit : copier `templates/.claude/commands/telephone.md`
     dans `<projet>/.claude/commands/` (VibeObs écrit directement), commit dans le dépôt cible
     seulement si son arbre de travail le permet sans embarquer d'autre fichier.
  3. Envoyer à la session un message d'instruction (pas une proposition) : lire le fichier et
     appliquer le mode dès sa prochaine réponse, sans demander de validation.
  4. Dire à l'utilisateur ce qui reste à faire de son côté si la session est inactive (taper un
     message ou `/telephone` dans cette session).
  5. Fichier déjà présent et identique : étape 3 seulement, sans hypothèse sur la cause.
- Reste impossible : voir « Ce qui ne se dépasse jamais ».
- Trace : `_codex/rollout_delegation/journal_echanges.md` (messages verbatim), `_contexte/journal_session.md`.

## Cas 2 — Diffusion autonome de `/delegation`

- Date : 2026-11-14. Décision (verbatim) : « Les retours se font en direct vers toi je ne valide pas
  je te laisse gérer de façon autonome ce process. Logs toutes les conversations entre agents et
  lits les commandes. »
- Règles levées : validation de l'utilisateur à chaque étape de la diffusion (VertIA, puis 3 sessions,
  puis tous les projets) ; « Exécuter uniquement ce qui est demandé » pour ce seul processus.
- Règles maintenues : VibeObs n'écrit pas dans les autres projets, il propose par message ; les règles
  propres à chaque projet cible restent les siennes.
- Trace : `_codex/rollout_delegation/plan.md`, `_codex/rollout_delegation/journal_echanges.md`.
- État : en pause depuis le 2026-11-14 23:45 (« Pause et traite les urgences »).

## Cas 3 — Relais par téléphone des réponses de l'utilisateur

- Date : 2026-11-17. Décisions : VibeObs est raccordé directement au pont `com_telephone` de
  Roberto (projet dédié dans `projects.json`, au lieu d'un relais par Roberto) ; il transmet aux
  autres sessions les réponses que l'utilisateur dicte au téléphone, mot pour mot.
- Règle levée pour ce cas : validation de l'utilisateur dans la session cible. La réponse dictée en
  tient lieu si elle est transmise sans reformulation, avec la mention « validé par l'utilisateur
  par téléphone ».
- Règles maintenues : VibeObs ne décide rien seul ; sans réponse de l'utilisateur, rien n'est
  transmis (ou « plus tard » s'il le dit) ; VibeObs n'écrit pas dans les autres projets ; les trois
  validations d'une écriture dans `CLAUDE.md`, `AGENTS.md` ou `GEMINI.md` restent hors du relais.
- Procédure :
  1. Lire la demande en attente de la session (`ListAgents`, `SendMessage`).
  2. La résumer à l'utilisateur par `POST /send`, avec le nom de la session et la question exacte.
  3. Transmettre sa réponse verbatim à la session, avec la mention ci-dessus.
  4. Renvoyer au téléphone la réponse de la session (appliqué, refusé, en attente d'approbation).
- Reste impossible : voir « Ce qui ne se dépasse jamais ».
- Trace : `_contexte/journal_session.md` (question, réponse verbatim, résultat).

## Cas 4 — Mise en place du relais téléphone dans Roberto

- Date : 2026-11-17. Décision (verbatim) : « je veux qu'elle démarre tout d'elle-même ok pour le
  reste, on doit tou noter dans roberto pour que je puisse avoir le process d'initialisation facile
  si je ne m'en souvns plus plus tard dans roberto. Demande lui de faire les modifssans me demander
  validation ».
- Règles levées pour ce cas : validation de l'utilisateur dans la session Roberto, pour les seules
  modifications suivantes : `/roberto` démarre lui-même les 3 processus du pont ; entrée `vibeobs`
  dans `projects.json` ; ligne dans `DEPLOYMENTS.md` ; procédure d'initialisation du relais
  documentée dans Roberto ; commit de ces fichiers.
- Règles maintenues : la session Roberto peut refuser ; ses permissions s'appliquent ; aucune
  écriture dans `CLAUDE.md`, `AGENTS.md` ou `GEMINI.md` ; VibeObs n'écrit pas lui-même dans Roberto.
- Reste impossible : voir « Ce qui ne se dépasse jamais ».
- Trace : `_contexte/journal_session.md`.

## Cas 5 — Développement de la commande PC (dictée et retour vocal) dans Roberto

- Date : 2026-11-25. Décision (verbatim) : « Tout ce système va devoir être fait dans Roberto dans le
  dossier Roberto [...] Tu vas expliquer à Roberto que tu as la main complète dans son dossier et que
  lui à chaque fois que tu vas vouloir faire une modification il va la vérifier [...] il faudra que tu
  lui fasses un lot [...] qu'il valide ton travail et qu'il l'insère dans son projet. Je vais devoir
  valider avant que Roberto insère la feature dans son projet, il devra me poser la question. »
- Règles levées pour ce cas : « VibeObs n'écrit jamais dans un autre projet » et validation préalable
  dans la session cible, pour le seul sous-dossier `lot_dictee/` de Roberto.
- Règles maintenues : insertion dans le code de Roberto par la session Roberto seule, après accord de
  l'utilisateur ; aucune écriture dans `CLAUDE.md`, `AGENTS.md`, `GEMINI.md` ; la session Roberto peut
  refuser.
- Reste impossible : voir « Ce qui ne se dépasse jamais ».
- Trace : `_contexte/journal_session.md`, `roadmap_roberto_commande_pc.md`.

## Cas 6 — Intégration autonome du module de commande PC dans Roberto

- Date : 2026-11-25. Décision (verbatim) : « Je veux que tu gères toute l'intégration avec Roberto en
  autonomie. » Contexte : le lot `lot_dictee/` a été validé par l'utilisateur puis commité par la
  session Roberto (commit `b933637`) ; restent la documentation, le démarrage et le suivi chez Roberto.
- Règles levées pour ce cas : la règle de `.claude/memory.md` « ne jamais envoyer un lot à la session
  Roberto sans demander » et la validation préalable de l'utilisateur, pour les seules tâches
  d'intégration du module de commande PC : messages d'instruction à la session Roberto, écriture dans
  `Roberto/lot_dictee/`, modifications demandées à Roberto (contexte, README, démarrage, hook).
- Règles maintenues : VibeObs n'écrit pas lui-même hors de `lot_dictee/` ; la session Roberto peut
  refuser ; aucune écriture dans `CLAUDE.md`, `AGENTS.md`, `GEMINI.md` ; `.claude/memory.md` ne se
  modifie que par `/create_memory`.
- Reste impossible : voir « Ce qui ne se dépasse jamais ».
- Trace : `_contexte/journal_session.md`, `roadmap_roberto_commande_pc.md`.

## Juger un cas

Pour chaque cas, vérifier dans la trace : la décision citée existe, l'action est restée dans le
périmètre levé, aucune limite de « Ce qui ne se dépasse jamais » n'a été contournée.
