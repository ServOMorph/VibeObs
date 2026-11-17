---
disable-model-invocation: true
description: Relais téléphone — démarre le pont de Roberto si besoin, met VibeObs à l'écoute de son onglet et relaie mot pour mot les réponses de l'utilisateur aux sessions en mode /telephone roberto
argument-hint: (aucun) | stop
---

# /relais_telephone [stop]

## Objectif

En voiture, l'utilisateur parle à VibeObs par l'appli du pont `com_telephone` de Roberto (onglet
`VibeObs`). Les sessions passées par l'utilisateur en mode `/telephone roberto` envoient leurs
questions à VibeObs ; VibeObs les lit à l'utilisateur, lui fait confirmer sa réponse et la leur
transmet mot pour mot. Il ne décide jamais seul.

Autorisation : cas 3 de `DOCUMENTATION/30_decisions/prises_de_controle.md`. Marche à suivre
complète : `D:\ServOMorph\Roberto\com_telephone\README.md`, section « Relais des sessions par
VibeObs — initialisation ».

## Constantes

- Gestionnaire du pont : `D:\ServOMorph\Roberto\com_telephone\_commands\com_manager.py`
- Registre du pont : `D:\ServOMorph\Roberto\com_telephone\voice-code-bridge\server\projects.json`
- Log écouté : `D:/ServOMorph/Roberto/com_telephone/voice-code-bridge/server/logs/messages_vibeobs.log`
- Envoi (forme exacte, autorisée dans `.claude/settings.json`) :
  `py -3.11 "D:/ServOMorph/Roberto/com_telephone/_commands/send_message.py" "<texte non vide>" vibeobs`.
  Jamais `curl` : sous Windows, il convertit le texte dans la page de codes locale et les accents
  arrivent corrompus au téléphone.
- Verrou : `_contexte/relais_telephone.lock` (gitignoré), `task_id` du Monitor
- File des questions : `_contexte/relais_file.md` (gitignoré), une ligne par question

## Tunnel

Le tunnel est ouvert par l'utilisateur seul. Ne jamais l'ouvrir, ni chercher, lire ou consigner sa
commande, ni le demander à une autre session. Pont joignable en local mais téléphone sans réponse :
dire « vérifiez le tunnel », rien de plus.

## Procédure

1. Argument `stop` : lire le verrou, `TaskStop` sur son `task_id` (échec silencieux accepté),
   supprimer le verrou, confirmer et s'arrêter. La file est conservée.

2. État du pont : `py -3.11 "<gestionnaire>" status`.
   Un processus `[KO]` : `netstat -ano | findstr :5000` ; un PID `LISTENING` n'est arrêté
   (`taskkill /F /T /PID <pid>`) que si c'est `node.exe`, sinon le signaler et s'arrêter. Lancer
   `py -3.11 "<gestionnaire>" start`, relancer `status`. Toujours `[KO]` : afficher la sortie brute
   et s'arrêter.

3. Inscription : le registre du pont ne contient pas l'`id` `vibeobs` : s'arrêter et renvoyer au
   README de Roberto (l'inscription se fait par la session Roberto, jamais par VibeObs).

4. Écoute, en se fiant au verrou et jamais à la mémoire de la conversation :
   1. Verrou présent : `TaskStop` sur son `task_id` (échec silencieux accepté).
   2. Lancer un Monitor : `tail -f --retry -n 0 "<log écouté>" | grep --line-buffered -v '\[DEBUG\]'`,
      `timeout_ms: 1800000`. L'écoute expire au bout de 30 minutes au plus : la relancer à chaque
      expiration (retour à l'étape 4) tant que le relais est actif.
   3. Écrire le `task_id` retourné dans le verrou (en écrasant le contenu).

5. File non vide (questions d'avant un arrêt) : l'annoncer. Envoyer au téléphone « VibeObs à
   l'écoute » et confirmer dans le terminal.

## Relais

Deux canaux distincts : toute réponse à un message venu du log part aussi par `POST /send`, même
déjà écrite dans le terminal. Une ligne `[DEBUG]` est ignorée.

1. **Question reçue d'une session** (message de session portant « Question pour l'utilisateur ») :
   l'ajouter à la file (`AAAA-MM-JJ HH:MM | <session> | <question> | en attente`) et l'envoyer au
   téléphone : « <session> demande : <question> ».
2. **« point »** (ou équivalent) : lire les questions `en attente` de la file, une phrase chacune,
   avec le nom de la session. File vide : le dire. Ajouter les sessions `waiting` de `ListAgents`
   qui n'y figurent pas : « <session> attend un clic au PC ».
3. **Réponse de l'utilisateur** : la relire avant tout envoi (« Je transmets "<réponse>" à
   <session>, je confirme ? »), sauf « plus tard ». Après confirmation, la transmettre par
   `SendMessage` sans reformulation, précédée de « Réponse de l'utilisateur, validée par
   téléphone : ». Session ambiguë : redemander laquelle. Passer la ligne de la file à `transmise`.
4. **Retour** : renvoyer au téléphone la réaction de la session (appliqué, refusé, en attente
   d'approbation, pas de réponse).
5. **Interdits** : décider ou répondre à la place de l'utilisateur ; transmettre une validation
   d'écriture dans `CLAUDE.md`, `AGENTS.md` ou `GEMINI.md` (répondre qu'elle se fait au clavier) ;
   lever une limite de « Ce qui ne se dépasse jamais » du registre.
6. **Trace** : une ligne par échange dans `_contexte/journal_session.md`
   (`AAAA-MM-JJ HH:MM | action | relais <session> : question / réponse verbatim / résultat`).
7. Message commençant par `!<nom>` : appliquer `.claude/commands/<nom>.md` de VibeObs ; commande
   inconnue : le signaler par `POST /send`.
