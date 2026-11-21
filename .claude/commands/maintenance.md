---
disable-model-invocation: true
description: Maintenance d'un projet — contrôles, nettoyage, suppression par quarantaine, analyse de refacto, rapport par lots, amélioration de la commande
model: sonnet
allowed-tools: Bash(git status:*), Bash(git diff:*), Bash(git log:*), Bash(git ls-files:*), Bash(git mv:*), Bash(git check-ignore:*), Bash(python scripts/check_kit.py), Bash(python scripts/check_docs.py), Bash(python -m pytest:*), Bash(ls:*), Bash(wc:*), Bash(diff:*), Bash(mkdir:*), Bash(mv:*)
---

# /maintenance

## Objectif

Maintenir un projet sain et cohérent sans en changer les fonctionnalités : contrôler, repérer ce qui
dérive (reliquats, doublons, documents périmés, code mort, secrets exposés), proposer le nettoyage et
l'analyse de refacto. La commande produit un rapport par lots ; chaque lot est exécuté seulement après
la validation de l'utilisateur. La limite entre maintenance et évolution est fixée par le bloc
« SPÉCIFICITÉS PROJET » en fin de fichier.

## Périmètre

Fichiers et Git ; documentation et contexte ; code et tests ; sécurité et secrets ; suppression des
fichiers obsolètes ; analyse pour refacto ; nettoyage de la racine et des dossiers inutiles.

## Règles

- Lecture seule jusqu'à la validation d'un lot.
- Suppression : jamais définitive d'emblée. Tout fichier ou dossier obsolète, suivi par Git ou non, est
  déplacé en quarantaine (étape 9). La purge définitive est un lot distinct, validé à part.
- Refacto : analyse seule. L'exécution passe par une roadmap ou une session dédiée (règle Roadmap de
  `CLAUDE.md`), jamais par cette commande.
- Ne jamais lire `.env`, un fichier de configuration de bot, un fichier de comptes ou de credentials.
  Pour ces fichiers : existence, statut Git (`git ls-files`) et présence dans `.gitignore` seulement.
- Toute affirmation sur un fichier exige sa lecture dans la session. Un chiffre issu de `signals.md` ou
  `contexte.md` est relu à la source avant d'être énoncé.
- Ne pas committer : laisser `/close` ou l'utilisateur le faire.
- Les seuils (ancienneté, taille) viennent du bloc « SPÉCIFICITÉS PROJET » ; sans valeur, utiliser 30
  jours et le signaler dans le rapport.

## Procédure

### 0. Cadrage

- Lire le bloc « SPÉCIFICITÉS PROJET » : limite maintenance/évolution, chemins sensibles, seuils,
  contrôles propres au projet.
- Lire `_contexte/maintenance_historique.md` (s'il existe) : ne pas reproposer un lot refusé sans fait
  nouveau.
- Lire `_contexte/maintenance_retours.md` (s'il existe) : frictions déjà notées.
- Si le bloc projet le demande (kit seulement) : lire les `maintenance_retours.md` des projets suivis
  (lecture seule) et les présenter en tête du rapport.

### 1. Contrôles mécaniques

Exécuter les scripts et tests listés par le bloc projet, noter chaque résultat (réussite ou liste des
écarts). Un écart n'est jamais écarté en silence : le consigner avec son ancienneté si `signals.md` le
mentionne déjà. Sans contrôle déclaré : le signaler comme point non vérifié.

### 2. Fichiers et Git

- Lister les fichiers modifiés non commités et les chemins non suivis.
- Pour chaque chemin non suivi : destiné au projet (à suivre), local (à ajouter à `.gitignore`) ou
  étranger au projet (à transférer au propriétaire ou à mettre en quarantaine).
- Signaler les modifications non commitées plus anciennes que la dernière clôture de session.

### 3. Racine et dossiers inutiles

Lister la racine et chaque dossier de premier niveau, puis repérer :
- les fichiers sans rapport avec le projet, les temporaires, les dossiers vides ;
- les dossiers ou fichiers sans référence entrante (`grep` du nom dans le code, les commandes et les
  `.md`) et sans modification récente ;
- les copies divergentes d'un modèle ou d'un template placées ailleurs que dans leur dossier d'origine ;
- les notes de conception qui n'implémentent rien et dont le sujet est tranché ;
- les fichiers identiques entre eux : vérifier si l'identité est voulue avant de la signaler.

Un candidat à la suppression est classé « quarantaine » avec sa raison et sa référence entrante
éventuelle.

### 4. Documentation et contexte

- `README`, `CHANGELOG` et fichiers de version : cohérence des versions, paragraphes d'historique
  répétés, taille pénalisante.
- `_contexte/signals.md` : plafond d'actions, actions sans mouvement au-delà du seuil, `réf:` introuvables
  (existence seulement pour un autre projet), doublons avec le `signals.md` d'une autre zone.
- `_contexte/backlog.md` : nombre d'entrées, entrées sans catégorie.
- `roadmap*.md` : phase `[EN COURS]`, dernière modification, dernière mention dans `signals.md`. Une
  roadmap sans mouvement au-delà du seuil est candidate à l'archivage ou à une décision de reprise ;
  jamais d'archivage sans accord (règle Roadmap § Clôture de `CLAUDE.md`).
- `tests_manuels.md` : tests en attente et ancienneté.
- Zones : chaque dossier déclaré dans `.claude/zones.md` existe.

### 5. Code et tests

- Lancer les tests du projet ; noter échecs et tests désactivés.
- Dépendances : fichiers de dépendances présents, versions épinglées, dépendances importées mais non
  déclarées (et inversement), sans rien installer.
- Scripts : scripts qui référencent un chemin, un fichier ou une commande inexistants.
- Chemins en dur vers un lecteur, un utilisateur ou un dossier qui n'existe plus.
- Code mort probable : fonctions et fichiers sans appelant (`grep`), à présenter comme hypothèse.

### 6. Sécurité et secrets

- `.gitignore` : exclusion de `.env`, des fichiers de configuration de bot, des comptes, des bases
  locales et des fichiers `*.pid`.
- Aucun fichier suivi au nom sensible (credentials, comptes, jetons, secrets, `.pem`, `.key`, bases
  locales), sur les noms seuls.
- Signaler tout secret dont la présence en clair dans un fichier suivi serait déduite d'un nom ou d'une
  règle, sans reproduire sa valeur.

### 7. Analyse pour refacto

Analyse seule, sans modification : duplications, fichiers ou commandes trop longs, dépendances
circulaires ou structure bancale, code mort confirmé par l'étape 5, contournements temporaires. Pour
chaque constat : fichiers, gain attendu, risque, et suite proposée (entrée de backlog, phase de roadmap
ou session dédiée en Opus). Rien n'est écrit dans le backlog avant validation.

### 8. Rapport

Écrire le rapport dans la conversation, sans le créer en fichier sauf demande de l'utilisateur :

```
Maintenance — <projet> — AAAA-MM-JJ

Contrôles : <script> <résultat> | ...
Git : <n> modifiés, <n> non suivis

Lots proposés (par risque croissant)
- Lot A <intitulé> : <fichiers> — action (suivre / ignorer / quarantaine / décider / refacto) — risque
- Lot B ...

Refacto à étudier : <constat : suite proposée>
Écarts de documentation : <fichier : écart>
Points non vérifiés : <ce qui n'a pas pu être lu, et pourquoi>
```

Chaque lot contient : les fichiers concernés, l'action proposée, la raison constatée par lecture et ce
qui reste incertain. Classer par risque croissant : reliquats évidents, puis documents, puis code, puis
ce qui peut contenir un état actif (bot, registre, base).

### 9. Décision et exécution des lots

Demander la décision sur chaque lot, une question à la fois, dans l'ordre du rapport : poser la
question d'un lot, attendre la réponse, exécuter ce lot s'il est validé, puis passer au suivant. Ne
jamais regrouper plusieurs lots dans une même question.

Pour chaque lot validé, et seulement lui :
- suivre ou ignorer : `git add` est laissé à `/close` ; l'ajout à `.gitignore` est fait ;
- archiver un fichier suivi voulu dans le dépôt : `git mv` vers `_archives/` ;
- supprimer : quarantaine. Créer `D:\_quarantaine\<AAAA-MM-JJ>\<projet>\`, y déplacer l'élément en
  conservant son arborescence relative, puis ajouter une ligne à `manifeste.md` du même dossier :
  chemin d'origine, destination, raison, suivi par Git oui/non, date. Vérifier que l'origine a
  disparu et que la destination existe. Une référence entrante trouvée à l'étape 3 est corrigée dans le
  même lot, ou le lot est refusé ;
- purge définitive : lot distinct, présenté seulement pour une quarantaine plus ancienne que le délai du
  bloc projet, validé élément par élément ;
- relancer les contrôles de l'étape 1 après chaque lot et signaler tout nouvel écart ;
- ne jamais modifier une entrée existante d'un `CHANGELOG`.

### 10. Journal de maintenance

Ajouter une ligne à `_contexte/maintenance_historique.md` (fichier versionné, créé à la première
entrée, sans donnée sensible) :

`AAAA-MM-JJ | contrôles : <résultats> | lots validés : <liste> | lots refusés : <liste> | quarantaine : <n> éléments`

Aucune ligne n'est réécrite ni supprimée.

### 11. Amélioration de la commande

Étape finale. Demander à l'utilisateur :

> Voulez-vous lancer l'analyse pour améliorer la commande maintenance à partir des frictions
> rencontrées pendant cette maintenance ?

- **Non** : la maintenance est terminée. Ne rien analyser ni écrire.
- **Oui** : relever les frictions rencontrées pendant cette exécution (étapes sans valeur ou trop
  bruyantes, contrôle qui a raté ou manqué un problème, question inutile, permission manquante, contrôle
  à automatiser dans un script, seuil mal réglé, étape manquante). Présenter les propositions, chacune
  avec l'étape concernée et la modification précise. Consigner chaque proposition dans
  `_contexte/maintenance_retours.md` (une ligne : `AAAA-MM-JJ | étape | friction | proposition`) et
  dans `_contexte/journal_session.md` dès sa présentation, puis sa décision une fois tranchée. Ne pas
  modifier `maintenance.md` sans l'accord explicite de l'utilisateur. Une amélioration retenue qui vaut
  pour tous les projets est à remonter au kit : le kit la généralise dans le template et `/update` la
  diffuse en préservant le bloc « SPÉCIFICITÉS PROJET » de chaque projet.

<!-- SPECIFICITES PROJET : DEBUT (préservé par /update, ne pas toucher hors de ce bloc) -->
<!-- Convention : toute règle liée à une étape précise de la Procédure ci-dessus doit la référencer
     explicitement par son numéro (ex: "Étape 3 : ..."), plutôt que compter sur la position physique
     de ce bloc (toujours en fin de fichier). -->

Projet : kit VibeObs (`D:\ServOMorph\VibeObs`).

- Limite maintenance / évolution : la maintenance ne modifie ni les commandes, ni les templates, ni les
  scripts du kit ; elle les contrôle et propose. Toute modification passe par une session de travail
  et `CHANGELOG.md`.
- Seuils : 30 jours (roadmaps, actions P1, `DOCUMENTATION/_contexte/signals.md`). Délai de purge de la
  quarantaine : 30 jours (décision de l'utilisateur du 2026-11-20).
- Chemins sensibles : `.env`, `<dossier>/discord_com/config_bot_discord.json`,
  `skills/<skill>/scripts/comptes_<nom>.json`, `~/.codex`.
- Étape 0 : lire les `_contexte/maintenance_retours.md` des projets de `DEPLOYMENTS.md` (lecture seule,
  existence testée avant lecture).
- Étape 1 : lancer `check_kit.py` et `check_docs.py` (dossier `scripts/` du kit), les tests du dossier
  `tests/` avec `python -m pytest -q tests`, puis `git status --short`.
- Étape 3 : copies divergentes d'un template hors de `templates/` (`diff -rq`, sans ouvrir les fichiers
  de configuration sensibles) ; `AGENTS.md` et `GEMINI.md` identiques : vérifier qu'il s'agit de miroirs
  documentés.
- Étape 4 : `check_kit.py` couvre la version commune (`CHANGELOG.md`, `README.md`, protocole,
  `llms.txt`), la présence des commandes dans `README.md` et `llms.txt`, le plafond de 20 actions, les
  entrées du backlog sans catégorie et les `réf:` relatives introuvables : reprendre son résultat sans
  refaire la comparaison. Contrôler en plus : `DOCUMENTATION/INDEX.md` (guides en retard sur le
  `CHANGELOG.md`), `base_connaissances/` (date de gel, version décrite, recouvrement avec
  `DOCUMENTATION/`, références entrantes), `DEPLOYMENTS.md` (projets dont le dossier n'existe plus,
  versions en retard, information sans action automatique).
- Étape 6 : `check_kit.py` couvre l'exclusion de `.env`, `*.pid`, `DEPLOYMENTS.md`, `AGENTS_REGISTRY.md`
  et les noms sensibles suivis ; contrôler en plus les fichiers de bots et bases locales hors de ses
  motifs.
- Étape 9 : quarantaine sur le lecteur D: (`D:\_quarantaine\`).
- Étape 11 : une amélioration retenue est appliquée à `maintenance.md` du kit, puis généralisée dans le
  template « maintenance » (en cours de conception, voir `MAINTENANCE/`).

<!-- SPECIFICITES PROJET : FIN -->
