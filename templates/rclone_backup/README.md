# rclone_backup

Sauvegarde miroir du projet vers `<remote-rclone>:BackUps/<dossier-canonique>/` via rclone.

Prérequis : installer rclone sous Windows dans `%LOCALAPPDATA%\\rclone\\rclone.exe` et configurer
un remote Google Drive. Lors de l'insertion, choisir un remote déjà configuré ou connecter un
nouveau compte Google ; le remote et le dossier Drive canonique sont enregistrés dans
`rclone_backup.json`, propre au projet. Le nom du dossier ne dépend donc pas de la casse du
chemin passé au script.

**Règle : un remote rclone est dédié à un seul projet par défaut.** Un partage entre projets
n'est accepté que s'il est déclaré explicitement pendant l'insertion ; la ligne du registre
« Remotes rclone » de `DEPLOYMENTS.md` (kit) porte alors la note `partagé:`. Sans déclaration,
l'insertion refuse un remote déjà attribué à un autre projet.

Le script exclut `.git`, `node_modules`, les environnements virtuels, les dossiers de build et les
fichiers sensibles usuels : `.env*`, clés privées, certificats, credentials, tokens, configuration
rclone et paramètres locaux.

Exécution :

```powershell
python backup_project.py <chemin_projet>
python backup_project.py <chemin_projet> --check
```

`--check` compare le projet local à la sauvegarde, sans la modifier. Le script est conçu pour être
appelé par `/close` après insertion du template. Une erreur rclone doit être signalée sans bloquer
la clôture.
