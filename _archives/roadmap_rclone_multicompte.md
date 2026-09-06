# Roadmap — rclone_backup : un compte Google dédié par projet

Objectif : garantir que chaque projet équipé du template `rclone_backup` sauvegarde
vers un compte Google **distinct**, corriger l'état actuel (tout atterrit dans le compte
Rayonne Toi) et empêcher la régression au niveau du kit.
Créée le : 2026-09-06
Clôturée le : 2026-09-06 — 3/3 phases achevées.
Écart assumé : `Appli_TSA_SDI_TDAH` partage volontairement `rayonne_toi_drive` avec
`Rayonne_Toi` (décision 2026-09-06). État final `rayonne_toi_drive:BackUps/` =
`Rayonne_Toi` + `Appli_TSA_SDI_TDAH` (et non `Rayonne_Toi` seul comme écrit en Phase 3).
Remotes actifs : `vibeobs_drive`, `sereniatech_drive`, `rayonne_toi_drive` ;
`googledrive:` supprimé.
Angle mort non traité : `meuniers/` présent sur le compte `sereniatech33@gmail.com`
(partagé avec `SérénIATech_dev`, non déclaré au registre) — à investiguer séparément.

---

## Constat de départ (ne pas supprimer)

- `rclone listremotes` : `googledrive:` et `rayonne_toi_drive:` — les deux `rclone lsd` renvoient
  un contenu racine identique : **même compte Google (Rayonne Toi)**, doublon de remote.
- `templates/rclone_backup/backup_project.py` : destination `<remote>:BackUps/<nom_projet>/`.
- `templates/rclone_backup/rclone_backup.json` : `{ "remote": "{{RCLONE_REMOTE}}" }`, valeur figée à l'insertion.
- Projets avec `rclone_backup` installé (find profondeur 4) :
  - `Appli_TSA_SDI_TDAH/claude-vibecoding-kit/rclone_backup.json` → `"remote": "rayonne_toi_drive"` (mauvais compte).
  - `Rayonne_Toi/claude-vibecoding-kit/rclone_backup/rclone_backup.json` → `"remote": "rayonne_toi_drive"` (compte correct).
- Kit VibeObs : sauvegarde séparée via `scripts/backup_file.py` → `googledrive:BackUps/VibeObs/` (mécanisme
  distinct du template, `close.md` étape ~184). Atterrit aussi dans le compte Rayonne Toi.
- `rclone lsd googledrive:BackUps` : `Appli_TSA_SDI_TDAH`, `BACKUPS-SerenIATech_dev`, `Rayonne_Toi`,
  `VibeObs`, `claude-vibecoding-kit`.
- `insert_template.md` étape 7bis, `create_projet.md` (bloc rclone_backup), `init_projet.md` Q4bis :
  proposent « utiliser un remote déjà configuré » sans aucun garde-fou anti-collision entre projets.

**Décisions utilisateur (2026-09-06)** :
- Règle retenue : **un compte Google dédié par projet** ; le template doit refuser un remote déjà
  utilisé par un autre projet.
- Données déjà mal placées dans le Drive de Rayonne Toi : **déplacer puis supprimer**.

**À clarifier en Phase 2** : le mapping projet → compte Google (l'utilisateur a ~13 comptes déjà
mappés à des profils Chrome, cf. `roadmap_reprise_multicompte.md`). Ne rien connecter sans ce mapping.

---

## Phase 1 — Durcissement du kit (template + commandes) [FAIT]

- [ ] `templates/rclone_backup/README.md` + `rclone_backup.json` : documenter que le remote est
      **dédié au projet**, jamais partagé.
- [ ] Registre projet → remote : choisir le support (fichier kit versionné ou `DEPLOYMENTS.md`
      gitignoré) et le format. Une ligne par projet : `<nom_projet> | <remote> | <compte Google>`.
- [ ] `insert_template.md` étape 7bis : garde-fou. Avant d'accepter un remote existant pour
      `rclone_backup`, consulter le registre ; si le remote est déjà pris par un autre projet,
      refuser et exiger la connexion d'un nouveau compte. Écrire la nouvelle ligne au registre
      après succès.
- [ ] `create_projet.md` (bloc `rclone_backup`, ~l.122-133) : même garde-fou, même écriture registre.
- [ ] `init_projet.md` Q4bis (projet sans git) : même garde-fou.
- [ ] Tests verrouillés (cas reproductibles, pas d'appel réseau) :
      remote neuf accepté + ligne registre créée ; remote déjà présent au registre → refus ;
      registre absent → création. Documenter le jeu de cas dans `templates/rclone_backup/analysis/`.
- [ ] `/doc_sync` si la surface documentée du kit change (CHANGELOG, README, doc protocole).

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer. Attendre sa
réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## Phase 2 — Comptes Google dédiés et repointage des configs [FAIT]

- [ ] Établir avec l'utilisateur le mapping projet → compte Google (au minimum : `Appli_TSA_SDI_TDAH`,
      `VibeObs`/kit ; `Rayonne_Toi` reste sur son compte ; statuer sur `SerenIATech_dev` et
      `claude-vibecoding-kit`).
- [ ] Pour chaque projet sans compte dédié : feu vert explicite, puis
      `rclone config create <projet>_drive drive` (auth navigateur, l'utilisateur choisit le compte),
      ne poursuivre qu'au succès.
- [ ] Mettre à jour le `rclone_backup.json` de chaque projet concerné avec son nouveau remote.
- [ ] Kit VibeObs : décider du remote dédié pour `scripts/backup_file.py` (aujourd'hui `googledrive:`)
      et mettre à jour `close.md` étape ~184 en conséquence.
- [ ] Statuer sur le remote `googledrive:` (doublon de `rayonne_toi_drive:`) : renommer vers un nom
      explicite ou supprimer après repointage de tous les usages.
- [ ] Renseigner le registre (Phase 1) pour tous les projets existants.
- [ ] Vérification : un `/close` par projet écrit bien dans le compte attendu (contrôle `rclone lsd`
      sur le bon remote).

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer. Attendre sa
réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## Phase 3 — Migration des données et purge du Drive Rayonne Toi [FAIT]

- [ ] Pour chaque dossier mal placé dans `<compte Rayonne Toi>:BackUps/` (`Appli_TSA_SDI_TDAH`,
      `VibeObs`, `claude-vibecoding-kit`, `BACKUPS-SerenIATech_dev` selon mapping Phase 2) :
      `rclone copy` vers `<bon_compte>:BackUps/<projet>/`, puis `rclone check` source/destination.
- [ ] Après contrôle OK : `rclone purge <compte Rayonne Toi>:BackUps/<projet>` pour chaque dossier
      étranger.
- [ ] État final attendu : `<compte Rayonne Toi>:BackUps/` ne contient plus que `Rayonne_Toi`.
- [ ] Mettre à jour `signals.md` / `contexte.md` : garde-fou permanent « un remote rclone = un projet ».

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer. Attendre sa
réponse écrite. Ne pas commencer la phase suivante sans confirmation.
