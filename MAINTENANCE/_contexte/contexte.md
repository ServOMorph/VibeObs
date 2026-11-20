# Contexte — maintenance

## Objectif (immuable sauf décision explicite)
Assurer la maintenance complète du projet VibeObs (fichiers et code) et concevoir puis maintenir le template « maintenance » inséré dans les projets suivis.

## Stack / contraintes techniques (stable, rarement modifié)
- Kit VibeObs : Markdown (commandes `.claude/commands/`, fichiers de contexte), Python en bibliothèque standard (`scripts/`, `ollama_call.py`), PowerShell et Bash, tests pytest (`tests/`).
- Contrôles existants dans le kit : `scripts/check_kit.py`, `scripts/check_docs.py`, commande `/maintenance` (rapport sans modification, corrections validées lot par lot).
- Templates du kit : `templates/<nom>/`, insérés dans un projet cible par `/insert_template` ; `DEPLOYMENTS.md` liste les projets suivis.
- Installation sur le lecteur D: quand c'est possible ; `.gitattributes` du kit : `* text=auto eol=lf`.
- Scripts de `MAINTENANCE/scripts/` : bibliothèque standard, sauf `lancer_sur_bureau.py` qui exige `pyvda` (venv hors dépôt `D:\_outils\venv_bureaux`). Dépôt VibeObs public : pas de secret ni d'identifiant dans les fichiers commités.

## État actuel (réécrit intégralement à chaque /close)
Migration des projets de C: vers D: presque terminée : 11 projets et 1 doublon en quarantaine, `TableauDeBord` et `ffmpeg` copiés sur D: (originaux gardés jusqu'au prochain redémarrage), site `site_internet_Sereniatech_V2` laissé sur C: sur ordre de l'utilisateur.
Scripts livrés : `migrer_projet.py` (12 tests), `lancer_sur_bureau.py`, `balayer_chemins.py`. Périmètre de la maintenance et règles de validation : à définir (action P1).

## Décisions structurantes (append only — 10 entrées max, 5 lignes max/entrée, archiver au-delà)
- 2026-11-19 : Création de l'agent maintenance (rôle : assurer la maintenance complète du projet VibeObs et concevoir puis maintenir le template « maintenance » inséré dans les projets suivis). Écriture : tout le dépôt VibeObs ; lecture étendue : projets de `DEPLOYMENTS.md` (lecture seule). Aucun projet suivi n'est nommé dans le rôle, pour pouvoir en ajouter.
- 2026-11-20 : Droits élargis décidés par l'utilisateur : lecture, écriture et suppression dans les autres projets et sur le PC (`agent_role.md` encore en lecture seule, à aligner). Toute suppression passe par la quarantaine `D:\_quarantaine\<date>\` avec `manifeste.md`, validation par lot ; GitHub : l'agent guide, l'utilisateur supprime ; scripts Python au maximum ; analyse déléguée à Ollama après contrôle que VertIA est ouvert ; session VS Code gardée ouverte, maintenance relancée après un redémarrage.
- 2026-11-20 : Migration par `scripts/migrer_projet.py` (copier, verifier, chemins, quarantaine `--confirmer`) : comparaison SHA-256, `--sans-lecture` pour les dossiers sensibles, `.env*` jamais lus, `CLAUDE.md`, `AGENTS.md` et `GEMINI.md` jamais modifiés par le script (trois validations).
