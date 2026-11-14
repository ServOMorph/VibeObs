---
type: guide
description: /telephone : réponses courtes pour petit écran, un choix à la fois, demandes rangées dans le planning
tags: guide, telephone, session
maj: 2026-11-14
---

# Mode téléphone

Commande : `/telephone` (active jusqu'à `/telephone off` ou la fin de la session). Déployée dans les
projets par `/init_projet` et `/update`. Source canonique : `.claude/commands/telephone.md`.

## Format des réponses

- 6 lignes au plus, hors bloc de choix ; ni tableau, ni titre, ni récapitulatif sans décision à prendre.
- Une seule question par réponse, par `AskUserQuestion` : 2 à 4 options, la proposition en premier
  avec « (Recommandé) » ; repli en choix numérotés si l'outil manque.
- Détail seulement sur demande (« détail », « pourquoi »). Les règles de vérification de `CLAUDE.md`
  restent entières.

## Demandes en cours de session

Chaque demande est rangée dans la roadmap active (maintenant, phase en cours, phase ultérieure,
nouvelle phase) : placement évident annoncé en une ligne, placement incertain demandé. Sans roadmap
active, l'agent propose d'en créer une. Les statuts restent à la charge de `/close`.

## Évolution

Les corrections de format faites par l'utilisateur sont écrites par `/close` dans
`_contexte/backlog.md` (catégorie `telephone`) et proposées comme modification de la commande, jamais
appliquées sans accord.
