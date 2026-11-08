# Roadmap — Fondations VibeObs et vitrine SérénIATech

Créée le 2026-11-05. But : asseoir les bases pour gagner du temps plus tard, pas aller vite.
Toute nouvelle demande de l'utilisateur est rangée ici (cf. `/telephone`, § Chaque nouvelle demande).

## Cadre
- Travail depuis un téléphone : mode `/telephone`, questions une par une, réponse en un clic.
- Archivage, jamais de suppression. Préparation seule : toute action sortante validée par l'utilisateur.
- Données sensibles : lecture autorisée, traitement local (Ollama), rien vers un service externe.
- Un rapport par phase, validation de l'utilisateur entre chaque phase.

## Phase 1 — Fondations du pilotage [FAIT]
- [fait] Questions une par une (mémoire projet).
- [fait] Commande `/telephone` (format court, choix en un clic, rangement dans ce planning).
- [fait] Règle des sessions ouvertes enregistrée (mémoire projet) ; exercée avec site et creation_llm. Conflit de traçage tranché (l'agent de la session ouverte trace dans son propre `signals.md`). Détection Codex : en backlog.
- Retex du mode téléphone : premières corrections intégrées à la commande.
- Gate : règle des sessions validée et enregistrée, mode téléphone utilisé sur une session complète.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 2 — Audit et nettoyage du kit [FAIT]
- [fait] `comptes_google.json` retiré du suivi Git et ignoré (historique public non réécrit, décision de l'utilisateur).
- [fait] Lot A archivé (`list`, `note_conception_pause_agents.md`) ; `PEDAGOGIE/` conservé.
- [fait] Lots B à F de la maintenance du 2026-11-05 (4 roadmaps archivées, `reprise_multicompte` et `discord_com/` hors Git).
- [fait] `signals.md` ramené à 20 actions P1 (12 actions vers le backlog, 2 doublons retirés). `check_docs.py` corrigé (frontmatter exclu du contrôle append-only).
- [fait] `llms.txt`, README, CHANGELOG. Guides DOCUMENTATION en retard : triage confié à l'agent `documentation` (`DOCUMENTATION/_contexte/signals.md`).
- [fait] Retex de `/maintenance` : à refaire, propositions perdues au compactage ; en backlog.
- Gate : `check_kit.py` et `check_docs.py` passent, rapport de phase validé.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 3 — Agent PEDAGOGIE [TODO]
- Mise de côté par l'utilisateur le 2026-11-07 au profit de la phase 4 ; reprise après celle-ci.
- [fait] Création par `/create_agent` (2026-11-06) : lecture étendue et périmètre d'écriture (`PEDAGOGIE/` seul, sans publication) validés ; agent lancé par `/start pedagogie`.
- Choix du parcours (hybride recommandé : projet plaisir comme véhicule, bases au rythme du besoin).
- Livrable : suite de la page de cours (parties 6 et suivantes), fiches PP, `dist/` prêt pour Netlify.
- Gate : agent lancé par `/start pedagogie`, première partie produite et validée.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 4 — Audit de SérénIATech_dev [EN COURS]
- Audit et nettoyage, mêmes règles que la phase 2. Constater la prise en charge de Gmail, Agenda et Drive.
- [fait] Lot C `zones.md` réparé ; lot B `.gitignore` (résidus d'outils, pyc, tessdata, runtime Discord, médias `short3_bloc_note`).
- [fait] Lot A : travail non commité sauvegardé par 13 commits `sauvegarde(<zone>)` ; lot D racine ; lot E `VertIA` détaché ; lot F 2 roadmaps terminées archivées.
- Gmail, Agenda, Drive : connecteurs claude.ai à autoriser, puis tester.
- Constats à transmettre aux zones (cf. `_contexte/signals.md`, action « Clore la phase 4 »).
- Gate : rapport validé.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 5 — Analyse fonctionnelle [TODO]
- Fonctionnalités manquantes à ajouter, puis nouvelles à créer dans SérénIATech_dev.
- Gate : rapport validé.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 6 — Plan d'automatisation [TODO]
- Clients, facturation et comptabilité, communication, pilotage. Outils : Gmail, Agenda, Drive, Discord, réseaux sociaux, YouTube.
- Gate : plan validé.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.
