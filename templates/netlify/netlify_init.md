# /netlify_init

La procédure détaillée est disponible dans `.claude/commands/netlify_init.md`.
Si l'agent ne charge pas les commandes Claude, il doit suivre ce parcours :

1. Analyser le projet : site statique ou application buildée. Conserver le
   `netlify.toml` existant s'il est déjà adapté ; ne pas imposer `npm`/`dist` à
   un site statique.
2. Ouvrir `https://app.netlify.com/` avec le user. Le user se connecte lui-même.
3. Dans son avatar : **User settings > Applications > Personal access tokens
   > New access token**. Le user conserve le token et le saisit directement,
   sans le partager avec l'agent, dans `.env.netlify` sous
   `NETLIFY_AUTH_TOKEN`.
4. Pour le déploiement automatique : **Add new project > Import an existing
   project**, choisir le dépôt Git et renseigner la commande de build et le
   dossier de publication adaptés au projet. Pour un site statique dans
   `site/`, laisser la commande de build vide et publier `site`.
5. Relever le **Project ID** sous **Project configuration > General > Project
   information** et le saisir dans `NETLIFY_SITE_ID` si les scripts API/CLI
   doivent être indépendants de `.netlify/`.

Le seul token Netlify du template est le PAT. Le Project ID n'est pas un
secret. Ne jamais coller un token dans le chat ni le committer.
