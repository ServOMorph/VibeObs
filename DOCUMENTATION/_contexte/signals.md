# Signals — documentation   (MAJ 2026-11-14)

## Actions ouvertes
- [P2|ouvert|zone kit] Valider le signal `/close` → Documentation sur une clôture réelle d'une autre zone
  - fait quand: un `/close <zone>` ajoute une action dédupliquée dans `DOCUMENTATION/_contexte/signals.md`, puis l'agent Documentation la traite
  - réf: .claude/commands/close.md, DOCUMENTATION/_contexte/signals.md

## Dernière session (2026-11-14)
<!-- Écrasé intégralement par /close. Synthèse < 25 lignes. -->
# Session du 2026-11-14

## Décisions prises
- Guides alignés sur le kit v6.0 : journal de session (v5.44), `/start` réduit (v5.38 à v5.40), `## Fin` après le push conditionnel (v5.37), `/init_projet` sans question de stack (v6.0), `/update` étape 8bis.

## Livrables produits ou modifiés
- `20_guides/sessions_start_close.md`, `20_guides/mettre_a_jour_un_projet.md`, `20_guides/initialiser_un_projet.md` : mis à jour, lignes `INDEX.md` datées 2026-11-14.
- `20_guides/creer_un_agent.md` aligné sur v5.20 ; `20_guides/sauvegarde_rclone.md`, `maintenance_du_kit.md`, `mode_telephone.md` créés ; sous-section « Hooks de zone » relue face aux templates `on_*_TEMPLATE.md` (fidèle).
- `30_decisions/journal.md` : deux entrées ajoutées.

## Hypothèses validées / invalidées
- VALIDE : `python scripts/check_docs.py` passe après les modifications.
- EN ATTENTE : relecture des modifications par l'utilisateur ; commit non fait.

## Prochaine étape exacte
Valider le signal `/close` → Documentation sur une clôture réelle d'une autre zone.

## Question bloquante pour la session suivante
Aucune
