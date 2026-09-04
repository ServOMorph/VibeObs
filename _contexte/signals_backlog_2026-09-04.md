# Backlog archive — 2026-09-04

Cette archive rassemble les actions P2 retirées de `signals.md` lors de son allègement.
Les détails opérationnels restent dans les fichiers référencés.

## Validations et pilotes

- Tester `notification`, `overlay`, la destination par défaut d`/insert_template`, la mémoire scopée de `/create_memory`, Q4bis de `/init_projet`, la conversion et le renommage de `/create_agent`, et les branches `enabled: false` / préfixe novice de `discord_com`.
- Re-documenter l’écran Onboarding de `appli_tsa_sdi_tdah` dans `control_pc.sqlite` seulement après accord explicite pour le Reset DB.
- Rejouer les tests de la commande locale `/create_agent` de `jeu_espace` et de la synthèse agents de `jeu_zombies`.

## Décisions de conception

- Trancher P14 (`agent_role_TEMPLATE.md`) et P7–P10 (`/create_agent`).
- Décider la suite des lots 2–4 de `PROPOSITIONS_AMELIORATION.md`, l’éventuelle revue de code conditionnelle dans les roadmaps, et le design de pause d’agents dans `/init_projet`.
- Décider si `roadmap_messages_zones.md` fusionne avec `roadmap_com_agents.md` et désigner un pilote de remplacement.
- Clarifier les branches non-main de `jeu_zombies` et `Appli_TSA_SDI_TDAH`, ainsi que le chemin réel d’`Open_Code_Apprentissage`.

## Maintenance et propagation

- Propager les mises à jour retardées à `jeu_zombies` et mener un `/doc_sync` complet.
- Corriger ou ignorer explicitement les écarts CRLF connus dans `check_kit.py` (sans normaliser les fichiers utilisateur).
- Ajouter ou vérifier l’exclusion Git des secrets `discord_com` à l’insertion.
- Tester les branches restantes de `/create_projet`.

## Contexte chaud archivé

- Le retrait de `templates/roberto/`, le transfert du reliquat vers `D:\ServOMorph\Roberto`, l’état du skill `chatgpt-orchestrateur`, la mise en place de `/create_memory`, et les détails historiques de `discord_com` restent documentés dans les fichiers et roadmaps cités depuis `signals.md`.
- Les garde-fous à conserver : secrets Discord uniquement dans `.env` gitignoré, écriture SQLite via le module Python `sqlite3` paramétré, et ne jamais propager la copie de test non suivie `discord_com/`.
