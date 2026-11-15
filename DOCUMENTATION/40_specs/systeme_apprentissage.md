---
type: spec
description: Système d'apprentissage du kit — réduire les sollicitations non pertinentes de l'utilisateur en apprenant de ses réponses
tags: apprentissage, sollicitations, règles, v0
maj: 2026-11-15
---

# Système d'apprentissage des sollicitations

But : qu'une session (ou une session gardienne comme SérénIATech_dev) ne pose à l'utilisateur que
les questions qu'il est seul à pouvoir trancher. Chaque réponse de l'utilisateur sert à décider seul
la fois suivante, sous des règles qu'il a validées.

## Fichiers (par projet qui l'utilise)

- `_contexte/apprentissage/sollicitations.md` — ajout seul, une ligne par question posée :
  `AAAA-MM-JJ HH:MM | demandeur | catégorie | question (1 ligne) | réponse | pertinente: oui|non|? | règle candidate`
  - `pertinente: non` : l'utilisateur dit qu'on n'aurait pas dû lui demander, ou la réponse découlait
    d'une règle, d'un fichier ou d'une décision déjà écrite.
- `_contexte/apprentissage/regles.md` — règles actives, une par entrée :
  `R<n> | catégorie | condition | décision prise sans demander | origine (lignes du journal) | validée le`.

## Boucle

1. Avant de solliciter l'utilisateur : chercher une règle active dont la condition s'applique. Trouvée :
   décider selon elle, tracer `appliqué R<n>` au journal, ne pas demander.
2. Sinon : demander (une question, choix en un clic), puis journaliser la question et la réponse.
3. Candidat : deux réponses identiques à des questions de même catégorie et de même condition, ou une
   question marquée `pertinente: non`, donnent une règle candidate.
4. Promotion : proposer la règle candidate à l'utilisateur en une question groupée (au plus une fois
   par session, à `/close` de préférence). Acceptée : ajoutée à `regles.md`. Refusée : notée au
   journal, la même règle n'est plus proposée.
5. Révision : une décision prise par règle que l'utilisateur contredit désactive la règle
   (`désactivée le … : <raison>`) et repasse la catégorie en demande.

## Jamais par règle

Toujours demander, même si une règle semble couvrir le cas : action irréversible, dépense, secret ou
donnée sensible, push ou publication, écriture dans un `CLAUDE.md`/`AGENTS.md`/`GEMINI.md`, usage
GPU hors jeton VRAM, tout ce que le harnais soumet à permission.

## Mesure

Indicateurs relevés au bilan de chaque étape du protocole de test : sollicitations par session,
part `pertinente: non`, décisions par règle, règles désactivées.

## État

v0 en cours (2026-11-15) selon `DOCUMENTATION/40_specs/protocole_de_test.md` ; fiche
`tests/apprentissage/fiche.md`. Premier utilisateur : SérénIATech_dev, session gardienne des
demandes adressées à ce projet.
