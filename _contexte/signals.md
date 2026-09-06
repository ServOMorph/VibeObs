# Signals — VibeObs (MAJ 2026-09-06)

## Actions ouvertes — pilotage

### P1 — à traiter avant le backlog
- Valider le correctif `templates/discord_com` en conditions réelles : deux notifications consécutives reçues et file finale `idle`.
  - fait quand: le bot local reçoit puis transmet deux notifications réelles sans perte.
  - réf: `templates/discord_com/`, `discord_com/` local (non versionné).
- Résoudre le vol de focus avant la phase 3 de `roadmap_reprise_multicompte.md`.
  - fait quand: une action de clic vise de façon fiable la nouvelle fenêtre Chrome.
  - réf: `roadmap_reprise_multicompte.md`.
- Rejouer la phase 2 de `create_com_agents` sur `D:\ServOMorph\Meuniers`.
  - fait quand: installation, échange agent↔racine et purge de message sont validés sur Meuniers.
  - réf: `roadmap_com_agents.md`.
- Valider `/insert_template`, la mémoire scopée de `/create_memory`, et la conversion de `/create_agent`.
  - fait quand: chaque flux est exercé au moins une fois avec son résultat attendu.
  - réf: `_contexte/signals_backlog_2026-09-04.md`.
- Fiabiliser la substitution Windows de `/init_projet` puis la tester.
  - fait quand: un projet cible Windows est initialisé avec les placeholders correctement résolus.
  - réf: `.claude/commands/init_projet.md`.
- Poursuivre la conception du skill générique d’orchestration multi-agents avec ChatGPT.
  - fait quand: le périmètre et le protocole minimal du skill sont formalisés.
  - réf: `roadmap_reprise_multicompte.md`.
- Valider la généricité de `/create_team` et d’Intercom sur un second projet cible.
  - fait quand: une seconde installation indépendante échange et accuse réception des messages.
  - réf: `.claude/commands/create_team.md`, `INTERCOM_AGENT.md`.
- Piloter l'installation d'une équipe parallèle isolée dans Appli_TSA_SDI_TDAH.
  - fait quand: les premiers cycles `start`/`close` de `ONBOARD` et `RETOURS` sont validés sans écriture sur `main`.
  - réf: `roadmap_agents_paralleles.md`, `.claude/commands/create_parallel_team.md`.
- Exécuter la Phase 3 de `roadmap_migration_close.md` (`/update D:\ServOMorph\Appli_TSA_SDI_TDAH` puis MAJ ligne `DEPLOYMENTS.md`), après le `/close` du kit et le `/close` d'Appli_TSA_SDI_TDAH.
  - fait quand: `/update` sur repos propres laisse `start.md`/`close.md` intacts hors SPECIFICITES, marqueurs uniques, `_contexte/` non touché.
  - réf: `roadmap_migration_close.md` Phase 3.

### Backlog P2
Voir [`signals_backlog_2026-09-04.md`](_contexte/signals_backlog_2026-09-04.md) : validations secondaires, décisions de conception, maintenance et contexte historique.

## Garde-fous permanents
- Secrets Discord uniquement dans `.env` gitignoré ; vérifier `git check-ignore` et `git status` avant un commit qui touche `discord_com/`.
- Écriture dans `control_pc.sqlite` via Python `sqlite3` paramétré, jamais par `INSERT` shell.

## Dernière session
# Session du 2026-09-06

## Décisions prises
- Migration de `close.md` vers le mécanisme SPECIFICITES pilotée par `roadmap_migration_close.md` ; Phase 3 (`/update`) reportée après les `/close` des deux repos (ordre : `/close` kit -> `/close` cible -> `/update`).
- `/start` et `/close` exposent quatre hooks de zone opt-in ; l'étape 10 de `close.md` (check_kit.py) devient conditionnelle à la présence du script.

## Livrables produits ou modifiés
- `.claude/commands/close.md` + `templates/.claude/commands/close.md` : hooks étapes 2-bis (Pré-synthèse) et 14-ter (Fin) ; étape 10 check_kit.py conditionnelle ; renvois « étape 11 » -> « étape 12 ».
- `.claude/commands/start.md` + `templates/.claude/commands/start.md` : hooks étapes 3-bis (Pré-synthèse) et 5-bis (Post-synthèse).
- `templates/on_start_TEMPLATE.md`, `templates/on_close_TEMPLATE.md` : contrats des sections de hook (opt-in).
- `DOCUMENTATION/20_guides/sessions_start_close.md` : sous-section « Hooks de zone ».
- `roadmap_migration_close.md` : nouvelle roadmap 3 phases ; Phases 1-2 [FAIT].
- Hors commit kit — Appli_TSA_SDI_TDAH : `close.md` migré (corps générique = templates verbatim, comportement projet en SPECIFICITES).

## Hypothèses validées / invalidées
- VALIDE : corps génériques `start.md`/`close.md` de la cible byte-identiques aux `templates/` du kit, marqueurs SPECIFICITES uniques (contrôle Python).
- VALIDE : `check_kit.py` exit 0 sur la paire miroir `close.md` / `templates/close.md`.
- EN ATTENTE : `/update` sur repos propres (Phase 3) — non exécuté, prématuré tant que kit et cible ne sont pas commités.

## Prochaine étape exacte
1. `/close` dans Appli_TSA_SDI_TDAH pour committer la migration cible (`start.md` + `close.md` + `discord_loop.md` + `on_close.md` + `.gitignore` + suppression `rclone_backup_files.txt`).
2. Session kit ultérieure : Phase 3 de `roadmap_migration_close.md`.

## Question bloquante pour la session suivante
Aucune.
