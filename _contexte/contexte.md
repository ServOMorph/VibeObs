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
- 2026-11-17 : kit v6.7 — garde VRAM sans faux positif sur un texte cité (echo/printf/Write-*), règle d'essai réel dans `/delegation`, repli presse-papier de `/create_agent` (exercé de bout en bout sur projet jetable).
- `/update` v6.6 : VertIA_v3 (v6.5), World Model (`ba4d382`) et Moulin du Sud (`ed28cb8`) faits ; reste `SérénIATech_dev` via sa session gardienne.
- Garde VRAM actif dans la zone SHORTS (`shorts-c2`, constaté le 2026-11-17).
- Système d'apprentissage : phase 1 (v0) en cours, session gardienne `sereniatech_dev` (`roadmap_apprentissage.md`).

## Décisions structurantes
_Décisions antérieures au 2026-10-10 archivées dans `_contexte/archive_decisions.md`._

- 2026-11-14 : `/init_projet` (v6.0) ne demande plus la stack et propose l'alias par défaut avec le nom du projet ; le champ « Stack » du `contexte.md` d'un projet créé se remplit au fil du travail.
- 2026-11-14 : journal de session (v5.44) gitignoré (un fichier versionné vidé par `/close` laisserait un résidu à chaque clôture et risquerait des données sensibles en dépôt public) ; seul `/close` écrit `signals.md` / `contexte.md`. Règle diffusée aux sessions ouvertes par message unique contrôlé, application validée dans chaque session. Limites assumées : perdu avec le disque, écriture dépendante de la discipline de l'agent (un `/compact` n'est pas détectable sans hook).
- 2026-11-14 : `/delegation` — Claude orchestre et délègue selon la tâche : Ollama (texte mécanique fourni, local), OpenCode gratuit (lecture et petite édition dans le dépôt), Codex (correctif multi-fichiers, revue), sous-agent Haiku (web, doc). Écriture dans le kit en worktree, aucun secret vers un exécutant cloud, journal de chaque délégation pour améliorer le routage.
- 2026-11-14 : commandes à lancement manuel marquées `disable-model-invocation: true` (description retirée du contexte, `/nom` conservé) au lieu d'être sorties de `.claude/` ; critère : lancement manuel seulement, appelée par aucune autre commande.
- 2026-11-15 : GPU — jeton VRAM obligatoire auprès de VertIA_v3 avant tout usage ; hook `PreToolUse` (`scripts/garde_vram.py`) bloque la commande sans jeton ; alerte `/compact` à 600 000 tokens (fenêtre 1 M).
- 2026-11-15 : accès à `SérénIATech_dev` uniquement par demande à la session gardienne `sereniatech_dev` (ni lecture ni écriture directe) ; `/update` classe les actions ouvertes du projet cible avant toute mise à jour (étape 0bis, obligatoire en batch).
- 2026-11-15 : une session ouverte valide ou refuse toute modification de son projet (refus : ne rien toucher, la recontacter après sa clôture) ; registre des artifacts du kit gitignoré car le dépôt est public et les titres citent des clients.
- 2026-11-16 : garde VRAM (`scripts/garde_vram.py`) étendu aux générateurs d'images et de musique locaux et à Blender ; diffusion aux autres projets par hook de zone, session nommée (`VRAM_SESSION`), appliqué par la session propriétaire après son accord (première : SHORTS de `SérénIATech_dev`, commit `2169a1a`).
- 2026-11-16 : `.claude/CLAUDE.md` du kit porte la ligne de renvoi vers `prises_de_controle.md` dans § Spécificités projet (kit seul, non diffusée) ; `check_kit.py` ignore cette section en miroir.
- 2026-11-17 : `/update` d'un projet à session ouverte : VibeObs écrit les fichiers de protocole et prépare le `CLAUDE.md` fusionné ; la session cible l'écrit après les trois validations de l'utilisateur, puis VibeObs commite et lance les 7 contrôles.
