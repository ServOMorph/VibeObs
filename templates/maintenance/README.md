# maintenance

Maintenance complète d'un projet (fichiers, Git, documentation, code, sécurité), par lots validés.

Fichiers :
- `maintenance.md` -> `.claude/commands/maintenance.md` du projet cible : commande `/maintenance` (socle du kit + bloc « SPÉCIFICITÉS PROJET » à renseigner, préservé par `/update`).
- `regles_validation.md` -> racine de la zone maintenance ou `DOCUMENTATION/` du projet : périmètre, actions par type, exclusions, quarantaine, fréquence.
- `_contexte/maintenance_retours.md` : une ligne par amélioration proposée de la commande (`AAAA-MM-JJ | étape | friction | proposition`).

Périmètre : le projet où la maintenance est lancée, et lui seul. Toute suppression passe par la quarantaine `D:\_quarantaine\<date>\` avec `manifeste.md` ; la purge est un lot distinct validé à part.

Après insertion : renseigner le bloc « SPÉCIFICITÉS PROJET » de `maintenance.md`, puis lancer `/maintenance`.
