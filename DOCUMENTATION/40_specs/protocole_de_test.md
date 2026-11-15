---
type: spec
description: Protocole obligatoire pour tester toute nouvelle fonction (commande, script, template, système) avant son import dans le kit
tags: tests, protocole, v0, v1, import
maj: 2026-11-15
---

# Protocole de test avant import

S'applique à toute fonction nouvelle ou modifiée en profondeur : commande, script, template, système
(apprentissage, délégation, etc.). Aucun import dans `templates/` ni diffusion par `/update` sans les
trois étapes ci-dessous, dans l'ordre. Une étape échouée renvoie à la précédente.

## Fiche de test

Un fichier par fonction : `tests/<fonction>/fiche.md` (racine du kit), créé avant la v0 :
- objectif en une phrase et critères de réussite observables (3 à 6, chacun vérifiable par une
  commande, un fichier ou une réponse) ;
- périmètre : fichiers créés ou modifiés, ce qui est hors test ;
- risques et retour arrière (comment désactiver la fonction) ;
- journal : une ligne par essai, en ajout seul,
  `AAAA-MM-JJ HH:MM | v0|v1 | testeur | cas | résultat (ok|ko) | constat | suite`.

## v0 — essai par l'auteur

- Lieu : le dépôt de l'auteur seulement (kit ou projet pilote), jamais dans `templates/`.
- Au moins un cas nominal et un cas limite par critère, exécutés réellement ; chaque essai journalisé.
- Sortie : tous les critères `ok` sur un essai réel. Bilan de 5 lignes au journal (marché, échoué,
  modifié). L'utilisateur est informé, sans validation requise sauf action irréversible.

## v1 — testeurs

- 3 sessions testeuses (projets différents), choisies pour couvrir des usages distincts ; aucune ne
  reçoit la fonction par `/update` : copie ciblée, annoncée par message avec la fiche.
- Chaque testeur l'utilise sur au moins un cas réel de son projet et renvoie par message un retour
  structuré : `fonction | cas | ok|ko | friction | proposition`. VibeObs journalise chaque retour
  verbatim dans la fiche.
- Correctifs : appliqués dans la version testée, puis renvoyés aux testeurs concernés ; un correctif
  qui change un critère relance la v0.
- Sortie : 3 testeurs `ok` sur leurs cas, aucun `ko` ouvert, bilan v1 de 5 lignes.

## Import

- Validation de l'utilisateur en une question (fiche et bilans v0/v1 en référence) ; pour un texte
  destiné à un `CLAUDE.md`, `AGENTS.md` ou `GEMINI.md`, la règle des trois validations s'ajoute.
- Copie dans `templates/`, entrée `CHANGELOG.md`, `/doc_sync`, puis diffusion par `/update`.
- La fiche reste dans `tests/<fonction>/` comme trace ; une régression constatée après import rouvre
  une v1.
