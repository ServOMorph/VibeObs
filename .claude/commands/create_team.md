---
description: Crée une équipe hiérarchique d'agents dans un projet cible, exécutable depuis le kit
argument-hint: "<chemin_projet_cible>" <dossier_equipe> [description ou chemin_fichier] [parent=<alias_equipe>]
model: sonnet
---

# /create_team <chemin_projet_cible> <dossier_equipe> [description ou chemin_fichier] [parent=<alias_equipe>]

## Objectif

Créer une équipe composée d'un **coordinateur-agent** et de ses membres directs. Une équipe est
un sous-dossier du projet cible et reste une zone à rôle : elle possède `agent_role.md`,
`_contexte/` et un manifeste `team.md`. Les agents et sous-équipes restent ajoutables ensuite.

Cette commande est kit-only, comme `/create_agent` : ne jamais la copier dans le projet cible.

## Contrat d'organisation

- Chaque membre remonte son état à son parent direct via `_contexte/statut.md`.
- Chaque parent donne des consignes à ses membres directs via `_contexte/messages.md`.
- Le coordinateur agrège seulement les statuts de ses membres directs ; il remonte ensuite sa
  propre synthèse. La zone racine ne lit donc que les statuts de ses équipes directes.
- Une équipe peut contenir des agents et des sous-équipes. Les échanges qui contournent le parent
  sont interdits.

## [PREFLIGHT] — aucune écriture

1. Résoudre le projet cible comme `/create_agent` : gérer les chemins avec espaces par préfixes
   croissants jusqu'à trouver `.claude/zones.md`. Dossier d'équipe absent : le demander. Le
   normaliser en MAJUSCULES.
2. Vérifier dans le projet cible : `.claude/zones.md`, `.claude/commands/start.md` et `close.md`.
   Un fichier absent : s'arrêter ; le projet doit d'abord passer par `/init_projet`.
3. Résoudre le parent : par défaut la zone racine (ligne de `zones.md` qui pointe sur la racine du
   projet). Un argument `parent=<alias>` peut le remplacer. L'alias parent doit pointer vers un
   dossier muni de `team.md`, sauf pour la zone racine.
4. Construire l'alias de l'équipe : `<alias-parent>-<nom-équipe-en-minuscules>`, en retirant le
   préfixe parent uniquement quand l'équipe est directement sous la racine (ex. `communication`,
   puis `communication-reseaux_sociaux`). Vérifier son unicité dans `zones.md`, l'absence du
   dossier cible et l'absence d'un membre homonyme. En cas de collision, s'arrêter et demander un
   autre nom ; jamais d'écrasement.
5. Vérifier les marqueurs `<!-- COM_AGENTS -->` de `start.md` et `close.md`. Absents dans les deux :
   la commande installera le mécanisme après confirmation. Présent dans un seul : signaler l'état
   incohérent et attendre une instruction. Présent dans les deux : le mécanisme sera seulement
   vérifié, jamais réinséré.

## [COLLECTE] — description, puis une seule validation

6. Accepter soit du texte collé, soit le chemin d'un fichier Markdown/texte lisible. Ne jamais
   déplacer ni modifier le fichier source. Extraire : rôle durable du coordinateur, membres directs
   (nom, type agent/équipe, rôle durable) et périmètre exceptionnel éventuel.
7. Une information indispensable manquante (rôle durable ou type d'un membre) : poser uniquement
   la question correspondante. Par défaut, chaque membre écrit dans son propre dossier ; ne jamais
   inventer d'extension de périmètre.
8. Afficher le plan interprété : arborescence, alias, parent, rôle et périmètre de chaque zone.
   Demander une unique confirmation explicite. Sans « oui », n'écrire aucun fichier.

## [ÉCRITURE] — opérations groupées après confirmation

9. Créer `<parent-dossier>/<EQUIPE>/` (ou `<projet>/<EQUIPE>/` si parent racine) et y écrire :
   - `agent_role.md` depuis `templates/agent_role_TEMPLATE.md`, avec `{{ALIAS_PARENT}}` = alias du
     parent, `{{ALIAS_AGENT}}` = alias équipe, rôle collecté et `{{COMMUNICATION_HIERARCHIQUE}}` =
     l'exception explicite : lecture des `statut.md` et écriture des `messages.md` des membres
     directs seulement ;
   - `_contexte/contexte.md` et `signals.md` depuis les templates ;
   - `team.md` depuis `templates/team_TEMPLATE.md`, contenant le parent et la table des membres.
10. Ajouter la ligne de l'équipe à `zones.md`. Pour chaque membre de type **agent**, créer son
    dossier dans l'équipe en appliquant les mêmes règles et fichiers que `/create_agent`, mais avec
    `{{ALIAS_PARENT}}` = alias équipe. Son alias est `<alias-équipe>-<membre>` et son périmètre reste
    son dossier ; sa charte lui autorise seulement l'écriture de son propre contexte.
11. Pour chaque membre de type **équipe**, exécuter récursivement cette commande avec l'alias de
    l'équipe créée comme parent, sans réutiliser de confirmation globale déjà donnée.
12. Mettre à jour la table des membres de chaque `team.md` parent après toutes les créations.
    Ajouter chaque coordinateur et chaque agent au `AGENTS_REGISTRY.md` du kit avec son alias,
    chemin, rôle, date et verdict « à évaluer ». Ajouter un bref retour dans
    `base_connaissances/ameliorations_create_agent.md` en précisant « création via create_team ».
13. Installer ou vérifier immédiatement `/create_com_agents <projet cible>`. Cette sous-commande
    adapte `start.md` et `close.md` au mécanisme hiérarchique ; elle ne doit pas modifier les
    chartes, `team.md` ni `zones.md`.

## [SORTIE]

14. Afficher une seule fois les fichiers créés/modifiés, avec liens absolus, l'arborescence créée et
    les alias. Rappeler : les périmètres sont déclaratifs, sauf les accès explicitement autorisés
    aux deux fichiers de communication des membres directs.
15. Confirmer : « ✅ Équipe <alias> créée dans <chemin>. Lancer /start <alias> pour coordonner
    l'équipe. »

<!-- SPECIFICITES PROJET : DEBUT (préservé par /update, ne pas toucher hors de ce bloc) -->
<!-- SPECIFICITES PROJET : FIN -->
