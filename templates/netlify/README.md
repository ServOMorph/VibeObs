# Template Netlify

Ce template ajoute au projet cible une configuration Netlify autonome :

- `netlify.toml` : build `npm run build`, publication de `dist` et fallback SPA ;
- `scripts/netlify_deploy.ps1` : build et déploiement manuel par CLI ;
- `scripts/netlify_api.py` : client REST générique pour l'API publique Netlify v1 ;
- `.env.netlify.example` : variables locales à renseigner, sans secret versionné ;
- `.claude/commands/netlify_init.md` : connexion guidée au compte Netlify ;
- `.claude/commands/netlify_deploy.md` : procédure que l'agent peut exécuter.

## Installer depuis le kit

Depuis le kit, lancer :

```text
/insert_template "CHEMIN_ABSOLU_DU_PROJET" netlify .
```

Le `.` est important : le template est copié à la racine du projet afin que
Netlify trouve `netlify.toml` et que les scripts soient disponibles sous
`scripts/`. La commande ne remplace jamais un fichier existant.

## Connexion initiale

Lancer `/netlify_init` depuis l'agent. La commande guide la connexion,
l'obtention du token et la liaison du dépôt sans exposer le secret dans la
conversation.

`.env.netlify` et `.netlify/` doivent être ignorés par Git. Ajouter ces deux
lignes au `.gitignore` du projet si elles n'y figurent pas déjà.

## Déploiement manuel

```powershell
.\scripts\netlify_deploy.ps1 -Production
```

Le script exécute la configuration de `netlify.toml`, puis publie en
production. Sans `-Production`, il crée un déploiement brouillon et affiche
l'URL de prévisualisation.

## API Netlify complète

Le client ne limite pas les routes : il transmet une méthode et un chemin à
l'API REST publique v1. Les droits sont ceux du token Netlify.

```powershell
# Lister les projets accessibles
python scripts/netlify_api.py --path /sites --paginate

# Lire un projet
python scripts/netlify_api.py --path /sites/$env:NETLIFY_SITE_ID

# Déclencher un build hook (URL complète autorisée)
python scripts/netlify_api.py --method POST --url "https://api.netlify.com/build_hooks/HOOK_ID"

# Appeler toute route v1 avec un corps JSON conservé dans un fichier
python scripts/netlify_api.py --method PATCH --path /sites/$env:NETLIFY_SITE_ID --data @payload.json
```

Pour connaître les routes, paramètres et permissions applicables, consulter la
documentation de l'API Netlify avant un appel modifiant des ressources.
