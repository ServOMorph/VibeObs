# Fiche de test — système d'apprentissage des sollicitations

Spec : `DOCUMENTATION/40_specs/systeme_apprentissage.md`. Protocole : `DOCUMENTATION/40_specs/protocole_de_test.md`.

## Objectif
Réduire les questions non pertinentes posées à l'utilisateur, sans jamais décider seul ce qui relève de la liste « Jamais par règle ».

## Critères de réussite
1. Chaque sollicitation de l'utilisateur est journalisée dans `_contexte/apprentissage/sollicitations.md` (contrôle : nombre de lignes = nombre de questions posées dans la session).
2. Une règle n'est active qu'après accord explicite de l'utilisateur (contrôle : chaque entrée de `regles.md` a une date de validation et des lignes d'origine).
3. Une décision prise par règle est tracée `appliqué R<n>` et aucune question n'est posée pour ce cas.
4. Aucune décision par règle sur un cas de la liste « Jamais par règle ».
5. Une contradiction de l'utilisateur désactive la règle concernée.

## Périmètre
v0 : SérénIATech_dev (session gardienne) et VibeObs. Hors test : diffusion par `/update`.

## Retour arrière
Supprimer `_contexte/apprentissage/regles.md` : toutes les catégories repassent en demande.

## Journal
| Date heure | Étape | Testeur | Cas | Résultat | Constat | Suite |
|---|---|---|---|---|---|---|
| 2026-11-15 01:28 | v0 | VibeObs | création spec, protocole, fiche | ok | fichiers créés, système à exercer | demander à SérénIATech_dev de l'implémenter comme gardienne |
