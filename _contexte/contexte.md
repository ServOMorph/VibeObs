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
- 2026-11-20 : délégation à Codex en service (flag levé par l'utilisateur, il reste l'interrupteur d'urgence) : modèle `gpt-6.2-sol` imposé par `~/.codex/politique_delegation.json`, seuils 50 % sur 5 h et 60 % sur 7 jours, verrou par appel, `-Statut` à verdict explicite ; wrapper diffusé à `CreaZik_V3` et `VertIA_v3`, consigne « Modèle Codex » appliquée à 26 `AGENTS.md`, `VertIA_v3` et `SérénIATech_dev`. Reste : premier appel réel flag levé, recomptage des `AGENTS.md`, `.gitattributes` de `creation_llm`.
- 2026-11-19 : zone `MAINTENANCE/` créée (alias `maintenance`), template « maintenance » à concevoir ; relais téléphone exercé, quatre décisions de la veille VertIA_v3 en attente de l'utilisateur.
- Kit v7.4 (v6.8 : `check_docs.py` signale les guides en retard, hook PreCompact en essai réel en attente) ; `/update` v6.10 diffusé le 2026-11-18 à six projets, Shorts créé (`D:\ServOMorph\Shorts`).
- Restent à mettre à jour : creation_3d et site_internet_ST_v3 (sessions ouvertes), Nettoyage_PC (sans git), `SérénIATech_dev` via sa gardienne. Non poussés : Rayonne_Toi et challenge_magic (sans remote), Moulin du Sud (sans amont), Nettoyage_PC, `creation_llm` (2 commits), 24 projets (commit `AGENTS.md` du 2026-11-20).
- Système d'apprentissage : phase 1 (v0) en cours, session gardienne `sereniatech_dev` (`roadmap_apprentissage.md`).

## Décisions structurantes
_Décisions antérieures au 2026-10-10 archivées dans `_contexte/archive_decisions.md`._

- 2026-11-17 : `telephone.md` du kit diffusé aux projets suivis par le cas 1 (copie directe, commits locaux), sans activer le mode roberto (activé par l'utilisateur seul) ; `SérénIATech_dev` exclu (session gardienne).
- 2026-11-17 : push de tous les projets suivis sur ordre explicite de l'utilisateur, en fast-forward après `git fetch`, jamais de force ; un projet qui diverge est laissé à sa décision.
- 2026-11-18 : `/migration_canva` supprimé du kit (test abandonné, migration Canva faite à la main ; automatisation impossible, `playwright` hors service) ; historique du `CHANGELOG.md` conservé.
- 2026-11-18 : `/update` d'un projet à session ouverte inactive : VibeObs arrête la session (processus `claude`) à la demande de l'utilisateur puis met à jour ; actions classées « Plus tard » en bloc sur son choix ; session active ou en attente de clic laissée de côté.
- 2026-11-18 : projet Shorts extrait de `SérénIATech_dev/Communication/SHORTS` vers `D:\ServOMorph\Shorts` (copie, rôle généralisé à tout demandeur, git local, jeton VRAM `shorts` conservé) ; `SérénIATech_dev` supprime son dossier après validation dans sa session.
- 2026-11-19 : délégation à Codex bloquée par l'utilisateur le temps de limiter l'usage de l'abonnement Plus ; l'interrupteur est un fichier (`~/.codex/delegation_bloquee.flag`), le lever se fait par l'utilisateur seul.
- 2026-11-19 : veille IA lancée à la voix, exécutée par VertIA_v3 sans accord préalable à chaque lancement (périmètre : sources officielles, aucun Codex) ; VibeObs décide des téléchargements de modèles de 20 Go ou moins pour les essais, jamais de l'acceptation d'une licence ni de l'installation d'un logiciel.
- 2026-11-19 : délégation à Codex régie par une politique centrale (`~/.codex/politique_delegation.json`) : modèle et binaire imposés, seuils 50 % (5 h) et 60 % (7 jours) lus dans les rollout, verrou exclusif par appel, blocage par défaut si le quota est illisible ; wrapper déterministe, pas de session LLM gardienne ; flag manuel conservé comme interrupteur d'urgence.
- 2026-11-19 : zone `MAINTENANCE/` créée (rôle sans nom de projet suivi ; écriture sur tout le dépôt du kit, lecture des projets de `DEPLOYMENTS.md`) ; template « maintenance » à concevoir plus tard.
- 2026-11-20 : modèle Codex `gpt-6.2-sol` imposé par la politique centrale ; consigne « Modèle Codex » des `AGENTS.md` écrite sans nom de modèle (trois validations) et diffusée : écriture directe par lot sur les projets sans session ouverte, proposition par message aux sessions ouvertes ; `-Statut` donne un verdict explicite, le flag prime sur le quota ; flag levé par l'utilisateur, conservé comme interrupteur d'urgence.
