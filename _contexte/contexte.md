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
- 2026-11-17 : kit v6.9 — `/relais_telephone` et mode `/telephone roberto` : relais vocal des sessions par le pont de Roberto, essai réel avec VertIA_v3 réussi, relais arrêté en fin de session (corrections à valider par l'utilisateur).
- Kit v6.8 : `check_docs.py` signale les guides en retard sur leurs sources (non bloquant) ; hook PreCompact qui trace le compactage dans le journal de session (essai réel en attente).
- `/update` v6.6 : VertIA_v3, World Model et Moulin du Sud faits ; reste `SérénIATech_dev` via sa session gardienne. Une vingtaine de projets ont des commits locaux non poussés (audit du 2026-11-17).
- Système d'apprentissage : phase 1 (v0) en cours, session gardienne `sereniatech_dev` (`roadmap_apprentissage.md`).

## Décisions structurantes
_Décisions antérieures au 2026-10-10 archivées dans `_contexte/archive_decisions.md`._

- 2026-11-14 : commandes à lancement manuel marquées `disable-model-invocation: true` (description retirée du contexte, `/nom` conservé) au lieu d'être sorties de `.claude/` ; critère : lancement manuel seulement, appelée par aucune autre commande.
- 2026-11-15 : GPU — jeton VRAM obligatoire auprès de VertIA_v3 avant tout usage ; hook `PreToolUse` (`scripts/garde_vram.py`) bloque la commande sans jeton ; alerte `/compact` à 600 000 tokens (fenêtre 1 M).
- 2026-11-15 : accès à `SérénIATech_dev` uniquement par demande à la session gardienne `sereniatech_dev` (ni lecture ni écriture directe) ; `/update` classe les actions ouvertes du projet cible avant toute mise à jour (étape 0bis, obligatoire en batch).
- 2026-11-15 : une session ouverte valide ou refuse toute modification de son projet (refus : ne rien toucher, la recontacter après sa clôture) ; registre des artifacts du kit gitignoré car le dépôt est public et les titres citent des clients.
- 2026-11-16 : garde VRAM (`scripts/garde_vram.py`) étendu aux générateurs d'images et de musique locaux et à Blender ; diffusion aux autres projets par hook de zone, session nommée (`VRAM_SESSION`), appliqué par la session propriétaire après son accord (première : SHORTS de `SérénIATech_dev`, commit `2169a1a`).
- 2026-11-16 : `.claude/CLAUDE.md` du kit porte la ligne de renvoi vers `prises_de_controle.md` dans § Spécificités projet (kit seul, non diffusée) ; `check_kit.py` ignore cette section en miroir.
- 2026-11-17 : `/update` d'un projet à session ouverte : VibeObs écrit les fichiers de protocole et prépare le `CLAUDE.md` fusionné ; la session cible l'écrit après les trois validations de l'utilisateur, puis VibeObs commite et lance les 7 contrôles.
- 2026-11-17 : la poussée des commits d'un projet suivi se fait projet par projet, après `git fetch`, avec la confirmation de l'utilisateur à chaque push, jamais automatiquement.
- 2026-11-17 : relais téléphone — VibeObs raccordé directement au pont de Roberto, transmet les réponses de l'utilisateur mot pour mot après relecture, ne décide jamais seul (cas 3 du registre) ; mise en place chez Roberto sur dérogation (cas 4) ; envoi UTF-8 par `send_message.py`, jamais `curl`.
- 2026-11-17 : le tunnel du pont est ouvert par l'utilisateur seul ; ni VibeObs ni aucune session ne le connaît ni ne l'ouvre ; modes de session : PC (`/telephone off`), écran (`/telephone`), voix (`/telephone roberto`, activé par l'utilisateur seul pour l'instant).
