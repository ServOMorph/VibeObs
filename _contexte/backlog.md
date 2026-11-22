# Backlog — VibeObs

- [amélioration] Mettre en œuvre l'harmonisation automatique `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` (source unique `INSTRUCTIONS.md` + 3 wrappers, portée générique/spécifique demandée avant chaque écriture, prise en contexte insistée) — reportée à plus tard sur ordre utilisateur.
  - fait quand: source + wrappers déployés, `/update` propage sans écraser les blocs spécifiques, `check_kit.py` contrôle l'écart.
  - réf: `templates/AGENTS.md` ; `.claude/commands/update.md` étape 7 ; `CHANGELOG.md` v5.3 ; `_contexte/archive_sessions.md` session 2026-09-04.
- [amélioration] Détection d'une session Codex ouverte avant modification d'un dossier (règle « Sessions ouvertes avant modification ») : aucun moyen fiable connu, Intercom du kit à envisager. `ListAgents`/`SendMessage` couvrent seulement Claude Code (validés le 2026-11-06).
  - fait quand: un moyen de détecter une session Codex est trouvé et ajouté à la règle de `.claude/memory.md`, ou l'impossibilité est actée.
  - réf: `.claude/memory.md` § Sessions ouvertes avant modification.
- [amélioration] Délégation : `ollama_call.py` a un délai fixe de 60 s, inférieur au chargement à froid de `qwen2.5:7b` (82 s mesurés) ; `run_opencode.ps1` ne garde dans `rapport.md` que le premier bloc du message final (liste d'anomalies restée dans `log.txt`). 2026-11-17 : `OLLAMA_TIMEOUT` (180 s par défaut) présent dans `ollama_call.py` ; rapport OpenCode complet constaté sur le lot H ; reste un lancement Ollama réel à froid.
  - fait quand: délai Ollama paramétrable (ou préchauffage documenté) et rapport OpenCode complet constatés sur un lancement réel.
  - réf: `ollama_call.py` ; `templates/delegation/scripts/run_opencode.ps1` ; `_codex/journal_delegation.md`.
- [piste] Intégrer le garde VRAM (`scripts/garde_vram.py` + hook `PreToolUse`) aux autres projets suivis, après observation en conditions réelles dans le kit. 2026-11-16 : motif étendu à `gen_images*.py`, `gen_musique.py` et Blender en ligne de commande (commit `a1dbe21`) ; première diffusion à la zone SHORTS de `SérénIATech_dev` par hook de zone, session `shorts` (commit `2169a1a`, appliquée par `shorts-c2`) ; blocage constaté à blanc sur `gen_images_qwen.py`, puis hook constaté actif dans `shorts-c2` le 2026-11-17. 2026-11-17 : faux positif sur texte cité (echo) corrigé dans le kit (v6.7) ; la copie utilisée par SHORTS n'a pas été vérifiée.
  - fait quand: le garde a bloqué puis laissé passer une commande GPU réelle dans le kit, et une décision de diffusion est prise.
  - réf: `scripts/garde_vram.py` ; `.claude/settings.json`.
- [amélioration] Registre des artifacts : l'étape 6-bis de `/close` dit « commité avec `_contexte/` » alors que le registre du kit est gitignoré (dépôt public, titres de clients) ; décider si le registre est versionné par défaut, ignoré par défaut, ou si `/close` contrôle la visibilité du dépôt.
  - fait quand: la formulation de l'étape 6-bis et le `.gitignore` des projets sont cohérents, ou le choix actuel est acté comme suffisant.
  - réf: `.claude/commands/close.md`.
- [finding] `garde_vram.py` bloque les commandes Bash dont le simple texte contient un nom de modèle ou d'outil GPU (messages envoyés au téléphone, notes de journal), même sans lancer de GPU ; contourné trois fois le 2026-11-19 en reformulant.
  - fait quand: le hook ne bloque plus une commande qui ne fait que citer un nom, ou la règle est actée comme suffisante.
  - réf: `scripts/garde_vram.py`.
