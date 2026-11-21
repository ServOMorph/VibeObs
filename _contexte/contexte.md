# Contexte — VibeObs

## Objectif (immuable sauf décision explicite)
Fournir un kit reproductible pour gérer le vibecoding sur des projets multi-sessions, avec contexte persistant via `/start`/`/close` et support multi-zones.

### Périmètre (décision du 2026-11-20, validée comme base)
- Dedans : le kit de protocole vibecoding (commandes, templates, `/update`, `DEPLOYMENTS.md`) ; les zones `documentation`, `pedagogie` et `maintenance` ; les relais (téléphone/Roberto, Intercom) ; la délégation Codex, OpenCode et Ollama.
- Dehors : le travail et les décisions métier des projets suivis (veille IA : `VertIA_v3`). En relais, VibeObs ne retient que ce qui touche le kit ou donne un template réutilisable.
- Règles gardées : session ouverte validée avant toute modification ; trois validations pour `CLAUDE.md`, `AGENTS.md` et `GEMINI.md`.

## Stack / contraintes techniques
- **Langage** : Markdown + Bash/PowerShell pour scripts
- **Framework** : Claude Code CLI + Agent SDK
- **Gestion git** : commits automatiques depuis `/close`
- **Modèles recommandés** : Haiku (start), Sonnet (close), Opus (plans/debug)
- **Intégration** : Ollama pour tâches sensibles/templated
- **Déploiement** : copie template vers projets via `/init`, tracking dans DEPLOYMENTS.md

## État actuel
- 2026-11-21 (soir) : kit v8.0 (`/create_team`, guide et `INTERCOM_AGENT.md` supprimés ; messagerie `intercom/` conservée) ; 19 actions ouvertes triées selon le périmètre, backlog à 15 entrées (tri en pause à l'harmonisation `CLAUDE.md` / `AGENTS.md` / `GEMINI.md`).
- Attentes : décision de l'utilisateur sur l'action « écarts reportés » de la zone maintenance (`_docs`, `control_PC`, droits sur `DOCUMENTATION/20_guides/`) ; règle d'IA locale de VertIA_v3 pour le `CLAUDE.md` du kit ; `init_projet` à diffuser par `/update`.
- Délégation à Codex en service (modèle `gpt-6.2-sol` par la politique centrale, flag levé, interrupteur d'urgence) ; `.gitattributes` créé dans `creation_llm` (à commiter par sa session) ; `AGENTS.md` de Moulin du Sud commité `3b41aac`, non poussé (`Lieux_Hybrides` sans `main` distant).
- `/update` v6.10 diffusé le 2026-11-18 ; restent creation_3d et site_internet_ST_v3 (sessions ouvertes), Nettoyage_PC (sans git), `SérénIATech_dev` via sa gardienne ; hook PreCompact en essai réel en attente (v6.8 : `check_docs.py` signale les guides en retard).
- Non poussés : Rayonne_Toi, challenge_magic et Shorts (sans remote), Moulin du Sud (sans amont), Nettoyage_PC. Système d'apprentissage : phase 1 (v0) en cours, session gardienne `sereniatech_dev`.

## Décisions structurantes
_Décisions antérieures au 2026-10-10 archivées dans `_contexte/archive_decisions.md`._

- 2026-11-19 : veille IA lancée à la voix, exécutée par VertIA_v3 sans accord préalable à chaque lancement (périmètre : sources officielles, aucun Codex) ; VibeObs décide des téléchargements de modèles de 20 Go ou moins pour les essais, jamais de l'acceptation d'une licence ni de l'installation d'un logiciel.
- 2026-11-19 : délégation à Codex régie par une politique centrale (`~/.codex/politique_delegation.json`) : modèle et binaire imposés, seuils 50 % (5 h) et 60 % (7 jours) lus dans les rollout, verrou exclusif par appel, blocage par défaut si le quota est illisible ; wrapper déterministe, pas de session LLM gardienne ; flag manuel conservé comme interrupteur d'urgence.
- 2026-11-19 : zone `MAINTENANCE/` créée (rôle sans nom de projet suivi ; écriture sur tout le dépôt du kit, lecture des projets de `DEPLOYMENTS.md`) ; template « maintenance » à concevoir plus tard.
- 2026-11-20 : modèle Codex `gpt-6.2-sol` imposé par la politique centrale ; consigne « Modèle Codex » des `AGENTS.md` écrite sans nom de modèle (trois validations) et diffusée : écriture directe par lot sur les projets sans session ouverte, proposition par message aux sessions ouvertes ; `-Statut` donne un verdict explicite, le flag prime sur le quota ; flag levé par l'utilisateur, conservé comme interrupteur d'urgence.
- 2026-11-20 : périmètre de VibeObs validé comme base (§ Périmètre) : kit de protocole, zones documentation/pedagogie/maintenance, relais, délégation ; hors périmètre : travail et décisions métier des projets suivis ; règles gardées : session ouverte validée avant modification, trois validations pour `CLAUDE.md`/`AGENTS.md`/`GEMINI.md`.
- 2026-11-20 : veille IA traitée par `VertIA_v3` seule ; en relais Roberto, VibeObs relaie sans garder en mémoire le contenu des sessions, sauf impact sur le kit ou template réutilisable ; section « Modèle Codex » ajoutée à `VibeObs/AGENTS.md` (trois validations).
- 2026-11-21 : Intercom agent abandonné (les sessions communiquent par `ListAgents` et `SendMessage`) ; premier essai réel de `/maintenance` : 5 améliorations appliquées (v7.7), écart `AGENTS.md` / `GEMINI.md` / `CLAUDE.md` assumé (section « Modèle Codex » propre à `AGENTS.md`).
- 2026-11-21 : maintenance = fichiers et Git, documentation et contexte, code et tests, sécurité, suppression des obsolètes, analyse pour refacto, nettoyage de la racine ; limite avec l'évolution fixée par projet. Suppression par quarantaine puis purge validée (30 jours) ; refacto en analyse seule ; retours des projets collectés par le kit (`maintenance_retours.md`) puis diffusés par `/update` ; journal court versionné `maintenance_historique.md`.
- 2026-11-21 : `/create_team` supprimé du kit (commande, guide, template d'équipe en quarantaine), kit v8.0 ; `init_projet` ne propose plus que `/create_agent` ; `INTERCOM_AGENT.md` supprimé, messagerie `intercom/` conservée.
- 2026-11-21 : tri des actions et du backlog selon le périmètre : travaux de projets suivis écartés ou transférés à leur propriétaire ; action de la Maintenance (`_docs`, `control_PC`) en attente de la décision de l'utilisateur ; règle d'IA locale de VertIA_v3 à instruire pour le `CLAUDE.md` du kit (trois validations).
