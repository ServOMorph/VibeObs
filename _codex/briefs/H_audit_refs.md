# Objectif
Lister les références mortes et les entrées probablement déjà faites dans `_contexte/signals.md` et `_contexte/backlog.md`. Critère d'acceptation : chaque anomalie citée avec fichier:ligne et preuve (commande ou fichier lu).

## Fichiers autorisés
- Aucun fichier modifiable. Lecture seule.

## Fichiers à lire
- `_contexte/signals.md`, `_contexte/backlog.md`
- Les fichiers du dépôt cités dans leurs lignes `réf:` (chemins relatifs au dépôt seulement).
- `_codex/journal_delegation.md`, `CHANGELOG.md` (pour juger si une entrée est déjà faite).

## Contexte autonome
Chaque action porte une ligne `réf:` (chemins entre backticks) et une ligne `fait quand:`. Les chemins absolus hors dépôt (`D:\...`, `C:\...`) sont hors périmètre : les compter, ne pas les ouvrir. Un chemin suivi d'un `§` ou « étape N » : vérifier aussi que la section ou l'étape existe dans le fichier. Une entrée « probablement faite » : son critère `fait quand:` semble rempli d'après le journal ou le CHANGELOG (exemple à examiner : l'entrée de `backlog.md` sur le délai Ollama et le rapport OpenCode, au regard du lot 2026-11-15 du journal).

## Étapes
1. Extraire toutes les références relatives au dépôt des deux fichiers.
2. Tester leur existence ; pour les sections/étapes citées, chercher le titre dans le fichier.
3. Pour chaque entrée, comparer `fait quand:` au journal et au CHANGELOG.

## Vérification
- Lister le nombre de références testées, mortes, hors dépôt.

## Ce qu'il ne faut pas faire
- Aucune modification, aucun commit.
- Ne pas sortir du dépôt.

Terminer par le rapport STATUT / FICHIERS / VERIFS / OUVERT, 15 lignes maximum, puis la liste des anomalies (une ligne chacune : fichier:ligne | type mort/section absente/probablement fait | preuve). La liste doit figurer dans le même message final que le rapport.
