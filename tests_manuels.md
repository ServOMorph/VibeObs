# Tests manuels en attente

## /insert_template — destination par défaut ROBERTO/

Vérifier sur un projet cible réel (ex: `/insert_template <projet> overlay`
sans dossier de destination) que :
- le dossier `<projet_cible>/ROBERTO/` est bien créé s'il n'existait pas ;
- les fichiers du template atterrissent dedans et pas à la racine du projet ;
- un projet où `ROBERTO/` existe déjà et contient déjà un template ne casse
  rien (fusion correcte, pas d'écrasement).

À valider avant de considérer la convention déployée pour tous les templates
existants (`control_PC`, `discord_com`, `overlay`).

## rclone multicompte — backup SérénIATech_dev vers sereniatech_drive

`ClaudeCode/backup_drive.py` de `SérénIATech_dev` a été repointé de `googledrive:`
vers `sereniatech_drive` (compte sereniatech33@gmail.com). À exécuter dans une
session de ce projet :
- lancer `python ClaudeCode/backup_drive.py` (ou son `/close`) ;
- vérifier que les archives, le miroir et la DB atterrissent bien dans
  `sereniatech_drive:BackUps/BACKUPS-SerenIATech_dev/` ;
- vérifier que le contrôle quota lit `sereniatech_drive:` sans erreur ;
- confirmer qu'aucun nouvel objet n'apparaît côté compte rayonnetoi@gmail.com.

## rclone multicompte — vérifier les /close des projets partagés

Pour `Rayonne_Toi` et `Appli_TSA_SDI_TDAH` (partage assumé de `rayonne_toi_drive`) :
au prochain `/close` de chacun, vérifier via `rclone lsf rayonne_toi_drive:BackUps`
que le backup atterrit dans le bon sous-dossier de projet.

## chatgpt-orchestrateur — correctif vol de focus (`focus_fiable.ps1`)

Le correctif (activation avec nouvelles tentatives + contrôle du focus avant chaque
clic, dans `cliquer_fenetre`, `coller_et_envoyer`, `copier_reponse`, `defiler_fenetre`)
n'a été validé qu'en syntaxe. À exécuter, VS Code ayant le focus au lancement :
- lancer `cliquer_fenetre.ps1` sur une fenêtre Chrome ChatGPT : le clic doit atterrir
  dans Chrome, pas dans VS Code ;
- répéter 5 fois de suite, y compris avec une autre application au premier plan ;
- simuler un échec (fenêtre cible minimisée ou bloquée) : le script doit s'arrêter
  avec le code 2 et le message « Focus non obtenu », sans aucun clic ;
- contrôler qu'aucun effet parasite de la touche Alt (barre de menus Chrome activée) ne
  gêne le clic ou la saisie qui suit ;
- si validé : mettre à jour `roadmap_reprise_multicompte.md` (blocage Phase 3) et la
  section dédiée de `skills/chatgpt-orchestrateur/SKILL.md`.

## /start et /close — attribution par zone (SérénIATech_dev)

Commandes déployées par `/update` le 2026-10-14 (étapes `/close` 3-bis, 4, 13, 15 ; `/start` 4c).
À rejouer dans une nouvelle session ouverte sur `SérénIATech_dev`, un scénario à la fois (scénarios 1 `/start` racine et 2 `/start shorts` validés le 2026-10-27 en v5.23 : ligne de comptage des éléments déjà marqués, aucun faux « non vérifiable » ; charte puis signaux de SHORTS affichés, aucun candidat 4c) :
- `/close` racine après un travail dans SHORTS : écart zone/travail signalé, éléments dans le signal de SHORTS (ou `[à transférer vers shorts]` si `agent_role.md` l'interdit), rien recopié à la racine ;
- session touchant plusieurs zones : seules les actions et points d'attention des autres zones sont modifiés, jamais leur « Dernière session » ;
- action déjà présente dans sa zone : mise à jour, aucun doublon ;
- signal ignoré par Git : non annoncé comme commité, signalé au bilan.
Observations du 2026-10-27 (`/close` racine sans travail dans SHORTS, v5.22/v5.23, commit `ca0b2c0`) : scénario 3 non couvert (aucun travail réalisé dans SHORTS) ; signals suivis par Git contrôlés (cas « ignoré » non testé) ; session précédente archivée ; 3 actions reportées, backlog non exercé. Divergences à trancher : (a) le constat « `contexte.md` de SHORTS obsolète » est écrit dans la synthèse de la racine mais pas dans le `signals.md` de SHORTS (zone propriétaire, écriture permise par sa charte) ; (b) étape 9 : bump de `CHANGELOG.md` (v1.111) pour une session sans modification de travail.
Transmettre chaque divergence au kit (scénario, étape, attendu, observé).

## /close v5.22 — points non exercés

Le jeu d'essai sur projet jetable (2026-10-27) a validé le tri, le plafond, la péremption, la promotion, le retrait, la ligne de renvoi, le non-chargement par `/start` et le cas `backlog.md` ignoré par Git. Restent à exercer dans un projet réel :
- `backlog.md` créé à la première entrée (aucun fichier vide au préalable) ;
- backlog vidé : fichier et ligne de renvoi supprimés ;
- `check_kit.py` présent et passant avant le commit d'un `/close` qui a écrit dans le backlog.
Transmettre chaque divergence au kit (scénario, étape, attendu, observé).

## /telephone par défaut — init et update

Jamais exercé en réel :
- `/init_projet <projet jetable>` : `.claude/commands/telephone.md` est présent dans la cible et commité avec `.claude/` ;
- `/update <projet existant sans telephone.md>` : le fichier est copié, listé dans le message final, et le contrôle d'identité de l'étape 10 passe ;
- `/update` d'un projet où `telephone.md` a été personnalisé : l'écart est signalé, pas silencieux.

## /close — push conditionnel (étape 14)

Jamais exercé en réel :
- projet sans remote (`git remote` vide) : aucun `git push` exécuté, rien mentionné au bilan ;
- projet dont le bloc `SPECIFICITES PROJET` de `close.md` ou `.claude/memory.md` interdit le push (ex. `SérénIATech_dev`) : aucun `git push`, rien proposé ni mentionné ;
- projet avec remote : `git push` exécuté ; en cas d'échec, erreur affichée telle quelle au bilan ;
- dans les trois cas : le hook « Fin » (14-ter) s'exécute après le commit.
Transmettre chaque divergence au kit (scénario, étape, attendu, observé).

## Journal de session (v5.44) — cycle réel dans un projet suivi

Dans un projet ayant le journal (ex: `creation_3d`, `XMage`) :
- vérifier que `_contexte/journal_session.md` reçoit des lignes au format `AAAA-MM-JJ HH:MM | décision|fichier|action | texte` pendant la session et après un `/compact` ;
- lancer `/close` : chaque ligne est reportée dans la synthèse, `signals.md` ou `contexte.md`, puis le journal est vidé après le commit ;
- `git status` ne montre ni le journal ni de résidu lié à son vidage ;
- rouvrir avec `/start` après un `/close` sauté : le journal non vide s'affiche sous « Journal non intégré ».

## /create_projet et /init_projet v6.0 — alias par défaut, plus de question stack

Au prochain `/create_projet <nom>` réel :
- l'alias de zone est proposé avec `<nom>` comme valeur par défaut ; une réponse vide ou confirmant retient `<nom>` ;
- aucune question sur la stack technique n'est posée ;
- `_contexte/contexte.md` du projet créé contient « Non définie à la création : à compléter au fil du projet. » dans la section Stack, sans `{{` résiduel.
Transmettre toute divergence au kit.

## Garde VRAM, alerte compact, console distante (v6.4)

Vérifier dans une session réelle du kit que :
- une commande GPU (ex. appel Ollama) est bloquée sans jeton, puis passe après `vram_lock.py acquire vibeobs --wait` ;
- l'alerte `/compact` s'affiche en début de réponse au-delà de 600 000 tokens de contexte ;
- `python scripts/console_distante.py lire <pid>` restitue l'écran d'une session `claude` et `touche <pid> ENTREE` répond à une validation, PC verrouillé.

## Registre des artifacts (v6.5)

Vérifier dans un projet mis à jour en v6.5 et ayant un artifact que :
- `/close` pose une question en un clic sur chaque artifact créé ou modifié et absent du registre ;
- « Oui » inscrit une ligne `nom | lien | rôle | source | MAJ` dans `_contexte/artifacts.md`, « Non » n'écrit rien ;
- un artifact déjà inscrit est mis à jour sans question ;
- `/start` charge le registre au démarrage suivant.

## Hook PreCompact (`scripts/hook_precompact.py`)

Vérifier dans une session réelle du kit que :
- un `/compact` manuel ajoute à `_contexte/journal_session.md` la ligne `| action | compactage manual : relire ce journal` ;
- le résumé produit conserve la tâche en cours, les fichiers modifiés non commités et la prochaine étape ;
- un compactage automatique écrit la ligne avec `auto` ;
- le compactage n'échoue jamais à cause du hook.

## Relais téléphone (`/relais_telephone`, `/telephone roberto`, v6.9)

Vérifier en conditions réelles que :
- VertIA_v3 a bien appliqué `/telephone off` après « fin du relais » (non confirmé par la session le 2026-11-17) ;
- une écoute de plus de 30 minutes est relancée à son expiration, sans écoute en double (verrou) ;
- une seconde session en mode `/telephone roberto` (autre que VertIA_v3) envoie sa question à VibeObs et reçoit la réponse validée ;
- le relais tient hors du PC (téléphone sur réseau mobile, tunnel ouvert par l'utilisateur) ;
- `/close` prochain d'une session en mode roberto ne laisse pas d'écoute ni de verrou résiduels.
