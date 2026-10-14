# Signals — VibeObs (MAJ 2026-10-14)

## Actions ouvertes — pilotage

### P1 — à traiter avant le backlog
- Valider en conditions réelles les nouveaux `/start` (étape 4c) et `/close` (étapes 3-bis, 13, 15) déployés dans `SérénIATech_dev` par `/update` le 2026-10-14. Scénario 1 (`/start` racine) : sortie reçue, aucun bloc 4c affiché, `roadmap_actions_ouvertes_luna.md` laissée à la racine sur décision de l'utilisateur ; scénarios 2 à 6 non rejoués.
  - fait quand: les 6 scénarios de `tests_manuels.md` (section « /start et /close — attribution par zone ») sont rejoués et leurs divergences transmises au kit, traitées ou écartées.
  - réf: `tests_manuels.md` ; `.claude/commands/close.md` étapes 3-bis et 13 ; `.claude/commands/start.md` étape 4c ; `SérénIATech_dev` commit « update: protocole vibecoding — zone racine — kit v5.20 ».
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
- Résoudre le vol de focus avant la phase 3 de `roadmap_reprise_multicompte.md`. 2026-10-12 : correctif `focus_fiable.ps1` codé et branché dans 4 scripts, validé en syntaxe seulement.
  - fait quand: le test manuel de `tests_manuels.md` (section « vol de focus ») est validé et `roadmap_reprise_multicompte.md` + `SKILL.md` sont mis à jour.
  - réf: `roadmap_reprise_multicompte.md` ; `skills/chatgpt-orchestrateur/scripts/focus_fiable.ps1` ; `tests_manuels.md`.
- Rejouer la phase 2 de `create_com_agents` sur `D:\ServOMorph\Meuniers`.
  - fait quand: installation, échange agent↔racine et purge de message sont validés sur Meuniers.
  - réf: `roadmap_com_agents.md`.
- Exercer `/create_memory <alias_zone> <contenu>` en exécution réelle (routage vers `<zone>/_contexte/memory.md`, en-tête créé si absent), et valider `/insert_template` + la conversion de `/create_agent`.
  - fait quand: chaque flux est exercé au moins une fois avec son résultat attendu.
  - réf: `_contexte/signals_backlog_2026-09-04.md` ; `create_memory.md` scopé déployé dans `D:\ServOMorph\Appli_TSA_SDI_TDAH` (commit `00166dd`).
- Tester la substitution Windows de `/init_projet` sur un projet réel. 2026-10-12 : méthode prescrite à l'étape 4 de `init_projet.md` (kit + template, kit v5.18), non encore exercée ; `rclone_backup.json` hors périmètre du script.
  - fait quand: un projet est initialisé en suivant la méthode, sans `{{` résiduel et avec `{{RACINE}}` Windows valide.
  - réf: `.claude/commands/init_projet.md` étape 4.
- Poursuivre la conception du skill générique d’orchestration multi-agents avec ChatGPT.
  - fait quand: le périmètre et le protocole minimal du skill sont formalisés.
  - réf: `roadmap_reprise_multicompte.md`.
- Valider la généricité de `/create_team` et d’Intercom sur un second projet cible.
  - fait quand: une seconde installation indépendante échange et accuse réception des messages.
  - réf: `.claude/commands/create_team.md`, `INTERCOM_AGENT.md`.
- Piloter l'installation d'une équipe parallèle isolée dans Appli_TSA_SDI_TDAH.
  - fait quand: les premiers cycles `start`/`close` de `ONBOARD` et `RETOURS` sont validés sans écriture sur `main`.
  - réf: `roadmap_agents_paralleles.md`, `.claude/commands/create_parallel_team.md`.
- Vérifier dans le rendu de l'interface utilisateur que la liste des templates de `/create_projet` s'affiche sans décalage de numérotation (0 en tête). Exécuté le 2026-10-12 (8 templates listés), rendu côté utilisateur non confirmé.
  - fait quand: l'utilisateur confirme l'affichage `0. Aucun template` suivi de `1.` à `8.` sans renumérotation.
  - réf: `.claude/commands/create_projet.md` étape [TEMPLATES] 17.
- Traiter l'écart `check_docs.py` : le commit `26b9cdd4` (2026-09-06) a modifié la ligne `maj:` du frontmatter de `journal.md` en plus d'ajouter une entrée en bas — le script considère cela comme une violation append-only. Décider : assouplir le contrôle pour exclure le frontmatter, ou traiter comme une vraie violation.
  - fait quand: `check_docs.py` passe sans écart, ou l'exception est explicitement documentée dans `40_specs/controle_qualite_base.md`.
  - réf: `scripts/check_docs.py`, `DOCUMENTATION/30_decisions/journal.md`, commit `26b9cdd4`.
- Mettre en œuvre l'harmonisation automatique `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` (source unique `INSTRUCTIONS.md` + 3 wrappers, portée générique/spécifique demandée avant chaque écriture, prise en contexte insistée) — reportée à plus tard sur ordre utilisateur.
  - fait quand: source + wrappers déployés, `/update` propage sans écraser les blocs spécifiques, `check_kit.py` contrôle l'écart.
  - réf: `templates/AGENTS.md` ; `.claude/commands/update.md` étape 7 ; `CHANGELOG.md` v5.3 ; `_contexte/archive_sessions.md` session 2026-09-04.
- Pousser le commit d'init de `D:\ServOMorph\CreaZik_V3` et renseigner sa stack (laissée vide à l'init) lors du premier `/start CreaZik_V3`.
  - fait quand: `git -C D:\ServOMorph\CreaZik_V3 status` montre la branche à jour avec `origin/main`, et `_contexte/contexte.md` de CreaZik_V3 porte une stack.
  - réf: `D:\ServOMorph\CreaZik_V3` commit `a8b74a8` ; `DEPLOYMENTS.md`.

- Démarrer les agents `textes` et `modeles_llm` de `D:\ServOMorph\CreaZik_V3` et valider leurs chartes en conditions réelles.
  - fait quand: `/start textes` et `/start modeles_llm` chargent leur charte sans warning, et `modeles_llm` crée `D:\AI\Musique\` sans écrire dans `webradio/tests_ace/`.
  - réf: `D:\ServOMorph\CreaZik_V3\TEXTES\agent_role.md`, `D:\ServOMorph\CreaZik_V3\MODELES_LLM\agent_role.md`, `AGENTS_REGISTRY.md`.

- Démarrer l'agent `jeux` d'`Appli_TSA_SDI_TDAH` et valider sa charte, notamment la faisabilité de `run_jeux.py` (accueil sans onboarding, outils ouverts) sans modifier `src/`.
  - fait quand: `/start jeux` charge la charte sans warning, `run_jeux.py` ouvre l'accueil avec jeux cliquables sans écrire dans `src/`, ou l'arbitrage nécessaire est tracé.
  - réf: `D:\ServOMorph\Appli_TSA_SDI_TDAH\JEUX\agent_role.md`, `AGENTS_REGISTRY.md`.

- Démarrer le projet test `site_internet_ST_v3` (refonte serenia-tech.fr + banc d'essai VibeObs) depuis une session ouverte sur sa racine.
  - fait quand: `/start site_st` charge le contexte sans warning et la phase 1 de la roadmap est engagée.
  - réf: `D:\ServOMorph\site_internet_ST_v3\roadmap_site_v3.md`, `DEPLOYMENTS.md`.

- Démarrer l'agent `shorts` de `SérénIATech_dev` (`Communication/SHORTS`) et réaliser l'état des lieux du dépôt sur les Shorts (charte complétée le 2026-10-14 : zone parente `communication`, écriture partagée `clip_promo/diffusion`).
  - fait quand: `/start shorts` charge la charte sans warning, l'état des lieux est écrit dans `Communication/SHORTS/` et validé par l'utilisateur, sans lecture des données sensibles.
  - réf: `Communication/SHORTS/agent_role.md` de SérénIATech_dev, `AGENTS_REGISTRY.md`.

- Démarrer l'agent `espace_l-invariable` de `SérénIATech_dev` (`Gestion clients/Clients/Espace_L-Invariable`), puis renommer son dossier en majuscules une fois le verrou levé.
  - fait quand: `/start espace_l-invariable` charge la charte sans warning ; renommage en `ESPACE_L-INVARIABLE` fait avec mise à jour de `clients.dossier` (id 8) dans `UI/sereniatech.db`, `zones.md` et `upload_short_atelier.py`.
  - réf: `Gestion clients/Clients/Espace_L-Invariable/_contexte/signals.md` (P2) de SérénIATech_dev, `AGENTS_REGISTRY.md`.

- Mettre à jour `DOCUMENTATION/20_guides/initialiser_un_projet.md` (§ Fichiers déployés : ajouter `.gitignore` et `_docs/protocole_vibecoding.md`, retirer `agent_role_TEMPLATE.md` non copié ; § Déroulé : données sensibles inscrites dans `CLAUDE.md`) — propositions en attente de validation utilisateur.
  - fait quand: guide corrigé et ligne `INDEX.md` datée, ou refus tracé.
  - réf: `.claude/commands/init_projet.md` étapes 3-4, `DOCUMENTATION/_contexte/signals.md`.

### Backlog P2
Voir [`signals_backlog_2026-09-04.md`](_contexte/signals_backlog_2026-09-04.md) : validations secondaires, décisions de conception, maintenance et contexte historique.

## Garde-fous permanents
- Secrets Discord uniquement dans `.env` gitignoré ; vérifier `git check-ignore` et `git status` avant un commit qui touche `discord_com/`.
- Écriture dans `control_pc.sqlite` via Python `sqlite3` paramétré, jamais par `INSERT` shell.
- rclone : un remote = un projet, compte Google dédié par projet. Partage entre projets seulement s'il est déclaré explicitement à l'insertion du template et tracé `partagé: A + B` dans `DEPLOYMENTS.md` § Remotes rclone. Remotes actifs : `vibeobs_drive` (servomorph14), `sereniatech_drive` (sereniatech33), `rayonne_toi_drive` (rayonnetoi — partagé Rayonne_Toi + Appli_TSA_SDI_TDAH).
- Sous auto-mode, le classifieur bloque tout upload cloud de secrets (`rclone copy` de `.env` et assimilés). Un hook `/close` « Fin » ne peut faire que `--refresh-list` ; l'upload Drive est manuel, hors session. Le classifieur n'est pas désactivable par `permissions.allow`.

## Dernière session
# Session du 2026-10-14

## Décisions prises
- `/close` attribue chaque élément à sa zone propriétaire (3-bis) et contrôle le statut Git des signaux avant d'annoncer un commit (13) ; `/start` signale les éléments mal classés (4c) sans les déplacer ; kit v5.21.
- Déploiement par `/update` dans `SérénIATech_dev` (blocs SPECIFICITES PROJET préservés, `create_memory.md` et `CLAUDE.md` mis à jour par la procédure standard).
- Roadmap `roadmap_actions_ouvertes_luna.md` laissée à la racine de `SérénIATech_dev` et étape 4c inchangée : « on ne change rien » (décision de l'utilisateur).

## Livrables produits ou modifiés
- `.claude/commands/start.md`, `close.md` et leurs templates, `Protocole_start_close_context.md`, `CHANGELOG.md`, `README.md`, `tests_manuels.md` : modifiés. Hors dépôt kit : `SérénIATech_dev/.claude/` (4 fichiers, commit d'update) ; `DEPLOYMENTS.md` (local, gitignoré).

## Hypothèses validées / invalidées
- VALIDE : miroir kit/template identique hors bloc, `check_kit.py` et 14 tests passent, commandes installées identiques aux templates (comparaison refaite après un faux positif).
- EN ATTENTE : comportement réel des étapes 3-bis, 4c, 13 (scénarios non rejoués) ; limite connue : 4c ne contrôle pas une roadmap posée à la racine.

## Prochaine étape exacte
L'utilisateur rejoue les scénarios dans `SérénIATech_dev` (nouvelle session, prompt de guidage fourni) puis transmet les divergences au kit.

## Question bloquante pour la session suivante
L'élément « df7ee31d — Tableau prévisions » (décider d'une roadmap dédiée : jours ou dates, extension sur plusieurs cases, sous-tâches) a été mentionné sans être traité : de quel projet ou zone vient-il ?
