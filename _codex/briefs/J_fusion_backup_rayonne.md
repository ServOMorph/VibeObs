# Objectif
Préparer, sans l'appliquer, la fusion des correctifs de `templates/rclone_backup/backup_project.py` (kit) dans la copie divergente `D:\ServOMorph\Rayonne_Toi\claude-vibecoding-kit\rclone_backup\backup_project.py`. Critère : un diff unifié proposé, applicable sur la copie Rayonne_Toi, qui conserve `load_config` et toutes ses spécificités.

## Fichiers autorisés
- Aucun fichier modifiable. Lecture seule (sandbox read-only). Le diff proposé figure dans le message final.

## Fichiers à lire
- `templates/rclone_backup/backup_project.py` (kit, corrigé).
- `git log -p --follow -- templates/rclone_backup/backup_project.py` (kit) pour isoler les 2 correctifs.
- `D:\ServOMorph\Rayonne_Toi\claude-vibecoding-kit\rclone_backup\backup_project.py` (copie cible).
- `git -C D:\ServOMorph\Rayonne_Toi diff -- claude-vibecoding-kit/rclone_backup/backup_project.py` et `git -C D:\ServOMorph\Rayonne_Toi log -3 --oneline -- claude-vibecoding-kit/rclone_backup/`.

## Contexte autonome
Les 2 correctifs à porter : (1) exclusion des artefacts régénérables de la sauvegarde ; (2) sorties console tolérantes à l'encodage (pas de plantage sur caractères non encodables sous Windows). La copie Rayonne_Toi a divergé : elle porte une fonction `load_config` absente du template et des modifications locales non commitées d'origine inconnue, à préserver intégralement. Une session Claude Code peut être ouverte sur Rayonne_Toi : lecture seule stricte.

## Étapes
1. Identifier les commits et hunks des 2 correctifs dans le kit.
2. Comparer avec la copie cible (état de travail, modifications non commitées incluses).
3. Produire un diff unifié minimal contre l'état de travail actuel de la copie, et lister les conflits ou choix d'arbitrage.
4. Vérifier la syntaxe du fichier fusionné hypothétique en raisonnant ; si possible `python -c "import ast; ast.parse(open(...).read())"` sur la copie actuelle seulement.

## Vérification
- Indiquer si les modifications non commitées touchent les mêmes zones que les correctifs.
- Contrôle impossible : OUVERT.

## Ce qu'il ne faut pas faire
- Aucune écriture dans Rayonne_Toi ni dans le kit, aucune commande git modifiante.

Terminer par le rapport STATUT / FICHIERS / VERIFS / OUVERT, 15 lignes maximum, puis le diff proposé et la liste des arbitrages, dans le même message final.
