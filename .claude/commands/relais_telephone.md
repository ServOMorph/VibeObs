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
déjà écrite dans le terminal. Une ligne `[DEBUG]` est ignorée, de même qu'une phrase parasite de la
reconnaissance vocale (« Sous-titres réalisés par… », « wap ») : ni réponse ni envoi.

**Jamais de silence.** L'utilisateur conduit et ne voit pas le terminal : il prend un silence pour
une panne. Chaque message `[canal:vocal]` ou `[canal:texte]` reçoit une réponse au téléphone dans la
minute, sans exception. La reconnaissance vocale découpe une phrase en plusieurs messages : une
phrase qui semble incomplète reçoit un accusé court (« Reçu, je vous écoute ») et jamais un silence
d'attente ; la réponse complète part dès que le sens est clair. Un message peu clair : demander de
répéter, par `POST /send`. Après une suite de fragments sans conclusion, envoyer au plus tard au bout
d'une minute un résumé de ce qui a été compris et demander si c'est complet. Seules les lignes
`[DEBUG]` restent sans réponse ; une phrase parasite est signalée au téléphone (« phrase non comprise »).

**Réponses courtes.** L'appli ferme le micro pendant la réponse vocale et perd ce que l'utilisateur dit
alors : chaque message envoyé au téléphone fait deux phrases courtes au plus (une seule question à la
fois), le détail va dans le terminal ou un fichier. Un accusé tient en une phrase.

**Points réguliers (décision de l'utilisateur du 2026-11-19).** Pendant toute action longue lancée par
le relais (veille, travail confié à une autre session, tâche de VibeObs), envoyer au téléphone un
point d'une phrase toutes les minutes, jusqu'à la fin. Mécanisme : au lancement de l'action,
démarrer un Monitor de cadence (`while true; do sleep 60; echo tick; done`, `timeout_ms` de 1800000)
et noter son `task_id` dans la ligne de la file ; à chaque `tick`, lire l'état réel (`ListAgents`,
fichier de rapport, sortie en cours) puis envoyer « toujours en cours : <étape> » ou « bloqué : <raison> » ;
à la fin, `TaskStop` sur la cadence et annoncer le résultat. Un point ne répète pas le précédent sans
fait nouveau : dire « pas de changement depuis une minute » plutôt qu'inventer.

1. **Question reçue d'une session** (message de session portant « Question pour l'utilisateur ») :
   l'ajouter à la file (`AAAA-MM-JJ HH:MM | <session> | <question> | en attente`) et l'envoyer au
   téléphone : « <session> demande : <question> ».
2. **« point »** (ou équivalent) : lire les questions `en attente` de la file, une phrase chacune,
   avec le nom de la session. File vide : le dire. Ajouter les sessions `waiting` de `ListAgents`
   qui n'y figurent pas : « <session> attend un clic au PC ». L'état d'une session se lit aussi dans
   son fil de conversation (`~/.claude/projects/`, lecture seule).
3. **Réponse de l'utilisateur** : la relire avant tout envoi (« Je transmets "<réponse>" à
   <session>, je confirme ? »), sauf « plus tard ». Pour une réponse qui engage (modification,
   envoi, suppression), seul un « oui » net vaut confirmation : tout autre mot ou « oui » ambigu =
   pas de transmission, redemander. Après confirmation, la transmettre par
   `SendMessage` sans reformulation, précédée de « Réponse de l'utilisateur, validée par
   téléphone : ». Réponse tapée au clavier du PC : réponse directe, sans relecture ni confirmation
   vocale ; la transmettre avec la même mention, puis en informer le téléphone. Session ambiguë :
   redemander laquelle. Passer la ligne de la file à `transmise`.
4. **Retour** : renvoyer au téléphone la réaction de la session (appliqué, refusé, en attente
   d'approbation, pas de réponse).
5. **Interdits** : décider ou répondre à la place de l'utilisateur ; transmettre une validation
   d'écriture dans `CLAUDE.md`, `AGENTS.md` ou `GEMINI.md` (répondre qu'elle se fait au clavier) ;
   lever une limite de « Ce qui ne se dépasse jamais » du registre.
6. **Trace** : une ligne par échange dans `_contexte/journal_session.md`
   (`AAAA-MM-JJ HH:MM | action | relais <session> : question / réponse verbatim / résultat`).
7. Message commençant par `!<nom>` : appliquer `.claude/commands/<nom>.md` de VibeObs ; commande
   inconnue : le signaler par `POST /send`.
8. **« fin du relais »** (arrêt immédiat) : (a) repasser en mode habituel (`/telephone off`) les
   sessions en mode `/telephone roberto` ; (b) demander à la session Roberto d'arrêter le pont ;
   (c) envoyer au téléphone un dernier message ; (d) arrêter l'écoute (équivalent de l'argument
   `stop`).
