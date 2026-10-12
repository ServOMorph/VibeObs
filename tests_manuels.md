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
