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
- 2026-11-18 (suite) : projet autonome Shorts créé (`D:\ServOMorph\Shorts`, extrait de `SérénIATech_dev`, session `shorts-4c` lancée en CLI).
- Kit v7.0 : `/migration_canva` supprimé ; v6.10 diffusé par `/update` à creation_videos, World Model, creation_llm, VertIA_v3, Appli et Roberto, tous poussés.
- Kit v6.8 : `check_docs.py` signale les guides en retard sur leurs sources ; hook PreCompact qui trace le compactage dans le journal de session (essai réel en attente).
- Restent à mettre à jour : creation_3d et site_internet_ST_v3 (sessions ouvertes), Nettoyage_PC (sans git), `SérénIATech_dev` via sa gardienne. Non poussés : Rayonne_Toi et challenge_magic (sans remote), Moulin du Sud (sans amont), Nettoyage_PC.
- Système d'apprentissage : phase 1 (v0) en cours, session gardienne `sereniatech_dev` (`roadmap_apprentissage.md`).

## Décisions structurantes
_Décisions antérieures au 2026-10-10 archivées dans `_contexte/archive_decisions.md`._

- 2026-11-16 : `.claude/CLAUDE.md` du kit porte la ligne de renvoi vers `prises_de_controle.md` dans § Spécificités projet (kit seul, non diffusée) ; `check_kit.py` ignore cette section en miroir.
- 2026-11-17 : `/update` d'un projet à session ouverte : VibeObs écrit les fichiers de protocole et prépare le `CLAUDE.md` fusionné ; la session cible l'écrit après les trois validations de l'utilisateur, puis VibeObs commite et lance les 7 contrôles.
- 2026-11-17 : la poussée des commits d'un projet suivi se fait projet par projet, après `git fetch`, avec la confirmation de l'utilisateur à chaque push, jamais automatiquement.
- 2026-11-17 : relais téléphone — VibeObs raccordé directement au pont de Roberto, transmet les réponses de l'utilisateur mot pour mot après relecture, ne décide jamais seul (cas 3 du registre) ; mise en place chez Roberto sur dérogation (cas 4) ; envoi UTF-8 par `send_message.py`, jamais `curl`.
- 2026-11-17 : le tunnel du pont est ouvert par l'utilisateur seul ; ni VibeObs ni aucune session ne le connaît ni ne l'ouvre ; modes de session : PC (`/telephone off`), écran (`/telephone`), voix (`/telephone roberto`, activé par l'utilisateur seul pour l'instant).
- 2026-11-17 : `telephone.md` du kit diffusé aux projets suivis par le cas 1 (copie directe, commits locaux), sans activer le mode roberto (activé par l'utilisateur seul) ; `SérénIATech_dev` exclu (session gardienne).
- 2026-11-17 : push de tous les projets suivis sur ordre explicite de l'utilisateur, en fast-forward après `git fetch`, jamais de force ; un projet qui diverge est laissé à sa décision.
- 2026-11-18 : `/migration_canva` supprimé du kit (test abandonné, migration Canva faite à la main ; automatisation impossible, `playwright` hors service) ; historique du `CHANGELOG.md` conservé.
- 2026-11-18 : `/update` d'un projet à session ouverte inactive : VibeObs arrête la session (processus `claude`) à la demande de l'utilisateur puis met à jour ; actions classées « Plus tard » en bloc sur son choix ; session active ou en attente de clic laissée de côté.
- 2026-11-18 : projet Shorts extrait de `SérénIATech_dev/Communication/SHORTS` vers `D:\ServOMorph\Shorts` (copie, rôle généralisé à tout demandeur, git local, jeton VRAM `shorts` conservé) ; `SérénIATech_dev` supprime son dossier après validation dans sa session.
