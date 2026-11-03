# Backlog — VibeObs

- [finding] `/close` étape 14bis : la détection « DEPLOYMENTS.md modifié » s'appuie sur `git diff --name-only`, or ce fichier est gitignoré ; la proposition de sauvegarde Drive ne peut donc jamais se déclencher.
  - fait quand: l'étape 14bis détecte la modification par un autre moyen (date ou empreinte), ou la décision de la laisser manuelle est tracée.
  - réf: `.claude/commands/close.md` (bloc SPECIFICITES PROJET, étape 14bis) ; `.gitignore` ligne 17.
- [finding] `/init_projet` étape 5 : si Q4 = oui mais que le dossier cible n'est pas un dépôt Git (cas `D:\xmage-test`, 2026-11-03), la commande ne prévoit ni `git init` ni question ; le `git add` échouerait. Fait à la main.
  - fait quand: l'étape 5 initialise le dépôt (ou pose la question) quand `.git` est absent.
  - réf: `.claude/commands/init_projet.md` étape 5.
