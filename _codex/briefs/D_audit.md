# Objectif
Auditer, sans rien modifier, trois fichiers de suivi du kit VibeObs et produire une liste d'anomalies précises (fichier:ligne + constat + action proposée).

## Fichiers autorisés
- Aucun. Lecture seule : ne modifier, créer ni supprimer aucun fichier.

## Fichiers à lire
- _contexte/signals.md
- _contexte/backlog.md
- tests_manuels.md
- DOCUMENTATION/20_guides/sauvegarde_rclone.md
- tout fichier du dépôt cité par un champ `réf:` (pour vérifier qu'il existe)

## Contexte autonome
Date du jour : 2026-11-14. Chaque action de signals.md et entrée de backlog.md a des champs `fait quand:` et `réf:`. Les chemins absolus hors du dépôt (D:\..., C:\...) ne sont pas lisibles : les classer « hors dépôt, non vérifiable », sans conclure.

Anomalies recherchées :
1. `réf:` citant un chemin du dépôt inexistant.
2. Action ou entrée dont le contenu contredit un fichier du dépôt (exemple connu à confirmer : signals.md « Garde-fous permanents » dit qu'un hook /close « Fin » ne peut faire que `--refresh-list`, alors que DOCUMENTATION/20_guides/sauvegarde_rclone.md décrit un passage en mode manuel).
3. Doublons de même objet entre signals.md, backlog.md et tests_manuels.md.
4. Actions sans `fait quand:` ou sans `réf:`.
5. Éléments datés de plus de 30 jours sans mise à jour.

## Étapes
1. Lire les fichiers, vérifier chaque `réf:` du dépôt.
2. Dresser la liste.

## Vérification
- Aucune commande requise. `git status` doit rester inchangé.

## Ce qu'il ne faut pas faire
- Aucune modification de fichier. Ne pas inventer : citer la ligne.

Rapport final : STATUT / FICHIERS (aucun) / VERIFS / OUVERT, puis la liste des anomalies, 25 lignes maximum au total, une anomalie par ligne.
