---
type: guide
description: Travailler en session : /start, /close, /compact, roadmap et modèles recommandés
tags: guide, session, start, close, compact
maj: 2026-09-05
---

# Travailler en session

Référence : [`../../_docs/protocole_vibecoding.md`](../../_docs/protocole_vibecoding.md) (sections /start, /close, ROADMAP).

## Cycle d'une session

1. **`/start [zone]`** (Haiku) — charge le contexte : `agent_role.md` si zone-agent (affiché intégralement), puis `signals.md` (priorité absolue : actions ouvertes, blocages, dernière session), puis `contexte.md` et `roadmap*.md` si présente
2. **Travail** — traiter d'abord les actions ouvertes de signals.md ; les actions avec champ `réf:` : lire la référence avant de demander des précisions
3. **`/close [zone]`** (Sonnet) — sauvegarde l'état : contexte.md (état actuel réécrit, décisions ajoutées), signals.md (dernière session écrasée), roadmap mise à jour, commit. Si une autre zone produit une information durable utile à l'équipe, elle est aussi ajoutée sans doublon à la file de triage de `DOCUMENTATION/_contexte/signals.md` ; l’agent Documentation décide ensuite de sa publication après validation utilisateur.

Zone implicite si l'argument est absent (working directory courant). Zone inconnue : erreur listant les alias valides de `zones.md`.

## Hooks de zone

Une zone peut exécuter des actions propres au démarrage ou à la clôture sans modifier `start.md` /
`close.md` : déposer un fichier `<dossier_zone>/_contexte/on_start.md` ou `on_close.md`. Mécanisme
opt-in — absence du fichier : cycle inchangé.

Sections reconnues et point de déclenchement :

| Fichier | Section | Moment |
|---------|---------|--------|
| `on_start.md` | `## Pré-synthèse` | après chargement du contexte, avant l'affichage de `signals.md` (étape 3-bis) |
| `on_start.md` | `## Post-synthèse` | après le 🎉 final (étape 5-bis) |
| `on_close.md` | `## Pré-synthèse` | avant la production de la synthèse de session (étape 2-bis) |
| `on_close.md` | `## Fin` | après `git push`, avant le bilan des résidus (étape 14-ter) |

Contrat : titres exacts (accents inclus), section absente = no-op, toute commande non bloquante,
`## Post-synthèse` peut ne pas rendre la main, `## Fin` s'exécute même après un échec du push.
Templates : `templates/on_start_TEMPLATE.md`, `templates/on_close_TEMPLATE.md`.

## Entre phases : /compact

Compression de l'historique en place. Usage normal entre phases d'une même session ; `/close` + `/start` entre sessions. Ne pas inverser les deux mécanismes.

## Roadmap

Chantier multi-phases : une seule phase `[EN COURS]` à la fois, checkpoint /compact obligatoire entre phases — ne pas commencer la phase suivante sans confirmation écrite. Statuts mis à jour par /close, jamais en cours de session. Chargée automatiquement par /start tant qu'active. Une fois toutes ses phases achevées, l'agent propose à l'utilisateur de l'archiver ; il ne l'archive jamais automatiquement.

## Modèles

/start : Haiku — /close : Sonnet — plans, debug, refacto/migration : Opus — tâche isolée : Haiku. Le critère pour Haiku n'est pas la taille de la tâche mais la complexité du contexte.

## Économie de tokens

- Si signals.md suffit à répondre à la question immédiate, contexte.md peut être chargé à la demande
- Toute assertion sur un fichier cité exige sa lecture effective dans la session
- Chiffres et états issus de signals.md / contexte.md sont datés, pas courants : relire la source primaire avant de les énoncer au présent
