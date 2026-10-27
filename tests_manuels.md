# Tests manuels en attente

## /insert_template — destination par défaut ROBERTO/

Vérifier sur un projet cible réel (ex: `/insert_template <projet> overlay`
sans dossier de destination) que :
- le dossier `<projet_cible>/ROBERTO/` est bien créé s'il n'existait pas ;
- les fichiers du template atterrissent dedans et pas à la racine du projet ;
- un projet où `ROBERTO/` existe déjà et contient déjà un template ne casse
  rien (fusion correcte, pas d'écrasement).

À valider avant de considérer la convention déployée pour tous les templates
existants (`control_PC`, `discord_com`, `overlay`).

## rclone multicompte — backup SérénIATech_dev vers sereniatech_drive

`ClaudeCode/backup_drive.py` de `SérénIATech_dev` a été repointé de `googledrive:`
vers `sereniatech_drive` (compte sereniatech33@gmail.com). À exécuter dans une
session de ce projet :
- lancer `python ClaudeCode/backup_drive.py` (ou son `/close`) ;
- vérifier que les archives, le miroir et la DB atterrissent bien dans
  `sereniatech_drive:BackUps/BACKUPS-SerenIATech_dev/` ;
- vérifier que le contrôle quota lit `sereniatech_drive:` sans erreur ;
- confirmer qu'aucun nouvel objet n'apparaît côté compte rayonnetoi@gmail.com.

## rclone multicompte — vérifier les /close des projets partagés

Pour `Rayonne_Toi` et `Appli_TSA_SDI_TDAH` (partage assumé de `rayonne_toi_drive`) :
au prochain `/close` de chacun, vérifier via `rclone lsf rayonne_toi_drive:BackUps`
que le backup atterrit dans le bon sous-dossier de projet.

## chatgpt-orchestrateur — correctif vol de focus (`focus_fiable.ps1`)

Le correctif (activation avec nouvelles tentatives + contrôle du focus avant chaque
clic, dans `cliquer_fenetre`, `coller_et_envoyer`, `copier_reponse`, `defiler_fenetre`)
n'a été validé qu'en syntaxe. À exécuter, VS Code ayant le focus au lancement :
- lancer `cliquer_fenetre.ps1` sur une fenêtre Chrome ChatGPT : le clic doit atterrir
  dans Chrome, pas dans VS Code ;
- répéter 5 fois de suite, y compris avec une autre application au premier plan ;
- simuler un échec (fenêtre cible minimisée ou bloquée) : le script doit s'arrêter
  avec le code 2 et le message « Focus non obtenu », sans aucun clic ;
- contrôler qu'aucun effet parasite de la touche Alt (barre de menus Chrome activée) ne
  gêne le clic ou la saisie qui suit ;
- si validé : mettre à jour `roadmap_reprise_multicompte.md` (blocage Phase 3) et la
  section dédiée de `skills/chatgpt-orchestrateur/SKILL.md`.

## /start et /close — attribution par zone (SérénIATech_dev)

Commandes déployées par `/update` le 2026-10-14 (étapes `/close` 3-bis, 4, 13, 15 ; `/start` 4c).
À rejouer dans une nouvelle session ouverte sur `SérénIATech_dev`, un scénario à la fois :
- `/start` racine : `signals.md` affiché intégralement ; bloc 4c présent seulement si justifié (sortie reçue le 2026-10-14 : aucun bloc, roadmap Luna laissée à la racine par décision) ; rejoué le 2026-10-27 : signals affiché intégralement, aucune roadmap ni hook, bloc 4c présent avec 2 éléments déjà marqués `[à transférer vers <alias>]` (business, ia-ados), doublon déclaré « non vérifiable : `_contexte/signals.md` introuvable » alors que `Business/_contexte/signals.md` et `Communication/Youtube/L'IA aux ados/_contexte/signals.md` existent et ne contiennent pas l'action (attendu : doublon « non ») — DIVERGENCE à transmettre au kit) ;
- `/start shorts` : charte puis signaux de la zone, bloc 4c éventuel ;
- `/close` racine après un travail dans SHORTS : écart zone/travail signalé, éléments dans le signal de SHORTS (ou `[à transférer vers shorts]` si `agent_role.md` l'interdit), rien recopié à la racine ;
- session touchant plusieurs zones : seules les actions et points d'attention des autres zones sont modifiés, jamais leur « Dernière session » ;
- action déjà présente dans sa zone : mise à jour, aucun doublon ;
- signal ignoré par Git : non annoncé comme commité, signalé au bilan.
Transmettre chaque divergence au kit (scénario, étape, attendu, observé).

## /close v5.22 — tri vers backlog.md

À rejouer dans un projet dont `signals.md` dépasse 20 actions ouvertes (ex: `Appli_TSA_SDI_TDAH` après application manuelle, ou `SérénIATech_dev` après `/update`) :
- `/close` : le bilan propose un tri vers `_contexte/backlog.md` avec la liste des candidates, sans le faire d'office ;
- après accord, `backlog.md` est créé à la première entrée (pas de fichier vide), au format `fait quand:` / `réf:`, et `signals.md` porte une seule ligne « Backlog : N entrées — `_contexte/backlog.md` » sans priorité, hors plafond ;
- `/start` suivant : `backlog.md` n'est pas chargé ;
- une action dont le `fait quand:` n'est plus atteignable est proposée au retrait, jamais supprimée en silence ;
- une entrée traitée est supprimée du backlog par le `/close` qui la constate ; backlog vidé : fichier et ligne de renvoi supprimés ;
- une entrée du backlog rendue urgente est promue dans `signals.md` (écrite, relue, puis retirée) ;
- `backlog.md` ignoré par Git : signalé au bilan, non annoncé comme commité.
Transmettre chaque divergence au kit (scénario, étape, attendu, observé).
