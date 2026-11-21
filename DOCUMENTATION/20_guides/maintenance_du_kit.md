---
type: guide
description: /maintenance : maintenance d'un projet, nettoyage par quarantaine, rapport par lots validés un à un, amélioration de la commande
tags: guide, maintenance, qualité
maj: 2026-11-20
---

# Maintenance d'un projet

Commande : `/maintenance`. Source canonique : `.claude/commands/maintenance.md` (socle générique, plus un
bloc « SPÉCIFICITÉS PROJET » préservé par `/update` ; le bloc du kit porte `check_kit.py`,
`check_docs.py`, `DEPLOYMENTS.md` et `base_connaissances/`).

## Définition

La maintenance maintient un projet sain et cohérent sans en changer les fonctionnalités. Périmètre :
fichiers et Git, documentation et contexte, code et tests, sécurité et secrets, suppression des
fichiers obsolètes, analyse pour refacto, nettoyage de la racine et des dossiers inutiles. La limite
avec l'évolution est fixée par chaque projet dans son bloc « SPÉCIFICITÉS PROJET ».

## Principe

Lecture seule jusqu'à la validation d'un lot. La commande ne committe pas (laissé à `/close`). Les
fichiers sensibles (`.env`, configuration de bot, comptes) ne sont jamais ouverts : seuls leur
existence, leur statut Git et leur présence dans `.gitignore` sont contrôlés. Le refacto est analysé,
jamais exécuté par la commande : il passe par une roadmap ou une session dédiée.

## Suppression : la quarantaine

Aucun fichier n'est supprimé d'emblée. Un élément obsolète, suivi par Git ou non, est déplacé vers
`D:\_quarantaine\<AAAA-MM-JJ>\<projet>\` avec une ligne dans `manifeste.md` (origine, destination,
raison, suivi par Git, date). La purge définitive est un lot distinct, présenté seulement après le
délai du bloc projet et validé élément par élément. Un fichier suivi voulu dans le dépôt peut
être archivé par `git mv` vers `_archives/`.

## Procédure

0. Cadrage : bloc projet, historique des maintenances (lots refusés), retours.
1. Contrôles mécaniques du projet.
2. Fichiers et Git.
3. Racine et dossiers inutiles.
4. Documentation et contexte.
5. Code et tests.
6. Sécurité et secrets.
7. Analyse pour refacto.
8. Rapport en lots classés par risque croissant.
9. Décision et exécution, un lot par question.
10. Une ligne dans `_contexte/maintenance_historique.md`.
11. Proposition d'améliorer la commande à partir des frictions rencontrées.

## Fichiers produits dans le projet

- `_contexte/maintenance_historique.md` : une ligne par maintenance (date, contrôles, lots validés et
  refusés, éléments mis en quarantaine), versionné.
- `_contexte/maintenance_retours.md` : frictions et propositions d'amélioration de la commande.

## Amélioration continue

L'étape 11 demande à l'utilisateur s'il veut analyser la commande. Non : la maintenance est terminée.
Oui : les propositions sont consignées dans `maintenance_retours.md` ; `maintenance.md` n'est modifié
qu'avec son accord. Le kit lit les `maintenance_retours.md` des projets suivis (étape 0 de son bloc),
généralise ce qui vaut pour tous dans le template, et `/update` le diffuse sans toucher au bloc
spécifique de chaque projet.

## Sortie

Un rapport dans la conversation (pas de fichier sauf demande), puis chaque lot soumis seul ; seul un
lot validé est exécuté et les contrôles sont relancés.
