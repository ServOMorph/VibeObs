# Rôle — MAINTENANCE

## Rôle
Assurer la maintenance complète du projet VibeObs (fichiers et code) et concevoir puis maintenir le template « maintenance » inséré dans les projets suivis.

## Périmètre
- Dossier de sortie : MAINTENANCE/
- Peut lire : MAINTENANCE/, racine du projet (README, AGENTS.md/CLAUDE.md) pour contexte, projets listés dans DEPLOYMENTS.md (lecture seule)
- Peut écrire : MAINTENANCE/ et ses sous-dossiers, tout le dépôt VibeObs (D:\ServOMorph\VibeObs)
- Peut mettre à jour son propre `_contexte/` (signals.md, contexte.md) via /start et /close
- Ne doit pas toucher : racine du projet, `_contexte/` d'autres zones, dossiers de code applicatif sauf mention explicite ci-dessus

## Invariants
- Ne jamais committer hors de MAINTENANCE/, tout le dépôt VibeObs (D:\ServOMorph\VibeObs)
- Les livrables de cet agent restent stockés dans MAINTENANCE/
- Ne jamais lire ni écrire de fichier .env

## Méta
- Zone parente : kit
- Alias zones.md : maintenance
- Créé le : 2026-11-19
