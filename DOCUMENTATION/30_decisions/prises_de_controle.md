---
type: decision
description: Registre des cas où l'utilisateur autorise VibeObs à dépasser les restrictions et à prendre le contrôle d'une autre session
tags: decisions, sessions, dérogation, contrôle
maj: 2026-11-14
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

## Juger un cas

Pour chaque cas, vérifier dans la trace : la décision citée existe, l'action est restée dans le
périmètre levé, aucune limite de « Ce qui ne se dépasse jamais » n'a été contournée.
