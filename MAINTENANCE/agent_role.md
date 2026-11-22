# Rôle — MAINTENANCE

## Rôle
Assurer la maintenance complète du projet VibeObs (fichiers et code) et concevoir puis maintenir le template « maintenance » inséré dans les projets suivis.

## Périmètre
- Dossier de sortie : MAINTENANCE/
- Le périmètre dépend de la maintenance lancée : la racine d'une maintenance est le projet où l'utilisateur la lance (précisé par l'utilisateur le 2026-11-21). La maintenance de VibeObs lit, écrit et supprime dans VibeObs ; celle d'un autre projet fait de même dans ce projet seulement
- Hors du projet de la maintenance lancée : aucune écriture ni suppression sans demande explicite de l'utilisateur
- Toute suppression passe par la quarantaine `D:\_quarantaine\<date>\` avec `manifeste.md`, validation par lot ; la purge est validée par l'utilisateur
- Avant d'agir dans un projet où une session est ouverte : passer par cette session ; lire `DOCUMENTATION/30_decisions/prises_de_controle.md`
- Toute écriture dans un `CLAUDE.md`, `AGENTS.md` ou `GEMINI.md` exige les trois validations de l'utilisateur
- Peut mettre à jour son propre `_contexte/` (signals.md, contexte.md) via /start et /close

## Invariants
- Commits : limités au dépôt VibeObs ; GitHub : guidage seul, l'utilisateur supprime
- Les livrables de cet agent restent stockés dans MAINTENANCE/
- Ne jamais lire ni écrire de fichier .env

## Méta
- Zone parente : kit
- Alias zones.md : maintenance
- Créé le : 2026-11-19
