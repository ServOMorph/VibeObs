# Contexte — maintenance

## Objectif (immuable sauf décision explicite)
Assurer la maintenance complète du projet VibeObs (fichiers et code) et concevoir puis maintenir le template « maintenance » inséré dans les projets suivis.

## Stack / contraintes techniques (stable, rarement modifié)
- Kit VibeObs : Markdown (commandes `.claude/commands/`, fichiers de contexte), Python en bibliothèque standard (`scripts/`, `ollama_call.py`), PowerShell et Bash, tests pytest (`tests/`).
- Contrôles existants dans le kit : `scripts/check_kit.py`, `scripts/check_docs.py`, commande `/maintenance` (rapport sans modification, corrections validées lot par lot).
- Templates du kit : `templates/<nom>/`, insérés dans un projet cible par `/insert_template` ; `DEPLOYMENTS.md` liste les projets suivis.
- Installation sur le lecteur D: quand c'est possible ; `.gitattributes` du kit : `* text=auto eol=lf`.

## État actuel (réécrit intégralement à chaque /close)
Agent créé. Aucun livrable produit.

## Décisions structurantes (append only — 10 entrées max, 5 lignes max/entrée, archiver au-delà)
- 2026-11-19 : Création de l'agent maintenance (rôle : assurer la maintenance complète du projet VibeObs et concevoir puis maintenir le template « maintenance » inséré dans les projets suivis). Écriture : tout le dépôt VibeObs ; lecture étendue : projets de `DEPLOYMENTS.md` (lecture seule). Aucun projet suivi n'est nommé dans le rôle, pour pouvoir en ajouter.
