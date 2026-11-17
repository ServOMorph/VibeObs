# Objectif
Comparer la version du kit déclarée pour chaque projet dans `DEPLOYMENTS.md` avec la version réellement présente dans le projet, et relever l'état git de chaque projet. Critère : un tableau complet, une ligne par projet, chaque valeur sourcée.

## Fichiers autorisés
- Aucun fichier modifiable. Lecture seule (sandbox read-only).

## Fichiers à lire
- `DEPLOYMENTS.md` (racine du kit).
- Dans chaque projet listé : `.claude/commands/start.md`, `.claude/commands/close.md`, `.claude/commands/update.md` (ligne de version ou en-tête), `.claude/kit_version*` ou tout fichier de version présent, et `git -C <projet> status -sb`, `git -C <projet> log -1 --oneline`.
- `CHANGELOG.md` du kit (pour identifier la version d'un fichier si aucune ligne de version explicite).

## Contexte autonome
`DEPLOYMENTS.md` liste les projets où le kit vibecoding est déployé et leur version. Version courante du kit : v6.7. Les projets peuvent avoir une session Claude Code ouverte : lecture seule stricte, aucune commande git qui écrit (pas de fetch, pull, stash, gc). Exclusion absolue : tout chemin contenant `SérénIATech_dev` ou `SerenIATech` (ne pas lire, noter « exclu »). `Moulin du Sud` est dans le dépôt `Lieux_Hybrides`, dossier `lieux/` : interroger git depuis la racine du dépôt.

## Étapes
1. Extraire de `DEPLOYMENTS.md` la liste projet / chemin / version déclarée.
2. Pour chaque projet non exclu : déterminer la version réelle et la source de cette déduction.
3. Relever `status -sb` (branche, avance/retard sur l'amont connu localement, nombre de fichiers modifiés) et le dernier commit.

## Vérification
- Nombre de projets lus, exclus, introuvables.
- Contrôle impossible (chemin absent, pas un dépôt git) : le signaler dans OUVERT.

## Ce qu'il ne faut pas faire
- Aucune écriture, aucune commande réseau, aucune commande git modifiante.
- Ne pas afficher le contenu des fichiers modifiés, seulement leur nombre.

Terminer par le rapport STATUT / FICHIERS / VERIFS / OUVERT, 15 lignes maximum, puis le tableau : projet | version déclarée | version réelle (source) | écart oui/non | git (branche, ahead/behind, nb modifiés) | dernier commit. Le tableau doit figurer dans le même message final.
