# Règles de validation de la maintenance

Statut : validées par l'utilisateur le 2026-11-22. Base : `.claude/commands/maintenance.md` (v7.7) et décisions des 2026-11-19, 2026-11-20 et 2026-11-21.

## 1. Périmètre
- Racine d'une maintenance = le projet où l'utilisateur la lance. Lecture, écriture et suppression dans ce projet seulement.
- Hors de ce projet : rien sans demande explicite.

## 2. Types d'éléments et actions autorisées
| Type | Sans validation | Après validation d'un lot |
|---|---|---|
| Contrôles, lecture, rapport | oui | - |
| Fichier obsolète, doublon, reliquat | non | déplacement en quarantaine |
| Document ou contexte périmé | non | correction ou archivage |
| Code mort, refacto | non | analyse seule ; exécution via roadmap ou session dédiée |
| Secret exposé | non | signalement ; correction guidée, jamais de lecture de la valeur |
| Chemin cassé | non | correction par script, lot validé |
| Commit | jamais par la commande | `/close` ou l'utilisateur |
| GitHub | jamais | l'agent guide, l'utilisateur supprime |

## 3. Exclusions absolues
- `.env*`, configuration de bot, comptes, credentials : ni lecture ni écriture (existence, statut Git, `.gitignore` seulement).
- `CLAUDE.md`, `AGENTS.md`, `GEMINI.md` : trois validations.
- Dossier `.git` ; projet avec session ouverte : passer par cette session.
- Données sensibles déclarées dans le `CLAUDE.md` du projet.

## 4. Quarantaine
- `D:\_quarantaine\<date>\` avec `manifeste.md` (élément, origine, date, motif, copie active), complété à chaque déplacement.
- Purge : lot distinct, validé à part, pour une quarantaine de plus de 30 jours.

## 5. Fréquence
- À la demande de l'utilisateur ; recommandée : après une grosse session de refacto ou de migration, puis une fois par mois.

## 6. Ollama
- Analyse déléguée seulement après contrôle que VertIA est ouvert ; jamais de donnée sensible.

