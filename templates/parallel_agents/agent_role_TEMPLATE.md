# Rôle — {{DOSSIER_AGENT}}

## Rôle
{{ROLE}}

## Mode d'exécution
- Type : {{MODE_AGENT}}
- Worktree : {{WORKTREE}}
- Branche dédiée : {{BRANCHE}}
- Branche d'intégration : {{BRANCHE_INTEGRATION}}

## Périmètre
- Dossier de sortie : {{DOSSIER_AGENT}}/
- Peut lire : son worktree, la racine du projet et les documents de contexte non sensibles nécessaires à son rôle
- Peut écrire : {{ECRITURE_AUTORISEE}}
- Ne doit pas modifier : {{ECRITURE_INTERDITE}}
- Peut mettre à jour son propre `_contexte/` via `/start` et `/close`

## Coordination
- Remonte son état uniquement à `{{ALIAS_PARENT}}` via son `_contexte/statut.md` à chaque `/close`.
- Reçoit les consignes uniquement de `{{ALIAS_PARENT}}` via son `_contexte/messages.md` au `/start`.
- Ne fusionne, ne rebase et ne déploie jamais sans demande explicite du coordinateur ou de l'utilisateur.
- Toute évolution intégrable doit préciser le commit, les fichiers concernés, les tests exécutés et les migrations éventuelles.

## Invariants
- Ne travaille que dans le worktree déclaré.
- Ne commit que sur `{{BRANCHE}}`.
- Ne modifie jamais `{{BRANCHE_INTEGRATION}}` directement.
- Ses livrables restent dans son dossier d'agent jusqu'à une intégration explicitement validée.

## Méta
- Zone parente : {{ALIAS_PARENT}}
- Alias zones.md : {{ALIAS_AGENT}}
- Créé le : {{DATE}}
