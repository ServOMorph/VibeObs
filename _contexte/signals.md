# Signals — VibeObs (MAJ 2026-09-10)

## Actions ouvertes — pilotage

### P1 — à traiter avant le backlog
- Traiter l'angle mort `meuniers/` sur le compte `sereniatech33@gmail.com` (partagé avec `SérénIATech_dev`, non déclaré au registre « Remotes rclone »).
  - fait quand: le remote de backup de `Meuniers` est identifié, sa ligne registre créée dans `DEPLOYMENTS.md` (avec `partagé:` si assumé) ou `Meuniers` repointé vers un compte dédié.
  - réf: `DEPLOYMENTS.md` § Remotes rclone (et § Templates installés : `Meuniers | rclone_backup | backup_project.py (racine)`) ; `_archives/roadmap_rclone_multicompte.md`.
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

## Dernière session
# Session du 2026-09-10

## Décisions prises
- Traçage des templates installés : section « Templates installés » dans `DEPLOYMENTS.md` (kit, gitignoré), une ligne par couple (projet, template) — même régime que la section « Remotes rclone ».
- Alimentation auto : `/insert_template` (étape `[SORTIE]` 9) écrit la ligne ; `/init_discord_mode` et `/create_projet` en héritent par délégation à cette procédure ; `/init_intercom` (nouvelle étape 6) écrit sa propre ligne.
- Rétro-remplissage initial par scan de signature (profondeur 6, exclusion des copies de kit embarquées) — détection non exhaustive assumée.

## Livrables produits ou modifiés
- `.claude/commands/insert_template.md` : étape `[SORTIE]` 9 (écriture registre), récap 9→10.
- `.claude/commands/init_intercom.md` : étape 6 (écriture registre), renum. 5→7.
- `DEPLOYMENTS.md` : section « Templates installés » + 8 lignes rétro (gitignoré, non commité).
- `CHANGELOG.md` : entrée v5.8.

## Hypothèses validées / invalidées
- VALIDE : `/init_discord_mode` et `/create_projet` délèguent déjà à la procédure `/insert_template` [SORTIE] → traçage hérité sans les modifier.
- INVALIDE (partiel) : le scan ne détecte pas `control_PC`/`notification`/`overlay`/`parallel_agents` ; 2 projets injoignables (chemins morts `Open_Code_Apprentissage`, `claude-vibecoding-kit`).
- EN ATTENTE : test réel d'une insertion `/insert_template` écrivant la ligne registre.

## Prochaine étape exacte
Exercer `/insert_template` en réel et vérifier l'écriture / non-duplication de la ligne « Templates installés ». Puis reprendre P1 (angle mort backup `meuniers/`).

## Question bloquante pour la session suivante
Aucune.
