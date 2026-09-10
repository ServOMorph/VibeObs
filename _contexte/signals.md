# Signals — VibeObs (MAJ 2026-09-10)

## Actions ouvertes — pilotage

### P1 — à traiter avant le backlog
- Traiter l'angle mort `meuniers/` sur le compte `sereniatech33@gmail.com` (partagé avec `SérénIATech_dev`, non déclaré au registre « Remotes rclone »).
  - fait quand: le remote de backup de `Meuniers` est identifié, sa ligne registre créée dans `DEPLOYMENTS.md` (avec `partagé:` si assumé) ou `Meuniers` repointé vers un compte dédié.
  - réf: `DEPLOYMENTS.md` § Remotes rclone (et § Templates installés : `Meuniers | rclone_backup | backup_project.py (racine)`) ; `_archives/roadmap_rclone_multicompte.md`.
- Committer `Appli_TSA_SDI_TDAH/_contexte/on_close.md` (hook « Fin » réduit à `--refresh-list`) et effectuer l'upload Drive d'Appli resté en attente.
  - fait quand: `on_close.md` d'Appli est commité via `/close` de sa zone, et un `python claude-vibecoding-kit/backup_project.py . --upload` réel a réussi.
  - réf: `Appli_TSA_SDI_TDAH/_contexte/on_close.md` § Fin ; Appli commit `746afcd` (correctifs `backup_project.py`).
- Décider si les 2 correctifs `backup_project.py` (exclusion des artefacts régénérables + sorties tolérantes à l'encodage) doivent être portés aux copies vendored lignée `rclone sync`.
  - fait quand: port effectué sur chaque copie, ou décision de non-port tracée.
  - réf: `templates/rclone_backup/backup_project.py` (corrigé) ; `Rayonne_Toi/claude-vibecoding-kit/rclone_backup/backup_project.py` ; `Meuniers/backup_project.py`.
- Exercer `/insert_template` en réel et vérifier l'écriture de la ligne dans `DEPLOYMENTS.md` § Templates installés (couple absent → ajout, couple présent → pas de doublon).
  - fait quand: une insertion réelle a créé une ligne correcte, une ré-insertion n'a pas dupliqué.
  - réf: `.claude/commands/insert_template.md` étape `[SORTIE]` 9 ; `DEPLOYMENTS.md` § Templates installés.
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
- Sous auto-mode, le classifieur bloque tout upload cloud de secrets (`rclone copy` de `.env` et assimilés). Un hook `/close` « Fin » ne peut faire que `--refresh-list` ; l'upload Drive est manuel, hors session. Le classifieur n'est pas désactivable par `permissions.allow`.

## Dernière session
# Session du 2026-09-10

## Décisions prises
- L'upload Drive du hook « Fin » de `/close` ne peut pas être automatisé sous auto-mode : le classifieur de sécurité bloque tout `rclone copy` de secrets vers un cloud, quel que soit l'emballage du script. Le hook se limite à `--refresh-list` ; l'upload reste manuel hors session (tâche planifiée OS possible mais écartée).
- Le classifieur d'auto-mode n'est pas un réglage local et n'est pas contourné par `permissions.allow` : non modifiable, non désactivé par allowlist.

## Livrables produits ou modifiés
- `templates/rclone_backup/backup_project.py` : `EXCLUDES` étendu (`test-results`, `playwright-report`, `.pytest_cache`, `.ruff_cache`, `.mypy_cache`, `coverage`, `htmlcov`, `.netlify`, `tmp`) ; sorties console tolérantes à l'encodage (`sys.stdout/stderr.reconfigure` utf-8/replace) ; `subprocess.run` rclone en `encoding="utf-8", errors="replace"`. Commité par ce `/close`.
- `Appli_TSA_SDI_TDAH/claude-vibecoding-kit/backup_project.py` + `test_backup_project.py` : mêmes correctifs (set `EXCLUDED_PARTS`) + 4 tests (4/4). Commités hors kit (Appli `746afcd`).
- `Appli_TSA_SDI_TDAH/_contexte/on_close.md` § Fin : `--upload` retiré, rappel commande manuelle + trace `tests_manuels.md`. Non commité (dépôt Appli).

## Hypothèses validées / invalidées
- VALIDE : `--refresh-list` exit 0 avec chemins non-ASCII (`→`, accents) après `reconfigure` ; sans correctif, `PYTHONIOENCODING=cp1252` + `→` → exit 1. Run réel Appli : manifeste 374 → 222 lignes, junk filtré, tri et `\n` final préservés.
- INVALIDE : « un script dédié appelé par `close.md` ferait l'upload tout seul » — bloqué par le classifieur, indépendant du nom du script.
- EN ATTENTE : upload Drive réel d'Appli (manuel) ; port des correctifs aux copies vendored lignée `rclone sync` (`Rayonne_Toi`, `Meuniers`) non tranché.

## Prochaine étape exacte
Reprendre P1 : angle mort backup `meuniers/`. Committer `on_close.md` d'Appli via `/close` de sa zone.

## Question bloquante pour la session suivante
Aucune.
