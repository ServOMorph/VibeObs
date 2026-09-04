---
type: guide
description: Créer une équipe d'agents avec worktrees Git et branches isolés
tags: guide, équipe, agents, worktree, git
maj: 2026-09-04
---

# Équipes d'agents parallèles

Commande : `/create_parallel_team <chemin_projet_cible> <dossier_equipe> [description ou fichier]`.
Elle complète `/create_team` quand au moins un agent doit modifier du code en parallèle.

## Modèle

Chaque membre reçoit une branche `agent/<alias>` et un worktree frère de la racine du projet.
Le checkout principal reste la branche d'intégration, par défaut `main`. Le coordinateur y lit les
statuts et transmet les consignes ; les agents ne fusionnent ni ne déploient.

| Mode | Écriture | Usage |
|---|---|---|
| `sandbox` | dossier d'agent uniquement | analyse, spécification, prototype isolé, tests préparatoires |
| `code` | périmètre explicitement autorisé dans son worktree | évolution applicative préparée pour intégration |

## Communication et intégration

Les statuts remontent par `_contexte/statut.md`. Les messages du parent passent par
`messages.md`, renommé en `messages.processing.md` avant lecture afin qu'un nouveau message ne soit
pas effacé pendant le traitement. Un coordinateur est l'unique émetteur vers chaque membre.

Un agent code livre un commit, les fichiers concernés, les tests exécutés, les migrations et les
points de validation. Le coordinateur propose l'intégration ; l'utilisateur l'autorise
explicitement. Aucun merge, rebase, push ou déploiement n'est automatique.

## Préconditions

- Projet Git initialisé et branche d'intégration identifiée.
- `start.md` et `close.md` reconnaissent les branches `agent/<alias>` ; un projet à politique de
  branches restrictive doit recevoir cette règle dans son bloc de spécificités.
- Les résidus déjà présents dans le checkout principal sont conservés et exclus des commits créés
  par la commande.
