# Signals — documentation   (MAJ 2026-09-04)

## Actions ouvertes
- [P2|ouvert|zone kit] Valider le signal `/close` → Documentation sur une clôture réelle d'une autre zone
  - fait quand: un `/close <zone>` ajoute une action dédupliquée dans `DOCUMENTATION/_contexte/signals.md`, puis l'agent Documentation la traite
  - réf: .claude/commands/close.md, DOCUMENTATION/_contexte/signals.md

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
