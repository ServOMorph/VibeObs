---
description: Déploie le projet courant sur Netlify sans exposer les secrets
argument-hint: [brouillon|production]
---

# /netlify_deploy [brouillon|production]

1. Vérifier que `netlify.toml` et `.env.netlify` existent, sans afficher le
   contenu de `.env.netlify`. Exiger une valeur non vide pour
   `NETLIFY_AUTH_TOKEN`.
2. Vérifier que l'arbre Git est propre. Si ce n'est pas le cas, afficher les
   fichiers modifiés et demander confirmation avant un déploiement manuel.
3. Lancer les tests et la vérification de type définis par le projet, si des
   scripts `test` et `typecheck` existent dans `package.json`. Arrêter au
   premier échec.
4. Exécuter `./scripts/netlify_deploy.ps1` pour un brouillon, ou
   `./scripts/netlify_deploy.ps1 -Production` si l'argument est
   `production`. Ne jamais afficher ni transmettre le token dans la commande
   ou le rapport.
5. Rapporter l'URL renvoyée par Netlify et le résultat du build. Ne pas
   relancer automatiquement en cas d'échec.
