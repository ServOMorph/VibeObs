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
- 2026-11-16 : kit v6.6 — retex `/maintenance` appliqué (`check_kit.py` : version, commandes de `llms.txt`, fichiers sensibles, hygiène du contexte ; test append-only de `check_docs.py`), garde VRAM étendu aux générateurs locaux et à Blender, `/delegation` : lot 2 tracé (délai Ollama paramétrable, rapport OpenCode complet), `/create_agent` précisé.
- `/update` v6.5 : VertIA_v3 fait (`b7230f6`) ; Moulin du Sud et World Model à reproposer après leur `/close`, `SérénIATech_dev` via sa session gardienne. Le kit est commité en local, non poussé.
- Garde VRAM diffusé à la zone SHORTS (hook de zone, session `shorts`), actif au prochain lancement de `shorts-c2`.
- Système d'apprentissage : phase 1 (v0) en cours, session gardienne `sereniatech_dev` (`roadmap_apprentissage.md`).

## Décisions structurantes
_Décisions antérieures au 2026-10-10 archivées dans `_contexte/archive_decisions.md`._

- 2026-11-12 : `/create_agent` reste générique : pas de mode « agent client » (besoin couvert par une commande projet), pas d'exception à la règle des MAJUSCULES ; un contrôle en échec ou sans sortie est refait avant toute conclusion d'absence (v5.43).
- 2026-11-14 : `/init_projet` (v6.0) ne demande plus la stack et propose l'alias par défaut avec le nom du projet ; le champ « Stack » du `contexte.md` d'un projet créé se remplit au fil du travail.
- 2026-11-14 : journal de session (v5.44) gitignoré (un fichier versionné vidé par `/close` laisserait un résidu à chaque clôture et risquerait des données sensibles en dépôt public) ; seul `/close` écrit `signals.md` / `contexte.md`. Règle diffusée aux sessions ouvertes par message unique contrôlé, application validée dans chaque session. Limites assumées : perdu avec le disque, écriture dépendante de la discipline de l'agent (un `/compact` n'est pas détectable sans hook).
- 2026-11-14 : `/delegation` — Claude orchestre et délègue selon la tâche : Ollama (texte mécanique fourni, local), OpenCode gratuit (lecture et petite édition dans le dépôt), Codex (correctif multi-fichiers, revue), sous-agent Haiku (web, doc). Écriture dans le kit en worktree, aucun secret vers un exécutant cloud, journal de chaque délégation pour améliorer le routage.
- 2026-11-14 : commandes à lancement manuel marquées `disable-model-invocation: true` (description retirée du contexte, `/nom` conservé) au lieu d'être sorties de `.claude/` ; critère : lancement manuel seulement, appelée par aucune autre commande.
- 2026-11-15 : GPU — jeton VRAM obligatoire auprès de VertIA_v3 avant tout usage ; hook `PreToolUse` (`scripts/garde_vram.py`) bloque la commande sans jeton ; alerte `/compact` à 600 000 tokens (fenêtre 1 M).
- 2026-11-15 : accès à `SérénIATech_dev` uniquement par demande à la session gardienne `sereniatech_dev` (ni lecture ni écriture directe) ; `/update` classe les actions ouvertes du projet cible avant toute mise à jour (étape 0bis, obligatoire en batch).
- 2026-11-15 : une session ouverte valide ou refuse toute modification de son projet (refus : ne rien toucher, la recontacter après sa clôture) ; registre des artifacts du kit gitignoré car le dépôt est public et les titres citent des clients.
- 2026-11-16 : garde VRAM (`scripts/garde_vram.py`) étendu aux générateurs d'images et de musique locaux et à Blender ; diffusion aux autres projets par hook de zone, session nommée (`VRAM_SESSION`), appliqué par la session propriétaire après son accord (première : SHORTS de `SérénIATech_dev`, commit `2169a1a`).
- 2026-11-16 : `.claude/CLAUDE.md` du kit porte la ligne de renvoi vers `prises_de_controle.md` dans § Spécificités projet (kit seul, non diffusée) ; `check_kit.py` ignore cette section en miroir.
