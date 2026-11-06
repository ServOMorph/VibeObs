# Roadmap — Fondations VibeObs et vitrine SérénIATech

Créée le 2026-11-05. But : asseoir les bases pour gagner du temps plus tard, pas aller vite.
Toute nouvelle demande de l'utilisateur est rangée ici (cf. `/telephone`, § Chaque nouvelle demande).

## Cadre
- Travail depuis un téléphone : mode `/telephone`, questions une par une, réponse en un clic.
- Archivage, jamais de suppression. Préparation seule : toute action sortante validée par l'utilisateur.
- Données sensibles : lecture autorisée, traitement local (Ollama), rien vers un service externe.
- Un rapport par phase, validation de l'utilisateur entre chaque phase.

## Phase 1 — Fondations du pilotage [EN COURS]
- [fait] Questions une par une (mémoire projet).
- [fait] Commande `/telephone` (format court, choix en un clic, rangement dans ce planning).
- [fait] Règle des sessions ouvertes enregistrée (mémoire projet) ; exercée avec site et creation_llm. Reste : détection Codex, conflit « tracer dans le signals du dossier » = modifier ce dossier.
- Retex du mode téléphone : premières corrections intégrées à la commande.
- Gate : règle des sessions validée et enregistrée, mode téléphone utilisé sur une session complète.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 2 — Audit et nettoyage du kit [TODO]
- [fait] `comptes_google.json` retiré du suivi Git et ignoré (historique public non réécrit, décision de l'utilisateur).
- [fait] Lot A archivé (`list`, `note_conception_pause_agents.md`) ; `PEDAGOGIE/` conservé.
- [fait] Lots B à F de la maintenance du 2026-11-05 (4 roadmaps archivées, `reprise_multicompte` et `discord_com/` hors Git).
- `signals.md` : 34 actions P1 pour un plafond de 20. `check_docs.py` en échec (journal).
- Documentation : `llms.txt`, guides DOCUMENTATION en retard, README, CHANGELOG.
- Retex de `/maintenance` (étape 10).
- Gate : `check_kit.py` et `check_docs.py` passent, rapport de phase validé.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 3 — Agent PEDAGOGIE [TODO]
- Création par `/create_agent` : lecture étendue validée ; périmètre d'écriture à valider.
- Choix du parcours (hybride recommandé : projet plaisir comme véhicule, bases au rythme du besoin).
- Livrable : suite de la page de cours (parties 6 et suivantes), fiches PP, `dist/` prêt pour Netlify.
- Gate : agent lancé par `/start pedagogie`, première partie produite et validée.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 4 — Audit de SérénIATech_dev [TODO]
- Audit et nettoyage, mêmes règles que la phase 2. Constater la prise en charge de Gmail, Agenda et Drive.
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
