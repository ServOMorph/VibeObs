# Signals — documentation   (MAJ 2026-09-04)

## Actions ouvertes
- [P2|ouvert|zone kit] Valider le signal `/close` → Documentation sur une clôture réelle d'une autre zone
  - fait quand: un `/close <zone>` ajoute une action dédupliquée dans `DOCUMENTATION/_contexte/signals.md`, puis l'agent Documentation la traite
  - réf: .claude/commands/close.md, DOCUMENTATION/_contexte/signals.md
- [P2|ouvert|source=kit] Relire la sous-section « Hooks de zone » de `20_guides/sessions_start_close.md` face aux sources canoniques (`start.md`/`close.md` étapes 3-bis/5-bis/2-bis/14-ter, `templates/on_start_TEMPLATE.md`, `templates/on_close_TEMPLATE.md`)
  - fait quand: la sous-section est confirmée fidèle aux numéros d'étape et au contrat des sections, ou corrigée
  - réf: DOCUMENTATION/20_guides/sessions_start_close.md, templates/on_start_TEMPLATE.md, templates/on_close_TEMPLATE.md
- [P2|ouvert|source=kit] `check_docs.py` échoue : « Journal non append-only : le commit 26b9cdd4 a modifié des lignes existantes » — écart préexistant hérité, sans lien avec les sessions rclone
  - fait quand: `python scripts/check_docs.py` repasse (journal corrigé ou règle du contrôle ajustée), ou l'écart est acté définitivement comme toléré
  - réf: scripts/check_docs.py, DOCUMENTATION/30_decisions/journal.md, commit 26b9cdd4
- [P2|ouvert|source=kit] Décider si la règle rclone « un remote = un projet, partage déclaré et tracé » mérite une entrée de base de connaissances (guide backup ou décision) et une ligne d'INDEX
  - fait quand: entrée créée dans `DOCUMENTATION/` (ou décision explicite de ne pas documenter), face aux sources `insert_template.md` étape 7bis, `templates/rclone_backup/README.md`, `templates/rclone_backup/analysis/garde_fou_collision.md`
  - réf: .claude/commands/insert_template.md, templates/rclone_backup/README.md, _archives/roadmap_rclone_multicompte.md
- [P2|ouvert|source=kit] Décider si la limite « sous auto-mode le classifieur bloque tout upload cloud de secrets ; un hook `/close` Fin ne peut faire que `--refresh-list`, l'upload est manuel hors session » mérite une entrée de base de connaissances (guide sessions/hooks) et une ligne d'INDEX.
  - fait quand: entrée créée ou mise à jour dans `DOCUMENTATION/` (ou décision explicite de ne pas documenter), face aux sources `templates/rclone_backup/backup_project.py`, `Appli_TSA_SDI_TDAH/_contexte/on_close.md` § Fin.
  - réf: DOCUMENTATION/20_guides/sessions_start_close.md, templates/rclone_backup/backup_project.py
- [P2|ouvert|source=kit] Mettre à jour `20_guides/initialiser_un_projet.md` après kit v5.17 : § Fichiers déployés (ajouter `.gitignore`, `_docs/protocole_vibecoding.md` ; retirer `agent_role_TEMPLATE.md` non copié par l'étape 3), § Déroulé (données sensibles inscrites dans `CLAUDE.md`)
  - fait quand: guide corrigé et date MAJ de sa ligne `INDEX.md` actualisée, ou décision explicite de ne pas le modifier
  - réf: .claude/commands/init_projet.md, CHANGELOG.md v5.17
- [P2|ouvert|source=kit] Mettre à jour `20_guides/creer_un_agent.md` après kit v5.20 : [PREFLIGHT] (parent englobant, remontée du projet cible, actions du parent), [COLLECTE] (lecture étendue, données sensibles), [ECRITURE] (migration d'actions, report si renommage refusé), § Après création (« zone racine » -> zone englobante)
  - fait quand: guide corrigé et date MAJ de sa ligne `INDEX.md` actualisée, ou décision explicite de ne pas le modifier
  - réf: .claude/commands/create_agent.md, CHANGELOG.md v5.20
- [P2|ouvert|source=kit] Comparer les guides de `DOCUMENTATION/20_guides/` aux commandes et versions du kit postérieures à leur date `INDEX.md` (guides datés du 2026-08-21 au 2026-09-04 ; kit en v5.27, dont `/maintenance` et `/telephone` absents de l'INDEX) et décider des mises à jour ; relever aussi les sources canoniques `llms.txt` et `README.md` mises à jour le 2026-11-06
  - fait quand: chaque guide concerné est mis à jour avec sa ligne `INDEX.md` datée, ou la décision de ne pas le modifier est tracée
  - réf: DOCUMENTATION/INDEX.md, CHANGELOG.md v5.20 à v5.27, llms.txt
- [P2|ouvert|source=kit] Mettre à jour `20_guides/sessions_start_close.md` après kit v5.37 : tableau des hooks (ligne 33 : `## Fin` « après `git push` » -> après le push conditionnel de l'étape 14) et contrat (ligne 36 : « même après un échec du push » -> après le commit, que le push ait eu lieu, ait été sauté ou ait échoué)
  - fait quand: guide corrigé et date MAJ de sa ligne `INDEX.md` actualisée, ou décision explicite de ne pas le modifier
  - réf: .claude/commands/close.md étapes 14 et 14-ter, CHANGELOG.md v5.37
- [P2|ouvert|source=kit] Mettre à jour `20_guides/sessions_start_close.md` après kit v5.38 : ligne 14 (`/start` charge `signals.md`) -> affichage réduit par défaut (« Prochaine étape exacte », « Question bloquante », ligne de compteurs), `--complet` pour le fichier entier, étape 4b limitée aux `réf:` de la prochaine étape, y compris en `--complet` (v5.39)
  - fait quand: guide corrigé et date MAJ de sa ligne `INDEX.md` actualisée, ou décision explicite de ne pas le modifier
  - réf: .claude/commands/start.md étapes 4, 4b et 4c, CHANGELOG.md v5.38 et v5.39
- [info|source=kit] L'écart `check_docs.py` (journal append-only, commit 26b9cdd4) est résolu le 2026-11-06 : le contrôle ignore le frontmatter ; `python scripts/check_docs.py` passe. L'action « `check_docs.py` échoue » ci-dessus peut être retirée par l'agent documentation.
  - réf: scripts/check_docs.py

## Dernière session (2026-09-04)
<!-- Écrasé intégralement par /close. Synthèse < 25 lignes. -->
# Session du 2026-09-04

## Décisions prises
- `check_docs.py` devient le gate mécanique de `/doc_sync` ; le passage sémantique reste une relecture ciblée des documents concernés.
- Les informations durables issues des autres zones sont mises en file de triage Documentation au `/close`, puis publiées seulement après validation utilisateur.

## Livrables produits ou modifiés
- `scripts/check_docs.py` : créé et validé sur la base réelle.
- `.claude/commands/doc_sync.md` : gate documentaire ajouté.
- `.claude/commands/close.md` et son miroir : file de triage Documentation ajoutée.
- `DOCUMENTATION/` : guide, index et journal synchronisés.

## Hypothèses validées / invalidées
- VALIDE : `python scripts/check_docs.py` et `python scripts/check_kit.py` passent sur la base réelle.
- VALIDE : le contrôle CRLF de `check_kit.py` doit cibler les seuls fichiers versionnés, conformément à son contrat.

## Prochaine étape exacte
Exécuter un `/close` d'une zone non documentaire ayant produit une information durable, puis vérifier la création et la déduplication de l'action de triage.

## Question bloquante pour la session suivante
Aucune
