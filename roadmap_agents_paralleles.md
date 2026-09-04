# Roadmap — Agents parallèles isolés

Objectif : permettre à un projet Git de créer une équipe d'agents avec contextes, échanges et worktrees isolés, sans écriture concurrente sur `main`.
Créée le : 2026-09-04

---

## Phase 1 — Socle du kit [FAIT]
- [x] Définir le contrat d'une équipe parallèle : rôles, branches, worktrees, statuts, messages et intégration.
- [x] Créer la commande kit-only `/create_parallel_team` et ses templates.
- [x] Ajouter les contrôles automatisés du socle et les exécuter.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer. Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## Phase 2 — Pilote Appli_TSA_SDI_TDAH [TODO]
- [ ] Créer l'équipe `EVOLUTIONS_TESTS`, son coordinateur et les deux agents à périmètres distincts.
- [ ] Installer la communication hiérarchique compatible avec les règles de branches du projet.
- [ ] Créer le worktree de l'agent code et vérifier un cycle `start`/`close` par agent.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer. Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## Phase 3 — Cadrage des évolutions produit [TODO]
- [ ] Faire produire le plan d'accueil des testeurs sans modification de l'application.
- [ ] Faire cadrer puis implémenter, dans le worktree isolé, le retour visuel annoté et son stockage Supabase.
- [ ] Présenter une demande d'intégration accompagnée des tests et validations nécessaires.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer. Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.
