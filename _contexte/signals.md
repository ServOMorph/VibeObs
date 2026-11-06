# Signals — VibeObs (MAJ 2026-11-06)

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
- Traiter l'écart `check_docs.py` : le commit `26b9cdd4` (2026-09-06) a modifié la ligne `maj:` du frontmatter de `journal.md` en plus d'ajouter une entrée en bas — le script considère cela comme une violation append-only. Décider : assouplir le contrôle pour exclure le frontmatter, ou traiter comme une vraie violation.
  - fait quand: `check_docs.py` passe sans écart, ou l'exception est explicitement documentée dans `40_specs/controle_qualite_base.md`.
  - réf: `scripts/check_docs.py`, `DOCUMENTATION/30_decisions/journal.md`, commit `26b9cdd4`.






- Mettre à jour `DOCUMENTATION/20_guides/initialiser_un_projet.md` (§ Fichiers déployés : ajouter `.gitignore` et `_docs/protocole_vibecoding.md`, retirer `agent_role_TEMPLATE.md` non copié ; § Déroulé : données sensibles inscrites dans `CLAUDE.md`) — propositions en attente de validation utilisateur.
  - fait quand: guide corrigé et ligne `INDEX.md` datée, ou refus tracé.
  - réf: `.claude/commands/init_projet.md` étapes 3-4, `DOCUMENTATION/_contexte/signals.md`.

- Corriger `init_projet.md` : étape 7 (préciser le tableau « Projets » de `DEPLOYMENTS.md` pour l'insertion de la ligne, pas la fin de fichier) et étape 5 (stager `AGENTS.md`/`GEMINI.md` quand Q7/Q8 sont « oui »), kit + template.
  - fait quand: les deux étapes sont corrigées dans `.claude/commands/init_projet.md` et son template, `check_kit.py` passe.
  - réf: `.claude/commands/init_projet.md` étapes 5 et 7 ; `D:\ServOMorph\REA` (`AGENTS.md`, `GEMINI.md` non commités). Écarts reproduits à l'identique lors de la création de `IA_Eco-Responsable` (2026-10-17) et de `creation_llm` (2026-10-22), contournés à la main. Reproduit une quatrième fois le 2026-11-03 sur `D:\xmage-test` (`AGENTS.md`/`GEMINI.md` non stagés par l'étape 5, ligne `DEPLOYMENTS.md` placée à la main sous la dernière ligne du tableau).


- Évaluer le mécanisme `DOCUMENTATION/` dans `D:\ServOMorph\Appli_TSA_SDI_TDAH` avant de le créer dans `SérénIATech_dev`. Mesures du 2026-10-24 : 0 consultation de la doc déclenchée par la seule consigne de `CLAUDE.md` sur 29 sessions locales ; 3 specs périmées (image de retour facultative, refus de consentement conservant le partage sans données de santé, exclusivité SDI/Avec DI) et dossiers imbriqués / durée de routine par jour non documentés.
  - fait quand: les 5 tests de la section « Évaluation DOCUMENTATION » de `tests_manuels.md` d'Appli sont passés (seuil 4/5 en autonomie dans le bon document), les specs périmées corrigées via `/start documentation` d'Appli, et une décision tracée sur les pistes (ligne « spec à mettre à jour » en fin de phase de roadmap, contrôle des « Sources » des specs dans `/close` étape 7, citation des documents clés dans les chartes d'agents).
  - réf: `D:\ServOMorph\Appli_TSA_SDI_TDAH\tests_manuels.md` ; `D:\ServOMorph\Appli_TSA_SDI_TDAH\DOCUMENTATION\40_specs\` ; Appli commits `3255b46`, `c970820`, `f6a6428`, `be4a1f0`.
- Créer `DOCUMENTATION/` dans `C:\Users\raph6\Documents\SerenIATech\SérénIATech_dev` (`/create_agent`) une fois l'évaluation Appli traitée. Décisions en attente de l'utilisateur : archiver `ClaudeCode/roadmap_base_connaissances.md` (6 phases TODO, base concurrente dans `ClaudeCode/base_connaissances/`) au profit de `DOCUMENTATION/` à la racine ; valider le périmètre proposé (carte du projet et processus d'abord ; exclusions : données sensibles, détail clients, tarification non stabilisée) ; exclure `Interim` et décider de l'inscrire aux données sensibles de `CLAUDE.md`. `AGENTS.md` et `GEMINI.md` de SérénIATech_dev ne mentionnent pas `DOCUMENTATION/` : le paragraphe du template est à ajouter. Migration de la section Spécificités projet vers l'INDEX déconseillée (déclencheurs plus fiables dans `CLAUDE.md`).
  - fait quand: l'agent `documentation` de SérénIATech_dev est créé, son `INDEX.md` existe, et les trois décisions ci-dessus sont tracées.
  - réf: `C:\Users\raph6\Documents\SerenIATech\SérénIATech_dev\ClaudeCode\roadmap_base_connaissances.md` ; `C:\Users\raph6\Documents\SerenIATech\SérénIATech_dev\.claude\CLAUDE.md` § Base de connaissances ; `.claude/commands/create_agent.md`.

- Faire appliquer le tri vers `_contexte/backlog.md` (v5.22 à v5.25) aux autres projets suivis. Fait : `SérénIATech_dev` en v5.25 (`/update`, 2026-10-29) ; `Appli_TSA_SDI_TDAH` : `close.md` aligné à la main sur le générique v5.25 (commit `d557510`, 2026-10-29), `start.md` non aligné. Validé sur un projet jetable (supprimé) : tri, plafond, péremption, promotion, croisement des `réf:`, catégories, ligne de renvoi totalisée, pas de bump sans modification de travail, constat rangé chez la zone concernée. Reste à exercer en réel : premier `/close` d'Appli en v5.25 (permissions `ls` / `test -e` dans `allowed-tools`, bilan sur ses 49 entrées de backlog sans catégorie, nombre d'entrées sans `réf:` précis), backlog créé à la première entrée, backlog vidé, `check_kit.py` présent avant commit.
  - fait quand: les autres projets de `DEPLOYMENTS.md` sont à v5.25 ou leur report est tracé, et un `/close` réel d'Appli en v5.25 a été observé, ses divergences transmises au kit.
  - réf: `DEPLOYMENTS.md` ; `CHANGELOG.md` v5.22 à v5.25 ; `tests_manuels.md` section « /close v5.22 » ; `D:\ServOMorph\Appli_TSA_SDI_TDAH\.claude\commands\close.md`.
- Décider si `/update` doit préserver les personnalisations du frontmatter de `close.md` hors bloc `SPECIFICITES PROJET`. Constat 2026-10-27 : `SérénIATech_dev` avait `PowerShell(python *menage_zone.py*)` dans `allowed-tools` ; la copie du kit l'aurait supprimée (conservée à la main), et le contrôle « identique hors spécificités » de l'étape 10 signale cet écart.
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

- Corriger l'incompatibilité `templates/parallel_agents` / `/insert_template` : ses deux fichiers contiennent des placeholders hors de la liste reconnue (`{{ROLE}}`, `{{WORKTREE}}`, `{{BRANCHE}}`, `{{ALIAS_PARENT}}`, `{{MEMBRES}}`...), donc l'insertion est toujours bloquée alors que `/create_projet` le propose (constat à la création de `Fiches_IME`, 2026-10-31).
  - fait quand: le template s'insère sans blocage (placeholders pris en charge ou template retiré de la liste de `/create_projet`) et `check_kit.py` passe.
  - réf: `templates/parallel_agents/` ; `.claude/commands/insert_template.md` étape 7 ; `.claude/commands/create_projet.md` [TEMPLATES].
Backlog : 18 entrées (finding 3, amélioration 4, piste 11) — `_contexte/backlog.md`

### Backlog P2
Voir [`signals_backlog_2026-09-04.md`](_contexte/signals_backlog_2026-09-04.md) : validations secondaires, décisions de conception, maintenance et contexte historique.

## Garde-fous permanents
- Secrets Discord uniquement dans `.env` gitignoré ; vérifier `git check-ignore` et `git status` avant un commit qui touche `discord_com/`.
- Écriture dans `control_pc.sqlite` via Python `sqlite3` paramétré, jamais par `INSERT` shell.
- rclone : un remote = un projet, compte Google dédié par projet. Partage entre projets seulement s'il est déclaré explicitement à l'insertion du template et tracé `partagé: A + B` dans `DEPLOYMENTS.md` § Remotes rclone. Remotes actifs : `vibeobs_drive` (servomorph14), `sereniatech_drive` (sereniatech33), `rayonne_toi_drive` (rayonnetoi — partagé Rayonne_Toi + Appli_TSA_SDI_TDAH).
- Sous auto-mode, le classifieur bloque tout upload cloud de secrets (`rclone copy` de `.env` et assimilés). Un hook `/close` « Fin » ne peut faire que `--refresh-list` ; l'upload Drive est manuel, hors session. Le classifieur n'est pas désactivable par `permissions.allow`.

## Dernière session

# Session du 2026-11-06 (suite : phase 2)

## Décisions prises
- Phase 1 (fondations) et phase 2 (audit du kit) de `roadmap_fondations.md` closes ; `check_docs.py` ignore désormais le frontmatter dans le contrôle append-only du journal.
- Tri des actions P1 validé par l'utilisateur : 12 actions vers le backlog, 2 doublons retirés, 1 laissée faute de `réf:` précis ; 20 actions P1 restent (plafond atteint).
- Guides DOCUMENTATION en retard confiés à l'agent `documentation` (triage dans son `signals.md`, ajouté à ce `/close`).

## Livrables produits ou modifiés
- `scripts/check_docs.py` : contrôle append-only du journal limité au corps (passe, exit 0).
- `llms.txt` : version v5.27, 9 commandes et 2 scripts de contrôle ajoutés. `README.md` : § État actuel ramené à la v5.27.
- `_contexte/backlog.md` : 14 entrées ajoutées (12 triées, détection Codex, retex de `/maintenance`).
- `roadmap_fondations.md`, `.claude/memory.md` (entrée « traçage des échanges »).

## Hypothèses validées / invalidées
- VALIDE : `check_kit.py`, `check_docs.py` et `pytest` (29 passés, 1 ignoré) passent.
- INVALIDE : retex de `/maintenance` du 2026-11-06 non transcrit avant le compactage -> refait en backlog.
- EN ATTENTE : détection d'une session Codex.

## Prochaine étape exacte
Phase 3 de `roadmap_fondations.md` : création de l'agent PEDAGOGIE par `/create_agent` (périmètre d'écriture limité à `PEDAGOGIE/`, sans publication Netlify), puis choix du parcours.

## Question bloquante pour la session suivante
Aucune
