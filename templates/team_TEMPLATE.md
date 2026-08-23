# Équipe — {{NOM_EQUIPE}}

## Coordinateur

- Alias : {{ALIAS_EQUIPE}}
- Zone parente : {{ALIAS_PARENT}}
- Dossier : {{DOSSIER_EQUIPE}}/

## Membres directs

| Alias | Type | Dossier | Rôle |
|---|---|---|---|
{{MEMBRES}}

## Circulation de l'information

- Les membres écrivent leur état dans `_contexte/statut.md` à chaque `/close`.
- Le coordinateur lit les statuts de ses membres directs au `/start`, les synthétise, puis fait remonter son propre statut à sa zone parente.
- Les consignes descendent exclusivement de la zone parente vers les membres directs, via leur `_contexte/messages.md`.
- Aucune communication directe ne contourne cette hiérarchie.
