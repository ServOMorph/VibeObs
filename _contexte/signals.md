# Signals — VibeObs (MAJ 2026-10-10)

## Actions ouvertes — pilotage

### P1 — à traiter avant le backlog
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
- Vérifier en conditions réelles que la liste des templates de `/create_projet` s'affiche sans décalage de numérotation (0 en tête).
  - fait quand: un `/create_projet` exécuté affiche `0. Aucun template` suivi de `1.` à `7.` sans renumérotation.
  - réf: `.claude/commands/create_projet.md` étape [TEMPLATES] 17.
- Traiter l'écart `check_docs.py` : le commit `26b9cdd4` (2026-09-06) a modifié la ligne `maj:` du frontmatter de `journal.md` en plus d'ajouter une entrée en bas — le script considère cela comme une violation append-only. Décider : assouplir le contrôle pour exclure le frontmatter, ou traiter comme une vraie violation.
  - fait quand: `check_docs.py` passe sans écart, ou l'exception est explicitement documentée dans `40_specs/controle_qualite_base.md`.
  - réf: `scripts/check_docs.py`, `DOCUMENTATION/30_decisions/journal.md`, commit `26b9cdd4`.
- Corriger la regex de version de `check_kit.py` (`get_version_from_readme`) : elle cherche le littéral `Kit v\d+\.\d+` et ne matche pas `Kit **v5.11**` (gras Markdown) — le contrôle de cohérence des versions ne vérifie donc jamais réellement README.md en pratique.
  - fait quand: la regex tolère le gras Markdown, ou le format de README.md est aligné sur ce qu'elle attend.
  - réf: `scripts/check_kit.py` fonction `get_version_from_readme`.
- Mettre en œuvre l'harmonisation automatique `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` (source unique `INSTRUCTIONS.md` + 3 wrappers, portée générique/spécifique demandée avant chaque écriture, prise en contexte insistée) — reportée à plus tard sur ordre utilisateur.
  - fait quand: source + wrappers déployés, `/update` propage sans écraser les blocs spécifiques, `check_kit.py` contrôle l'écart.
  - réf: `templates/AGENTS.md` ; `.claude/commands/update.md` étape 7 ; `CHANGELOG.md` v5.3 ; `_contexte/archive_sessions.md` session 2026-09-04.
- Pousser le commit d'init de `D:\ServOMorph\CreaZik_V3` et renseigner sa stack (laissée vide à l'init) lors du premier `/start CreaZik_V3`.
  - fait quand: `git -C D:\ServOMorph\CreaZik_V3 status` montre la branche à jour avec `origin/main`, et `_contexte/contexte.md` de CreaZik_V3 porte une stack.
  - réf: `D:\ServOMorph\CreaZik_V3` commit `a8b74a8` ; `DEPLOYMENTS.md`.

- Démarrer les agents `textes` et `modeles_llm` de `D:\ServOMorph\CreaZik_V3` et valider leurs chartes en conditions réelles.
  - fait quand: `/start textes` et `/start modeles_llm` chargent leur charte sans warning, et `modeles_llm` crée `D:\AI\Musique\` sans écrire dans `webradio/tests_ace/`.
  - réf: `D:\ServOMorph\CreaZik_V3\TEXTESgent_role.md`, `D:\ServOMorph\CreaZik_V3\MODELES_LLMgent_role.md`, `AGENTS_REGISTRY.md`.

- Démarrer l'agent `jeux` d'`Appli_TSA_SDI_TDAH` et valider sa charte, notamment la faisabilité de `run_jeux.py` (accueil sans onboarding, outils ouverts) sans modifier `src/`.
  - fait quand: `/start jeux` charge la charte sans warning, `run_jeux.py` ouvre l'accueil avec jeux cliquables sans écrire dans `src/`, ou l'arbitrage nécessaire est tracé.
  - réf: `D:\ServOMorph\Appli_TSA_SDI_TDAH\JEUXgent_role.md`, `AGENTS_REGISTRY.md`.

### Backlog P2
Voir [`signals_backlog_2026-09-04.md`](_contexte/signals_backlog_2026-09-04.md) : validations secondaires, décisions de conception, maintenance et contexte historique.

## Garde-fous permanents
- Secrets Discord uniquement dans `.env` gitignoré ; vérifier `git check-ignore` et `git status` avant un commit qui touche `discord_com/`.
- Écriture dans `control_pc.sqlite` via Python `sqlite3` paramétré, jamais par `INSERT` shell.
- rclone : un remote = un projet, compte Google dédié par projet. Partage entre projets seulement s'il est déclaré explicitement à l'insertion du template et tracé `partagé: A + B` dans `DEPLOYMENTS.md` § Remotes rclone. Remotes actifs : `vibeobs_drive` (servomorph14), `sereniatech_drive` (sereniatech33), `rayonne_toi_drive` (rayonnetoi — partagé Rayonne_Toi + Appli_TSA_SDI_TDAH).
- Sous auto-mode, le classifieur bloque tout upload cloud de secrets (`rclone copy` de `.env` et assimilés). Un hook `/close` « Fin » ne peut faire que `--refresh-list` ; l'upload Drive est manuel, hors session. Le classifieur n'est pas désactivable par `permissions.allow`.

## Dernière session
# Session du 2026-10-10

## Décisions prises
- Agent `jeux` créé dans `Appli_TSA_SDI_TDAH/JEUX` via `/create_agent` (alias `jeux`, parent racine) : jeux pour TSA/SDI/TDAH, 5 jeux simples proposés avant développement.
- Jeux non branchés sur l'application pendant le développement ; test via `run_jeux.py` (racine, périmètre d'écriture étendu) ; `src/` et `IA-TSA` en lecture seule.
- Message de mise à jour pour la zone parente copié dans le presse-papier.
- Pas de `/doc_sync` : aucune commande ni template du kit modifié.

## Livrables produits ou modifiés
- `Appli_TSA_SDI_TDAH` : `JEUX/agent_role.md`, `JEUX/_contexte/`, `.claude/zones.md` (non commités dans ce repo).
- `AGENTS_REGISTRY.md` (gitignoré) : ligne `jeux` ajoutée.
- `base_connaissances/ameliorations_create_agent.md` : entrée du jour.

## Hypothèses validées / invalidées
- VALIDE : `start.md` d'Appli référence `agent_role.md` (pas de warning).
- EN ATTENTE : faisabilité de `run_jeux.py` sans toucher `src/` ; emplacement des données de recherche du projet.

## Prochaine étape exacte
`/start jeux` depuis `D:\ServOMorph\Appli_TSA_SDI_TDAH`.

## Question bloquante pour la session suivante
Aucune.
