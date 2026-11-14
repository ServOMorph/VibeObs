---
type: guide
description: /maintenance : contrôler le kit, repérer les dérives, rapport par lots validés un à un
tags: guide, maintenance, qualité
maj: 2026-11-14
---

# Maintenance du kit

Commande kit seulement : `/maintenance`. Source canonique : `.claude/commands/maintenance.md`.

## Principe

Lecture seule jusqu'à la validation d'un lot. Aucun fichier n'est supprimé : un obsolète est archivé
dans `_archives/` par `git mv`. La commande ne committe pas (laissé à `/close`). Les fichiers sensibles
(`.env`, configuration de bot, comptes) ne sont jamais ouverts : seuls leur existence, leur statut
Git et leur présence dans `.gitignore` sont contrôlés.

## Ce qui est contrôlé

1. Contrôles mécaniques : `check_kit.py`, `check_docs.py`, `pytest`, `git status`.
2. Dépôt Git : modifiés non commités, non suivis (à suivre, à ignorer ou étrangers au kit).
3. Reliquats à la racine : fichiers sans rapport, dossiers vides, copies divergentes de templates.
4. Roadmaps sans mouvement depuis plus de 30 jours.
5. Documentation : version du `README.md` et de `llms.txt`, taille du `CHANGELOG.md`, guides de
   `DOCUMENTATION/` en retard sur le CHANGELOG, `base_connaissances/`, `tests_manuels.md`.
6. Contexte de session : plafond de 20 actions, `réf:` existantes, backlog, `zones.md`, `DEPLOYMENTS.md`.
7. Sécurité : `.gitignore` et aucun credential suivi par Git.

## Sortie

Un rapport dans la conversation (pas de fichier sauf demande), avec des lots classés par risque
croissant. Chaque lot est soumis seul, une question à la fois ; seul un lot validé est exécuté, puis
`check_kit.py` est relancé. Une fois tous les lots tranchés, la commande propose d'analyser la
maintenance elle-même, sans modifier `maintenance.md` sans accord.
