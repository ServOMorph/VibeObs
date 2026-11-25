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
- 2026-11-25 : chantier Roberto « commande du PC » (manette, voix) intégré et remis à la session Roberto (cas 5 et 6) ; VibeObs n'y travaille plus ; phase 6 (template) non décidée.
- 2026-11-24 : `/update` v8.1 diffusé à 23 projets sans session ; VertIA_v3 refuse provisoirement, Creation llm sans réponse ; restent les sessions ouvertes (Moulin du Sud, creation_3d, World Model, Shorts, creation_videos, creation_llm, SérénIATech_dev) et Nettoyage_PC (sans git).
- Kit v8.3 ; backlog à 6 entrées ; skill `chatgpt-orchestrateur` en quarantaine (purge à partir du 2026-12-21) ; délégation à Codex en service (modèle `gpt-6.2-sol`, flag levé).
- Attentes : règle d'IA locale à diffuser par `/update` avec `init_projet` ; hook PreCompact : cas automatique à observer ; `.gitattributes` de `creation_llm` à commiter par sa session ; règle « Lots Roberto » de `.claude/memory.md` à retirer.
- Non poussés : Rayonne_Toi, challenge_magic et Shorts (sans remote), Moulin du Sud (sans amont), Nettoyage_PC. Système d'apprentissage : phase 1 (v0) en cours, session gardienne `sereniatech_dev`.

## Décisions structurantes
_Décisions antérieures au 2026-10-10 archivées dans `_contexte/archive_decisions.md`._

- 2026-11-20 : périmètre de VibeObs validé comme base (§ Périmètre) : kit de protocole, zones documentation/pedagogie/maintenance, relais, délégation ; hors périmètre : travail et décisions métier des projets suivis ; règles gardées : session ouverte validée avant modification, trois validations pour `CLAUDE.md`/`AGENTS.md`/`GEMINI.md`.
- 2026-11-20 : veille IA traitée par `VertIA_v3` seule ; en relais Roberto, VibeObs relaie sans garder en mémoire le contenu des sessions, sauf impact sur le kit ou template réutilisable ; section « Modèle Codex » ajoutée à `VibeObs/AGENTS.md` (trois validations).
- 2026-11-21 : Intercom agent abandonné (les sessions communiquent par `ListAgents` et `SendMessage`) ; premier essai réel de `/maintenance` : 5 améliorations appliquées (v7.7), écart `AGENTS.md` / `GEMINI.md` / `CLAUDE.md` assumé (section « Modèle Codex » propre à `AGENTS.md`).
- 2026-11-21 : maintenance = fichiers et Git, documentation et contexte, code et tests, sécurité, suppression des obsolètes, analyse pour refacto, nettoyage de la racine ; limite avec l'évolution fixée par projet. Suppression par quarantaine puis purge validée (30 jours) ; refacto en analyse seule ; retours des projets collectés par le kit (`maintenance_retours.md`) puis diffusés par `/update` ; journal court versionné `maintenance_historique.md`.
- 2026-11-21 : `/create_team` supprimé du kit (commande, guide, template d'équipe en quarantaine), kit v8.0 ; `init_projet` ne propose plus que `/create_agent` ; `INTERCOM_AGENT.md` supprimé, messagerie `intercom/` conservée.
- 2026-11-21 : tri des actions et du backlog selon le périmètre : travaux de projets suivis écartés ou transférés à leur propriétaire ; action de la Maintenance (`_docs`, `control_PC`) en attente de la décision de l'utilisateur ; règle d'IA locale de VertIA_v3 à instruire pour le `CLAUDE.md` du kit (trois validations).
- 2026-11-22 : skill `chatgpt-orchestrateur` abandonné (quarantaine, purge validée à part après 30 jours) ; hook PreCompact validé en manuel ; backlog réduit à 6 entrées.
- 2026-11-23 : règle d'IA locale de VertIA_v3 ajoutée aux `CLAUDE.md` du kit et du template (section `## IA locale et GPU`, trois validations) : portail `vertia_gen.py` pour image, musique, voix, vidéo et texte sous 20 appels ; un seul jeton GPU pour un lot de texte de 20 appels ou plus, jamais un jeton par appel ; diffusion par `/update` en attente.
- 2026-11-24 : `/update` v8.1 reconnu par VertIA_v3 (section ajoutée à son `CLAUDE.md` par elle-même) ; `/update` complet à reproposer après son `/close`, sans écriture dans VertIA.
- 2026-11-25 : chantier Roberto « commande du PC » mené depuis VibeObs (cas 5) puis intégré et remis à la session Roberto (cas 6 : intégration autonome) ; module, `/manette`, hook de lecture vocale et suivi vivent chez Roberto ; VibeObs ne garde que le registre et la roadmap.
