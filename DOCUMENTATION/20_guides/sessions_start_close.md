---
type: guide
description: Travailler en session : /start, /close, /compact, journal de session, roadmap et modèles recommandés
tags: guide, session, start, close, compact, journal
maj: 2026-11-14
---

# Travailler en session

Référence : [`../../_docs/protocole_vibecoding.md`](../../_docs/protocole_vibecoding.md) (sections /start, /close, ROADMAP).

## Cycle d'une session

1. **`/start [zone]`** (Haiku) — charge le contexte : `agent_role.md` si zone-agent (affiché intégralement), puis `signals.md` (priorité absolue), `contexte.md`, `roadmap*.md` si présente et `journal_session.md` s'il existe. Affichage réduit par défaut : « Prochaine étape exacte » et « Question bloquante » mot pour mot, puis une ligne de compteurs (`Actions ouvertes : N (dont P1 : x) · Backlog : B · Phase en cours : <titre>`, partie sans objet retirée) ; `signals.md` entier avec `--complet` ou si l'une des deux sections manque. Les `réf:` lues sont celles des seules actions citées par la prochaine étape, même en `--complet`. Un journal non vide est signalé « Journal non intégré » avant les compteurs (session précédente non close)
2. **Travail** — traiter d'abord les actions ouvertes de signals.md ; les actions avec champ `réf:` : lire la référence avant de demander des précisions
3. **`/close [zone]`** (Sonnet) — lit d'abord le journal de session, puis sauvegarde l'état : contexte.md (état actuel réécrit, décisions ajoutées), signals.md (dernière session écrasée), roadmap mise à jour, commit. Si une autre zone produit une information durable utile à l'équipe, elle est aussi ajoutée sans doublon à la file de triage de `DOCUMENTATION/_contexte/signals.md` ; l’agent Documentation décide ensuite de sa publication après validation utilisateur. Les éléments non résolus sont triés : seul ce qui appelle une action ou une décision dans les prochaines sessions reste dans `signals.md` (≤ 20 entrées) ; la dette technique, les findings de revue non corrigés et les pistes différées vont dans `_contexte/backlog.md` (ajout en fin de fichier, entrées traitées supprimées, non chargé par `/start`, représenté par une ligne « Backlog : N entrées » dans `signals.md` ; chaque entrée a une catégorie et un `réf:` vérifié, et `/close` propose en bilan la promotion des entrées dont le `réf:` cite un fichier modifié). Après le commit constaté, le journal est vidé.

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
| `on_close.md` | `## Fin` | après le commit (étape 13) et le push conditionnel (étape 14), avant le bilan des résidus (étape 14-ter) |

Contrat : titres exacts (accents inclus), section absente = no-op, toute commande non bloquante,
`## Post-synthèse` peut ne pas rendre la main, `## Fin` s'exécute après le commit, que le push ait eu lieu, ait été sauté ou ait échoué.
Templates : `templates/on_start_TEMPLATE.md`, `templates/on_close_TEMPLATE.md`.

## Entre phases : /compact

Compression de l'historique en place. Usage normal entre phases d'une même session ; `/close` + `/start` entre sessions. Ne pas inverser les deux mécanismes.

## Journal de session

Fichier `<dossier_zone>/_contexte/journal_session.md`, **gitignoré** (`**/_contexte/journal_session.md`, posé par `/init_projet` et `/update`), en ajout seul. Il protège contre la perte d'information due aux `/compact` des sessions longues, sans que `/close` cesse d'être le seul écrivain de `signals.md`, `contexte.md` et des roadmaps.

- Format : une ligne par événement, `AAAA-MM-JJ HH:MM | décision|fichier|action | texte`, écrite au moment de l'événement (décision actée, fichier créé ou modifié, action ouverte ou close). Jamais de donnée sensible.
- Aucune ligne n'est réécrite ni supprimée en cours de session ; le journal ne modifie jamais une `roadmap*.md`.
- Relu juste après chaque `/compact`.
- `/close` l'intègre à la synthèse, vérifie que chaque ligne est reportée (`signals.md`, `contexte.md` ou synthèse), puis le vide après un commit constaté dans `git show --name-only HEAD` — jamais avant. Commit en échec : journal intact.
- Limites : fichier local, perdu avec le disque ; l'écriture dépend de la discipline de l'agent (un `/compact` n'est pas détectable sans hook).

Source canonique : `CLAUDE.md` § Journal de session, `start.md` étapes 3 et 4, `close.md` étapes 3, 12 et 13 ; kit v5.44.

## Roadmap

Chantier multi-phases : une seule phase `[EN COURS]` à la fois, checkpoint /compact obligatoire entre phases — ne pas commencer la phase suivante sans confirmation écrite. Statuts mis à jour par /close, jamais en cours de session. Chargée automatiquement par /start tant qu'active. Une fois toutes ses phases achevées, l'agent propose à l'utilisateur de l'archiver ; il ne l'archive jamais automatiquement.

## Modèles

/start : Haiku — /close : Sonnet — plans, debug, refacto/migration : Opus — tâche isolée : Haiku. Le critère pour Haiku n'est pas la taille de la tâche mais la complexité du contexte.

## Économie de tokens

- Si signals.md suffit à répondre à la question immédiate, contexte.md peut être chargé à la demande
- Toute assertion sur un fichier cité exige sa lecture effective dans la session
- Chiffres et états issus de signals.md / contexte.md sont datés, pas courants : relire la source primaire avant de les énoncer au présent
