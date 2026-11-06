# Délégation réutilisable — 1.0.0

> Adaptation VibeObs : les jetons du préambule et de `install.ps1` s'écrivent `[[PROJET]]`, `[[FICHIERS_REGLES]]`,
> `[[INTERDITS]]` et `[[VERIFICATIONS]]` (et non des accolades doubles) pour que `/insert_template` n'en bloque pas l'insertion.
> Source d'origine : `D:\ServOMorph\CreaZik_V3\_templates\delegation` (v1.0.0). Cette copie est celle du kit ;
> en cas de mise à jour de la source, reporter la même substitution.

Ce kit installe deux lanceurs dans un projet. Ils assemblent un préambule permanent et un brief autonome, conservent les traces dans `_codex/runs/` et affichent uniquement le rapport final lors d'une exécution réelle.

## Prérequis et installation

Windows, PowerShell 5.1, application Codex ou Codex CLI accessible dans le PATH ; OpenCode accessible dans le PATH pour son lanceur. Installer et authentifier les exécutants séparément. Le modèle OpenCode par défaut demandé est `opencode/deepseek-v4.1-flash-free` : disponibilité et gratuité à vérifier auprès du fournisseur avant usage ; aucun appel réel n'est effectué par l'installation.

Copier ce dossier dans un emplacement de votre choix, puis :

```powershell
.\install.ps1 -Projet 'D:\Projets\MonProjet' -NomProjet 'MonProjet' `
  -FichiersRegles 'Lire AGENTS.md et les règles applicables du projet.' `
  -Interdits 'Aucun déploiement ni redémarrage de service.' `
  -Verifications 'JS : node --check <fichier> ; Python : python -m py_compile <fichier>.'
```

L'installation crée `_codex/run_codex.ps1`, `_codex/run_opencode.ps1`, `_codex/PREAMBULE.md`, la configuration OpenCode à la racine et l'exclusion `_codex/runs/` dans `.gitignore`. Elle conserve tous les fichiers existants et n'ajoute pas de doublon à l'exclusion. Une réinstallation ne met donc pas à jour les scripts ou les paramètres du préambule : comparer et remplacer manuellement les fichiers concernés si nécessaire. Une configuration OpenCode existante est toujours conservée : relire ses permissions avant usage.

## Usage

Depuis le projet cible, copier `BRIEF_TEMPLATE.md` dans un fichier de travail et remplir toutes ses sections. Les chemins des fichiers du brief sont relatifs à la racine du projet.

```powershell
.\_codex\run_codex.ps1 -Brief '.\brief_tache.md' -Name 'relecture' -Sandbox read-only -DryRun
.\_codex\run_codex.ps1 -Brief '.\brief_tache.md' -Name 'correction' -Sandbox workspace-write
.\_codex\run_opencode.ps1 -Brief '.\brief_tache.md' -Name 'simple' -DryRun
.\_codex\run_opencode.ps1 -Brief 'Objectif et contexte autonome, fichiers autorisés, contrôles...' -Name 'simple' -Model 'opencode/deepseek-v4.1-flash-free'
```

`-Brief` accepte un texte ou un chemin existant (résolu depuis le dossier courant). `-Name` accepte lettres ASCII, chiffres, tirets et underscores, avec une lettre ou un chiffre initial. `-Root` désigne un projet existant ; par défaut, c'est le parent du dossier où sont installés les scripts. Le préambule reste celui placé à côté du lanceur. Les traces vont dans `<Root>/_codex/runs/<horodatage>_<nom>_<identifiant>/` (préfixe `oc_` pour OpenCode). L'identifiant évite les collisions.

`-DryRun` prépare uniquement `brief.md` puis affiche la commande PowerShell échappée, sans appeler l'exécutant, même s'il n'est pas installé. Une exécution réelle crée aussi `log.txt` et `rapport.md`. Le lanceur relaie le code de sortie de l'exécutant ; un rapport absent est une erreur. Examiner également STATUT et OUVERT : un code de processus nul ne prouve pas la réussite métier. Le journal n'est pas affiché automatiquement.

## Choisir l'exécutant

| Exécutant | Usage |
| --- | --- |
| Codex | Relecture avec `-Sandbox read-only`, code délicat avec périmètre précis. |
| OpenCode gratuit | Tâches simples et bien délimitées ; brief entièrement autonome. |
| Agents Claude | Travail nécessitant un navigateur ou un contexte long. |

## Sécurité et économie

- Définir explicitement les fichiers modifiables ; aucun commit ni push par l'exécutant. Ne jamais lancer deux exécutants sur les mêmes fichiers en même temps.
- Privilégier les permissions restreintes et le mode lecture seule pour les revues. Le périmètre du brief est une consigne, pas une barrière technique par fichier ; `workspace-write` et `edit: allow` autorisent davantage que la liste du brief. Relire les différences avant intégration.
- Ne transmettre aucun secret ni donnée sensible à un modèle cloud : vérifier le brief, les pièces jointes et les fichiers accessibles. Les permissions ne remplacent pas cette sélection préalable.
- La configuration OpenCode interdit les outils web et l'accès hors dépôt, autorise l'édition et refuse bash par défaut. Exceptions listées dans le JSON sans commentaire : `node --check *`, `python -m py_compile *`, `python -m pytest *`, `git status*`, `git diff*`. Adapter cette liste au projet ; les tests exécutent du code du dépôt, les motifs génériques ne constituent pas une isolation système et des permissions globales ou outils supplémentaires doivent être examinés.
- Brief court et autonome ; rapport de 15 lignes maximum. Ne lire que le rapport en fonctionnement normal ; consulter le journal seulement pour diagnostiquer un problème. Les traces locales peuvent contenir du code : ne pas les publier.

## Pièges rencontrés

Retours du dépôt d'origine, à revalider si les versions changent :

- Codex `exec` a bloqué avec un prompt envoyé par tube stdin. Le lanceur passe un court message désignant le brief relatif, avec `-o <rapport>`, `-C <racine>` et `--sandbox read-only|workspace-write`.
- Le Codex npm ancien (0.154) a refusé un modèle configuré par l'abonnement (« model not supported with a ChatGPT account »), alors que le binaire de l'application fonctionnait. Découverte prioritaire : `$env:LOCALAPPDATA\OpenAI\Codex\bin\*\codex.exe`, fichier le plus récent par date de modification, puis `codex` du PATH ; erreur explicite sinon.
- OpenCode attend le message positionnel avant les options : `opencode run "<message>" -m <modèle> --dir <racine> -f <fichier>`. Sinon `-f` peut absorber le message. `--auto` peut être refusé par les garde-fous de l'agent appelant : utiliser la configuration de permissions.
- Avec ces restrictions, OpenCode ne lit pas hors dépôt et bash reste limité à la liste autorisée. Fournir tout le contexte dans le brief, sans dépendance à une conversation antérieure.
- PowerShell 5.1 transforme stderr d'un programme natif en erreurs : l'appel est encadré par `ErrorActionPreference = 'Continue'`, puis la préférence est restaurée. Les fichiers générés sont écrits en UTF-8 sans BOM ; les sources PowerShell utilisent uniquement des caractères ASCII pour éviter l'interprétation ANSI de PowerShell 5.1.
- Certains harnais protègent les dossiers `runs/` contre la suppression. Les exclure de git plutôt que les nettoyer automatiquement.

## Contrôles locaux sans modèle

Le script `tests/verify.ps1` analyse la syntaxe, installe dans un dossier temporaire neuf, répète l'installation en contrôlant les contenus existants, teste les deux `-DryRun` et tente de nettoyer uniquement ce dossier temporaire. Il n'appelle ni Codex ni OpenCode.

```powershell
powershell -NoProfile -File .\tests\verify.ps1
```
