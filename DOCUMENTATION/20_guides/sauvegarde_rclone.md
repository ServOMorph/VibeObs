---
type: guide
description: Sauvegarde Google Drive par rclone : un remote par projet, limite de l'auto-mode sur l'upload
tags: guide, backup, rclone, sécurité
maj: 2026-11-14
---

# Sauvegarder un projet vers Google Drive (rclone)

Template `templates/rclone_backup/` (`backup_project.py`, `rclone_backup.json`), inséré par
`/insert_template` ou proposé par `/init_projet` à un projet sans Git (Q4bis). Source canonique :
[`../../templates/rclone_backup/README.md`](../../templates/rclone_backup/README.md),
`.claude/commands/insert_template.md` étape 7bis.

## Règle : un remote = un projet

Un remote rclone est dédié à un seul projet par défaut. Un partage entre projets n'est admis que
s'il est déclaré explicitement à l'insertion ; la ligne du registre « Remotes rclone » de
`DEPLOYMENTS.md` (kit) porte alors `partagé: A + B`. Sans déclaration, l'insertion refuse un remote
déjà attribué à un autre projet.

Raison : deux projets sur un même compte Drive sans le savoir mélangent leurs sauvegardes et leurs
quotas ; le registre rend chaque attribution visible et contrôlable.

Nouveau compte : nom logique `<nom_projet_en_minuscules>_drive`, absent de `rclone listremotes` et
du registre ; `rclone config create <remote> drive` ouvre un navigateur pour choisir le compte Google.

## Utilisation

```powershell
python backup_project.py <chemin_projet>          # miroir vers <remote>:BackUps/<dossier>/
python backup_project.py <chemin_projet> --check  # comparaison, sans modifier la sauvegarde
```

Exclusions : `.git`, `node_modules`, environnements virtuels, builds, `.env*`, clés, certificats,
credentials, tokens, configuration rclone, paramètres locaux. Une erreur rclone est signalée sans
bloquer `/close`.

## Limite : auto-mode et upload cloud

Sous auto-mode de Claude Code, le classifieur de sécurité refuse les copies `rclone` vers un cloud
(constaté avec des secrets dans le périmètre). Ni `permissions.allow` ni un réglage local ne le
contournent.

Conséquence pour un hook `/close` § Fin (`_contexte/on_close.md`) qui sauvegarde : il demande à
l'utilisateur de passer en mode manuel (`Shift+Tab`) et attend sa confirmation écrite avant toute
copie ; sans réponse, il ne lance rien et trace l'upload restant à faire. Exemple réel :
`Appli_TSA_SDI_TDAH/_contexte/on_close.md` § Fin (copie claire puis copie chiffrée des secrets).
