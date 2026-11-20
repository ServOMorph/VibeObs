# Signals — documentation   (MAJ 2026-11-20)

## Actions ouvertes
- [P2|ouvert|zone kit] Valider le signal `/close` → Documentation sur une clôture réelle d'une autre zone
  - fait quand: un `/close <zone>` ajoute une action dédupliquée dans `DOCUMENTATION/_contexte/signals.md`, puis l'agent Documentation la traite
  - réf: .claude/commands/close.md, DOCUMENTATION/_contexte/signals.md

- [P2|ouvert|source=kit] Décider si `/delegation` (routage Codex / OpenCode / Ollama / sous-agents Haiku, journal `_codex/journal_delegation.md`) et la règle `disable-model-invocation` des commandes manuelles méritent un guide et une ligne d'INDEX
  - fait quand: guide créé ou mis à jour dans `DOCUMENTATION/`, ou décision explicite de ne pas documenter.
  - réf: .claude/commands/delegation.md, _codex/journal_delegation.md, CHANGELOG.md v6.1 et v6.2

- [P2|ouvert|source=kit] Mentionner dans le guide le repli de `/create_agent` [SORTIE] : message affiché dans un bloc de code si `Set-Clipboard` échoue (kit v6.7)
  - fait quand: `20_guides/creer_un_agent.md` ligne [SORTIE] mise à jour, ou décision explicite de ne pas le documenter.
  - réf: DOCUMENTATION/20_guides/creer_un_agent.md, .claude/commands/create_agent.md étape 10

- [P2|ouvert|source=kit] Traiter les 3 guides signalés « probablement en retard » par le nouvel avertissement de `check_docs.py` (kit v6.8) : `initialiser_un_projet.md`, `maintenance_du_kit.md`, `mettre_a_jour_un_projet.md` ; décider aussi si le hook PreCompact (`scripts/hook_precompact.py`) entre dans un guide.
  - fait quand: `python scripts/check_docs.py` n'affiche plus d'avertissement pour ces guides (mis à jour ou `maj` revue), et décision tracée pour le hook PreCompact.
  - réf: scripts/check_docs.py, scripts/hook_precompact.py, DOCUMENTATION/20_guides/

- [P2|ouvert|source=kit] Mettre à jour la ligne d'`INDEX.md` de `30_decisions/prises_de_controle.md` (cas 3 relais par téléphone et cas 4 mise en place du relais dans Roberto ajoutés le 2026-11-17, date `maj` du fichier passée à 2026-11-17) et décider si `20_guides/mode_telephone.md` documente `/telephone roberto` et `/relais_telephone` (kit v6.9)
  - fait quand: ligne d'INDEX et date alignées sur le fichier, et `20_guides/mode_telephone.md` mis à jour ou décision explicite de ne pas documenter le mode roberto.
  - réf: DOCUMENTATION/30_decisions/prises_de_controle.md, DOCUMENTATION/20_guides/mode_telephone.md, .claude/commands/telephone.md, .claude/commands/relais_telephone.md

- [P2|ouvert|source=kit] Décider si le blocage de la délégation à Codex (interrupteur `~/.codex/delegation_bloquee.flag`, 2026-11-19, complété le 2026-11-19 par la politique `~/.codex/politique_delegation.json` : modèle et binaire centralisés, seuils 50 % sur 5 h et 60 % sur 7 jours lus dans `~/.codex/sessions`, verrou exclusif par appel, `_codex/garde_codex.sh` pour les scripts shell ; accord de l'utilisateur à l'étape 7 du `/close` du 2026-11-19 pour en faire un guide `20_guides/politique_codex.md`), la délégation à VibeObs des téléchargements de modèles de 20 Go ou moins (jamais licences ni installations) et les règles du relais téléphone (jamais de silence, réponses courtes, points toutes les minutes) méritent une entrée dans `30_decisions/prises_de_controle.md`, `20_guides/mode_telephone.md` ou `20_guides/` (guide de la délégation)
  - fait quand: les entrées sont ajoutées à `DOCUMENTATION/` et à `INDEX.md`, ou décision explicite de ne pas les documenter.
  - réf: .claude/commands/delegation.md, .claude/commands/relais_telephone.md, DOCUMENTATION/30_decisions/prises_de_controle.md, CHANGELOG.md v7.1 et v7.2, _codex/run_codex.ps1, _codex/garde_codex.sh

- [P2|ouvert|source=maintenance] Décider si la migration des projets de `C:\...\ServOMorph` vers `D:\ServOMorph` (copie vérifiée par SHA-256, chemins en dur corrigés, original en quarantaine `D:\_quarantaine\<date>\` avec `manifeste.md`, jamais de suppression directe), l'outil `D:\_outils\venv_bureaux` (pyvda, placement des fenêtres sur un bureau virtuel) et le script `MAINTENANCE/scripts/migrer_projet.py` méritent un guide `20_guides/` et une ligne d'`INDEX.md` (emplacement des projets, convention de quarantaine)
  - fait quand: guide créé et ligne d'INDEX ajoutée, ou décision explicite de ne pas documenter.
  - réf: MAINTENANCE/scripts/migrer_projet.py, MAINTENANCE/_contexte/contexte.md

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
