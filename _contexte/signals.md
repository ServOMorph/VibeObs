# Signals — VibeObs (MAJ 2026-09-06)

## Actions ouvertes — pilotage

### P1 — à traiter avant le backlog
- Valider le correctif `templates/discord_com` en conditions réelles : deux notifications consécutives reçues et file finale `idle`.
  - fait quand: le bot local reçoit puis transmet deux notifications réelles sans perte.
  - réf: `templates/discord_com/`, `discord_com/` local (non versionné).
- Résoudre le vol de focus avant la phase 3 de `roadmap_reprise_multicompte.md`.
  - fait quand: une action de clic vise de façon fiable la nouvelle fenêtre Chrome.
  - réf: `roadmap_reprise_multicompte.md`.
- Rejouer la phase 2 de `create_com_agents` sur `D:\ServOMorph\Meuniers`.
  - fait quand: installation, échange agent↔racine et purge de message sont validés sur Meuniers.
  - réf: `roadmap_com_agents.md`.
- Exercer `/create_memory <alias_zone> <contenu>` en exécution réelle (routage vers `<zone>/_contexte/memory.md`, en-tête créé si absent), et valider `/insert_template` + la conversion de `/create_agent`.
  - fait quand: chaque flux est exercé au moins une fois avec son résultat attendu.
  - réf: `_contexte/signals_backlog_2026-09-04.md` ; `create_memory.md` scopé déployé dans `D:\ServOMorph\Appli_TSA_SDI_TDAH` (commit `00166dd`).
- Fiabiliser la substitution Windows de `/init_projet` puis la tester.
  - fait quand: un projet cible Windows est initialisé avec les placeholders correctement résolus.
  - réf: `.claude/commands/init_projet.md`.
- Poursuivre la conception du skill générique d’orchestration multi-agents avec ChatGPT.
  - fait quand: le périmètre et le protocole minimal du skill sont formalisés.
  - réf: `roadmap_reprise_multicompte.md`.
- Valider la généricité de `/create_team` et d’Intercom sur un second projet cible.
  - fait quand: une seconde installation indépendante échange et accuse réception des messages.
  - réf: `.claude/commands/create_team.md`, `INTERCOM_AGENT.md`.
- Piloter l'installation d'une équipe parallèle isolée dans Appli_TSA_SDI_TDAH.
  - fait quand: les premiers cycles `start`/`close` de `ONBOARD` et `RETOURS` sont validés sans écriture sur `main`.
  - réf: `roadmap_agents_paralleles.md`, `.claude/commands/create_parallel_team.md`.

### Backlog P2
Voir [`signals_backlog_2026-09-04.md`](_contexte/signals_backlog_2026-09-04.md) : validations secondaires, décisions de conception, maintenance et contexte historique.

## Garde-fous permanents
- Secrets Discord uniquement dans `.env` gitignoré ; vérifier `git check-ignore` et `git status` avant un commit qui touche `discord_com/`.
- Écriture dans `control_pc.sqlite` via Python `sqlite3` paramétré, jamais par `INSERT` shell.

## Dernière session
# Session du 2026-09-06

## Décisions prises
- L'écart `/create_memory` signalé depuis Appli_TSA_SDI_TDAH était un déploiement périmé (cible v3.1), pas un bug kit : `create_memory.md` du kit porte la résolution d'alias de zone depuis v3.31 (2026-08-18). Résolu par `/update`.
- `/update` sur Appli_TSA_SDI_TDAH : helper Ollama conservé dans `scripts/ollama_call.py` (pas racine), écart documenté dans `CLAUDE.md` § Spécificités projet ; pas de copie `ollama_call.py` racine, `AGENTS.md`/`GEMINI.md` non touchés (cohérence préservée).

## Livrables produits ou modifiés
- `DEPLOYMENTS.md` (kit, gitignoré) : ligne Appli_TSA_SDI_TDAH → v5.4 / 2026-09-06.
- `roadmap_migration_close.md` : Phase 3 [FAIT] ; roadmap achevée 3/3, archivage proposé à l'utilisateur.
- Hors commit kit — Appli_TSA_SDI_TDAH : commit `eef53e1` (migration Phase 2 non commitée récupérée : `close.md`/`start.md`/`discord_loop.md`/`on_close.md`) + commit `00166dd` (`/update` : `create_memory.md` scopé + `CLAUDE.md` fusionné kit v5.4), poussés sur `main`.

## Hypothèses validées / invalidées
- VALIDE : `/update` sur repo cible propre — `_contexte/` et `zones.md` intacts (git diff vide), une seule paire de marqueurs SPECIFICITES par fichier, commit limité aux fichiers protocole.
- VALIDE : corps génériques `start.md`/`close.md` de la cible déjà byte-identiques au kit (Phase 2) → `/update` no-op sur ces deux fichiers.
- EN ATTENTE : `/create_memory <alias_zone> <contenu>` jamais exercé en exécution réelle.

## Prochaine étape exacte
Exercer `/create_memory <alias_zone> <contenu>` en réel sur Appli_TSA_SDI_TDAH (crée `<zone>/_contexte/memory.md`, confirme le routage), puis reprendre le backlog P1.

## Question bloquante pour la session suivante
Aucune.
