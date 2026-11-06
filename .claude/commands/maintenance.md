---
description: Maintenance régulière du kit VibeObs — contrôles, détection des reliquats, dérives de documentation, rapport et propositions
model: sonnet
allowed-tools: Bash(git status:*), Bash(git diff:*), Bash(git log:*), Bash(git ls-files:*), Bash(python scripts/check_kit.py), Bash(python scripts/check_docs.py), Bash(python -m pytest:*), Bash(ls:*), Bash(wc:*), Bash(diff:*)
---

# /maintenance

## Objectif

Contrôler l'état du kit VibeObs (`D:\ServOMorph\VibeObs`), repérer ce qui dérive (reliquats, doublons,
documents périmés, écarts entre sources) et proposer des actions. Cette commande ne modifie rien par
elle-même : elle produit un rapport, et chaque correction est exécutée seulement après validation de
l'utilisateur, lot par lot.

## Règles

- Lecture seule jusqu'à la validation d'un lot. Jamais de suppression : tout fichier obsolète est
  archivé dans `_archives/` (déplacement versionné par Git).
- Ne jamais lire `.env`, `<dossier>/discord_com/config_bot_discord.json`, ni un fichier de comptes ou de
  credentials (ex. `skills/<skill>/scripts/comptes_<nom>.json`). Pour ces fichiers : vérifier seulement
  l'existence, le statut Git (`git ls-files`) et la présence dans `.gitignore`.
- Toute affirmation sur un fichier exige sa lecture dans la session. Un chiffre issu de `signals.md`
  ou `contexte.md` est relu à la source avant d'être énoncé.
- Ne pas committer : laisser `/close` ou l'utilisateur le faire.

## Procédure

### 1. Contrôles mécaniques

Exécuter et noter le résultat (réussite, ou liste des écarts) :
```bash
python scripts/check_kit.py
python scripts/check_docs.py
python -m pytest -q tests
git status --short
```
Un écart n'est jamais écarté en silence : le consigner dans le rapport, avec son ancienneté si
`signals.md` le mentionne déjà.

### 2. Dépôt Git

- Lister les fichiers modifiés non commités et les chemins non suivis.
- Pour chaque chemin non suivi : indiquer s'il est destiné au kit (à suivre), local (à ajouter à
  `.gitignore`) ou étranger au kit (à archiver ou à transférer vers le projet propriétaire).
- Signaler les modifications non commitées plus anciennes que la dernière session de `/close`.

### 3. Reliquats à la racine

Lister le contenu de la racine et repérer :
- les fichiers sans rapport avec le kit (ex. liste de chemins d'un autre projet, fichier temporaire) ;
- les dossiers vides ;
- les copies divergentes d'un template placées hors de `templates/` (comparer avec `diff -rq`, sans
  ouvrir les fichiers de configuration sensibles) ;
- les notes de conception qui n'implémentent rien et dont le sujet est tranché ;
- les fichiers identiques entre eux (ex. `AGENTS.md` et `GEMINI.md`) : vérifier si l'identité est voulue
  (miroirs documentés) avant de la signaler comme doublon.

### 4. Roadmaps

Pour chaque `roadmap*.md` à la racine : relever la phase `[EN COURS]`, la date de dernière
modification et la dernière mention dans `_contexte/signals.md`. Une roadmap sans mouvement depuis plus
de 30 jours est candidate à l'archivage ou à une décision explicite de reprise. Ne jamais archiver
sans l'accord de l'utilisateur (règle Roadmap § Clôture de `CLAUDE.md`).

### 5. Documentation

- `README.md` : version annoncée égale à la dernière entrée de `CHANGELOG.md` ; liste des commandes
  cohérente avec `.claude/commands/` ; paragraphes d'historique qui répètent d'anciennes versions.
- `CHANGELOG.md` : taille ; proposer une archive des versions anciennes si le fichier dépasse un
  volume pénalisant pour la lecture.
- `DOCUMENTATION/` : date de mise à jour de `DOCUMENTATION/_contexte/signals.md` et actions ouvertes
  plus anciennes que 30 jours ; guides en retard sur le CHANGELOG (comparer la date de chaque guide
  dans `INDEX.md` aux versions du kit qui touchent son sujet).
- `base_connaissances/` : date de gel, version du kit qu'elle décrit, recouvrement avec
  `DOCUMENTATION/`, références entrantes (`grep` du nom du dossier dans les `.md` et commandes). Un
  dossier gelé, périmé et sans référence entrante est candidat à l'archivage.
- `tests_manuels.md` : tests en attente et ancienneté.
- `llms.txt` : cohérence avec la version et la liste des commandes.

### 6. Contexte de session

- `_contexte/signals.md` : nombre d'actions ouvertes (plafond 20), actions P1 sans mouvement depuis
  plus de 30 jours, existence des fichiers cités en `réf:`.
- `_contexte/backlog.md` : nombre d'entrées, entrées sans catégorie, entrées dont la `réf:` n'existe
  plus.
- Doublons entre `_contexte/signals.md` et `DOCUMENTATION/_contexte/signals.md`.
- `.claude/zones.md` : chaque dossier de zone existe.
- `DEPLOYMENTS.md` : projets dont le dossier n'existe plus, versions du kit en retard sur la version
  courante (information, sans action automatique).

### 7. Sécurité

- `.gitignore` : `.env`, fichiers de configuration de bots, `*.pid`, bases locales et registres de
  chemins absolus (`DEPLOYMENTS.md`, `AGENTS_REGISTRY.md`) y figurent.
- `git ls-files` : aucun fichier de credentials, de comptes ou de jetons suivi par Git. Le nom d'un
  fichier suffit à le signaler ; ne pas ouvrir son contenu.
- Signaler tout secret dont la présence en clair dans un fichier suivi serait déduite d'un nom ou
  d'une règle, sans reproduire sa valeur.

### 8. Rapport

Écrire le rapport dans la conversation, sans le créer en fichier sauf demande de l'utilisateur :

```
Maintenance du kit — AAAA-MM-JJ

Contrôles : check_kit <résultat> | check_docs <résultat> | pytest <résultat>
Git : <n> modifiés, <n> non suivis

Lots proposés (par priorité)
- Lot A <intitulé> : <fichiers> — action proposée (archiver / suivre / ignorer / décider) — risque
- Lot B ...

Écarts de documentation : <fichier : écart>
Points non vérifiés : <ce qui n'a pas pu être lu, et pourquoi>
```

Chaque lot contient : les fichiers concernés, l'action proposée, la raison constatée par lecture, et ce
qui reste incertain. Classer les lots par risque croissant (reliquats évidents d'abord, puis
documents, puis ce qui peut contenir un état actif comme un bot ou un registre).

### 9. Décision et exécution des lots

Après le rapport, demander la décision sur chaque lot, une question à la fois, dans l'ordre du
rapport : poser la question d'un lot, attendre la réponse de l'utilisateur, exécuter ce lot s'il est
validé, puis passer au lot suivant. Ne jamais regrouper plusieurs lots dans une même question.

Pour chaque lot validé par l'utilisateur, et seulement lui :
- archiver par `git mv` vers `_archives/` (ou déplacer le fichier non suivi), en conservant le nom ;
- ajouter une ligne au CHANGELOG seulement si un fichier de travail du kit a changé ;
- relancer le contrôle `scripts/check_kit.py` après chaque lot et signaler tout nouvel écart ;
- ne jamais modifier une entrée existante de `CHANGELOG.md` ni le journal de `DOCUMENTATION/`.

### 10. Analyse de la maintenance

Seulement une fois tous les lots de l'étape 9 tranchés, demander à l'utilisateur :

> Voulez-vous que j'analyse cette maintenance et que je propose des points d'amélioration ? Je
> regarderais : les contrôles qui ont raté ou manqué un problème, les étapes de cette commande qui ont
> donné peu de valeur ou trop de bruit, les contrôles à automatiser dans `check_kit.py` ou
> `check_docs.py`, et la fréquence de maintenance adaptée à l'activité du kit.

Ne pas lancer cette analyse sans sa réponse. Si l'utilisateur accepte, présenter les propositions sans
modifier `maintenance.md` : la mise à jour de cette commande est une modification du kit qui passe par
son accord explicite.
