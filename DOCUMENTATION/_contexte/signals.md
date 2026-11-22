# Signals — documentation   (MAJ 2026-11-22)

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

- [P2|ouvert|source=kit] Décider si le hook PreCompact (`scripts/hook_precompact.py`) entre dans un guide (les 3 guides en retard ont été mis à jour le 2026-11-21, commit 56fa3cc, `check_docs.py` sans avertissement)
  - fait quand: guide créé ou mis à jour, ou décision explicite de ne pas documenter le hook.
  - réf: scripts/hook_precompact.py, DOCUMENTATION/20_guides/

- [P2|ouvert|source=kit] Mettre à jour la ligne d'`INDEX.md` de `30_decisions/prises_de_controle.md` (cas 3 relais par téléphone et cas 4 mise en place du relais dans Roberto ajoutés le 2026-11-17, date `maj` du fichier passée à 2026-11-17) et décider si `20_guides/mode_telephone.md` documente `/telephone roberto` et `/relais_telephone` (kit v6.9)
  - fait quand: ligne d'INDEX et date alignées sur le fichier, et `20_guides/mode_telephone.md` mis à jour ou décision explicite de ne pas documenter le mode roberto.
  - réf: DOCUMENTATION/30_decisions/prises_de_controle.md, DOCUMENTATION/20_guides/mode_telephone.md, .claude/commands/telephone.md, .claude/commands/relais_telephone.md

- [P2|ouvert|source=kit] Décider si le blocage de la délégation à Codex (interrupteur `~/.codex/delegation_bloquee.flag`, 2026-11-19, complété le 2026-11-19 par la politique `~/.codex/politique_delegation.json` : modèle et binaire centralisés, seuils 50 % sur 5 h et 60 % sur 7 jours lus dans `~/.codex/sessions`, verrou exclusif par appel, `_codex/garde_codex.sh` pour les scripts shell ; accord de l'utilisateur à l'étape 7 du `/close` du 2026-11-19 pour en faire un guide `20_guides/politique_codex.md`), la délégation à VibeObs des téléchargements de modèles de 20 Go ou moins (jamais licences ni installations) et les règles du relais téléphone (jamais de silence, réponses courtes, points toutes les minutes) méritent une entrée dans `30_decisions/prises_de_controle.md`, `20_guides/mode_telephone.md` ou `20_guides/` (guide de la délégation)
  - fait quand: les entrées sont ajoutées à `DOCUMENTATION/` et à `INDEX.md`, ou décision explicite de ne pas les documenter.
  - réf: .claude/commands/delegation.md, .claude/commands/relais_telephone.md, DOCUMENTATION/30_decisions/prises_de_controle.md, CHANGELOG.md v7.1 et v7.2, _codex/run_codex.ps1, _codex/garde_codex.sh

- [P2|ouvert|source=maintenance] Décider si la migration des projets de `C:\...\ServOMorph` vers `D:\ServOMorph` (copie vérifiée par SHA-256, chemins en dur corrigés, original en quarantaine `D:\_quarantaine\<date>\` avec `manifeste.md`, jamais de suppression directe), l'outil `D:\_outils\venv_bureaux` (pyvda, placement des fenêtres sur un bureau virtuel) et le script `MAINTENANCE/scripts/migrer_projet.py` méritent un guide `20_guides/` et une ligne d'`INDEX.md` (emplacement des projets, convention de quarantaine)
  - fait quand: guide créé et ligne d'INDEX ajoutée, ou décision explicite de ne pas documenter.
  - réf: MAINTENANCE/scripts/migrer_projet.py, MAINTENANCE/_contexte/contexte.md

- [P2|ouvert|source=kit] Décider si le périmètre de VibeObs (décision du 2026-11-20 : dedans, dehors, règles gardées) mérite un document dans `10_concepts/` et une ligne d'`INDEX.md`
  - fait quand: document créé et ligne d'INDEX ajoutée, ou décision explicite de ne pas le documenter.
  - réf: `_contexte/contexte.md` § Périmètre (racine du kit)

- [P2|ouvert|source=kit] Relire `20_guides/messagerie_interprojets.md` et `INDEX.md` après l'abandon de l'Intercom agent (décision de l'utilisateur du 2026-11-21 : les sessions communiquent déjà par `ListAgents` et `SendMessage`) ; périmètre exact (`INTERCOM_AGENT.md` seul ou aussi la messagerie `intercom/`) à confirmer par la racine
  - fait quand: le guide est mis à jour ou retiré selon le périmètre confirmé, ou décision explicite de le conserver.
  - réf: `DOCUMENTATION/20_guides/messagerie_interprojets.md` ; `_contexte/signals.md` (racine du kit)

- [P2|ouvert|source=maintenance] Décider si `/insert_template` (insertion d'un template du kit dans un projet cible, placeholders, jamais d'écrasement silencieux) mérite un guide `20_guides/` et une ligne d'`INDEX.md` (aucun guide n'existe ; le template « maintenance » est décrit dans `maintenance_du_kit.md`)
  - fait quand: guide créé et ligne d'INDEX ajoutée, ou décision explicite de ne pas documenter.
  - réf: .claude/commands/insert_template.md, DOCUMENTATION/20_guides/maintenance_du_kit.md

## Dernière session (2026-11-22)
<!-- Écrasé intégralement par /close. Synthèse < 25 lignes. -->
# Session du 2026-11-22

## Décisions prises
- Demande de Maintenance VibeObs (message de session) acceptée : documenter le template « maintenance » (commit 238ac84) ; écriture limitée à DOCUMENTATION/, ni README.md, ni CHANGELOG.md, ni llms.txt.

## Livrables produits ou modifiés
- `20_guides/maintenance_du_kit.md` (section template et règles de validation) et `INDEX.md` (ligne et date 2026-11-22) : mis à jour.

## Hypothèses validées / invalidées
- VALIDE : `check_docs.py` et `check_kit.py` passent.
- INVALIDE : un guide d'insertion de templates existait ; il n'existe pas, action P2 ouverte.
- EN ATTENTE : bump CHANGELOG et /doc_sync non faits (hors périmètre d'écriture de la zone).

## Prochaine étape exacte
Valider le signal `/close` → Documentation sur une clôture réelle d'une autre zone.

## Question bloquante pour la session suivante
Aucune
