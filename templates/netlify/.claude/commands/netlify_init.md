---
description: Guide la connexion Netlify, la création du token et la liaison du dépôt sans exposer les secrets
argument-hint:
---

# /netlify_init

## Objectif

Connecter le projet courant à Netlify une seule fois, préparer le déploiement
manuel et activer les déploiements automatiques à chaque `git push`. Quand un
navigateur connecté est disponible, accompagner le user dans l'interface
Netlify ; le user effectue lui-même toute authentification ou création de
secret.

## Règles de sécurité

- Ne jamais demander au user de coller un token dans la conversation.
- Ne jamais lire, afficher, logger ou committer `.env.netlify`.
- Le seul secret requis par le template est `NETLIFY_AUTH_TOKEN`. Les secrets
  propres à l'application doivent être créés dans Netlify séparément, avec les
  noms demandés par le projet.
- Ne jamais remplacer un `netlify.toml` existant sans avoir analysé le projet
  et obtenu l'accord explicite du user.

## Procédure guidée

1. Analyser le projet avant toute configuration. Déterminer :
   - **site statique** : pas de `package.json`, mais un `index.html` dans un
     dossier tel que `site/`, `public/` ou la racine. Le build command doit
     rester vide et le publish directory doit être ce dossier (par exemple
     `site`).
   - **application buildée** : `package.json` et un script de build. Utiliser
     le script réel et son dossier de sortie ; ne jamais supposer `npm`/`dist`.
   Si `netlify.toml` existe déjà et correspond au projet, le conserver. Sinon,
   présenter la correction proposée et attendre l'accord du user.
2. Vérifier que `.gitignore` exclut `.env.netlify` et `.netlify/`. S'ils sont
   absents, proposer de les ajouter ; attendre l'accord du user avant toute
   écriture.
3. Si un navigateur contrôlable est disponible, ouvrir le tableau de bord
   Netlify et guider visuellement le user. Sinon, lui demander d'ouvrir
   `https://app.netlify.com/`. Le user se connecte lui-même, gère son mot de
   passe, son SSO et sa 2FA ; l'agent attend sa confirmation.
4. Demander au user d'ouvrir un terminal à la racine du projet et d'exécuter :

   ```powershell
   npx netlify login
   ```

   Le user termine l'authentification dans son navigateur. Attendre sa
   confirmation explicite avant de poursuivre.
5. Dans Netlify, guider le user vers son avatar, **User settings**, puis
   **Applications > Personal access tokens > New access token**. Il choisit un
   nom, une expiration et, si demandé, l'accès à son équipe SSO. Au moment où
   Netlify affiche la valeur une seule fois, le user la copie directement dans
   son gestionnaire de mots de passe puis dans son fichier local : l'agent ne
   la lit jamais. C'est le seul token requis pour la CLI et l'API de ce
   template ; le Project ID est un identifiant, pas un token.
6. Demander au user de créer localement `.env.netlify` à partir de
   `.env.netlify.example` et d'y saisir lui-même :

   ```text
   NETLIFY_AUTH_TOKEN=<token créé dans Netlify>
   ```

   Il peut laisser `NETLIFY_SITE_ID` vide à ce stade. Demander uniquement une
   confirmation que le fichier est prêt, jamais son contenu.
7. Si le dépôt est déjà hébergé sur GitHub, GitLab, Bitbucket ou Azure DevOps,
   préférer le tableau de bord Netlify : **Add new project > Import an
   existing project**, sélectionner le fournisseur puis le dépôt. Dans les
   réglages de build, appliquer le résultat de l'étape 1 (site statique :
   commande vide et dossier `site`/équivalent ; application : commande et
   sortie réelles). Confirmer le premier déploiement. Lier ce dépôt active les
   déploiements automatiques à chaque push sur la branche de production.
   Si aucun dépôt distant n'existe, demander au user d'en créer un avant de
   promettre des mises à jour automatiques.
8. Si le user veut plutôt créer ou relier le projet depuis le terminal,
   demander son accord puis exécuter :

   ```powershell
   npx netlify init
   ```

   Le guider dans les choix sans publier en production sans accord explicite.
   Attendre la confirmation que l'initialisation a réussi.
9. Demander au user de relever le **Project ID** dans Netlify :
   **Project configuration > General > Project information**. Il peut ensuite
   le renseigner lui-même dans `NETLIFY_SITE_ID` de `.env.netlify`. Cet
   identifiant n'est pas un secret ; il est optionnel si `.netlify/` est déjà
   lié, mais recommandé pour les scripts et les appels d'API explicites.
10. Si l'application emploie d'autres variables de build ou de runtime,
   identifier seulement leurs noms dans le code et guider le user vers
   **Project configuration > Environment variables**. Le user saisit les
   valeurs directement dans Netlify. Ne jamais les demander dans le chat.
11. Proposer un premier brouillon avec :

   ```powershell
   .\scripts\netlify_deploy.ps1
   ```

   Après succès, proposer la production avec
   `./scripts/netlify_deploy.ps1 -Production` ou le déploiement automatique
   par `git push`. Ne jamais lancer une publication de production sans accord
   explicite.

## Rapport final

Indiquer uniquement : connexion CLI terminée ou non, projet lié ou non,
déploiement automatique configuré ou non, et les prochaines actions. Ne pas
inclure de token, de contenu de `.env.netlify` ou de valeur d'environnement.
