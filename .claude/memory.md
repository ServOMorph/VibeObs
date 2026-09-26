# Mémoire projet
<!-- Fichier géré via /create_memory. Ne pas modifier manuellement sauf pour supprimer des entrées. -->

## 2026-09-25 — Skill cohérence CLAUDE/AGENTS/GEMINI

Idée à expérimenter, née pendant la création du projet PromptGuard : un skill déclenché automatiquement à chaque modification de `CLAUDE.md`, `AGENTS.md` ou `GEMINI.md`, qui réharmonise les trois fichiers (le kit ne fait aujourd'hui qu'un contrôle manuel par hash SHA-256 lors de `/init_projet`/`/update`). Le skill maintiendrait aussi une liste extensible des fichiers `.md` requis quand un nouvel LLM/agent est rencontré. Décision : l'expérimenter d'abord en local dans PromptGuard, pas de généralisation au kit VibeObs pour l'instant.

## 2026-09-25 — Skill cohérence : divergences par fichier

Complément à l'idée ci-dessus : chaque fichier (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`) doit pouvoir porter une section qui lui est propre, pour couvrir les cas où un comportement doit diverger d'un LLM à l'autre. Garder une trace séparée du contenu de base (canonique, sans les divergences) pour permettre la comparaison et la réharmonisation du tronc commun.
