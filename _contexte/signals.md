# Signals — VibeObs (MAJ 2026-09-06)

## Actions ouvertes — pilotage

### P1 — à traiter avant le backlog
- Traiter l'angle mort `meuniers/` sur le compte `sereniatech33@gmail.com` (partagé avec `SérénIATech_dev`, non déclaré au registre « Remotes rclone »).
  - fait quand: le remote de backup de `Meuniers` est identifié, sa ligne registre créée dans `DEPLOYMENTS.md` (avec `partagé:` si assumé) ou `Meuniers` repointé vers un compte dédié.
  - réf: `DEPLOYMENTS.md` § Remotes rclone ; `_archives/roadmap_rclone_multicompte.md`.
- Exécuter le backup réel de `SérénIATech_dev` vers `sereniatech_drive` et vérifier les `/close` des projets partageant `rayonne_toi_drive`.
  - fait quand: `tests_manuels.md` sections « rclone multicompte » toutes validées et retirées.
  - réf: `tests_manuels.md`.
- Valider le correctif `templates/discord_com` en conditions réelles : deux notifications consécutives reçues et file finale `idle`.
  - fait quand: le bot local reçoit puis transmet deux notifications réelles sans perte.
  - réf: `templates/discord_com/`, `discord_com/` local (non versionné).
- Résoudre le vol de focus avant la phase 3 de `roadmap_reprise_multicompte.md`.
  - fait quand: une action de clic vise de façon fiable la nouvelle fenêtre Chrome.
  - réf: `roadmap_reprise_multicompte.md`.
- Rejouer la phase 2 de `create_com_agents` sur `D:\ServOMorph\Meuniers`.
  - fait quand: installation, échange agent↔racine et purge de message sont validés sur Meuniers.
  - réf: `roadmap_com_agents.md`.
- Exercer `/create_memory <alias_zone> <contenu>` en exécution réelle (routage vers `<zone>/_contexte/memory.md`, en-tête créé si absent), et valider `/insert_template` + la conversion de `/create_agent`.
  - fait quand: chaque flux est exercé au moins une fois avec son résultat attendu.
  - réf: `_contexte/signals_backlog_2026-09-04.md` ; `create_memory.md` scopé déployé dans `D:\ServOMorph\Appli_TSA_SDI_TDAH` (commit `00166dd`).
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

### Backlog P2
Voir [`signals_backlog_2026-09-04.md`](_contexte/signals_backlog_2026-09-04.md) : validations secondaires, décisions de conception, maintenance et contexte historique.

## Garde-fous permanents
- Secrets Discord uniquement dans `.env` gitignoré ; vérifier `git check-ignore` et `git status` avant un commit qui touche `discord_com/`.
- Écriture dans `control_pc.sqlite` via Python `sqlite3` paramétré, jamais par `INSERT` shell.
- rclone : un remote = un projet, compte Google dédié par projet. Partage entre projets seulement s'il est déclaré explicitement à l'insertion du template et tracé `partagé: A + B` dans `DEPLOYMENTS.md` § Remotes rclone. Remotes actifs : `vibeobs_drive` (servomorph14), `sereniatech_drive` (sereniatech33), `rayonne_toi_drive` (rayonnetoi — partagé Rayonne_Toi + Appli_TSA_SDI_TDAH).

## Dernière session
# Session du 2026-09-06

## Décisions prises
- rclone multicompte : un remote = un projet, compte Google dédié par projet ; partage entre projets uniquement si déclaré à l'insertion (tracé `partagé: A + B` dans `DEPLOYMENTS.md`).
- `Appli_TSA_SDI_TDAH` partage volontairement `rayonne_toi_drive` avec `Rayonne_Toi` : état final `rayonne_toi_drive:BackUps/` = `Rayonne_Toi` + `Appli_TSA_SDI_TDAH` (écart assumé vs texte Phase 3 de la roadmap).
- `BACKUPS-SerenIATech_dev` et `claude-vibecoding-kit` sur le compte rayonnetoi : purge directe (sereniatech_drive a déjà un backup plus complet, pas de fusion).

## Livrables produits ou modifiés
- Kit durci : `insert_template.md` (7bis a→f), `create_projet.md`, `init_projet.md` (+miroir), `templates/rclone_backup/README.md` + `analysis/garde_fou_collision.md` (5 cas).
- Backup kit repointé : `scripts/backup_file.py` + `close.md` 14bis → `vibeobs_drive`.
- Remotes créés : `vibeobs_drive` (servomorph14), `sereniatech_drive` (sereniatech33) ; `googledrive:` supprimé. `DEPLOYMENTS.md` registre finalisé (gitignoré).
- Données migrées puis purgées du compte rayonnetoi : `VibeObs/` (copy+check → `vibeobs_drive`), `BACKUPS-SerenIATech_dev/`, `claude-vibecoding-kit/` ; `claude-vibecoding-kit/` aussi purgé de `sereniatech_drive`.
- `SérénIATech_dev/ClaudeCode/backup_drive.py` repointé → `sereniatech_drive` (dépôt séparé, non commité ici).
- `roadmap_rclone_multicompte.md` → `_archives/` (3/3 phases FAIT).

## Hypothèses validées / invalidées
- VALIDE : `vibeobs_drive` et `sereniatech_drive` sont des comptes distincts de rayonnetoi (empreintes `rclone about`).
- VALIDE : migration `VibeObs/` — `rclone check` 0 différence avant purge.
- EN ATTENTE : backup réel `SérénIATech_dev` → `sereniatech_drive` ; `/close` de `Rayonne_Toi` et `Appli_TSA_SDI_TDAH` (`tests_manuels.md`).

## Prochaine étape exacte
Traiter l'angle mort `meuniers/` sur le compte `sereniatech33@gmail.com` (2 projets, non déclaré au registre). Puis reprendre backlog P1.

## Question bloquante pour la session suivante
Aucune.
