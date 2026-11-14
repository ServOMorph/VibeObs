# Signals — VibeObs (MAJ 2026-11-14)

## Actions ouvertes — pilotage

### P1 — à traiter avant le backlog
- Valider en conditions réelles les nouveaux `/start` (étape 4c) et `/close` (étapes 3-bis, 13, 15) déployés dans `SérénIATech_dev` par `/update` le 2026-10-14. Scénario 1 (`/start` racine) : sortie reçue, aucun bloc 4c affiché, `roadmap_actions_ouvertes_luna.md` laissée à la racine sur décision de l'utilisateur ; scénarios 2 à 6 non rejoués. 2026-10-27 : scénarios 1 et 2 validés en v5.23 (correctif 4c, commit `03b5a54`) ; scénarios 3 à 6 restants (dont le `/close` racine après travail dans SHORTS). 2026-10-27 : `/close` racine sans travail dans SHORTS observé (commit `ca0b2c0` de SérénIATech_dev), deux divergences à trancher consignées dans `tests_manuels.md`. 2026-10-27 : `close.md` de `SérénIATech_dev` mis à jour en v5.22 ; le test « /close v5.22 » peut se jouer dans la même session. 2026-10-29 : `close.md` en v5.25 et `start.md` en v5.23 dans `SérénIATech_dev` (`/update`, permission `menage_zone.py` conservée à la main) ; scénarios 3 à 6 toujours non rejoués.
  - fait quand: les 6 scénarios de `tests_manuels.md` (section « /start et /close — attribution par zone ») sont rejoués et leurs divergences transmises au kit, traitées ou écartées.
  - réf: `tests_manuels.md` ; `.claude/commands/close.md` étapes 3-bis et 13 ; `.claude/commands/start.md` étape 4c ; `SérénIATech_dev` commit « update: protocole vibecoding — zone racine — kit v5.20 ».
- Effectuer l'upload Drive d'Appli resté en attente. 2026-11-14 : `on_close.md` d'Appli est commité (dernier commit `b78f73a`) ; son § Fin ne se limite plus à `--refresh-list` : il demande le passage en mode manuel (`Shift+Tab`) et attend la confirmation écrite avant les copies claire et chiffrée.
  - fait quand: un `/close` réel d'Appli a exécuté son § Fin en mode manuel et `backup_project.py . --check` passe.
  - réf: `D:\ServOMorph\Appli_TSA_SDI_TDAH\_contexte\on_close.md` § Fin ; `DOCUMENTATION/20_guides/sauvegarde_rclone.md`.
- Porter les 2 correctifs `backup_project.py` (exclusion des artefacts régénérables + sorties tolérantes à l'encodage) à la copie vendored de `Rayonne_Toi`. 2026-11-12 : `Meuniers` archivé, non-port décidé ; pour `Rayonne_Toi`, port reporté : la copie a divergé (fonction `load_config` absente du template) et porte des modifications non commitées d'origine inconnue. À fusionner à la main une fois ces modifications commitées par une session de `Rayonne_Toi`.
  - fait quand: les modifications locales de la copie `Rayonne_Toi` sont commitées, puis les 2 correctifs y sont fusionnés sans perdre `load_config`.
  - réf: `templates/rclone_backup/backup_project.py` (corrigé) ; `D:\ServOMorph\Rayonne_Toi\claude-vibecoding-kit\rclone_backup\backup_project.py`.
- Exécuter le backup réel de `SérénIATech_dev` vers `sereniatech_drive` et vérifier les `/close` des projets partageant `rayonne_toi_drive`.
  - fait quand: `tests_manuels.md` sections « rclone multicompte » toutes validées et retirées.
  - réf: `tests_manuels.md`.
- Valider le correctif `templates/discord_com` en conditions réelles : deux notifications consécutives reçues et file finale `idle`.
  - fait quand: le bot local reçoit puis transmet deux notifications réelles sans perte.
  - réf: `templates/discord_com/`, `discord_com/` local (non versionné).
- Résoudre le vol de focus avant la phase 3 de `_archives/local/roadmap_reprise_multicompte.md` (archivée hors Git le 2026-11-05). 2026-10-12 : correctif `focus_fiable.ps1` codé et branché dans 4 scripts, validé en syntaxe seulement.
  - fait quand: le test manuel de `tests_manuels.md` (section « vol de focus ») est validé et `roadmap_reprise_multicompte.md` + `SKILL.md` sont mis à jour.
  - réf: `_archives/local/roadmap_reprise_multicompte.md` ; `skills/chatgpt-orchestrateur/scripts/focus_fiable.ps1` ; `tests_manuels.md`.
- Valider la conversion de `/create_agent` en exécution réelle. 2026-11-13 : `/create_memory <alias_zone>` (routage, en-tête créé) et `/insert_template` (ligne de registre, pas de doublon à la ré-insertion) validés sur zone et projet jetables, supprimés après test.
  - fait quand: `/create_agent` est exercé au moins une fois avec son résultat attendu.
  - réf: `_contexte/signals_backlog_2026-09-04.md` ; `.claude/commands/create_agent.md`.
- Évaluer le mécanisme `DOCUMENTATION/` dans `D:\ServOMorph\Appli_TSA_SDI_TDAH` avant de le créer dans `SérénIATech_dev`. Mesures du 2026-10-24 : 0 consultation de la doc déclenchée par la seule consigne de `CLAUDE.md` sur 29 sessions locales ; 3 specs périmées (image de retour facultative, refus de consentement conservant le partage sans données de santé, exclusivité SDI/Avec DI) et dossiers imbriqués / durée de routine par jour non documentés.
  - fait quand: les 5 tests de la section « Évaluation DOCUMENTATION » de `tests_manuels.md` d'Appli sont passés (seuil 4/5 en autonomie dans le bon document), les specs périmées corrigées via `/start documentation` d'Appli, et une décision tracée sur les pistes (ligne « spec à mettre à jour » en fin de phase de roadmap, contrôle des « Sources » des specs dans `/close` étape 7, citation des documents clés dans les chartes d'agents).
  - réf: `D:\ServOMorph\Appli_TSA_SDI_TDAH\tests_manuels.md` ; `D:\ServOMorph\Appli_TSA_SDI_TDAH\DOCUMENTATION\40_specs\` ; Appli commits `3255b46`, `c970820`, `f6a6428`, `be4a1f0`.
- Créer `DOCUMENTATION/` dans `C:\Users\raph6\Documents\SerenIATech\SérénIATech_dev` (`/create_agent`) une fois l'évaluation Appli traitée. Décisions en attente de l'utilisateur : archiver `ClaudeCode/roadmap_base_connaissances.md` (6 phases TODO, base concurrente dans `ClaudeCode/base_connaissances/`) au profit de `DOCUMENTATION/` à la racine ; valider le périmètre proposé (carte du projet et processus d'abord ; exclusions : données sensibles, détail clients, tarification non stabilisée) ; exclure `Interim` et décider de l'inscrire aux données sensibles de `CLAUDE.md`. `AGENTS.md` et `GEMINI.md` de SérénIATech_dev ne mentionnent pas `DOCUMENTATION/` : le paragraphe du template est à ajouter. Migration de la section Spécificités projet vers l'INDEX déconseillée (déclencheurs plus fiables dans `CLAUDE.md`).
  - fait quand: l'agent `documentation` de SérénIATech_dev est créé, son `INDEX.md` existe, et les trois décisions ci-dessus sont tracées.
  - réf: `C:\Users\raph6\Documents\SerenIATech\SérénIATech_dev\ClaudeCode\roadmap_base_connaissances.md` ; `C:\Users\raph6\Documents\SerenIATech\SérénIATech_dev\.claude\CLAUDE.md` § Base de connaissances ; `.claude/commands/create_agent.md`.

- Faire appliquer le tri vers `_contexte/backlog.md` (v5.22 à v5.25) aux autres projets suivis. Fait : `SérénIATech_dev` en v5.25 (`/update`, 2026-10-29) ; `Appli_TSA_SDI_TDAH` : `close.md` aligné à la main sur le générique v5.25 (commit `d557510`, 2026-10-29), `start.md` non aligné. Validé sur un projet jetable (supprimé) : tri, plafond, péremption, promotion, croisement des `réf:`, catégories, ligne de renvoi totalisée, pas de bump sans modification de travail, constat rangé chez la zone concernée. Reste à exercer en réel : premier `/close` d'Appli en v5.25 (permissions `ls` / `test -e` dans `allowed-tools`, bilan sur ses 49 entrées de backlog sans catégorie, nombre d'entrées sans `réf:` précis), backlog créé à la première entrée, backlog vidé, `check_kit.py` présent avant commit. 2026-11-14 : 21 projets sans session ouverte passés en v5.44 (au-dessus de v5.25).
  - fait quand: les autres projets de `DEPLOYMENTS.md` sont à v5.25 ou leur report est tracé, et un `/close` réel d'Appli en v5.25 a été observé, ses divergences transmises au kit.
  - réf: `DEPLOYMENTS.md` ; `CHANGELOG.md` v5.22 à v5.25 ; `tests_manuels.md` section « /close v5.22 » ; `D:\ServOMorph\Appli_TSA_SDI_TDAH\.claude\commands\close.md`.

- Suivre l'implémentation du rapport de phase 5 (`roadmap_fondations.md` phase 5) : relayé le 2026-11-09 à « Business SerenIA Tech », reformulation validée, ordre révisé ; implémentation par les zones ui et gestion-clients (1, 2, 5, 3, 6) et business (7), la 4 attendant la décision CAE ; lignes orphelines de `Gestion clients/_contexte/signals.md` à reclasser par cette zone. Suivre aussi l'application, par la session ouverte « Business SerenIA Tech », des constats de l'audit de `SérénIATech_dev` (phase 4 close, constats transmis le 2026-11-08, reformulation contrôlée). Annoncé par cette session : renommage indexé non commité de `20261016_1830_reunion.md` (gestion-clients) et copies `.opencode/commands/` archivées dans `_archives/racine_2026-11-08/opencode_commands/`, avec l'accord de l'utilisateur. Restent : modification du 2026-11-07 9h11 (linkedin, roberto) qualifiée de rangement par la session Business, origine toujours inconnue (ce n'est pas elle) ; `contexte.md` de `linkedin` ligne 20 périmée ; 13 zones sauvegardées hors `/close` (signals non mis à jour) ; `VertIA` signalé seulement. Suivre aussi la phase 6 (plan d'automatisation), menée par l'utilisateur dans la session SérénIATech_dev (décision du 2026-11-09) : plan à relire à son retour pour la validation de la phase. Le bloc « Dernière session 2026-10-20 » de `roberto` est clos : il figure dans `derniere_session.md` de roberto (relu le 2026-11-09).
  - fait quand: la session Business a tracé l'échange de phase 5 dans son `signals.md` et les zones ui / gestion-clients ont repris les fonctionnalités dans leurs signaux, chaque constat de phase 4 est appliqué ou écarté par l'utilisateur dans la session concernée, et la session a tracé l'échange dans son propre `signals.md`, et le plan de la phase 6 est présenté à l'utilisateur et validé.
  - réf: `roadmap_fondations.md` phases 4, 5 et 6 ; `C:\Users\raph6\Documents\SerenIATech\SérénIATech_dev\.claude\zones.md`.
- Propager le journal de session (kit v5.44) et les `/start` récents aux projets suivis. 2026-11-14 : v5.44 écrite dans le kit (journal gitignoré ; `/start` l'affiche s'il est non vide ; `/close` l'intègre puis le vide ; `/update` étape 8bis). 9 sessions Claude Code ouvertes ont reçu une version unique (reformulation contrôlée, accord de l'utilisateur dans chaque session) ; application confirmée par creation_3d, XMage, zone UI SérénIa Tech, VertIA_v3, World Model, Creation video, Creation llm et Site Internet v3 ; correctif `.gitignore` confirmé par creation_3d, VertIA_v3, zone UI, Creation video, XMage et Site Internet v3 (appliqué d'emblée), non confirmé par Creation llm et World Model ; Sécurité (nettoyage_pc, hors Git) sans retour d'application. `/update` v5.44 sur 21 projets sans session ouverte, un par un, 7 contrôles passés (commits `update: protocole vibecoding` dans chaque dépôt ; Moulin du Sud commité à la main : son dépôt est `Lieux_Hybrides`, dossier suivi sous `lieux/`). Restent : `SérénIATech_dev` (v5.42) ; les projets à session ouverte (`Nettoyage_PC`, `site_internet_ST_v3`, `creation_llm`, `VertIA_v3`, `creation_3d`, `WorldModel`, `creation_videos`, `xmage-test`), dont les blocs projet portent la règle mais dont le `/update` complet reste à faire à la fermeture des sessions (relever les sessions ouvertes avant). L'association nom de session / dossier est supposée, non vérifiée (hors VertIA_v3). `telephone.md` : `Nettoyage_PC` (v3.10) ne l'a pas, `/update` le copiera. Reste aussi l'observation d'un `/start` en réel dans un projet suivi.
  - fait quand: les projets restants sont mis à jour par `/update` en v5.44 (ou leur report est tracé), un cycle réel du journal a été observé dans un projet suivi (`tests_manuels.md`) et le `/start` de l'un des projets suivis a été observé en réel.
  - réf: `DEPLOYMENTS.md` ; `tests_manuels.md` section « Journal de session (v5.44) » ; `.claude/commands/update.md` étape 8bis ; `.claude/commands/start.md` étapes 3 et 4.
- Tester `/migration_canva` avec deux comptes Canva réels (kit v6.2, lancement manuel) et confirmer au prochain `/start` que les commandes en `disable-model-invocation` (`cherche_fonction`, `cherche_meilleure_action`, `maintenance`, `migration_canva`) ne figurent plus dans la liste des skills du modèle.
  - fait quand: une migration d'au moins un dossier est menée jusqu'à l'étape 6 (preuve finale), les 5 points « à vérifier » du fichier sont tranchés, et l'absence des 4 commandes de la liste est constatée.
  - réf: `.claude/commands/migration_canva.md` ; `CHANGELOG.md` v6.2.
- Exercer `/delegation` sur un second lot et mesurer l'économie de tokens Claude (usage des sous-agents disponible, Codex et OpenCode non mesurés).
  - fait quand: un second lot est tracé dans `_codex/journal_delegation.md` avec son bilan, et une règle de routage est ajustée ou confirmée.
  - réf: `.claude/commands/delegation.md` ; `_codex/journal_delegation.md`.
Backlog : 22 entrées (finding 1, amélioration 5, piste 16) — `_contexte/backlog.md`

### Backlog P2
Voir [`signals_backlog_2026-09-04.md`](signals_backlog_2026-09-04.md) : validations secondaires, décisions de conception, maintenance et contexte historique.

## Garde-fous permanents
- Secrets Discord uniquement dans `.env` gitignoré ; vérifier `git check-ignore` et `git status` avant un commit qui touche `discord_com/`.
- Écriture dans `control_pc.sqlite` via Python `sqlite3` paramétré, jamais par `INSERT` shell.
- rclone : un remote = un projet, compte Google dédié par projet. Partage entre projets seulement s'il est déclaré explicitement à l'insertion du template et tracé `partagé: A + B` dans `DEPLOYMENTS.md` § Remotes rclone. Remotes actifs : `vibeobs_drive` (servomorph14), `sereniatech_drive` (sereniatech33), `rayonne_toi_drive` (rayonnetoi — partagé Rayonne_Toi + Appli_TSA_SDI_TDAH).
- Sous auto-mode, le classifieur bloque tout upload cloud de secrets (`rclone copy` de `.env` et assimilés). Un hook `/close` « Fin » qui sauvegarde demande le passage en mode manuel et attend une confirmation écrite avant toute copie ; sans réponse, il ne lance rien et trace l'upload restant. Le classifieur n'est pas désactivable par `permissions.allow`.

## Dernière session

# Session du 2026-11-14 (suite)

## Décisions prises
- `/delegation` (kit) : Codex, OpenCode gratuit, Ollama et sous-agents Haiku comme exécutants ; Claude orchestre ; sollicitations limitées (commit/push main, écriture hors projet, exécutant bloqué, irréversible) ; journal `_codex/journal_delegation.md` versionné.
- Commandes à lancement manuel : `disable-model-invocation: true` (description hors contexte du modèle, `/nom` conservé) plutôt qu'un déplacement hors de `.claude/`.
- Corrections de l'audit OpenCode appliquées par `/close` (règle « seul `/close` écrit `signals.md` »).

## Livrables produits ou modifiés
- `DOCUMENTATION/` : 4 guides alignés, 3 guides créés (`f325480`).
- Kit v6.1 (`dee116d`, `45f4f09`, `3eb5736`) : `/delegation`, lanceurs PS 5.1 corrigés, 3 findings du backlog corrigés par Codex ; v6.2 (`dfd802b`) : `/migration_canva`, `disable-model-invocation` sur 4 commandes.
- `_contexte/` : signals, backlog (3 findings retirés), contexte mis à jour par ce `/close`.

## Hypothèses validées / invalidées
- VALIDE : Codex (correctif cadré, 88 s) et OpenCode gratuit (audit, 13 anomalies exactes) utilisables ; `check_kit.py` et `check_docs.py` passent.
- INVALIDE : Ollama pour une synthèse demandant du jugement (bilan superficiel, refait) -> réservé aux textes mécaniques.
- EN ATTENTE : effet réel de `disable-model-invocation` sur `.claude/commands/` ; 5 points Canva « à vérifier ».

## Prochaine étape exacte
Tester `/migration_canva` avec les deux comptes Canva ; au `/start` suivant, constater l'absence des 4 commandes manuelles de la liste des skills. Ensuite : `/update` v5.44 de `SérénIATech_dev` et des projets à session fermée.

## Question bloquante pour la session suivante
Dans quels dossiers tournent les sessions « pilote-74 » et « agent-trader-f8 » ?
