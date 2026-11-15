# Contexte — VibeObs

## Objectif (immuable sauf décision explicite)
Fournir un kit reproductible pour gérer le vibecoding sur des projets multi-sessions, avec contexte persistant via `/start`/`/close` et support multi-zones.

## Stack / contraintes techniques
- **Langage** : Markdown + Bash/PowerShell pour scripts
- **Framework** : Claude Code CLI + Agent SDK
- **Gestion git** : commits automatiques depuis `/close`
- **Modèles recommandés** : Haiku (start), Sonnet (close), Opus (plans/debug)
- **Intégration** : Ollama pour tâches sensibles/templated
- **Déploiement** : copie template vers projets via `/init`, tracking dans DEPLOYMENTS.md

## État actuel
- 2026-11-15 (suite) : kit v6.5 — `/close` demande à l'utilisateur s'il garde chaque artifact (registre `_contexte/artifacts.md`, relu par `/start`) ; v6.4 — garde VRAM et alerte `/compact` par hooks, `console_distante.py`, `/update` étape 0bis ; v6.3 — trois validations avant écriture dans un `CLAUDE.md`.
- `/update` v6.5 refusé par VertIA_v3, Moulin du Sud et World Model (travail en cours) ; à reproposer après leur `/close`. Le kit v6.5 est commité en local, non poussé.
- Système d'apprentissage et protocole de test créés (`roadmap_apprentissage.md`, phase 1 v0 en cours, session gardienne `sereniatech_dev`).
- `SérénIATech_dev` et les projets à session ouverte restent à mettre à jour par `/update`, après classement des actions ouvertes.

## Décisions structurantes
_Décisions antérieures au 2026-10-10 archivées dans `_contexte/archive_decisions.md`._

- 2026-11-11 : `/close` étape 9 (v5.41) : `tests_manuels.md` et `roadmap*.md` sont des fichiers de suivi, exclus du déclencheur de bump de version (le statut de roadmap est mis à jour par `/close` lui-même).
- 2026-11-11 : `/update` (v5.42) : `allowed-tools` de `start.md`/`close.md` = liste du kit + ajouts du projet (signalés) ; retraits du projet non conservés ; étape 10 tolère les ajouts en fin de ligne.
- 2026-11-12 : `/create_agent` reste générique : pas de mode « agent client » (besoin couvert par une commande projet), pas d'exception à la règle des MAJUSCULES ; un contrôle en échec ou sans sortie est refait avant toute conclusion d'absence (v5.43).
- 2026-11-14 : `/init_projet` (v6.0) ne demande plus la stack et propose l'alias par défaut avec le nom du projet ; le champ « Stack » du `contexte.md` d'un projet créé se remplit au fil du travail.
- 2026-11-14 : journal de session (v5.44) gitignoré (un fichier versionné vidé par `/close` laisserait un résidu à chaque clôture et risquerait des données sensibles en dépôt public) ; seul `/close` écrit `signals.md` / `contexte.md`. Règle diffusée aux sessions ouvertes par message unique contrôlé, application validée dans chaque session. Limites assumées : perdu avec le disque, écriture dépendante de la discipline de l'agent (un `/compact` n'est pas détectable sans hook).
- 2026-11-14 : `/delegation` — Claude orchestre et délègue selon la tâche : Ollama (texte mécanique fourni, local), OpenCode gratuit (lecture et petite édition dans le dépôt), Codex (correctif multi-fichiers, revue), sous-agent Haiku (web, doc). Écriture dans le kit en worktree, aucun secret vers un exécutant cloud, journal de chaque délégation pour améliorer le routage.
- 2026-11-14 : commandes à lancement manuel marquées `disable-model-invocation: true` (description retirée du contexte, `/nom` conservé) au lieu d'être sorties de `.claude/` ; critère : lancement manuel seulement, appelée par aucune autre commande.
- 2026-11-15 : GPU — jeton VRAM obligatoire auprès de VertIA_v3 avant tout usage ; hook `PreToolUse` (`scripts/garde_vram.py`) bloque la commande sans jeton ; alerte `/compact` à 600 000 tokens (fenêtre 1 M).
- 2026-11-15 : accès à `SérénIATech_dev` uniquement par demande à la session gardienne `sereniatech_dev` (ni lecture ni écriture directe) ; `/update` classe les actions ouvertes du projet cible avant toute mise à jour (étape 0bis, obligatoire en batch).
- 2026-11-15 : une session ouverte valide ou refuse toute modification de son projet (refus : ne rien toucher, la recontacter après sa clôture) ; registre des artifacts du kit gitignoré car le dépôt est public et les titres citent des clients.
