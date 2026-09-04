# Signals — VibeObs (MAJ 2026-09-04)

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

### Backlog P2
Voir [`signals_backlog_2026-09-04.md`](_contexte/signals_backlog_2026-09-04.md) : validations secondaires, décisions de conception, maintenance et contexte historique.

## Garde-fous permanents
- Secrets Discord uniquement dans `.env` gitignoré ; vérifier `git check-ignore` et `git status` avant un commit qui touche `discord_com/`.
- Écriture dans `control_pc.sqlite` via Python `sqlite3` paramétré, jamais par `INSERT` shell.

## Dernière session
# Session du 2026-09-04

## Décisions prises
- Le kit et le dépôt GitHub sont renommés VibeObs ; le remote local est `origin` vers `ServOMorph/VibeObs`.
- `/create_projet_public` est remplacée par `/create_projet` (Git local ou GitHub public/privé).
- Les backups rclone sont distribués comme template avec un remote explicite ; le template Netlify est ajouté.

## Livrables produits ou modifiés
- Documentation, contexte, zones et scripts de backup : références renommées vers VibeObs.
- `.claude/commands/create_projet.md`, `templates/rclone_backup/` et `templates/netlify/` : création ou mise à jour prêtes à versionner.

## Hypothèses validées / invalidées
- VALIDE : `check_kit.py` et `check_docs.py` passent après synchronisation documentaire.
- EN ATTENTE : test Discord réel du correctif de file.

## Prochaine étape exacte
Autoriser le lancement temporaire du bot, envoyer deux notifications réelles, puis vérifier `queue.json` à `idle`.

## Question bloquante pour la session suivante
Autoriser le lancement temporaire du bot Discord pour ce test réel ?
