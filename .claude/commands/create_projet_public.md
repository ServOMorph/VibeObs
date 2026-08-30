---
description: Crée un projet vierge — dossier dans le parent défini dans .env, dépôt GitHub public, puis /init_projet
argument-hint: "<nom_projet>"
model: sonnet
---

# /create_projet_public <nom_projet>

## Objectif

Créer un projet à partir de rien : un dossier sous le dossier parent défini dans `.env`, un
dépôt GitHub public sur le compte de l'utilisateur, le dépôt local initialisé et poussé, puis
l'enchaînement sur `/init_projet` pour poser le protocole vibecoding.

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
6. `gh auth status` — doit être connecté. Récupérer le login : `gh api user -q .login`
   (`<login>`). Échec → s'arrêter.
7. `gh repo view <login>/<nom_projet>` — si la commande réussit (le dépôt existe déjà) →
   s'arrêter et demander un autre nom.

## [CREATION LOCALE]

8. Créer `<cible>`.
9. Initialiser le dépôt :
   ```bash
   git -C "<cible>" init
   git -C "<cible>" branch -M main
   ```
10. Créer `<cible>/README.md` contenant uniquement `# <nom_projet>` (un fichier est nécessaire
    pour le premier commit ; `/init_projet` complétera le reste).
11. Premier commit :
    ```bash
    git -C "<cible>" add -A
    git -C "<cible>" commit -m "init: création du dépôt"
    ```

## [CREATION GITHUB]

12. Créer le dépôt public et le pousser en une commande :
    ```bash
    gh repo create <login>/<nom_projet> --public --source "<cible>" --remote origin --push
    ```
    Échec → afficher l'erreur telle quelle et s'arrêter. Le dépôt local reste en place (pas de
    rollback) — le signaler.

## [DESCRIPTION]

13. Demander : "Courte description du projet (1 phrase) ?" Attendre la réponse (`<desc>`).
14. L'appliquer au dépôt GitHub :
    ```bash
    gh repo edit <login>/<nom_projet> --description "<desc>"
    ```

## [INIT PROTOCOLE]

15. Enchaîner sur `/init_projet` tel que défini dans `.claude/commands/init_projet.md`, avec
    `<cible>` comme argument (ne jamais redemander le chemin). Proposer `<desc>` comme réponse
    par défaut à la question "Objectif du projet" (Q2) de `/init_projet`, ajustable par
    l'utilisateur ; laisser `/init_projet` poser ses autres questions normalement.
    `/init_projet` fait lui-même le commit initial du protocole (son étape 5, projet sous git)
    et enregistre le déploiement dans `<kit>/DEPLOYMENTS.md`.

## [SORTIE]

16. Un seul récapitulatif :
    - Dossier créé : `<cible>` (lien cliquable).
    - Dépôt GitHub public : `https://github.com/<login>/<nom_projet>`.
    - Description appliquée.
    - Reprise de la sortie de `/init_projet` (alias de zone, `/start <alias>` pour commencer).

<!-- SPECIFICITES PROJET : DEBUT (préservé par /update, ne pas toucher hors de ce bloc) -->
<!-- Convention : toute règle liée à une phase précise de la Procédure ci-dessus doit la
     référencer explicitement par son ancre ([PREFLIGHT]/[CREATION LOCALE]/[CREATION GITHUB]/
     [DESCRIPTION]/[INIT PROTOCOLE]/[SORTIE]), plutôt que par un numéro d'étape ou la position
     physique de cette zone. -->
<!-- SPECIFICITES PROJET : FIN -->
