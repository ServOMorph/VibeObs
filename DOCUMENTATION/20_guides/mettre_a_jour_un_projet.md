---
type: guide
description: /update : réaligner les fichiers de protocole d'un projet déployé sur le kit
tags: guide, update, protocole, spécificités
maj: 2026-11-14
---

# Mettre à jour un projet déployé

Commande : `/update <chemin_projet_cible>` (ou `all` pour balayer `DEPLOYMENTS.md`).
Se lance **depuis le repo du kit**. Source canonique : `.claude/commands/update.md`.

## Ce que `/update` touche

Réaligne sur la dernière version du kit : `start.md`, `close.md`, `create_memory.md`,
`telephone.md`, `ollama_call.py`, et fusionne partiellement `CLAUDE.md`. Fait deux commits dans le repo
cible (`backup:` puis `update:`), puis estampille la ligne du projet dans `DEPLOYMENTS.md` (kit).

Étape 8bis (v5.44) : si la cible est un dépôt Git, ajoute `**/_contexte/journal_session.md` à son
`.gitignore` (fichier créé si absent, existant jamais réordonné) et l'inclut au commit `update:`. Un
journal déjà suivi par Git est signalé au rapport, sans être désuivi. Cible sans dépôt : rien.

Les permissions `allowed-tools` ajoutées par le projet dans `start.md`/`close.md` sont relevées
puis réinjectées en fin de ligne (v5.42) et signalées ; les retraits du projet ne sont pas conservés.

Ne touche jamais : `_contexte/`, `zones.md`, la section « Données sensibles » et la section
« Spécificités projet » de `CLAUDE.md`, le bloc `SPECIFICITES PROJET` de `start.md`/`close.md`, un
`AGENTS.md` ou `GEMINI.md` déjà présents, et aucun dossier de zone-agent.

## Préalable : repo cible propre

`/update` stage `.claude/commands/` dans son commit `backup:`. Si du travail cible non commité y
traîne (ex. une migration `start.md`/`close.md` restée dans le working tree), il part sous un
message « backup » trompeur et un `_contexte/` modifié reste orphelin. Committer ou remiser la
cible avant de lancer `/update`.

## Corps générique aligné = `/update` no-op

Quand le corps générique de `start.md`/`close.md` de la cible est déjà byte-identique aux
`templates/` du kit (comportement projet entièrement porté dans le bloc `SPECIFICITES PROJET`),
`/update` recopie puis réinjecte le bloc à l'identique : aucun changement sur ces deux fichiers.
C'est l'état cible visé pour tout projet à `start.md`/`close.md` forké.

## Déviation assumée sur un choix structurant du projet

Si le projet cible a fait un choix structurant incompatible avec une règle générique du kit,
`/update` ne force pas la règle. Exemple : l'helper Ollama placé dans `scripts/ollama_call.py` et
référencé ainsi dans `CLAUDE.md`, `AGENTS.md`, `GEMINI.md` — copier un `ollama_call.py` racine et
réécrire la seule section `CLAUDE.md` créerait un doublon et une incohérence à trois fichiers.

Règle : ne pas copier le fichier générique, conserver le chemin projet, **documenter l'écart dans
`CLAUDE.md` § Spécificités projet** (sous-section `###` qui référence la section concernée par son
titre), et ne pas toucher `AGENTS.md`/`GEMINI.md` déjà présents. Les contrôles nominaux de
`/update` qui attendent la forme kit sont alors des écarts connus, pas des échecs.
