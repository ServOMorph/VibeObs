---
description: Passe la session en mode téléphone — réponses très courtes, un choix à la fois, proposition mise en avant, chaque demande rangée dans le planning
---

# /telephone [off]

## Objectif

L'utilisateur travaille depuis un téléphone : lecture sur petit écran, saisie courte. Ce mode réduit
chaque réponse à ce qui permet de décider. Il reste actif jusqu'à `/telephone off` ou la fin de la
session.

## Format de chaque réponse

- 6 lignes au plus, hors bloc de choix. Pas de tableau, pas de titre, pas de récapitulatif de ce qui
  a été fait si rien ne demande de décision.
- Une seule question par réponse, posée avec l'outil `AskUserQuestion` (réponse en un clic) : 2 à
  4 options, la proposition en premier avec « (Recommandé) » dans son libellé, une raison en une
  ligne dans sa description. Le texte qui précède la question tient en une ligne d'état.
- Repli si l'outil est indisponible : choix numérotés en texte, proposition en premier et en gras.
- Le détail n'est donné que sur demande (« détail », « pourquoi »).
- Les règles de vérification de `CLAUDE.md` restent entières : une réponse courte n'autorise aucune
  affirmation non vérifiée.

## Chaque nouvelle demande

1. La ranger dans le planning actif (la roadmap `roadmap_*.md` en cours de la zone) : maintenant,
   phase en cours, phase ultérieure, ou nouvelle phase. Ranger = annoncer l'emplacement dans la
   réponse ; la roadmap n'est modifiée en session que pour ajouter une demande validée, ses statuts
   restent à la charge de `/close`.
2. Placement évident : l'annoncer en une ligne et poursuivre.
3. Placement incertain, ou demande qui change l'ordre des phases : demander, au format ci-dessus.
4. Aucun planning actif : proposer d'en créer un avant de ranger la demande.

## Évolution du mode

Chaque correction de format par l'utilisateur (trop long, question mal posée, choix manquant) est
retenue pendant la session, puis écrite par `/close` dans `_contexte/backlog.md` (catégorie
`telephone`, fichier créé à la première entrée) et proposée comme modification de cette commande.
Ne jamais modifier cette commande sans accord. Le mode n'écrit rien dans la mémoire projet.

## /telephone off

Revenir au format habituel et le confirmer en une ligne.
