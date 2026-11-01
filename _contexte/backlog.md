# Backlog — VibeObs

- [finding] `/close` étape 14bis : la détection « DEPLOYMENTS.md modifié » s'appuie sur `git diff --name-only`, or ce fichier est gitignoré ; la proposition de sauvegarde Drive ne peut donc jamais se déclencher.
  - fait quand: l'étape 14bis détecte la modification par un autre moyen (date ou empreinte), ou la décision de la laisser manuelle est tracée.
  - réf: `.claude/commands/close.md` (bloc SPECIFICITES PROJET, étape 14bis) ; `.gitignore` ligne 17.
