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
