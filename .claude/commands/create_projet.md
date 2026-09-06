---
description: Crée un projet vierge — Git local ou dépôt GitHub, puis /init_projet et templates optionnels
argument-hint: "<nom_projet>"
model: sonnet
---

# /create_projet <nom_projet>

## Objectif

Créer un projet à partir de rien : un dossier sous le dossier parent défini dans `.env`, un dépôt
Git local, éventuellement relié et poussé vers GitHub (public ou privé), puis l'enchaînement sur
`/init_projet` pour poser le protocole vibecoding. Une fois le protocole installé, l'utilisateur
peut sélectionner les templates à ajouter.

Cette commande vit dans le kit et n'est jamais copiée dans les projets cibles : elle s'exécute
toujours depuis le kit, nom du projet en argument. `<kit>` = dossier de travail actif.

## [PREFLIGHT] — résolution, aucune écriture

1. Résoudre `<nom_projet>` depuis `$ARGUMENTS`. Absent → demander "Nom du nouveau projet (sert
   à la fois de nom de dossier et de nom de dépôt GitHub) ?" et s'arrêter jusqu'à réponse.
2. Valider le nom : `^[A-Za-z0-9._-]+$`, ni `.` ni `..`, pas de `.` en tête. Non conforme →
   s'arrêter et redemander un nom compatible GitHub (pas d'espace ni de caractère spécial).
3. Lire `<kit>/.env`. Absent → s'arrêter : "Copier `.env.example` vers `.env` et renseigner
   `PROJETS_PARENT_DIR`." Extraire la valeur :
   ```bash
   grep -E '^PROJETS_PARENT_DIR=' "<kit>/.env" | head -1 | cut -d= -f2-
   ```
   Vide → même arrêt.
4. `<parent>` = valeur résolue en chemin absolu. Si `<parent>` n'existe pas comme dossier →
   s'arrêter (ne pas créer le parent, c'est une erreur de configuration).
5. `<cible>` = `<parent>/<nom_projet>`. Si `<cible>` existe et n'est pas vide → s'arrêter (ne
   jamais écraser). Si `<cible>` existe et est vide : utilisable.
6. Demander le mode de dépôt :
   ```text
   Où créer le dépôt ?
   1. Git local uniquement
   2. Git local + dépôt GitHub
   Répondez par 1 ou 2.
   ```
   Attendre la réponse (`<mode_depot>`). Toute autre réponse → réafficher exactement cette
   question. Si `2`, demander ensuite :
   ```text
   Visibilité du dépôt GitHub :
   1. Public
   2. Privé
   Répondez par 1 ou 2.
   ```
   Attendre la réponse (`<visibilite>`). Toute autre réponse → réafficher exactement cette question.
7. Seulement si `<mode_depot>` vaut `2` : exécuter `gh auth status`, puis récupérer le login avec
   `gh api user -q .login` (`<login>`). Échec → s'arrêter.
8. Seulement si `<mode_depot>` vaut `2` : `gh repo view <login>/<nom_projet>`. Si la commande réussit
   (le dépôt existe déjà) → s'arrêter et demander un autre nom.

## [CREATION LOCALE]

9. Créer `<cible>`.
10. Initialiser le dépôt :
   ```bash
   git -C "<cible>" init
   git -C "<cible>" branch -M main
   ```
11. Créer `<cible>/README.md` contenant uniquement `# <nom_projet>` (un fichier est nécessaire
    pour le premier commit ; `/init_projet` complétera le reste).
12. Premier commit :
    ```bash
    git -C "<cible>" add -A
    git -C "<cible>" commit -m "init: création du dépôt"
    ```

## [CREATION GITHUB] — seulement si GitHub a été choisi

13. Définir `<option_visibilite>` à `--public` si `<visibilite>` vaut `1`, sinon à `--private`.
    Créer le dépôt GitHub et le pousser en une commande :
    ```bash
    gh repo create <login>/<nom_projet> <option_visibilite> --source "<cible>" --remote origin --push
    ```
    Échec → afficher l'erreur telle quelle et s'arrêter. Le dépôt local reste en place (pas de
    rollback) — le signaler.

## [DESCRIPTION] — seulement si GitHub a été choisi

14. Demander : "Courte description du projet (1 phrase) ?" Attendre la réponse (`<desc>`).
15. L'appliquer au dépôt GitHub :
    ```bash
    gh repo edit <login>/<nom_projet> --description "<desc>"
    ```

## [INIT PROTOCOLE]

16. Enchaîner sur `/init_projet` tel que défini dans `.claude/commands/init_projet.md`, avec
    `<cible>` comme argument (ne jamais redemander le chemin). Proposer `<desc>` comme réponse
    par défaut à la question "Objectif du projet" (Q2) de `/init_projet` si GitHub a été choisi ;
    sinon, laisser `/init_projet` poser cette question normalement. Laisser `/init_projet` poser
    ses autres questions normalement.
    `/init_projet` fait lui-même le commit initial du protocole (son étape 5, projet sous git)
    et enregistre le déploiement dans `<kit>/DEPLOYMENTS.md`.

## [TEMPLATES] — après /init_projet

17. Une fois `/init_projet` terminé, lister les sous-dossiers installables de `<kit>/templates/`
    (exclure les dossiers techniques `_contexte`, `.claude` et `__pycache__`) dans cet ordre, avec une numérotation :
    ```text
    Templates disponibles :
    1. control_PC
    2. discord_com
    3. intercom
    4. netlify
       5. notification
       6. overlay
       7. rclone_backup
       0. Aucun template

    Répondez uniquement par le ou les numéros souhaités, séparés par des virgules (ex. 2,5).
    ```
    Construire cette liste dynamiquement à partir des dossiers réellement présents ; ne jamais
    proposer de dossier technique ou généré. Une réponse doit être `0` seul ou une liste de numéros valides,
    sans doublon. Sinon, réafficher la question. Pour chaque sélection, enchaîner
    `/insert_template <cible> <nom_template>` selon `.claude/commands/insert_template.md`.

    Si `rclone_backup` est sélectionné, expliciter avant son insertion :
    - le dossier source sera `<cible>` ; le miroir sera envoyé vers
      `<remote-rclone>:BackUps/<nom_projet>/` ; `.git`, `node_modules`, les environnements virtuels,
      `dist`, `build` et `__pycache__` seront exclus ;
    - **un remote rclone est dédié à un seul projet par défaut ; un partage entre projets doit
      être déclaré explicitement** : la collecte et le contrôle anti-collision du compte sont ceux
      de l'étape 7bis de `/insert_template` (lecture du registre « Remotes rclone » de
      `<kit>/DEPLOYMENTS.md`, refus d'un remote déjà attribué à un autre projet sauf partage
      confirmé explicitement, connexion d'un nouveau compte Google avec feu vert explicite avant
      `rclone config create`, écriture du remote retenu dans `rclone_backup.json` puis dans le
      registre avec la note `partagé:` le cas échéant) ;
    - à chaque `/close`, la sauvegarde se lance avec ce compte sans redemander de connexion. Si
      rclone échoue, afficher l'erreur sans bloquer la clôture.

## [SORTIE]

18. Un seul récapitulatif :
    - Dossier créé : `<cible>` (lien cliquable).
    - Dépôt local initialisé.
    - Si GitHub a été choisi : dépôt GitHub `<visibilité>` : `https://github.com/<login>/<nom_projet>`
      et description appliquée.
    - Templates insérés, ou confirmation qu'aucun n'a été sélectionné.
    - Reprise de la sortie de `/init_projet` (alias de zone, `/start <alias>` pour commencer).

<!-- SPECIFICITES PROJET : DEBUT (préservé par /update, ne pas toucher hors de ce bloc) -->
<!-- Convention : toute règle liée à une phase précise de la Procédure ci-dessus doit la
     référencer explicitement par son ancre ([PREFLIGHT]/[CREATION LOCALE]/[CREATION GITHUB]/
     [DESCRIPTION]/[INIT PROTOCOLE]/[TEMPLATES]/[SORTIE]), plutôt que par un numéro d'étape ou la position
     physique de cette zone. -->
<!-- SPECIFICITES PROJET : FIN -->
