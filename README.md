# VibeObs — Persistance de contexte pour le vibecoding avec Claude Code

Kit de protocole pour travailler avec Claude Code sur des projets qui s'étalent dans le temps.

Stack : **Claude Code** (agent IA), **Markdown** (fichiers de contexte), **Python** (lanceur Ollama en stdlib pur), **Ollama** (délégation locale optionnelle). Zéro infrastructure, zéro dépendance Python — uniquement la bibliothèque standard.

Résout le problème structurel du vibecoding : **le contexte est perdu à chaque nouvelle conversation**. Sans protocole, chaque session repart de zéro, les décisions prises ne sont pas tracées, et l'IA ne sait pas où en est le projet.

État actuel : le kit v6.6 conserve une mémoire projet (`.claude/memory.md`, alimentée par `/create_memory`) pour les décisions et pistes non encore implémentées — dont un skill de cohérence `CLAUDE.md`/`AGENTS.md`/`GEMINI.md` à expérimenter d'abord dans un projet tiers avant toute généralisation. Il trace aussi les templates insérés dans chaque projet (section « Templates installés » de `DEPLOYMENTS.md`, alimentée par `/insert_template`, `/init_discord_mode`, `/create_projet` et `/init_intercom`) ; le template `rclone_backup` impose un dossier Drive canonique configuré, exclut les secrets et permet un contrôle `--check` ; il offre des hooks de zone opt-in à `/start` et `/close` (`<dossier_zone>/_contexte/on_start.md` / `on_close.md`) — l'upload cloud d'un hook « Fin » étant bloqué sous auto-mode par le classifieur, le hook s'y limite à rafraîchir le manifeste et l'envoi vers Drive reste manuel. `agent_role_TEMPLATE.md` répercute désormais automatiquement un périmètre d'écriture étendu dans ses Invariants.

## Ce que ça fait

- `/start [zone] [--complet]` — charge le contexte du projet au démarrage de session (zone implicite si absent) ; affiche la prochaine étape et des compteurs, `--complet` pour tout `signals.md`
- `/close [zone]` — sauvegarde l'état, met à jour les fichiers de contexte, committe (zone implicite si absent)
- `/init_projet` — initialise le protocole dans un nouveau projet en quelques questions
- `/create_projet <nom_projet>` — crée un projet vierge : dossier sous `PROJETS_PARENT_DIR` (défini dans `.env`), Git local ou dépôt GitHub public/privé via `gh`, puis enchaîne `/init_projet` et propose les templates installables ; kit uniquement, s'exécute toujours depuis le kit
- `/update` — met à jour les fichiers de protocole dans un projet déjà initialisé, sans toucher aux données projet
- `/create_memory [alias_zone] [contenu]` — ajoute une entrée dans la mémoire projet persistante (`.claude/memory.md`) ou, si un alias de zone est reconnu, dans la mémoire de cette zone (`<dossier_zone>/_contexte/memory.md`, chargée par `/start`)
- `/create_agent <chemin_projet_cible> <dossier> [rôle]` — crée un agent (zone à rôle : charte `agent_role.md` + `_contexte/` propre, pilotable par `/start`/`/close`) dans un projet cible ; s'exécute toujours depuis le kit, n'est jamais copiée dans les projets cibles
- `/create_parallel_team <chemin_projet_cible> <dossier_equipe> [description ou fichier]` — crée une équipe dont chaque membre travaille dans son worktree Git et sa branche isolée ; le coordinateur propose les intégrations, jamais automatiques ; kit uniquement
- `/create_com_agents <chemin_projet_cible>` — installe un mécanisme de communication hiérarchique (`_contexte/statut.md` mis à jour à chaque `/close`, messages relevés sans effacer une arrivée concurrente) dans un projet cible déjà initialisé ; s'exécute toujours depuis le kit, ne modifie que `start.md`/`close.md` du projet cible
- `/insert_template <chemin_projet_cible> <nom_template> [dossier_destination]` — insère un template (`templates/<nom>/`) dans un projet cible, résout les placeholders génériques (`{{NOM_PROJET}}`/`{{ALIAS_PROJET}}`/`{{DATE}}`) et ne jamais écraser un fichier déjà présent ; s'exécute toujours depuis le kit, jamais copiée dans les projets cibles
- `/init_discord_mode <chemin_projet_cible>` — insère le template `discord_com` dans un projet cible et guide la configuration jusqu'à un bot opérationnel (token, channel_id, invitation OAuth2, Message Content Intent, dépendances) ; kit uniquement, s'exécute toujours depuis le kit
- `/init_intercom <chemin_projet_cible>` — installe la messagerie locale append-only Intercom dans un projet déjà initialisé ; kit uniquement
- `/intercom_inbox` — lit la boîte Intercom ; disponible dans le kit et copiée par `/init_intercom` dans le projet cible
- `/intercom_listen` — surveille la boîte Intercom dans un terminal persistant ; disponible dans le kit et copiée par `/init_intercom` dans le projet cible
- `/cherche_meilleure_action [décision]` — commande d'aide à la décision (kit uniquement) : analyse le contexte réel de la zone, évalue les options selon des critères explicites, recommande une action et demande confirmation ; à invoquer quand on ne sait pas quoi faire ensuite
- `/doc_sync` — synchronise toute la documentation du kit (commandes, templates, structure) après une modification
- `/telephone [off]` — mode téléphone : réponses de 6 lignes au plus, un choix numéroté à la fois avec la proposition en avant, chaque demande rangée dans le planning actif ; les corrections de format alimentent l'évolution du mode (copiée par défaut dans tout projet créé par `/init_projet` ou `/create_projet` et réalignée par `/update`)
- `/maintenance` — maintenance d'un projet : contrôles mécaniques, fichiers et Git, nettoyage de la racine, documentation et contexte, code et tests, sécurité, analyse pour refacto ; rapport par lots, suppression par quarantaine seulement après validation, journal `_contexte/maintenance_historique.md`, puis proposition d'améliorer la commande à partir des frictions rencontrées (socle générique et bloc « Spécificités projet »)
- `/cherche_fonction <description>` — recherche une fonctionnalité déjà codée dans d'anciens projets à partir d'une description ; les dossiers cibles sont toujours redemandés à chaque appel (kit uniquement)
- `/delegation [projet]` — active la délégation à Codex, OpenCode et Ollama comme sous-agents (template `delegation`), avec routage par type de tâche et journal `_codex/journal_delegation.md` pour mesurer l'économie de tokens Claude (kit uniquement)
- `/relais_telephone [stop]` — relais téléphone : démarre si besoin le pont `com_telephone` de Roberto, met VibeObs à l'écoute de son onglet et transmet mot pour mot aux sessions les réponses dictées par l'utilisateur (kit uniquement, lancement manuel)
- `CLAUDE.md` — règles permanentes appliquées à toutes les conversations
- `AGENTS.md` / `GEMINI.md` (optionnels, sur confirmation) — équivalents `CLAUDE.md` pour les agents non-Claude (Codex, ChatGPT, Gemini...)
- Base de connaissances `DOCUMENTATION/` (optionnelle, via agent dédié créé par `/create_agent`) — documentation métier du projet en `.md`, consultée par tous les agents (`INDEX.md` catalogue + progressive disclosure)
- Support multi-zones (plusieurs sous-projets dans un même repo)
- Intégration Ollama pour les tâches répétitives sans envoyer de données en cloud

## Démarrage rapide

### 1. Cloner ce repo

```bash
git clone https://github.com/ServOMorph/VibeObs.git
```

### 2. Ouvrir ce kit dans Claude Code

Dans Claude Code, ouvrir le dossier du kit (VibeObs).

### 3. Lancer l'initialisation

```
/init_projet <chemin vers le projet à initialiser>
```

Claude pose les questions d'initialisation (alias proposé par défaut avec le nom du projet, objectif, git, zone, données sensibles et fichiers d'instructions ; sans git, une question complémentaire propose un backup miroir Google Drive à chaque `/close`), puis demande si un agent seul ou une équipe doit être créé. La racine du projet cible est l'argument fourni — non demandée. L'agent ou l'équipe est créé dans la même exécution après l'initialisation, sur confirmation du plan interprété.

### 4. Démarrer

```
/start <alias>
```

## Structure du kit

```
VibeObs/
├── README.md                             # ce fichier
├── Protocole_start_close_context.md      # documentation complète
├── CHANGELOG.md                          # historique des versions
├── llms.txt                              # description du dépôt pour agents IA tiers
├── LICENSE                               # MIT
├── DEPLOYMENTS.md                        # registre des projets initialisés (ignoré par git)
├── AGENTS_REGISTRY.md                    # registre des agents créés (ignoré par git)
├── roadmap_*.md                          # chantiers multi-phases en cours (kit lui-même)
├── note_conception_*.md                  # notes de conception non encore tranchées
│
├── .claude/                              # instance du protocole appliquée au kit lui-même
│   ├── CLAUDE.md                         # règles permanentes
│   └── commands/                         # /start /close /update /init_projet /create_memory /telephone
│       │                                 #   + kit uniquement : /create_agent
│       │                                 #                     /create_parallel_team /create_com_agents
│       └───────────────────────────────  #                     /cherche_meilleure_action /doc_sync
│                                          #                     /cherche_fonction /delegation /relais_telephone
├── _contexte/                            # contexte du kit (contexte, signals, archive_decisions)
├── scripts/
│   ├── backup_file.py                    # sauvegarde horodatée d'un fichier vers Google Drive (rclone)
│   ├── deploy_create_memory.py           # déploiement massif d'un fichier sur les projets de DEPLOYMENTS.md
│   ├── compact_euros.py                  # équivalent API indicatif, en euros, des tokens libérés par /compact
│   ├── garde_vram.py                     # hook PreToolUse : commande GPU bloquée sans jeton VRAM (VertIA_v3)
│   ├── alerte_compact.py                 # hook UserPromptSubmit : alerte /compact au-delà de 600 000 tokens
│   ├── hook_precompact.py                # hook PreCompact : trace le compactage dans le journal de session
│   ├── console_distante.py               # lire une console et envoyer des touches à distance
│   └── check_kit.py / check_docs.py       # contrôles mécaniques du kit et de la base documentaire
├── dashboard/                            # sources du dashboard « VibeObs Dev » (artifact)
├── tests/                                # suite unittest du lanceur Ollama
├── base_connaissances/                   # audit des projets déployés + journaux de retex /create_agent
├── _archives/                            # roadmaps closes et documents historiques
└── templates/                            # patron copié dans les projets cibles par /init_projet
    ├── .claude/
    │   ├── CLAUDE.md                     # règles pour l'IA
    │   ├── zones.md                      # table alias → dossiers réels
    │   └── commands/
    │       ├── init_projet.md            # commande /init_projet
    │       ├── start.md                  # commande /start
    │       ├── close.md                  # commande /close
    │       ├── update.md                 # commande /update
    │       ├── create_memory.md          # commande /create_memory
    │       └── telephone.md              # commande /telephone (copiée par défaut)
    ├── _contexte/
    │   ├── contexte.md                   # contexte stable du projet
    │   └── signals.md                    # actions ouvertes, blocages, dernière session
    ├── ollama_call.py                    # délégation vers modèle local
    ├── rclone_backup/                    # template de backup miroir Google Drive via rclone
    ├── delegation/                       # template de délégation de tâches à Codex et OpenCode (lanceurs, préambule, brief, installateur)
    ├── ollama/                           # template d'usage d'Ollama local : lanceur ollama_call.py et section de consignes pour le CLAUDE.md
    ├── agent_role_TEMPLATE.md            # template de charte pour /create_agent
    ├── roadmap_TEMPLATE.md               # template pour chantiers multi-phases
    ├── on_start_TEMPLATE.md              # contrat des sections du hook de zone _contexte/on_start.md
    ├── on_close_TEMPLATE.md              # contrat des sections du hook de zone _contexte/on_close.md
    ├── AGENTS.md                         # équivalent CLAUDE.md pour agents non-Claude (Codex, ChatGPT...), sur confirmation
    └── GEMINI.md                         # équivalent CLAUDE.md spécifique à Gemini, sur confirmation
    ├── control_PC/                       # template local de contrôle visuel, macros et workflows par application
    ├── discord_com/                      # intégration Discord ↔ Claude Code, généricisée depuis Agents_IA_V2
    ├── netlify/                          # déploiement Netlify : CLI, API REST générique et CI Git
    ├── overlay/                          # overlay néon plein écran, signal de fin de tâche d'agent
    └── notification/                     # notification systray (icône + bulle Windows), alternative à overlay
```

Les commandes `/create_agent`, `/create_parallel_team`, `/create_com_agents`, `/insert_template`, `/cherche_meilleure_action`
et `/doc_sync` vivent uniquement dans `.claude/commands/` du kit : elles s'exécutent depuis le kit
et ne sont jamais copiées dans les projets cibles, donc absentes de `templates/`.

## Documentation

Lire `Protocole_start_close_context.md` pour le détail complet : stratégie de gestion du contexte, table des modèles recommandés, formats canoniques, intégration Ollama.

L'historique des versions est consigné dans `CHANGELOG.md`.

## Prérequis

- [Claude Code](https://claude.ai/code)
- Git
- (Optionnel) [Ollama](https://ollama.com) + `python`/`python3` pour la délégation locale

## Dépendances

**Aucune dépendance externe Python.** Le lanceur Ollama utilise uniquement la bibliothèque standard (`urllib`, `json`, `os`, `sys`). Aucun `requirements.txt` nécessaire. Seule exception : `MAINTENANCE/scripts/lancer_sur_bureau.py` (placement de fenêtres sur un bureau virtuel Windows) exige `pyvda`, installé dans un venv hors dépôt.

## État actuel

Kit **v8.3** (2026-11-25) : cas 6 de `prises_de_controle.md` (intégration autonome du module de commande PC dans Roberto, chantier remis à sa session) ; de la v8.2 (2026-11-25) : cas 5 (commande PC de Roberto développée dans `Roberto/lot_dictee/`), règle « demander avant d'envoyer un lot à Roberto » ; de la v8.1 (2026-11-23) : section `## IA locale et GPU` ajoutée aux `CLAUDE.md` du kit et du template (portail `vertia_gen.py`, un seul jeton GPU pour un lot de texte de 20 appels ou plus), diffusion par `/update` en attente ; de la v8.0 (2026-11-21) : `/create_team`, son guide et `INTERCOM_AGENT.md` supprimés (la messagerie `intercom/` est conservée), question 9 de `/init_projet` limitée à `/create_agent` ; de la v7.7 (2026-11-21) : `/maintenance` améliorée après son premier essai réel (permissions, éléments ignorés volumineux, manifeste de quarantaine, transfert à la session propriétaire, lecture de `DEPLOYMENTS.md`) ; de la v7.6 (2026-11-20) : `/maintenance` réécrite en socle générique (12 étapes, quarantaine, refacto en analyse seule, journal de maintenance, amélioration de la commande) avec bloc « Spécificités projet » propre au kit ; de la v7.5 (2026-11-20) : section « Modèle Codex » ajoutée à l'`AGENTS.md` du kit, périmètre de VibeObs défini (`_contexte/contexte.md`) ; de la v7.4 (2026-11-20) : délégation à Codex avec modèle `gpt-6.2-sol` imposé par la politique centrale, `run_codex.ps1` corrigé (`-DryRun` en code 0, verdict explicite de `-Statut`, le flag primant sur le quota) et diffusé à `CreaZik_V3` et `VertIA_v3`, flag levé ; de la v7.3 (2026-11-20) : scripts de la zone `MAINTENANCE/` (`migrer_projet.py` : migration d'un projet d'un lecteur à l'autre avec copie vérifiée, correction des chemins et quarantaine ; `lancer_sur_bureau.py` ; `balayer_chemins.py`) ; de la v7.2 (2026-11-19) : politique centrale de la délégation à Codex (`~/.codex/politique_delegation.json` : modèle et binaire imposés, seuils 50 % sur 5 h et 60 % sur 7 jours lus dans les sessions de Codex, verrou exclusif par appel ; `run_codex.ps1 -Statut` et `-Passe`, `_codex/garde_codex.sh` pour les scripts shell) en plus de l'interrupteur `~/.codex/delegation_bloquee.flag` ; zone `MAINTENANCE/` (template « maintenance » à concevoir) ; de la v7.1 : section « Modèle Codex » du modèle `AGENTS.md` et règles du relais téléphone (jamais de silence, réponses courtes, points toutes les minutes).

## Vérifier le lanceur Ollama

La suite est dans `tests/test_ollama_call.py`.

```powershell
python -m unittest discover -s tests -v
$env:OLLAMA_LIVE_TEST = "1"
python -m unittest tests.test_ollama_call.OllamaCallTests.test_live_ollama_returns_a_response -v
```

Le second test appelle réellement Ollama ; il reste désactivé par défaut.

## Licence

MIT — voir [LICENSE](LICENSE).
