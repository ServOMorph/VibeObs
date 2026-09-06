# rclone_backup

Sauvegarde miroir du projet vers `<remote-rclone>:BackUps/<nom-du-projet>/` via rclone.

Prérequis : installer rclone sous Windows dans `%LOCALAPPDATA%\\rclone\\rclone.exe` et configurer
un remote Google Drive. Lors de l'insertion, choisir un remote déjà configuré ou connecter un
nouveau compte Google ; le choix est enregistré dans `rclone_backup.json`, propre au projet.

**Règle : un remote rclone est dédié à un seul projet par défaut.** Un partage entre projets
n'est accepté que s'il est déclaré explicitement pendant l'insertion ; la ligne du registre
« Remotes rclone » de `DEPLOYMENTS.md` (kit) porte alors la note `partagé:`. Sans déclaration,
l'insertion refuse un remote déjà attribué à un autre projet.

Le script exclut `.git`, `node_modules`, les environnements virtuels et les dossiers de build.
Il est conçu pour être appelé par `/close` après insertion du template. Une erreur rclone doit être
signalée sans bloquer la clôture.
