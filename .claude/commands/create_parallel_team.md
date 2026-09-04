---
description: Crée une équipe d'agents travaillant dans des worktrees Git isolés
argument-hint: "<chemin_projet_cible>" <dossier_equipe> [description ou chemin_fichier]
model: sonnet
---

# /create_parallel_team <chemin_projet_cible> <dossier_equipe> [description ou chemin_fichier]

## Objectif

Créer une équipe hiérarchique dont chaque membre travaille dans son propre worktree Git et sa
branche dédiée. Cette commande est réservée aux chantiers où des agents peuvent écrire du code en
parallèle : elle complète `/create_team`, qui reste adapté aux zones documentaires ou aux tâches
sans écriture concurrente.

La commande vit uniquement dans le kit. Elle ne crée jamais de worktree dans le checkout principal
du projet cible.

## [PREFLIGHT] — aucune écriture

1. Résoudre le projet cible, le dossier d'équipe et la description comme `/create_team`. Vérifier
   `.git/`, `.claude/zones.md`, `start.md` et `close.md`. Le dossier d'équipe est normalisé en
   MAJUSCULES ; son alias est en minuscules.
2. Lire `git status --short` et le signaler. Préserver tout résidu existant : ne jamais le stager,
   le déplacer ou le supprimer. Vérifier que la branche d'intégration demandée existe (par défaut
   `main`) et que chaque branche `agent/<alias>` ainsi que chaque worktree cible sont absents.
3. Vérifier que `start.md` et `close.md` acceptent le travail d'une zone hors de la branche
   d'intégration. Si le projet possède une politique de branches restrictive, demander la règle
   explicite à ajouter pour les branches `agent/<alias>` avant toute écriture.
4. Vérifier les marqueurs `<!-- COM_AGENTS -->`. Absents dans les deux : le mécanisme sera installé
   après création. Présent dans un seul : s'arrêter. Présent dans les deux : le vérifier seulement.
5. Interpréter la description en exigeant pour chaque membre : rôle durable, mode `sandbox` ou
   `code`, périmètre d'écriture, branches ou dossiers interdits, et critère de livraison. Une
   information manquante : poser une question groupée, puis afficher l'arborescence et demander une
   unique confirmation explicite.

## [ÉCRITURE] — opérations groupées après confirmation

6. Créer dans le checkout principal le coordinateur et les squelettes de tous les membres :
   `agent_role.md`, `_contexte/` et `team.md` depuis `templates/parallel_agents/`. Ajouter tous les
   alias à `zones.md` et au registre d'agents du kit. Ces squelettes sont la base commune ; ils ne
   contiennent aucun livrable applicatif.
7. Installer ou vérifier `/create_com_agents <projet cible>`, puis adapter les blocs de politique
   de branches du projet cible pour reconnaître `agent/<alias>` comme branche de travail isolée :
   elle peut exécuter `/start` et `/close`, mais ne peut ni déployer ni intégrer vers la branche
   d'intégration. Créer ensuite un commit de préparation limité à cette coordination, aux chartes
   et à `zones.md`.
8. Pour chaque membre, créer un worktree frère dans
   `<projet>.worktrees/<alias>/` avec `git worktree add -b agent/<alias> <chemin> <branche-intégration>`.
   Dans le checkout principal, remplacer les chemins des zones membres de `zones.md` par leurs
   chemins absolus de worktree puis créer un commit de configuration. Dans chaque worktree, ajuster
   uniquement le chemin de sa propre zone vers son dossier local et créer le commit d'initialisation
   de zone sur sa branche. Le rôle interdit explicitement toute écriture hors du périmètre validé.
9. Ne pas pousser, fusionner, rebase ou déployer automatiquement.

## [VALIDATION] — avant la sortie

11. Pour chaque membre, exécuter un `/start <alias>` à blanc et vérifier que la charte, le contexte
    et la branche attendue sont bien résolus. Écrire un message du coordinateur, vérifier sa lecture
    puis sa purge, et faire un `/close` à blanc qui produit un `statut.md` sans toucher à la branche
    d'intégration.
12. Vérifier `git worktree list`, `git status --short` du checkout principal et de chaque worktree,
    puis exécuter les contrôles applicables au projet. Les résidus initiaux restent hors des commits.

## [SORTIE]

13. Afficher les worktrees, branches, alias, périmètres et fichiers créés. Rappeler qu'un livrable
    de code doit être proposé au coordinateur avec commit, tests, migrations et points de validation
    avant toute intégration.
