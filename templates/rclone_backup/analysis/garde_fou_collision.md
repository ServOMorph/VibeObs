# Garde-fou anti-collision de remote — cas verrouillés

Dossier `analysis/` : traçage côté kit, jamais copié dans les projets cibles.

Contrôle défini dans `insert_template.md` étape 7bis (source de vérité), référencé par
`create_projet.md` (bloc rclone_backup) et `init_projet.md` (Q4bis). Registre : section
« Remotes rclone » de `<kit>/DEPLOYMENTS.md`.

Ces cas se rejouent à la main lors d'une insertion réelle de `rclone_backup` ; ils ne
nécessitent aucun appel réseau autre que `rclone listremotes`.

## Cas 1 — remote neuf accepté

- Contexte : projet cible sans ligne dans le registre ; l'utilisateur connecte un nouveau compte.
- Attendu :
  - le nom logique proposé suit la convention `<nom_projet_en_minuscules>_drive` ;
  - `rclone config create <remote> drive` lancé seulement après feu vert explicite ;
  - `rclone_backup.json` écrit avec ce remote ;
  - une nouvelle ligne `| <projet> | <remote> | <compte> | <DATE> | |` ajoutée au registre.

## Cas 2 — remote déjà attribué à un autre projet, partage non déclaré → refus

- Contexte : le registre contient déjà `| AutreProjet | x_drive | ... |` ; l'utilisateur demande
  à réutiliser `x_drive` pour la cible et ne confirme pas de partage assumé.
- Attendu :
  - `x_drive` n'apparaît pas dans la liste numérotée des remotes réutilisables ;
  - la désignation explicite de `x_drive` déclenche le rappel de la règle et la demande de
    confirmation de partage ; sans confirmation, refus ;
  - redirection vers la connexion d'un nouveau compte ; aucun contournement silencieux ;
  - `rclone_backup.json` non écrit tant qu'un remote valide n'est pas retenu.

## Cas 3 — registre absent ou section vide

- Contexte : `DEPLOYMENTS.md` sans section « Remotes rclone », ou section sans ligne de données.
- Attendu :
  - aucun blocage : tous les remotes de `rclone listremotes` sont réutilisables ;
  - après choix/connexion, la section « Remotes rclone » est créée si absente, puis la ligne ajoutée.

## Cas 4 — ré-insertion sur le même projet

- Contexte : le registre contient déjà `| Cible | cible_drive | ... |` ; nouvelle insertion sur Cible.
- Attendu :
  - `cible_drive` accepté tel quel (pas traité comme collision) ;
  - ligne du registre inchangée ou seulement redatée.

## Cas 5 — partage explicitement déclaré → accepté + note registre

- Contexte : le registre contient déjà `| AutreProjet | x_drive | ... |` ; l'utilisateur désigne
  `x_drive` pour la cible et confirme explicitement un partage assumé entre la cible et
  `AutreProjet`.
- Attendu :
  - `x_drive` est accepté et écrit dans `rclone_backup.json` de la cible ;
  - la section « Remotes rclone » porte une ligne pour la cible et une pour `AutreProjet`, chacune
    avec la note `partagé: <cible> + AutreProjet` ;
  - aucune connexion de nouveau compte n'est lancée.
