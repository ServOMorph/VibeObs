# Signals — VibeObs (MAJ 2026-11-11)

## Actions ouvertes — pilotage

### P1 — à traiter avant le backlog
- Valider en conditions réelles les nouveaux `/start` (étape 4c) et `/close` (étapes 3-bis, 13, 15) déployés dans `SérénIATech_dev` par `/update` le 2026-10-14. Scénario 1 (`/start` racine) : sortie reçue, aucun bloc 4c affiché, `roadmap_actions_ouvertes_luna.md` laissée à la racine sur décision de l'utilisateur ; scénarios 2 à 6 non rejoués. 2026-10-27 : scénarios 1 et 2 validés en v5.23 (correctif 4c, commit `03b5a54`) ; scénarios 3 à 6 restants (dont le `/close` racine après travail dans SHORTS). 2026-10-27 : `/close` racine sans travail dans SHORTS observé (commit `ca0b2c0` de SérénIATech_dev), deux divergences à trancher consignées dans `tests_manuels.md`. 2026-10-27 : `close.md` de `SérénIATech_dev` mis à jour en v5.22 ; le test « /close v5.22 » peut se jouer dans la même session. 2026-10-29 : `close.md` en v5.25 et `start.md` en v5.23 dans `SérénIATech_dev` (`/update`, permission `menage_zone.py` conservée à la main) ; scénarios 3 à 6 toujours non rejoués.
  - fait quand: les 6 scénarios de `tests_manuels.md` (section « /start et /close — attribution par zone ») sont rejoués et leurs divergences transmises au kit, traitées ou écartées.
  - réf: `tests_manuels.md` ; `.claude/commands/close.md` étapes 3-bis et 13 ; `.claude/commands/start.md` étape 4c ; `SérénIATech_dev` commit « update: protocole vibecoding — zone racine — kit v5.20 ».
- Committer `Appli_TSA_SDI_TDAH/_contexte/on_close.md` (hook « Fin » réduit à `--refresh-list`) et effectuer l'upload Drive d'Appli resté en attente.
  - fait quand: `on_close.md` d'Appli est commité via `/close` de sa zone, et un `python claude-vibecoding-kit/backup_project.py . --upload` réel a réussi.
  - réf: `Appli_TSA_SDI_TDAH/_contexte/on_close.md` § Fin ; Appli commit `0f6c1f5` (correctifs `backup_project.py`).
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
- Résoudre le vol de focus avant la phase 3 de `_archives/local/roadmap_reprise_multicompte.md` (archivée hors Git le 2026-11-05). 2026-10-12 : correctif `focus_fiable.ps1` codé et branché dans 4 scripts, validé en syntaxe seulement.
  - fait quand: le test manuel de `tests_manuels.md` (section « vol de focus ») est validé et `roadmap_reprise_multicompte.md` + `SKILL.md` sont mis à jour.
  - réf: `_archives/local/roadmap_reprise_multicompte.md` ; `skills/chatgpt-orchestrateur/scripts/focus_fiable.ps1` ; `tests_manuels.md`.
- Exercer `/create_memory <alias_zone> <contenu>` en exécution réelle (routage vers `<zone>/_contexte/memory.md`, en-tête créé si absent), et valider `/insert_template` + la conversion de `/create_agent`.
  - fait quand: chaque flux est exercé au moins une fois avec son résultat attendu.
  - réf: `_contexte/signals_backlog_2026-09-04.md` ; `create_memory.md` scopé déployé dans `D:\ServOMorph\Appli_TSA_SDI_TDAH` (commit `e4c6e5b`).
- Poursuivre la conception du skill générique d’orchestration multi-agents avec ChatGPT.
  - fait quand: le périmètre et le protocole minimal du skill sont formalisés.
  - réf: `_archives/local/roadmap_reprise_multicompte.md` (réf à préciser : l'action restée en P1 faute de chemin précis au tri du 2026-11-06 ; à reclasser en backlog).






- Évaluer le mécanisme `DOCUMENTATION/` dans `D:\ServOMorph\Appli_TSA_SDI_TDAH` avant de le créer dans `SérénIATech_dev`. Mesures du 2026-10-24 : 0 consultation de la doc déclenchée par la seule consigne de `CLAUDE.md` sur 29 sessions locales ; 3 specs périmées (image de retour facultative, refus de consentement conservant le partage sans données de santé, exclusivité SDI/Avec DI) et dossiers imbriqués / durée de routine par jour non documentés.
  - fait quand: les 5 tests de la section « Évaluation DOCUMENTATION » de `tests_manuels.md` d'Appli sont passés (seuil 4/5 en autonomie dans le bon document), les specs périmées corrigées via `/start documentation` d'Appli, et une décision tracée sur les pistes (ligne « spec à mettre à jour » en fin de phase de roadmap, contrôle des « Sources » des specs dans `/close` étape 7, citation des documents clés dans les chartes d'agents).
  - réf: `D:\ServOMorph\Appli_TSA_SDI_TDAH\tests_manuels.md` ; `D:\ServOMorph\Appli_TSA_SDI_TDAH\DOCUMENTATION\40_specs\` ; Appli commits `3255b46`, `c970820`, `f6a6428`, `be4a1f0`.
- Créer `DOCUMENTATION/` dans `C:\Users\raph6\Documents\SerenIATech\SérénIATech_dev` (`/create_agent`) une fois l'évaluation Appli traitée. Décisions en attente de l'utilisateur : archiver `ClaudeCode/roadmap_base_connaissances.md` (6 phases TODO, base concurrente dans `ClaudeCode/base_connaissances/`) au profit de `DOCUMENTATION/` à la racine ; valider le périmètre proposé (carte du projet et processus d'abord ; exclusions : données sensibles, détail clients, tarification non stabilisée) ; exclure `Interim` et décider de l'inscrire aux données sensibles de `CLAUDE.md`. `AGENTS.md` et `GEMINI.md` de SérénIATech_dev ne mentionnent pas `DOCUMENTATION/` : le paragraphe du template est à ajouter. Migration de la section Spécificités projet vers l'INDEX déconseillée (déclencheurs plus fiables dans `CLAUDE.md`).
  - fait quand: l'agent `documentation` de SérénIATech_dev est créé, son `INDEX.md` existe, et les trois décisions ci-dessus sont tracées.
  - réf: `C:\Users\raph6\Documents\SerenIATech\SérénIATech_dev\ClaudeCode\roadmap_base_connaissances.md` ; `C:\Users\raph6\Documents\SerenIATech\SérénIATech_dev\.claude\CLAUDE.md` § Base de connaissances ; `.claude/commands/create_agent.md`.

- Faire appliquer le tri vers `_contexte/backlog.md` (v5.22 à v5.25) aux autres projets suivis. Fait : `SérénIATech_dev` en v5.25 (`/update`, 2026-10-29) ; `Appli_TSA_SDI_TDAH` : `close.md` aligné à la main sur le générique v5.25 (commit `d557510`, 2026-10-29), `start.md` non aligné. Validé sur un projet jetable (supprimé) : tri, plafond, péremption, promotion, croisement des `réf:`, catégories, ligne de renvoi totalisée, pas de bump sans modification de travail, constat rangé chez la zone concernée. Reste à exercer en réel : premier `/close` d'Appli en v5.25 (permissions `ls` / `test -e` dans `allowed-tools`, bilan sur ses 49 entrées de backlog sans catégorie, nombre d'entrées sans `réf:` précis), backlog créé à la première entrée, backlog vidé, `check_kit.py` présent avant commit.
  - fait quand: les autres projets de `DEPLOYMENTS.md` sont à v5.25 ou leur report est tracé, et un `/close` réel d'Appli en v5.25 a été observé, ses divergences transmises au kit.
  - réf: `DEPLOYMENTS.md` ; `CHANGELOG.md` v5.22 à v5.25 ; `tests_manuels.md` section « /close v5.22 » ; `D:\ServOMorph\Appli_TSA_SDI_TDAH\.claude\commands\close.md`.
- Décider si `/update` doit préserver les personnalisations du frontmatter de `close.md` hors bloc `SPECIFICITES PROJET`. Constat 2026-10-27 : `SérénIATech_dev` avait `PowerShell(python *menage_zone.py*)` dans `allowed-tools` ; la copie du kit l'aurait supprimée (conservée à la main), et le contrôle « identique hors spécificités » de l'étape 10 signale cet écart. 2026-11-11 : SérénIATech_dev a retiré `git push` de `allowed-tools` et ajouté une ligne d'étape 14 dans son bloc `SPECIFICITES PROJET` ; le push conditionnel du kit (v5.37) rend le retrait inutile, mais le prochain `/update` de ce projet doit être contrôlé (ligne de spécificités intacte, `allowed-tools` du kit).
  - fait quand: `update.md` (étapes 5 et 10) préserve ou signale explicitement ces ajouts, ou la décision de ne pas le faire est tracée.
  - réf: `.claude/commands/update.md` étapes 5 et 10 ; `SérénIATech_dev` commit `61b8e47`.
- Décider si la copie `_docs/protocole_vibecoding.md` du kit (en-tête v5.0, non alignée sur le protocole actuel) doit être réalignée, et vérifier la version recopiée par `/init_projet` étape 3. `Appli_TSA_SDI_TDAH/_docs/` ne contient pas ce fichier.
  - fait quand: copie du kit réalignée ou décision de non-alignement tracée, et la copie déployée par `/init_projet` est constatée à la version courante.
  - réf: `.claude/commands/init_projet.md` ligne 77 ; `_docs/protocole_vibecoding.md` ; `Protocole_start_close_context.md`.

- Trancher la définition du « fichier de travail » de `/close` étape 9 : `tests_manuels.md` et les `roadmap*.md` sont des fichiers de suivi, mais la règle v5.25 les compte comme travail (seuls `_contexte/`, `README.md`, `CHANGELOG.md` sont exclus). Constat 2026-10-29 : le retrait d'une section de `tests_manuels.md` seule imposerait un bump de version du kit. Non bumpé cette fois.
  - fait quand: la règle exclut explicitement ces fichiers de suivi (kit + template, `check_kit.py` passe), ou la décision de les compter est tracée.
  - réf: `.claude/commands/close.md` étape 9 ; `templates/.claude/commands/close.md` ; `CHANGELOG.md` v5.25.

- Trancher les 3 propositions du journal `/create_agent` du 2026-10-30 : (a) mode « agent client » avec création en base préalable, (b) exception à la règle des majuscules quand le dossier est lié à une base, (c) un échec de lecture de `start.md` ne vaut jamais absence de référence.
  - fait quand: chaque proposition est implémentée dans `create_agent.md` (kit + template, `check_kit.py` passe) ou écartée avec motif tracé.
  - réf: `base_connaissances/ameliorations_create_agent.md` entrée 2026-10-30 ; `.claude/commands/create_agent.md` [PREFLIGHT].

- Suivre l'implémentation du rapport de phase 5 (`roadmap_fondations.md` phase 5) : relayé le 2026-11-09 à « Business SerenIA Tech », reformulation validée, ordre révisé ; implémentation par les zones ui et gestion-clients (1, 2, 5, 3, 6) et business (7), la 4 attendant la décision CAE ; lignes orphelines de `Gestion clients/_contexte/signals.md` à reclasser par cette zone. Suivre aussi l'application, par la session ouverte « Business SerenIA Tech », des constats de l'audit de `SérénIATech_dev` (phase 4 close, constats transmis le 2026-11-08, reformulation contrôlée). Annoncé par cette session : renommage indexé non commité de `20261016_1830_reunion.md` (gestion-clients) et copies `.opencode/commands/` archivées dans `_archives/racine_2026-11-08/opencode_commands/`, avec l'accord de l'utilisateur. Restent : modification du 2026-11-07 9h11 (linkedin, roberto) qualifiée de rangement par la session Business, origine toujours inconnue (ce n'est pas elle) ; `contexte.md` de `linkedin` ligne 20 périmée ; 13 zones sauvegardées hors `/close` (signals non mis à jour) ; `VertIA` signalé seulement. Suivre aussi la phase 6 (plan d'automatisation), menée par l'utilisateur dans la session SérénIATech_dev (décision du 2026-11-09) : plan à relire à son retour pour la validation de la phase. Le bloc « Dernière session 2026-10-20 » de `roberto` est clos : il figure dans `derniere_session.md` de roberto (relu le 2026-11-09).
  - fait quand: la session Business a tracé l'échange de phase 5 dans son `signals.md` et les zones ui / gestion-clients ont repris les fonctionnalités dans leurs signaux, chaque constat de phase 4 est appliqué ou écarté par l'utilisateur dans la session concernée, et la session a tracé l'échange dans son propre `signals.md`, et le plan de la phase 6 est présenté à l'utilisateur et validé.
  - réf: `roadmap_fondations.md` phases 4, 5 et 6 ; `C:\Users\raph6\Documents\SerenIATech\SérénIATech_dev\.claude\zones.md`.
- Exercer le nouveau `/start` (v5.38, 4b corrigée en v5.39) en réel : affichage réduit par défaut, `--complet`, repli si une section manque, bloc 4c sur tout le fichier ; puis le propager aux projets suivis par `/update`. 2026-11-11 : cas racine, `--complet` et bloc 4c conformes ; restent `/start <zone> --complet` et le repli sans « Prochaine étape exacte ».
  - fait quand: les cas de `tests_manuels.md` (section « /start — affichage réduit ») sont joués et leurs divergences transmises au kit, traitées ou écartées.
  - réf: `tests_manuels.md` ; `.claude/commands/start.md` étapes 4, 4b et 4c ; `DEPLOYMENTS.md`.
Backlog : 20 entrées (finding 3, amélioration 4, piste 13 ; dont 1 sans `réf:` précis) — `_contexte/backlog.md`

### Backlog P2
Voir [`signals_backlog_2026-09-04.md`](_contexte/signals_backlog_2026-09-04.md) : validations secondaires, décisions de conception, maintenance et contexte historique.

## Garde-fous permanents
- Secrets Discord uniquement dans `.env` gitignoré ; vérifier `git check-ignore` et `git status` avant un commit qui touche `discord_com/`.
- Écriture dans `control_pc.sqlite` via Python `sqlite3` paramétré, jamais par `INSERT` shell.
- rclone : un remote = un projet, compte Google dédié par projet. Partage entre projets seulement s'il est déclaré explicitement à l'insertion du template et tracé `partagé: A + B` dans `DEPLOYMENTS.md` § Remotes rclone. Remotes actifs : `vibeobs_drive` (servomorph14), `sereniatech_drive` (sereniatech33), `rayonne_toi_drive` (rayonnetoi — partagé Rayonne_Toi + Appli_TSA_SDI_TDAH).
- Sous auto-mode, le classifieur bloque tout upload cloud de secrets (`rclone copy` de `.env` et assimilés). Un hook `/close` « Fin » ne peut faire que `--refresh-list` ; l'upload Drive est manuel, hors session. Le classifieur n'est pas désactivable par `permissions.allow`.

## Dernière session

# Session du 2026-11-11 (suite 3)

## Décisions prises
- `/start` étape 4b (v5.39) : `réf:` lues d'office seulement pour les actions citées par la prochaine étape, même en `--complet` (lire celles des 19 actions était trop coûteux en tokens).
- Cas `/start` racine, `--complet` et bloc 4c jugés conformes par l'utilisateur ; sections retirées de `tests_manuels.md`.

## Livrables produits ou modifiés
- `.claude/commands/start.md` et miroir template : étapes 1 et 4b.
- `CHANGELOG.md` (v5.39), `README.md`, `llms.txt`, `Protocole_start_close_context.md` (en-tête), `tests_manuels.md`.
- `DOCUMENTATION/_contexte/signals.md` : action `sessions_start_close.md` complétée (4b, v5.39).

## Hypothèses validées / invalidées
- VALIDE : `check_kit.py` et `check_docs.py` passaient après la correction de l'étape 4b (avant bump de version).
- EN ATTENTE : `/start <zone> --complet` et repli sans « Prochaine étape exacte » ; plan de la phase 6 de SérénIATech_dev.

## Prochaine étape exacte
Attendre le plan de la phase 6 (menée dans SérénIATech_dev). En attendant : jouer `/start documentation --complet` et le repli sans « Prochaine étape exacte » (`tests_manuels.md`, section « /start — affichage réduit »), ou traiter une P1 du kit : définition du « fichier de travail » de `/close` étape 9, ou frontmatter de `close.md` préservé par `/update`.

## Question bloquante pour la session suivante
Aucune
