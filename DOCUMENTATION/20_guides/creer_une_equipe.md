---
type: guide
description: Créer une équipe hiérarchique d'agents avec /create_team
tags: guide, équipe, agents, communication
maj: 2026-08-23
---

# Créer une équipe d'agents

Commande : `/create_team <chemin_projet_cible> <dossier_equipe> [description ou fichier]`.
Elle s'exécute depuis le kit, jamais depuis le projet cible.

## Modèle

Une équipe est un coordinateur-agent, placé dans son propre dossier. Elle contient des agents et
éventuellement des sous-équipes. Chaque équipe possède `team.md`, manifeste de ses membres directs
et de son parent. Les alias sont hiérarchiques (`communication-site_internet`, par exemple).

## Communication

Les statuts remontent d'un membre vers son parent et les messages descendent du parent vers ses
membres directs. Les échanges utilisent `_contexte/statut.md` et `_contexte/messages.md`.
`/create_team` installe automatiquement ce mécanisme via `/create_com_agents`.

## Entrée et sécurité

La description peut être collée ou lue depuis un fichier. La commande complète seulement les
informations indispensables absentes, affiche l'arborescence interprétée, puis attend une unique
confirmation avant toute écriture. Les agents gardent par défaut un périmètre limité à leur dossier.

## Ajouts ultérieurs

`/create_agent ... parent=<alias_equipe>` ajoute un agent à une équipe et met à jour son `team.md`.
`/create_team ... parent=<alias_equipe>` crée une sous-équipe. Les structures plates existantes
restent supportées par `/create_com_agents`.
