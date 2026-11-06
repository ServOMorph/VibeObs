# Backlog — VibeObs

- [finding] `/close` étape 14bis : la détection « DEPLOYMENTS.md modifié » s'appuie sur `git diff --name-only`, or ce fichier est gitignoré ; la proposition de sauvegarde Drive ne peut donc jamais se déclencher.
  - fait quand: l'étape 14bis détecte la modification par un autre moyen (date ou empreinte), ou la décision de la laisser manuelle est tracée.
  - réf: `.claude/commands/close.md` (bloc SPECIFICITES PROJET, étape 14bis) ; `.gitignore` ligne 17.
- [finding] `/init_projet` étape 5 : si Q4 = oui mais que le dossier cible n'est pas un dépôt Git (cas `D:\xmage-test`, 2026-11-03), la commande ne prévoit ni `git init` ni question ; le `git add` échouerait. Fait à la main.
  - fait quand: l'étape 5 initialise le dépôt (ou pose la question) quand `.git` est absent.
  - réf: `.claude/commands/init_projet.md` étape 5.
- [piste] Roadmap `agents_paralleles` archivée le 2026-11-05 (phase 2 inachevée) : faire exécuter et vérifier un cycle `/start`/`/close` par agent (`ONBOARD`, `RETOURS`) dans son worktree d'Appli_TSA_SDI_TDAH ; phase 3 (évolutions produit) non commencée.
  - fait quand: un cycle par agent est exécuté et vérifié, ou l'abandon du pilote est décidé.
  - réf: `_archives/roadmap_agents_paralleles.md`
- [piste] Roadmap `com_agents` archivée le 2026-11-05 (phase 2 inachevée) : pilote de `/create_com_agents` sur `D:\ServOMorph\Meuniers` jamais fait (installation, placement 2c/2d au `/start`, écriture de `statut.md` au `/close`, `messages.md` lu puis purgé), puis bilan et propagation dans les templates.
  - fait quand: le pilote est joué et son bilan tranché, ou l'abandon du mécanisme est décidé.
  - réf: `_archives/roadmap_com_agents.md`, `.claude/commands/create_com_agents.md`
