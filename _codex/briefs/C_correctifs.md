# Objectif
Corriger 3 défauts des commandes du kit VibeObs (fichiers Markdown d'instructions pour Claude Code). Critère : les 3 corrections présentes, `python scripts/check_kit.py` affiche « Tous les contrôles sont passants ».

## Fichiers autorisés
- .claude/commands/close.md (uniquement entre les marqueurs `<!-- SPECIFICITES PROJET : DEBUT` et `FIN -->`)
- .claude/commands/init_projet.md et templates/.claude/commands/init_projet.md (miroirs : contenu identique)
- .claude/commands/update.md et templates/.claude/commands/update.md (miroirs : contenu identique)

## Fichiers à lire
- les fichiers autorisés ; scripts/check_kit.py

## Contexte autonome
Style : français, phrases courtes, même mise en forme que le reste du fichier. Ne rien reformuler hors des passages corrigés.

1. close.md, bloc SPECIFICITES PROJET, « Étape 14bis » : la condition « Vérifier si `DEPLOYMENTS.md` fait partie des fichiers modifiés de cette session (voir `git diff --name-only` de l'étape 13) » ne peut jamais être vraie car `DEPLOYMENTS.md` est gitignoré. La remplacer par : comparer la date de dernière modification de `DEPLOYMENTS.md` (`(Get-Item DEPLOYMENTS.md).LastWriteTime`) à la date du commit précédant celui de l'étape 13 (`git log -1 --skip=1 --format=%cI`) ; plus récente = modifié pendant la session. Garder le reste de l'étape.
2. init_projet.md, étape « 5. Commit initial (si réponse "oui" à Q4) » : si `$ARGUMENTS/.git` est absent, exécuter d'abord `git -C "$ARGUMENTS" init` (et le signaler au bilan) avant les `git add`. Appliquer aux deux miroirs.
3. update.md : `/update` ne recopie jamais `<kit>/Protocole_start_close_context.md` vers `<cible>/_docs/protocole_vibecoding.md` (copie figée à la version de l'init). Ajouter cette copie à l'étape 5 (tableau des fichiers copiés tels quels ; créer `_docs/` si absent), l'ajouter au `git add` de l'étape 9 (`_docs/protocole_vibecoding.md`), au contrôle 1 de l'étape 10 (comparé à `Protocole_start_close_context.md` du kit) et à la liste des fichiers de l'étape 11. Ne pas toucher au mode initialisation de l'étape 2. Appliquer aux deux miroirs.

## Étapes
1. Lire les fichiers, appliquer les 3 corrections.
2. Vérifier que chaque paire de miroirs est identique (`git diff --no-index` entre les deux).
3. Lancer `python scripts/check_kit.py`.

## Vérification
- `python scripts/check_kit.py` -> « Tous les contrôles sont passants ».
- `git diff --stat` -> seuls les 5 fichiers autorisés.

## Ce qu'il ne faut pas faire
- Aucun commit, push, ni changement dans CHANGELOG.md, README.md ou d'autres fichiers.

Terminer par le rapport STATUT / FICHIERS / VERIFS / OUVERT, 15 lignes maximum.
