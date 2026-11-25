# Mémoire projet
<!-- Fichier géré via /create_memory. Ne pas modifier manuellement sauf pour supprimer des entrées. -->

## 2026-09-25 — Skill cohérence CLAUDE/AGENTS/GEMINI

Idée à expérimenter, née pendant la création du projet PromptGuard : un skill déclenché automatiquement à chaque modification de `CLAUDE.md`, `AGENTS.md` ou `GEMINI.md`, qui réharmonise les trois fichiers (le kit ne fait aujourd'hui qu'un contrôle manuel par hash SHA-256 lors de `/init_projet`/`/update`). Le skill maintiendrait aussi une liste extensible des fichiers `.md` requis quand un nouvel LLM/agent est rencontré. Décision : l'expérimenter d'abord en local dans PromptGuard, pas de généralisation au kit VibeObs pour l'instant.

## 2026-09-25 — Skill cohérence : divergences par fichier

Complément à l'idée ci-dessus : chaque fichier (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`) doit pouvoir porter une section qui lui est propre, pour couvrir les cas où un comportement doit diverger d'un LLM à l'autre. Garder une trace séparée du contenu de base (canonique, sans les divergences) pour permettre la comparaison et la réharmonisation du tronc commun.

## 2026-11-05 — Questions posées une par une

Dans le projet VibeObs, toujours poser les questions à l'utilisateur une par une et attendre sa réponse avant de poser la suivante. Ne jamais regrouper plusieurs questions dans un même message.

## 2026-11-05 — Sessions ouvertes avant modification

Avant de modifier un dossier depuis VibeObs, vérifier si une session ChatGPT Codex ou Claude Code (VS Code) y est ouverte.
- Aucune session : procéder.
- Session ouverte : ne rien modifier ; envoyer la demande à l'agent de cette session. Il la traite après sa tâche en cours, l'analyse et renvoie sa reformulation. La contrôler et la lui renvoyer validée ou corrigée. L'agent demande alors à l'utilisateur s'il l'applique : la validation se fait toujours dans la session de l'agent, jamais dans VibeObs.
- Périmètre : modifications seulement, la lecture reste libre.
- Sans réponse de l'agent (session fermée) : le signaler à l'utilisateur, ne pas modifier.
- Tracer chaque échange (demande, reformulation, décision) dans le `signals.md` du dossier concerné.
- Détection : `ListAgents`/`SendMessage` pour Claude Code (non testés) ; aucun moyen fiable connu pour Codex (Intercom du kit à envisager).

## 2026-11-06 — Traçage des échanges entre sessions

Précise la règle « Sessions ouvertes avant modification » (point « Tracer chaque échange »). VibeObs n'écrit jamais dans le dossier d'une session ouverte, pas même dans son `signals.md`. C'est l'agent de cette session qui trace l'échange (demande, reformulation, décision) dans son propre `signals.md`, au `/close`. VibeObs n'en garde pas de copie.

## 2026-11-15 — Validation par la session ouverte

Précise « Sessions ouvertes avant modification » : avant de modifier un projet qui a une session ouverte (update, règle, fichier du protocole), demander à cette session de valider ou de refuser la modification, puis attendre sa réponse. Refus (travail en cours, écriture de CLAUDE.md sans les trois validations dans cette session) : ne rien toucher, la recontacter après la clôture de son travail en cours ; ne jamais passer outre. Constaté le 2026-11-15 : VertIA_v3 et Moulin du Sud ont refusé un /update pour ces raisons.

## 2026-11-25 — Lots Roberto : demander avant envoi
Chantier Roberto (commande PC, `lot_dictee/`) : ne jamais envoyer un lot à la session Roberto sans avoir demandé à l'utilisateur avant, y compris l'annonce d'un lot prêt ou d'un résultat d'essai. Décision de l'utilisateur du 2026-11-25.
