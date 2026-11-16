# Objectif
Refaire le retex de la commande `/maintenance` du kit (son étape 10), perdu le 2026-11-06. Produire uniquement des propositions, sans modifier aucun fichier.

## Fichiers autorisés
- Aucun (lecture seule).

## Fichiers à lire
- `.claude/commands/maintenance.md`
- `scripts/check_kit.py`, `scripts/check_docs.py`
- `_contexte/archive_sessions.md` : sections des sessions du 2026-11-06 et suivantes qui mentionnent `maintenance` (chercher avec `rg -n maintenance _contexte/archive_sessions.md`)
- `CHANGELOG.md` : entrées mentionnant `maintenance`, `check_kit` ou `check_docs`

## Contexte autonome
`/maintenance` est une commande à lancement manuel qui contrôle la cohérence du kit. L'analyse demandée couvre quatre axes : contrôles ratés ou manquants (incidents réels du CHANGELOG ou des sessions qu'un contrôle aurait dû attraper), étapes peu utiles ou redondantes avec `check_kit.py`/`check_docs.py`, contrôles manuels automatisables dans ces scripts, fréquence de lancement recommandée.

## Étapes
1. Lire `maintenance.md` et lister ses étapes.
2. Pour chaque étape, déterminer si `check_kit.py` ou `check_docs.py` la couvre déjà (citer fonction ou ligne).
3. Relever dans le CHANGELOG et les sessions archivées les incidents de cohérence qu'aucun contrôle n'a détectés.
4. Formuler au plus 10 propositions concrètes, chacune avec son fondement (fichier:ligne).

## Vérification
- Chaque proposition cite au moins une source fichier:ligne lue.
- Proposition sans source : la retirer ou la marquer « hypothèse ».

## Ce qu'il ne faut pas faire
- Aucune écriture, commit, push.
- Ne pas exécuter `/maintenance` ni modifier `maintenance.md`.

Terminer par le rapport STATUT / FICHIERS / VERIFS / OUVERT. Exception à la limite de 15 lignes : après OUVERT, ajouter une section `PROPOSITIONS:` d'au plus 10 lignes, une proposition par ligne, au format `[axe] proposition — source fichier:ligne`.
