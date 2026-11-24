# Archive des sessions — VibeObs
<!-- Ce fichier contient les anciennes sessions de signals.md, archivées automatiquement par /close -->
<!-- Format: chaque session est séparée par une ligne vide -->

---

# Session du 2026-09-13

## Décisions prises
- `/create_projet` place `0. Aucun template` en tête de la liste de sélection (jamais en dernier) pour éviter la renumérotation Markdown.

## Livrables produits ou modifiés
- `.claude/commands/create_projet.md` : correctif de numérotation de la liste des templates.
- Nouveau projet `VertIA_v2` (`D:\ServOMorph\VertIA_v2`) : Git local + dépôt GitHub public (https://github.com/ServOMorph/VertIA_v2), protocole vibecoding initialisé (zone `VertIA`), aucun template inséré.
- `DEPLOYMENTS.md` : ligne ajoutée pour `VertIA_v2`.

## Hypothèses validées / invalidées
- EN ATTENTE : vérification en conditions réelles de la nouvelle numérotation lors d'un prochain `/create_projet`.

## Prochaine étape exacte
Rejouer `/create_projet` pour confirmer l'affichage correct de la liste des templates.

## Question bloquante pour la session suivante
Aucune.

---

# Session du 2026-09-04

## Décisions prises
- Les fichiers `.claude/CLAUDE.md`, `AGENTS.md` et `GEMINI.md` doivent être strictement identiques lorsqu'ils coexistent dans un projet.

## Livrables produits ou modifiés
- Skill local `harmonize-agent-instructions` : créé et validé ; il analyse les écarts puis attend le choix explicite d'une source canonique.
- Projets pilotes : fichiers d'instructions harmonisés depuis leur `.claude/CLAUDE.md` respectif.

## Hypothèses validées / invalidées
- VALIDE : une vérification par hash SHA-256 garantit l'identité binaire des trois fichiers.
- EN ATTENTE : les chemins de projets futurs peuvent employer des variantes de nommage ; les résoudre avant toute écriture.

## Prochaine étape exacte
Reprendre l'action P1 de validation des cycles `start`/`close` dans les worktrees `ONBOARD` et `RETOURS`.

## Question bloquante pour la session suivante
Aucune.

---

# Session du 2026-09-04

## Décisions prises
- Le kit et le dépôt GitHub sont renommés VibeObs ; le remote local est `origin` vers `ServOMorph/VibeObs`.
- `/create_projet_public` est remplacée par `/create_projet` (Git local ou GitHub public/privé).
- Les backups rclone sont distribués comme template avec un remote explicite ; le template Netlify est ajouté.

## Livrables produits ou modifiés
- Documentation, contexte, zones et scripts de backup : références renommées vers VibeObs.
- `.claude/commands/create_projet.md`, `templates/rclone_backup/` et `templates/netlify/` : création ou mise à jour prêtes à versionner.

## Hypothèses validées / invalidées
- VALIDE : `check_kit.py` et `check_docs.py` passent après synchronisation documentaire.
- EN ATTENTE : test Discord réel du correctif de file.

## Prochaine étape exacte
Autoriser le lancement temporaire du bot, envoyer deux notifications réelles, puis vérifier `queue.json` à `idle`.

## Question bloquante pour la session suivante
Autoriser le lancement temporaire du bot Discord pour ce test réel ?

# Session du 2026-08-20

## Décisions prises
- `MASCOTTE/` (zone-agent extraite par l'utilisateur en projet standalone) supprimée du kit ; références retirées de `templates/roberto/.claude/zones.md` et `README.md`. `UI_WEB/mascotte/` conservé (intégration indépendante).
- `AUTOMATISATIONS/` et `com_telephone/` déplacés hors du kit vers `D:\ServOMorph\Roberto` (projet standalone, nouveau repo git).
- Process verrouillant les fichiers arrêtés avec autorisation explicite pour débloquer les déplacements (watcher `run.py --watch`, 3 process com_telephone, 2x `node server.js`).

## Livrables produits ou modifiés
- `templates/roberto/MASCOTTE/` : supprimé.
- `templates/roberto/AUTOMATISATIONS/`, `com_telephone/` : supprimés du kit (déplacés).
- `D:\ServOMorph\Roberto\AUTOMATISATIONS\`, `com_telephone\` : créés, `.gitignore` ajouté (`__pycache__/`).
- Commit kit `d81f96a` (retrait MASCOTTE + extraction), push OK. Commit `Roberto` `b802f4b`, premier push OK (branche `main` créée sur le remote).

## Hypothèses validées / invalidées
- INVALIDE : déplacement direct des dossiers sans arrêt préalable des process qui les servaient → échecs silencieux (`Device or resource busy`, `Permission denied`) sur `mv`/`Move-Item`.
- VALIDE : tous les fichiers effacés par erreur (`rm -rf` intermédiaire sur une destination partiellement peuplée) étaient récupérables — tout était tracké en git côté kit, restauré via `git checkout HEAD`.

## Prochaine étape exacte
Relancer manuellement depuis `D:\ServOMorph\Roberto` les process arrêtés si besoin (UI workflow quotidien, 3 process com_telephone).

## Question bloquante pour la session suivante
Aucune.

---

# Session du 2026-08-19

## Décisions prises
- UI vocale enrichie : état "réflexion" (cercle orange, distinct de l'écoute bleue et de la réponse verte), bouton pause micro (suspendre la capture sans quitter l'écran vocal, ex. pour parler à quelqu'un d'autre).
- Pilotage des 3 serveurs (Node/STT/TTS) centralisé dans un script unique (`com_manager.py`) + commande Claude Code associée (`com_manager.md`), qui active aussi automatiquement le watcher `messages.log` au démarrage.

## Livrables produits ou modifiés
- `voice-code-bridge/mobile/index.html`, `app.js` : état "thinking" orange, bouton pause micro, reset des classes CSS à l'ouverture de l'écran vocal.
- `com_telephone/_commands/com_manager.py` : nouveau — start/stop/restart/status des 3 process. Bug trouvé et corrigé : `taskkill` nécessite `/T` (le lanceur `py -3.11` spawn un processus enfant distinct, sinon orphelin après `stop`).
- `com_telephone/_commands/com_manager.md` : nouveau, commande Claude Code (inclut l'activation/arrêt du `Monitor` sur `messages.log`).
- `com_telephone/README.md` : nouveau, vue d'ensemble du dossier.

## Hypothèses validées / invalidées
- VALIDE : centraliser le lancement des 3 process robustifie le prototype (bug `taskkill` trouvé en le testant réellement, pas en théorie).
- EN ATTENTE : boucle de "enregistrement démarré" observée se répétant toutes les 2-7s sans transcription ni erreur entre les occurrences (déclenchement VAD suspect) — signalée à l'utilisateur, aucune réponse reçue avant la fin de session.

## Prochaine étape exacte
Diagnostiquer la boucle de déclenchement micro rapproché (bruit ambiant ? seuil `SPEECH_THRESHOLD` trop bas ?). Authentification de l'UI toujours à faire.

## Question bloquante pour la session suivante
La boucle de re-déclenchement rapide du micro (constatée, cause non identifiée) empêche-t-elle une utilisation normale, ou n'était-ce qu'un test involontaire ?

---

# Session du 2026-08-18 (roadmap multi-compte + délégation réelle ROBERTO)

## Décisions prises
- Roadmap `roadmap_reprise_multicompte.md` Phase 1 (suivi tokens) et Phase 2 (rotation de compte Google) terminées et commitées ; conception évoluée en `comptes_usage.json`/`compte_actif.json` (statut actif/inactif/epuise) plutôt que le simple `comptes_utilises.json` prévu au départ.
- Risque de vol de focus `SetForegroundWindow` découvert et documenté (`SKILL.md`) comme préalable bloquant à la Phase 3.
- Pivot décidé par l'utilisateur : delegation maximale du code à ChatGPT sur la vraie mission ROBERTO (`Appli_TSA_SDI_TDAH`) plutôt que poursuivre mécaniquement la roadmap — test explicite d'autonomie.
- Test Markdown vs JSON sur les échanges avec ChatGPT : les deux fonctionnent, JSON pas plus économe sur du contenu plat (voir `roadmap_reprise_multicompte.md` Phase 5).

## Livrables produits ou modifiés
- `skills/chatgpt-orchestrateur/scripts/{maj_usage,definir_compte_actif,maj_compte_usage,ouvrir_nouveau_compte}.ps1`, `comptes_google.json` : créés et testés
- `skills/chatgpt-orchestrateur/SKILL.md` : sections suivi tokens + risque de vol de focus ajoutées
- `roadmap_reprise_multicompte.md` : Phases 1/2 FAIT, blocage focus ajouté en tête de Phase 3
- `D:\ServOMorph\Appli_TSA_SDI_TDAH\ROBERTO\` (hors dépôt kit) : Flux A de la state machine complet et testé (10 étapes, 29 tests), délégué à ChatGPT

## Hypothèses validées / invalidées
- VALIDE : déléguer l'écriture de code à ChatGPT (audit, script, tests) puis se contenter d'appliquer/vérifier côté Claude Code fonctionne bien en conditions réelles sur 10 itérations consécutives.
- VALIDE : la vérification systématique par capture après un collage évite les échecs silencieux (piège de calibration déjà documenté, reconfirmé sur un envoi long).
- INVALIDE : `SetForegroundWindow` + coordonnées de clic suffisent à cibler fiablement une fenêtre précise — un vol de focus silencieux est possible.

## Prochaine étape exacte
Résoudre ou contourner le vol de focus avant la Phase 3 de `roadmap_reprise_multicompte.md`. Sur ROBERTO : reprendre l'étape 11 (CLI `process_manual_test.py`), interrompue par l'utilisateur avant envoi, rien n'a été perdu.

## Question bloquante pour la session suivante
Aucune.

---

# Session du 2026-08-13 (init Capafy_AI + backup Google Drive pour projets sans git)

## Décisions prises
- `/init_projet` exécuté sur `D:\ServOMorph\Capafy_AI` (zone `capafy_ai`, première zone, ni `AGENTS.md` ni `GEMINI.md`). Mis sous git par l'utilisateur après l'init ; commit initial + push effectués a posteriori (`.claude/scheduled_tasks.lock` exclu du commit, verrou runtime non pertinent en git).
- Nouvelle fonctionnalité dans `/init_projet` : si le projet cible n'est pas sous git, Q4bis propose d'automatiser un backup miroir du dossier vers Google Drive à chaque `/close` (nouveau script `backup_project.py`, `rclone sync`, exclusions standard) — injecté dans le bloc "Spécificités projet" du `close.md` du projet cible si accepté.
- `/doc_sync` exécuté : miroir `templates/.claude/commands/init_projet.md` répercuté (était en retard), `README.md`/`CHANGELOG.md`/`Protocole_start_close_context.md` alignés. Kit v3.17.

## Livrables produits ou modifiés
- `templates/backup_project.py` (nouveau) : script de sauvegarde miroir via rclone.
- `.claude/commands/init_projet.md`, `templates/.claude/commands/init_projet.md` : Q4bis + étape 4bis (injection close.md) + copie conditionnelle.
- `README.md`, `CHANGELOG.md`, `Protocole_start_close_context.md` : synchronisés (v3.17).
- Hors dépôt kit (`Capafy_AI`) : init complet (`.claude/`, `_contexte/`, `ollama_call.py`, `_docs/`), commit initial + push vers `github.com/ServOMorph/Capafy_AI`.

## Hypothèses validées / invalidées
- EN ATTENTE : Q4bis/`backup_project.py` n'a jamais tourné en conditions réelles depuis l'ajout.

## Prochaine étape exacte
Tester Q4bis en conditions réelles sur un futur `/init_projet` avec projet sans git.

## Question bloquante pour la session suivante
Aucune



---

# Session du 2026-08-13 (commande create_com_agents + pilote Roberto2)

## Décisions prises
- `create_com_agents` (nouvelle commande kit) conçue et installée en conditions réelles sur Roberto2 : mécanisme en étoile agent↔orchestrateur (`statut.md` pull écrasé, `messages.md` push purgé), `start.md`/`close.md` de Roberto2 modifiés.
- Bug détecté en conditions réelles : l'étape conditionnelle d'agrégation `statut.md` (4c, placée après la synthèse narrative de `signals.md`) a été sautée au premier `/start roberto2`. Corrigée : déplacée en `2d`, adjacente à `2b`/`2c`, avant tout paragraphe narratif — appliquée à la fois dans Roberto2 et dans `create_com_agents.md` (kit), avec la raison documentée pour éviter la régression sur de futures installations.

## Livrables produits ou modifiés
- `.claude/commands/create_com_agents.md` (nouveau, kit) : commande + correctif de placement.
- `roadmap_com_agents.md` (nouveau, kit).
- Hors dépôt kit (Roberto2) : `.claude/commands/start.md`, `.claude/commands/close.md` modifiés.

## Hypothèses validées / invalidées
- INVALIDE : une étape conditionnelle placée après un paragraphe de synthèse narrative est fiable à l'exécution — sautée lors du premier test réel.
- EN ATTENTE : le correctif (2d) n'a pas encore été retesté en conditions réelles ; `/close mascotte` réel et test `messages.md` pas encore faits.

## Prochaine étape exacte
Sur Roberto2 : relancer `/start roberto2` pour valider le correctif 2d, puis `/close mascotte` réel, puis test écriture/lecture `messages.md`.

## Question bloquante pour la session suivante
Aucune



---

# Session du 2026-08-12 (agent MASCOTTE dans Roberto2)

## Décisions prises
- Agent MASCOTTE créé dans Roberto2 via `/create_agent` : affichage visuel de la mascotte animée dans l'UI web (élément qui bouge pendant un chargement), migration `roadmap_migration_ui_web.md` Phase 2. Rôle précisé après lecture du dossier (`_contexte/contexte.md`, `UI_WEB/`) — argument initial insuffisant seul.

## Livrables produits ou modifiés
- Hors dépôt kit (Roberto2) : `MASCOTTE/agent_role.md`, `MASCOTTE/_contexte/{signals,contexte}.md` créés, `.claude/zones.md` (ligne mascotte).
- `AGENTS_REGISTRY.md` (hors git) : entrée `mascotte` ajoutée.
- `ameliorations_create_agent.md` : entrée 2026-08-12 (agent mascotte, Roberto2).

## Hypothèses validées / invalidées
- EN ATTENTE : l'agent n'a jamais tourné (`/start mascotte` jamais lancé), aucun livrable produit par l'agent lui-même.

## Prochaine étape exacte
Sur Roberto2 : lancer `/start mascotte` pour démarrer la première session de travail sur l'animation.

## Question bloquante pour la session suivante
Aucune



---

# Session du 2026-08-12 (conception système de communication kit → zone)

## Décisions prises
- Système de communication kit → zone conçu en 2 niveaux : `urgent.md` (vérifié via une instruction `CLAUDE.md`, avant toute action significative — écriture, modif, commit) et `messages.md` (lu à `/start`, priorité avant `signals.md`). Format compact commun : `[AAAA-MM-JJ] <message>`.
- Sens unique kit → projet cible, distinct de l'expérimentation "synthèse agents" (jeu_zombies) qui va dans l'autre sens.
- Déploiement en pilote isolé sur Roberto2 (bloc "Spécificités projet") avant toute modification des templates du kit — décision explicite de l'utilisateur, propagation différée à la validation.

## Livrables produits ou modifiés
- `roadmap_messages_zones.md` (nouveau, racine du kit) : cadrage (2 niveaux, format, mécanisme, risque de version non à jour) + 3 phases (pilote Roberto2, validation réelle, déploiement kit).
- `_contexte/contexte.md`, `_contexte/archive_decisions.md` : purge des décisions structurantes (>10 entrées), 5 entrées archivées.

## Hypothèses validées / invalidées
- EN ATTENTE : aucune implémentation faite (Phase 1 non commencée), le mécanisme n'a jamais tourné.

## Prochaine étape exacte
Implémenter Phase 1 dans Roberto2 : blocs "Spécificités projet" de `D:\ServOMorph\Roberto2\.claude\commands\start.md` (lecture/purge `messages.md`) et `.claude\CLAUDE.md` (vérification `urgent.md`), test à blanc.

## Question bloquante pour la session suivante
Aucune



---

# Session du 2026-08-12 (propagation create_memory.md — clôture a posteriori après /clear accidentel)

## Décisions prises
- Gap corrigé : `create_memory.md` manquait à l'étape 3 d'`init_projet.md` (fichier jamais propagé aux nouveaux projets).
- Déploiement massif effectué via nouveau script `deploy_create_memory.py` (lecture de `DEPLOYMENTS.md`, copie si absent) plutôt que manuellement — pratique actée pour tout déploiement massif futur.
- Session clôturée a posteriori : l'utilisateur a fait `/clear` avant `/close`, conversation perdue. Reconstruction de la synthèse à partir du commit `57a3522` et de l'état réel des fichiers/dépôts, sans les détails fins de la conversation d'origine.

## Livrables produits ou modifiés
- `.claude/commands/init_projet.md` : ligne ajoutée à l'étape 3.
- `deploy_create_memory.py` (nouveau, racine du kit).
- `create_memory.md` propagé et committé dans les 22 projets réels de `DEPLOYMENTS.md` (18 déjà committés par la session d'origine ; 4 recommis lors de cette clôture — `site_internet_Sereniatech_V2`, `jeu_espace`, `Participation_GitHub`, `Roberto2` — où le fichier était présent sur disque mais non commité dans leur dépôt respectif).
- 2 projets sans dépôt git (`Moulin du Sud`, `Nettoyage_PC`) : fichier présent sur disque, commit non applicable.
- `Open_Code_Apprentissage` : toujours chemin introuvable (gap déjà connu, voir action ouverte `DEPLOYMENTS.md`).

## Hypothèses validées / invalidées
- INVALIDE : l'entrée `signals.md` écrite par la session d'origine décrivait un déploiement "en cours" (test sur Roberto2) alors que le commit montrait un déploiement déjà terminé sur 25 projets — incohérence corrigée par cette clôture.

## Prochaine étape exacte
Aucune sur ce sujet — propagation `create_memory.md` considérée close. Par ailleurs, étape 12bis de `/close` (sauvegarde `DEPLOYMENTS.md` vers Google Drive) validée en conditions réelles lors de cette clôture : confirmation demandée, upload déclenché, fichier `DEPLOYMENTS_20260812_115450.md` déposé dans `googledrive:BackUps/claude-vibecoding-kit/`. Action ouverte correspondante close.

## Question bloquante pour la session suivante
Aucune



---

# Session du 2026-08-12 (sauvegarde automatique DEPLOYMENTS.md vers Google Drive)

## Décisions prises
- Système de sauvegarde automatique de `DEPLOYMENTS.md` vers Google Drive créé, intégré à `/close` du kit (étape 12bis, optionnelle, confirmation utilisateur requise).
- Réutilisation du pattern rclone existant (SérénIATech_dev) plutôt que réécriture complète.
- Destination fixée sur `googledrive:BackUps/claude-vibecoding-kit/` (compte Google inchangé, confirmé par l'utilisateur).

## Livrables produits ou modifiés
- `backup_file.py` (nouveau) : script générique de sauvegarde horodatée via rclone (`copyto`).
- `.claude/commands/close.md` : étape 12bis ajoutée, corruption "e" isolé (ligne 122) corrigée, `allowed-tools` étendu.

## Hypothèses validées / invalidées
- VALIDE : `rclone copyto` nécessaire au lieu de `rclone copy` — `copy` ignorait le nom horodaté et écrasait avec le nom du fichier source (bug détecté et corrigé en session).
- VALIDE : rclone déjà configuré et authentifié avec le compte Google actuel, aucune reconfiguration nécessaire.

## Prochaine étape exacte
Observer le comportement de l'étape 12bis lors des prochains `/close` réels du kit ; envisager une rotation si le dossier grossit.

## Question bloquante pour la session suivante
Aucune



---

# Session du 2026-08-11 (commande locale /create_agent pour jeu_espace)

## Décisions prises
- Nouvelle commande locale `/create_agent` créée dans `jeu_espace` (projet externe) : permet à l'orchestrateur (zone racine) de créer lui-même des agents dans son propre projet, sans passer par le kit. Copie autonome (templates embarqués localement), inspirée de `/create_agent` du kit mais adaptée : pas d'argument chemin projet cible, pas d'écriture dans les fichiers de bookkeeping du kit (`AGENTS_REGISTRY.md`, `ameliorations_create_agent.md`), pas de phase `[AUDIT]`.
- Portée limitée à un test isolé sur `jeu_espace` — aucun template du kit modifié, propagation à décider après retour d'expérience.
- Rappel de validation à échéance ~2026-08-25 ajouté aux actions ouvertes du kit, sur demande explicite.

## Livrables produits ou modifiés
- Hors dépôt kit (`jeu_espace`) : `.claude/commands/create_agent.md`, `.claude/templates/agent_role_TEMPLATE.md`, `.claude/templates/_contexte/signals.md`, `.claude/templates/_contexte/contexte.md` créés.
- `_contexte/signals.md` (kit) : action de rappel de validation ajoutée.

## Hypothèses validées / invalidées
- EN ATTENTE : la commande n'a jamais tourné en conditions réelles — aucun agent créé via ce flux à ce stade.

## Prochaine étape exacte
Lancer `/create_agent <dossier> [rôle]` réellement depuis `jeu_espace` pour valider le flux ; trancher garder/écarter/propager au kit d'ici ~2026-08-25.

## Question bloquante pour la session suivante
Aucune.



---

# Session du 2026-08-10 (agent review + expérimentation synthèse agents)

## Décisions prises
- Agent `review` créé dans `jeu_zombies` via `/create_agent` (rôle : revue de code continue, périmètre par défaut).
- Feature "synthèse agents pour l'orchestrateur" conçue et implémentée en expérimentation, limitée à `jeu_zombies` : les zones-agents écrivent une synthèse à `/close` dans un fichier partagé, la zone racine la lit à `/start` et propose des actions. Propagation au kit explicitement différée à un bilan positif (Phase 3 de sa roadmap dédiée).

## Livrables produits ou modifiés
- `ameliorations_create_agent.md` : entrée agent `review` ajoutée.
- `AGENTS_REGISTRY.md` (hors git) : entrée `review` ajoutée.
- Hors dépôt kit (`jeu_zombies`) : `REVIEW/agent_role.md`, `REVIEW/_contexte/{signals,contexte}.md`, `_contexte/synthese_agents.md`, `roadmap_synthese_agents.md` créés ; `.claude/zones.md` (ligne review), `.claude/commands/close.md` (étape 7 + renumérotation), `.claude/commands/start.md` (étape 4c), `REVIEW/agent_role.md`, `DESIGN/agent_role.md` (exception de périmètre), `_contexte/signals.md` modifiés.

## Hypothèses validées / invalidées
- EN ATTENTE : la feature "synthèse agents" n'a pas encore tourné en conditions réelles (Phase 2 de `roadmap_synthese_agents.md`, jeu_zombies) — aucune validation empirique à ce stade.

## Prochaine étape exacte
Sur jeu_zombies : exécuter Phase 2 de `roadmap_synthese_agents.md` (`/close review`, `/close design`, `/start` racine réels). Sur le kit : décider la propagation après le bilan de Phase 3.

## Question bloquante pour la session suivante
Aucune.



---

# Session du 2026-08-10 (discussion code review dans les roadmaps, sans conclusion)

## Décisions prises
- Aucune décision actée. Discussion exploratoire sur l'ajout d'une phase de code review dans le modèle de roadmap, interrompue avant validation finale.

## Livrables produits ou modifiés
- Aucun (échange uniquement, aucun fichier de commande/template modifié).

## Hypothèses validées / invalidées
- INVALIDE (reconsidérée en séance) : ma proposition initiale de gate systématique en fin de phase — jugée trop coûteuse en tokens sur les phases triviales par l'utilisateur, remplacée par une proposition de seuil conditionnel.
- EN ATTENTE : validation utilisateur de "seuil conditionnel + tri des findings par sévérité" avant toute modification de `CLAUDE.md`.

## Prochaine étape exacte
Si validation : rédiger la modification de la section Roadmap dans `.claude/CLAUDE.md` et `templates/.claude/CLAUDE.md` (miroir), définissant le seuil de déclenchement et la règle de tri des findings.

## Question bloquante pour la session suivante
L'utilisateur valide-t-il "seuil conditionnel + tri par sévérité" pour la revue de code dans les roadmaps, ou souhaite-t-il une autre combinaison ?



---

# Session du 2026-08-08 (vérification et push réel des 18 dépôts en attente)

## Décisions prises
- Vérification effective (fetch + status) des 18 dépôts + le kit, au lieu de se fier à l'état daté du 2026-08-05 : seuls 5 (kit, VisioAide, crea_zik, Appli_TSA_SDI_TDAH, jeu_zombies) étaient déjà poussés. Les 13 restants avaient chacun 1 commit local en avance — poussés cette session sur demande explicite de l'utilisateur.
- `Lieux_Hybrides` confirmé sans upstream configuré : cohérent avec la décision antérieure de ne pas l'auto-configurer, action considérée close sans relance.

## Livrables produits ou modifiés
- 13 dépôts externes poussés vers leur remote : robert-ia, Jeu pour Nino, JeGeekUtile, TableauDeBord, IA-TSA, La Rev, IA_V7, jeux_vibecoder, AutoClaude, Projet_de_reve, site_internet_Sereniatech_V2, jeu_espace, Roberto.
- `_contexte/signals.md`, `_contexte/contexte.md` (kit) : mis à jour, action P1 close.

## Hypothèses validées / invalidées
- INVALIDE : l'hypothèse implicite que "commit local = probablement poussé depuis" — faux pour 13 des 18 dépôts, confirmée par vérification directe plutôt que par la mémoire de session antérieure.

## Prochaine étape exacte
Trancher le statut des branches non-main (`jeu_zombies`, `Appli_TSA_SDI_TDAH`) si besoin ; aucune urgence, action P2 existante inchangée.

## Question bloquante pour la session suivante
Aucune



---

# Session du 2026-08-05 (correctif étape push native sur 18 projets + corruption close.md kit)

## Décisions prises
- Bug confirmé : sur les 18 close.md où le push automatique avait été activé (15 propagés le 2026-08-04 + 3 zones test antérieures), l'instruction restait dans le bloc "Spécificités projet" au lieu d'être une étape native, contrairement au close.md du kit. Corrigé sur les 18 fichiers, chacun commité isolément (seul close.md stagé, pas les autres fichiers en attente propres à chaque projet).
- Corruption locale (non commitée, sans impact sur l'historique git) détectée dans `.claude/commands/close.md` du kit — étape 11 remplacée par un caractère isolé "é" — restaurée via `git checkout` avant toute autre action.

## Livrables produits ou modifiés
- 18 `close.md` externes corrigés et commités (push non fait, en attente confirmation) : robert-ia, Jeu pour Nino, Appli_TSA_SDI_TDAH, VisioAide, crea_zik, JeGeekUtile, TableauDeBord, IA-TSA, La Rev, IA_V7, jeux_vibecoder, AutoClaude, Projet_de_reve, jeu_zombies, site_internet_Sereniatech_V2, Lieux_Hybrides (Moulin du Sud), jeu_espace, Roberto.
- `.claude/commands/close.md` (kit) : corruption locale restaurée (aucun diff résiduel, rien à commiter dessus).
- `CHANGELOG.md`, `README.md` : bump v3.10.

## Hypothèses validées / invalidées
- VALIDE : les 18 fichiers partageaient exactement le même défaut, correction uniforme applicable sans cas particulier.
- À NOTER (ni validé ni invalidé) : `jeu_zombies` commité sur `feat/insertion-designs`, `Appli_TSA_SDI_TDAH` sur `v5.0` — branches courantes de ces dépôts, non `main`, non modifiées par la session mais à surveiller.

## Prochaine étape exacte
Pousser les 18 commits locaux si l'utilisateur confirme (action P1 ouverte) ; sinon les laisser en attente.

## Question bloquante pour la session suivante
Aucune



---

# Session du 2026-08-04 (décision garder + propagation git push à 15 projets)

## Décisions prises
- `git push` automatique après `/close` : décision "garder" actée (les 4 zones test ont bien poussé). Promu en étape native (12) du template et du `close.md` du kit, retrait de l'ancien hack "Spécificités projet".
- Propagation faite aux 15 projets déployés avec remote git (sur 17 : `SérénIATech_dev` sans remote, `Open_Code_Apprentissage` introuvable, exclus). Commit dans les 15, push dans 14 — `Lieux_Hybrides` laissé en commit local sur refus explicite de configurer l'upstream.

## Livrables produits ou modifiés
- `templates/.claude/commands/close.md`, `.claude/commands/close.md` (kit) : étape push native, renumérotation 12→13→14.
- 15 `close.md` externes modifiés + commités (`robert-ia`, `Jeu pour Nino`, `JeGeekUtile`, `TableauDeBord`, `IA-TSA`, `La Rev`, `IA_V7`, `jeux_vibecoder`, `AutoClaude`, `Projet_de_reve`, `jeu_zombies`, `site_internet_Sereniatech_V2`, `Moulin du Sud`/`Lieux_Hybrides`, `jeu_espace`, `Roberto`).
- `README.md`, `CHANGELOG.md` (v3.9) mis à jour.

## Hypothèses validées / invalidées
- VALIDE : le push automatique fonctionne en conditions réelles (4/4 zones test).
- INVALIDE (corrigée en session) : le script de propagation initial corrompait les accents insérés — bug de lecture d'encodage PowerShell, corrigé avant tout commit.

## Prochaine étape exacte
Configurer l'upstream de `Lieux_Hybrides` si le push y est souhaité (décision utilisateur en attente) ; vérifier au fil des prochains `/close` de chaque projet propagé que l'étape 12 fonctionne dans leur flux réel.

## Question bloquante pour la session suivante
Aucune



---

# Session du 2026-08-04 (propagation git push crea_zik + correctif doc_sync.md)

## Décisions prises
- `git push` automatique (étape 11bis) propagé à un 4ème projet, `crea_zik`, sur demande explicite utilisateur — même patron que les 3 zones test existantes (allowed-tools + étape complémentaire dans le bloc "Spécificités projet"). Décision garder/écarter toujours en attente.
- Corruption pré-existante corrigée dans `.claude/commands/doc_sync.md` (`a---` → `---` en tête de frontmatter) après confirmation utilisateur, plutôt que commitée telle quelle ou laissée en résidu.

## Livrables produits ou modifiés
- Hors dépôt kit : `D:\ServOMorph\crea_zik\.claude\commands\close.md` modifié (`allowed-tools` + étape 10bis git push).
- `.claude/commands/doc_sync.md` (kit) : frontmatter corrigé.
- `_contexte/signals.md`, `_contexte/contexte.md` : mis à jour.

## Hypothèses validées / invalidées
- EN ATTENTE : toujours aucune décision garder/écarter sur le push automatique — 4 zones en test désormais au lieu de 3.

## Prochaine étape exacte
Observer le résultat de ce `/close` (première exécution réelle de l'étape 11bis sur le kit) ; trancher garder/écarter d'ici quelques temps.

## Question bloquante pour la session suivante
Aucune



---

# Session du 2026-08-02 (test git push après /close)

## Décisions prises
- `git push` automatique après le commit de `/close` ajouté en test sur 3 zones : le kit lui-même, `Appli_TSA_SDI_TDAH`, `VisioAide` — décision utilisateur confirmée (push, pas pull) via question explicite.
- Ajout fait directement dans chaque `close.md` (bloc "Spécificités projet"), pas dans le template — la propagation reste à trancher après observation.

## Livrables produits ou modifiés
- `.claude/commands/close.md` (kit) : `allowed-tools` + étape 11bis (git push) ajoutés.
- `_contexte/signals.md` : action ouverte P2 ajoutée pour trancher garder/écarter/propager.
- Hors dépôt kit : `D:\ServOMorph\Appli_TSA_SDI_TDAH\.claude\commands\close.md`, `D:\ServOMorph\VisioAide\.claude\commands\close.md` modifiés à l'identique.

## Hypothèses validées / invalidées
- EN ATTENTE : ce `/close` est la première exécution réelle du `git push` (kit) — comportement à observer dans le bilan de fin de commande.

## Prochaine étape exacte
Observer les prochains `/close` sur les 3 zones test ; trancher garder/écarter d'ici quelques temps et, si retenu, propager au template + `/update` sur les projets avec remote git.

## Question bloquante pour la session suivante
Aucune



---

# Session du 2026-08-01 (workflow GEMINI.md + rattrapage Moulin du Sud)

## Décisions prises
- `/init_projet` et `/update` : ajout de la question de création de `GEMINI.md`, sur le même modèle qu'`AGENTS.md` (jamais automatique, jamais écrasé) — résout l'action P1 gap GEMINI.md.
- Analyse d'un `/close` réel sur `moulin_du_sud` (projet externe) : étape 7 (base de connaissances) validée en conditions réelles pour la première fois — première moitié de l'action P1 test réel `DOCUMENTATION/` close.
- Rattrapage de 3 commits sur le dépôt externe Moulin du Sud (résidus non commités de sessions antérieures) : lot `DOCUMENTATION/`, déplacement `Accueil Handicap` vers la racine (rename propre vérifié par diff avant commit), alignement protocole v3.3.
- `DEPLOYMENTS.md` (kit, hors git) : version Moulin du Sud corrigée v3.1 → v3.3, non commitée (fichier gitignored du kit).

## Livrables produits ou modifiés
- `templates/GEMINI.md` : nouveau template (calqué sur `templates/AGENTS.md`).
- `.claude/commands/init_projet.md`, `templates/.claude/commands/init_projet.md` : Q8 + copie conditionnelle `GEMINI.md`.
- `.claude/commands/update.md`, `templates/.claude/commands/update.md` : étape 7 renommée et étendue à `GEMINI.md` (symétrique à `AGENTS.md`).
- `DEPLOYMENTS.md` (hors git) : version Moulin du Sud corrigée.
- Hors dépôt kit (Moulin du Sud) : 3 commits de rattrapage (voir Décisions prises).

## Hypothèses validées / invalidées
- VALIDE : l'étape 7 de `/close` (base de connaissances) fonctionne en conditions réelles sur une zone tierce.
- VALIDE : fusionner GEMINI.md dans l'étape 7 existante d'`/update` (au lieu de renuméroter) évite toute casse de numérotation.
- EN ATTENTE : la question GEMINI.md n'a jamais été posée via un appel réel d'`/init_projet`/`/update`.

## Prochaine étape exacte
Tester `/init_projet`/`/update` en conditions réelles pour valider la question GEMINI.md ; actions P1 restantes : Test 3 conversion `/create_agent`, test presse-papier étape 10.

## Question bloquante pour la session suivante
Aucune



---

# Session du 2026-07-31 (étape presse-papier /create_agent + agents dev/design jeu_espace)

## Décisions prises
- `/create_agent` : nouvelle étape `[SORTIE]` proposant de copier dans le presse-papier un message de mise à jour pour l'agent racine, plutôt que de l'écrire dans `signals.md` du projet cible (demande explicite de l'utilisateur, revert de la première approche).
- Agents `dev`/`design` créés dans jeu_espace (projet externe), question groupée sur le périmètre d'écriture (dev étendu au code Godot racine, design restreint à son dossier).
- Kit bumpé en v3.5 (minor) via `/doc_sync`.

## Livrables produits ou modifiés
- `.claude/commands/create_agent.md` : étape 10 (presse-papier) ajoutée, renumérotation 10→11/11→12.
- `CHANGELOG.md`, `Protocole_start_close_context.md` : entrées v3.5 ajoutées (miroir vérifié).
- `ameliorations_create_agent.md` : entrée agents dev/design (jeu_espace).
- `AGENTS_REGISTRY.md` (hors git) : entrées dev/design ajoutées.
- Hors dépôt kit (jeu_espace) : agents `dev`/`design` créés (agent_role.md + `_contexte/`), `zones.md` mis à jour ; modification initiale de `_contexte/signals.md` (message pour l'orchestrateur) annulée sur demande utilisateur.

## Hypothèses validées / invalidées
- VALIDE : l'ajout de l'étape presse-papier n'a pas nécessité de bump major (structure `_contexte/` inchangée).
- EN ATTENTE : l'étape 10 n'a jamais été exercée via un appel réel de `/create_agent` — message généré et copié manuellement, hors du flux de la commande.

## Prochaine étape exacte
Tester l'étape 10 (presse-papier) lors d'un prochain appel réel de `/create_agent` ; trancher les actions P1 en attente (GEMINI.md, test réel base de connaissances, Test 3 conversion).

## Question bloquante pour la session suivante
Aucune



---

# Session du 2026-07-31 (init jeu_espace + rattrapage commits)

## Décisions prises
- `/init_projet` exécuté sur `D:\ServOMorph\jeu_espace` (zone `orchestrateur`, repo sous git, `AGENTS.md` créé sur confirmation) d'après `_DOCS/idée de base.txt`.
- Corruption accidentelle (`" pl"` parasite avant un commentaire) corrigée dans `.claude/commands/create_agent.md`, détectée lors du contrôle `git status` avant clôture.
- Décision utilisateur : inclure dans le commit de clôture les changements non commités de sessions antérieures (`ameliorations_create_agent.md`, `note_conception_pause_agents.md`) plutôt que les laisser en suspens.

## Livrables produits ou modifiés
- Hors dépôt kit (`jeu_espace`) : `.claude/CLAUDE.md`, `.claude/zones.md`, `.claude/commands/start.md`, `.claude/commands/close.md`, `_contexte/contexte.md`, `_contexte/signals.md`, `ollama_call.py`, `_docs/protocole_vibecoding.md`, `AGENTS.md`. Commit initial fait dans ce repo.
- `DEPLOYMENTS.md` (hors git) : entrée ajoutée pour jeu_espace / orchestrateur / v3.3.
- `.claude/commands/create_agent.md` : corruption corrigée.
- `ameliorations_create_agent.md`, `note_conception_pause_agents.md` : commités cette session (contenu de sessions antérieures, non modifié).
- `CHANGELOG.md` : entrée v3.4.

## Hypothèses validées / invalidées
- EN ATTENTE : gap `GEMINI.md` (action P1) toujours ouvert, non retraité — jeu_espace n'en avait pas besoin.
- INVALIDE : les clôtures précédentes n'avaient pas réellement tout commité malgré leur message — `create_agent.md`/`ameliorations_create_agent.md` restaient en souffrance.

## Prochaine étape exacte
Sur jeu_espace : décider si `/create_agent` est lancé pour `codeur` et `design`. Sur le kit : surveiller les résidus non commités aux prochaines clôtures.

## Question bloquante pour la session suivante
Aucune



---

# Session du 2026-07-31 (init Open_Code_Apprentissage)

## Décisions prises
- `/init_projet` exécuté sur `D:\ServOMorph\Open_Code_Apprentissage` (zone `orchestrateur`, repo déjà sous git) — reformulation + questions préalables avant lancement, conformément à la demande explicite de l'utilisateur dans le fichier `but du projet.txt` du projet cible.
- 3 agents validés pour ce projet après discussion (pas de création lancée cette session) : `notes`, `NARRATEUR`, `data`.
- `GEMINI.md` créé manuellement sur demande explicite, hors procédure standard `/init_projet` (qui ne gère qu'`AGENTS.md`) — gap consigné en action ouverte.

## Livrables produits ou modifiés
- Hors dépôt kit (`Open_Code_Apprentissage`) : `.claude/CLAUDE.md`, `.claude/zones.md`, `.claude/commands/start.md`, `.claude/commands/close.md`, `_contexte/contexte.md`, `_contexte/signals.md`, `ollama_call.py` (modèle par défaut `gemma4:12b`), `AGENTS.md`, `GEMINI.md`, `_DOCS/protocole_vibecoding.md`. Commit initial fait dans ce repo.
- `DEPLOYMENTS.md` (hors git) : entrée ajoutée pour Open_Code_Apprentissage / orchestrateur / v3.3.
- `README.md` : section "État actuel" corrigée — restait bloquée à v3.2, ne mentionnait pas les ajouts v3.3 (base de connaissances, AGENTS.md) de la session précédente. Correction documentaire, pas de bump (aucun template/commande déployé modifié).
- Aucun fichier de commande/template du kit modifié cette session.

## Hypothèses validées / invalidées
- VALIDE : la procédure de reformulation + questions avant lancement (demandée par l'utilisateur pour ce projet précis) s'intègre sans friction dans `/init_projet` tel qu'il existe.
- EN ATTENTE : la pause de réflexion sur le nombre d'agents avant `/create_agent` n'est pour l'instant qu'un pattern ad hoc suivi manuellement dans cette session, pas une étape formalisée du kit.

## Prochaine étape exacte
Sur Open_Code_Apprentissage : lancer `/create_agent` pour les 3 agents validés (notes, NARRATEUR, data). Sur le kit : session dédiée pour formaliser GEMINI.md dans `/init_projet` et documenter le pattern "pause réflexion agents".

## Question bloquante pour la session suivante
Aucune



---

# Session du 2026-07-30 (base de connaissances)

## Décisions prises
- Système de base de connaissances `.md` (pattern "progressive disclosure" : `INDEX.md` catalogue + docs individuels, jamais de suppression, archivage à la place) validé — d'abord implémenté dans Moulin du Sud (agent `documentation`), puis généralisé au kit.
- `/close` (template) : nouvelle étape 7 conditionnelle proposant une entrée/MAJ dans `DOCUMENTATION/` en fin de session, jamais automatique (confirmation utilisateur requise, la zone fermée n'a pas la main sur le dossier d'une autre zone).
- `AGENTS.md` introduit comme équivalent `CLAUDE.md` pour agents non-Claude — jamais créé automatiquement : `/init_projet` (Q7) et `/update` (étape 7) posent la question à chaque fois, sautée en mode batch, jamais écrasé s'il existe déjà.
- Kit bumpé en v3.3.

## Livrables produits ou modifiés
- `templates/.claude/commands/close.md` : étape 7 (base de connaissances), renumérotation 8→13.
- `templates/.claude/CLAUDE.md`, `.claude/CLAUDE.md` (Moulin du Sud) : section "Base de connaissances" ajoutée.
- `templates/AGENTS.md` : nouveau template.
- `.claude/commands/init_projet.md` : Q7 + copie conditionnelle `AGENTS.md`.
- `.claude/commands/update.md` : étape 7 (AGENTS.md optionnel, jamais écrasé), renumérotation 8→11.
- `ameliorations_create_agent.md`, `AGENTS_REGISTRY.md` (hors git) : entrée agent `documentation`.
- Hors dépôt kit (Moulin du Sud) : agent `documentation` créé (`agent_role.md`, `_contexte/`, `DOCUMENTATION/INDEX.md`), `AGENTS.md` créé, `.claude/close.md`/`CLAUDE.md` alignés sur le kit.

## Hypothèses validées / invalidées
- VALIDE (recherche web/GitHub) : la progressive disclosure (`INDEX.md` + docs ciblés) est le pattern documenté en 2026 pour ce cas d'usage, cohérent avec le principe déjà appliqué par `signals.md`/`contexte.md`.
- EN ATTENTE : aucun test réel — `DOCUMENTATION/INDEX.md` de Moulin du Sud est vide, l'étape 7 de `/close` et la question AGENTS.md de `/update`/`/init_projet` n'ont jamais tourné en conditions réelles.

## Prochaine étape exacte
Remplir `DOCUMENTATION/` de Moulin du Sud via `/start documentation` ; tester `/close` sur une autre zone de Moulin du Sud pour valider l'étape 7 en conditions réelles.

## Question bloquante pour la session suivante
Aucune



---

# Session du 2026-07-30 (agents MAJUSCULES)

## Décisions prises
- `/create_agent` : dossier de l'agent (créé ou converti) normalisé en MAJUSCULES pour la reconnaissance visuelle dans l'arborescence ; l'alias de zone reste en minuscules.
- Mode conversion : si le dossier existant a une casse non conforme, il est renommé (`git mv` si suivi par git) et le chemin mis à jour dans `zones.md` (alias inchangé).
- Kit bumpé en v3.2.

## Livrables produits ou modifiés
- `.claude/commands/create_agent.md` : règle MAJUSCULES ajoutée en [PREFLIGHT], cas de renommage documenté en [ECRITURE] (mode conversion).
- `ameliorations_create_agent.md` : entrée 2026-07-30 (agent `editeur`, crea_zik) — premier test de la règle en mode création.
- Agent `editeur` créé dans `D:\ServOMorph\crea_zik\EDITEUR` (hors dépôt kit), périmètre étendu à `frontend/`/`backend/` sur décision utilisateur.
- `AGENTS_REGISTRY.md` (hors git) : entrée `editeur`.
- `CHANGELOG.md`, `Protocole_start_close_context.md`, `README.md` : synchronisés via `/doc_sync`.

## Hypothèses validées / invalidées
- VALIDE : la règle MAJUSCULES fonctionne en mode création (dossier `EDITEUR` créé directement en majuscules, alias `editeur` dérivé correctement).
- EN ATTENTE : le renommage en mode conversion (dossier existant à la casse non conforme) n'a pas été exercé en conditions réelles — aucun agent minuscule actuel à convertir.

## Prochaine étape exacte
Tester le renommage en mode conversion dès qu'un agent existant à la casse non conforme se présente ; sinon trancher les actions P2 en attente (P7-P10, Lots 2-4, jeu_zombies).

## Question bloquante pour la session suivante
Aucune



---

# Session du 2026-07-28

## Décisions prises
- README.md : ligne `/doc_sync` ajoutée dans "Ce que ça fait" (omission préexistante comblée).
- Nouvelle section "Tests manuels" dans `CLAUDE.md` (kit + template) : chemin relatif générique `tests_manuels.md`, décision utilisateur après signalement que le chemin absolu jeu_zombies proposé cassait la généricité du template.
- Nouvelle sous-section "Déclencheurs de vérification" dans `CLAUDE.md` (kit + template), suite à une affirmation non vérifiée en session (jeu_zombies déclaré absent de `DEPLOYMENTS.md` sans l'avoir lu).
- Kit bumpé en v3.1.

## Livrables produits ou modifiés
- `README.md` : ligne `/doc_sync` ajoutée.
- `.claude/CLAUDE.md`, `templates/.claude/CLAUDE.md` : sections "Tests manuels" + "Déclencheurs de vérification" ajoutées (miroir vérifié identique).
- `CHANGELOG.md`, `Protocole_start_close_context.md` : entrées v3.1.
- `/doc_sync` exécuté deux fois dans la session, aucun conflit ni asymétrie détecté.

## Hypothèses validées / invalidées
- INVALIDE : affirmation "jeu_zombies n'est pas dans `DEPLOYMENTS.md`" — faux, il y figure (v2.26) ; fichier non lu avant l'affirmation. Corrigé par les nouvelles règles de vérification.

## Prochaine étape exacte
`/update` sur jeu_zombies pour le faire passer de v2.26 à v3.1, reporté par l'utilisateur.

## Question bloquante pour la session suivante
Aucune



---


---

# Session du 2026-08-15

## Décisions prises
- `roadmap_template_roberto.md` close (5/5 phases FAIT) : bilan garder tel quel, aucun ajustement nécessaire sur le template ni sur la commande.

## Livrables produits ou modifiés
- `templates/roberto/` : template extrait et généricisé depuis `D:\ServOMorph\Roberto2` (MACROS, MASCOTTE, UI_WEB, scripts racine, 30 fichiers hors `analysis/`) ; placeholders `{{NOM_PROJET}}`/`{{ALIAS_PROJET}}`/`{{DATE}}` appliqués à `README.md`, `.claude/zones.md`, `MASCOTTE/agent_role.md`.
- `.claude/commands/insert_template.md` : testé de bout en bout sur un projet cible de test (idempotence, résolution des placeholders, code Python compilable, aucun chemin résiduel vers `Roberto2`).
- `roadmap_template_roberto.md` : Phases 3/4/5 passées à FAIT.
- `README.md`, `CHANGELOG.md` (v3.22 -> v3.23) : synchronisés via `/doc_sync`.

## Hypothèses validées / invalidées
- VALIDE : `/insert_template` fonctionne comme prévu en conditions réelles (idempotence, placeholders, exclusion `analysis/`, préservation des binaires).
- INVALIDE : l'inventaire Phase 1 affirmait "aucun chemin absolu en dur dans le code Python" — deux scripts (`MACROS/tester_memoire_opencode.py`, `MACROS/tester_communication_opencode.py`) en contredisaient. Pivot : corrigés par résolution relative `Path(__file__)`, cohérente avec le reste du code.

## Prochaine étape exacte
Aucune action immédiate sur `roberto` (usage réel différé par l'utilisateur). Reprendre les actions ouvertes prioritaires (P1) de ce fichier.

## Question bloquante pour la session suivante
Aucune

---

# Session du 2026-08-16

## Décisions prises
- Corruption d'encodage de `control_pc.sqlite` corrigée : cause confirmée (insertion manuelle via CLI shell, codepage non-UTF8 — `discover_right_window.py` n'écrit jamais en base, vérifié par lecture du script). Question AGENTS.md/GEMINI.md de `/update`/`/init_projet` confirmée fonctionnelle par l'utilisateur en conditions réelles.

## Livrables produits ou modifiés
- `templates/control_PC/database/control_pc.sqlite` : 6 lignes `discoveries` corrompues (id 1-6, `appli_tsa_sdi_tdah`) supprimées ; 5 ré-observées en conditions réelles (captures + clics confirmés sur l'app ouverte) et réinsérées (id 8-12) via `sqlite3` Python, encodage vérifié correct.
- `templates/control_PC/analysis/appli_tsa_sdi_tdah/` (non commité, conforme à la convention `analysis/` éphémère) : captures et clics de la session de ré-observation.

## Hypothèses validées / invalidées
- VALIDE : `discover_right_window.py` n'écrit jamais dans SQLite — corruption venait d'une insertion manuelle CLI, pas du script.
- EN ATTENTE : écran Onboarding non ré-observé (nécessite un `Reset DB` assumé, action destructive non déclenchée cette session).

## Prochaine étape exacte
Reprendre les actions ouvertes prioritaires (P1) de ce fichier. Décider si/quand traiter l'Onboarding restant (Reset DB assumé).

## Question bloquante pour la session suivante
Aucune

---

# Session du 2026-08-16

## Décisions prises
- Nouvelle commande `/cherche_fonction` créée : recherche générique d'une fonctionnalité déjà codée dans d'anciens projets, dossiers cibles toujours redemandés à chaque appel (jamais mémorisés).
- Intégration Discord ↔ Claude Code extraite et généricisée en template kit réutilisable, source `Agents_IA_V2\Templates\_discord_integration\` : commandes `bot.py` spécifiques au projet source (poker/coach_DQN) retirées, ne reste que le relais générique.
- Contournement temporaire décidé pour débloquer le test : `intents.message_content = False` dans la copie de test uniquement (jamais dans le template livrable), le toggle "Message Content Intent" du Developer Portal Discord ne persistant pas malgré plusieurs tentatives.

## Livrables produits ou modifiés
- `.claude/commands/cherche_fonction.md` : créé.
- `templates/discord_com/` : nouveau template (bot.py, bot_manager.py, claude_bridge.py, discord_loop.py, docs, `.claude/commands/discord_loop.md`) — vérifié sans placeholder `{{...}}` non reconnu, sans credential réel.
- `discord_com/` (racine kit) : copie de test locale, **non commitée intentionnellement** (résidu attendu).
- `.gitignore` : ajout `discord_com/config_bot_discord.json` et `discord_com/bot.pid`.

## Hypothèses validées / invalidées
- VALIDE : le template se connecte correctement au gateway Discord une fois token/channel_id valides.
- INVALIDE : le toggle Message Content Intent du portail Discord ne se sauvegarde pas via les manipulations standard testées — cause non identifiée, contournement temporaire appliqué à la place.
- EN ATTENTE : accès au salon (`403 Missing Access` sur `fetch_channel`) — bot probablement jamais invité sur le serveur de test.

## Prochaine étape exacte
Inviter le bot sur le serveur (URL OAuth2, scope `bot`, permissions View Channel + Send Messages), relancer `discord_com/bot.py`, confirmer l'échange de message. Puis résoudre le blocage Message Content Intent et rétablir `message_content = True`.

## Question bloquante pour la session suivante
Aucune

---

# Session du 2026-08-18 (init_discord_mode validée en conditions réelles + faille token corrigée)

## Décisions prises
- `/init_discord_mode` testée en conditions réelles pour la première fois (ROBERTO, SérénIATech_dev) : insertion + configuration + validation (`bot_manager.py status`, `!ping`) confirmées.
- Faille de sécurité détectée en cours de test (token lu/écrit par Claude) et corrigée structurellement : token déplacé dans `discord_com/.env`, jamais touché par Claude ; `config_bot_discord.json` réduit à `enabled`/`channel_id`.

## Livrables produits ou modifiés
- `templates/discord_com/bot.py` : lecture du token via `os.environ`/`python-dotenv`
- `templates/discord_com/requirements.txt` : `python-dotenv` ajouté
- `templates/discord_com/config_bot_discord.example.json` : `bot_token` retiré
- `templates/discord_com/.env.example` : créé
- `templates/discord_com/SETUP.md`, `DISCORD_SECURITY.md` : workflow `.env` documenté
- `.claude/commands/init_discord_mode.md` : règle absolue token + vérifications booléennes
- Déploiement réel (hors dépôt kit) : `ROBERTO/discord_com/` dans SérénIATech_dev

## Hypothèses validées / invalidées
- VALIDE : `/init_discord_mode` fonctionnelle de bout en bout en conditions réelles.
- INVALIDE : workflow initial (token manipulé par Claude) → pivot vers `.env` rempli par l'utilisateur.

## Prochaine étape exacte
Trancher l'automatisation `.gitignore` pour `discord_com/.env` côté projets cibles. Sinon, restent à tester pour `discord_com` : mode `enabled: false`, préfixe novice `"? "`.

## Question bloquante pour la session suivante
Aucune

---

# Session du 2026-08-18

## Décisions prises
- Périmètre de lecture de la zone `roberto` (`Appli_TSA_SDI_TDAH`) étendu à `_contexte/signals.md`/`contexte.md` racine (lecture seule), suite à un constat utilisateur : la zone travaillait sans connaître l'état réel des autres chantiers du projet (notamment `sync-marie`).
- Diagnostic d'un problème réel (pas seulement un risque) : une session `/close roberto` antérieure avait écrit sa synthèse dans les fichiers `_contexte/` racine au lieu de ceux de la zone `roberto` — mémoire de zone restée figée depuis sa création. Corrigé.
- Mission ROBERTO mise en pause à la demande de l'utilisateur ; reprise prévue via `/start` sur la zone globale, pas sur `roberto`.

## Livrables produits ou modifiés
- `Appli_TSA_SDI_TDAH/ROBERTO/agent_role.md`, `.claude/commands/start.md` : lecture élargie de la zone `roberto` aux fichiers `_contexte` racine.
- `Appli_TSA_SDI_TDAH/ROBERTO/_contexte/signals.md`/`contexte.md` : resynchronisés avec l'état réel (Phases 1-2 FAIT, gap corrigé, journal testeur), committé (`029efaf`).
- Deux correctifs de mécanisme proposés mais non implémentés : `close.md` (empêcher l'écriture hors de la zone `roberto`), `start.md` racine (lire `AGENT_STATE.md` pour que la zone globale voie l'état des flux ROBERTO).

## Hypothèses validées / invalidées
- VALIDE : fusionner la zone `roberto` dans la zone principale aurait cassé l'isolation de contexte voulue par le système de zones — le vrai problème était un manque de lecture croisée, pas l'existence de deux zones séparées.
- EN ATTENTE : généralisation de ce pattern de lecture croisée entre zones (zone-agent ↔ zone parente) aux templates du kit, pas encore tranchée.

## Prochaine étape exacte
Depuis `Appli_TSA_SDI_TDAH` : `/start` sur la zone globale pour reprendre la main. Côté kit : décider si le pattern de lecture croisée doit être généralisé (`start.md`/`close.md`/`agent_role_TEMPLATE.md`).

## Question bloquante pour la session suivante
Aucune.

---

# Session du 2026-08-19 (partie 1)

## Décisions prises
- Prototype "assistant vocal distant pour Claude Code" (dossier de travail `roberto/com_telephone/`) : PWA mobile + WebSocket + Whisper local (STT) + Piper local (TTS), accès distant via tunnel Cloudflare déjà configuré (`vertia-test.serenia-tech.fr` → port 5000).
- UI en chat (style ChatGPT) plutôt que l'interface minimaliste initiale, à la demande de l'utilisateur.
- Capture vocale via `MediaRecorder` + détection de silence maison, la Web Speech API du navigateur étant écartée (non supportée sur Safari/iOS).
- Traitement des messages reste manuel (Claude Code lit `messages.log` via un watcher persistant et répond via un endpoint `/send`) — pas de branchement autonome côté serveur, confirmé suffisant par l'utilisateur.

## Livrables produits ou modifiés
- `templates/roberto/com_telephone/voice-code-bridge/mobile/index.html`, `app.js` : UI chat + écran vocal (capture, VAD, lecture audio, boucle continue).
- `templates/roberto/com_telephone/voice-code-bridge/server/server.js` : serveur Node (HTTP+WS, relais STT/TTS, log debug/messages).
- `templates/roberto/com_telephone/voice-code-bridge/server/stt_server.py` : serveur Whisper local (faster-whisper, port 5001).
- `templates/roberto/com_telephone/voice-code-bridge/server/tts_server.py` + `voices/fr_FR-siwis-medium.onnx(.json)` : serveur Piper local (port 5002).

## Hypothèses validées / invalidées
- VALIDE : Whisper local (faster-whisper) + Piper local suffisent pour un pipeline STT/TTS gratuit, sans cloud, avec les modèles/paquets déjà présents sur le PC.
- INVALIDE : Web Speech API du navigateur pour le STT — pivot vers `MediaRecorder` + Whisper serveur.
- INVALIDE : test via Firefox iOS — `secureContext`/`mediaDevices` indisponibles ; pivot vers Safari (fonctionnel).
- VALIDE : boucle conversationnelle continue (écoute → réponse → réécoute) opérationnelle, avec déblocage audio Safari via un geste utilisateur initial.

## Prochaine étape exacte
Ajouter une authentification (mot de passe) sur l'UI avant exposition prolongée via le tunnel public — actuellement aucune protection.

## Question bloquante pour la session suivante
Aucune.

---

# Session du 2026-09-10

## Décisions prises
- Traçage des templates installés : section « Templates installés » dans `DEPLOYMENTS.md` (kit, gitignoré), une ligne par couple (projet, template) — même régime que la section « Remotes rclone ».
- Alimentation auto : `/insert_template` (étape `[SORTIE]` 9) écrit la ligne ; `/init_discord_mode` et `/create_projet` en héritent par délégation à cette procédure ; `/init_intercom` (nouvelle étape 6) écrit sa propre ligne.
- Rétro-remplissage initial par scan de signature (profondeur 6, exclusion des copies de kit embarquées) — détection non exhaustive assumée.

## Livrables produits ou modifiés
- `.claude/commands/insert_template.md` : étape `[SORTIE]` 9 (écriture registre), récap 9→10.
- `.claude/commands/init_intercom.md` : étape 6 (écriture registre), renum. 5→7.
- `DEPLOYMENTS.md` : section « Templates installés » + 8 lignes rétro (gitignoré, non commité).
- `CHANGELOG.md` : entrée v5.8.

## Hypothèses validées / invalidées
- VALIDE : `/init_discord_mode` et `/create_projet` délèguent déjà à la procédure `/insert_template` [SORTIE] → traçage hérité sans les modifier.
- INVALIDE (partiel) : le scan ne détecte pas `control_PC`/`notification`/`overlay`/`parallel_agents` ; 2 projets injoignables (chemins morts `Open_Code_Apprentissage`, `claude-vibecoding-kit`).
- EN ATTENTE : test réel d'une insertion `/insert_template` écrivant la ligne registre.

## Prochaine étape exacte
Exercer `/insert_template` en réel et vérifier l'écriture / non-duplication de la ligne « Templates installés ». Puis reprendre P1 (angle mort backup `meuniers/`).

## Question bloquante pour la session suivante
Aucune.

---

# Session du 2026-09-16

## Décisions prises
- Rôle DOCUMENTATION d'un projet cible pouvant couvrir métier + technique en un seul agent, structure calquée sur celle du kit (10_concepts/20_guides/30_decisions/40_specs).
- P14 tranchée et implémentée : `agent_role_TEMPLATE.md` § Invariants réutilise `{{ECRITURE_ETENDUE}}`, cohérence automatique avec le Périmètre pour tout agent à écriture étendue.

## Livrables produits ou modifiés
- `templates/agent_role_TEMPLATE.md` : Invariants paramétrés (P14).
- `base_connaissances/ameliorations_create_agent.md` : entrée P14 (propositions + historique), entrée création agent documentation.
- `CHANGELOG.md` : v5.12.
- Hors kit (autre dépôt) : agent DOCUMENTATION créé dans `Appli_TSA_SDI_TDAH` via `/create_agent`, commité côté ce projet (`88bf668`).

## Hypothèses validées / invalidées
- VALIDE : réutiliser `{{ECRITURE_ETENDUE}}` dans la ligne "Ne jamais committer hors de" suffit à corriger P14, sans toucher `create_agent.md`.

## Prochaine étape exacte
Répercuter P14 sur les chartes déjà écrites avec périmètre étendu si un besoin réel se présente (DESIGN/DISCORD d'Appli_TSA_SDI_TDAH) — pas fait rétroactivement cette session.

## Question bloquante pour la session suivante
Aucune.

---
# Session du 2026-09-26

## Décisions prises
- Nouveau projet `PromptGuard` créé (Git local + GitHub public) via `/create_projet` → `/init_projet`, stack et agents validés par l'utilisateur.
- Idée de skill de cohérence `CLAUDE.md`/`AGENTS.md`/`GEMINI.md` à expérimenter localement dans PromptGuard d'abord, pas de généralisation au kit pour l'instant.

## Livrables produits ou modifiés
- `.claude/memory.md` (kit) : créé, 2 entrées (skill de cohérence + divergences par fichier).
- `base_connaissances/ameliorations_create_agent.md` : entrée session PromptGuard (3 agents créés en lot).
- `DEPLOYMENTS.md`, `AGENTS_REGISTRY.md` (hors git) : PromptGuard et ses 3 agents enregistrés.
- Projet `D:\ServOMorph\PromptGuard` : protocole vibecoding posé, agents `securite`/`qa`/`documentation` créés.

## Hypothèses validées / invalidées
- VALIDE : les flags d'isolation de Claude CLI (`--tools`, `--strict-mcp-config`, etc.) existent en 2.1.259.
- EN ATTENTE : leur efficacité réelle pour isoler Claude CLI (test canari à faire côté PromptGuard/SECURITE).
- EN ATTENTE : skill de cohérence des 3 fichiers `.md` (expérimentation à mener côté PromptGuard).

## Prochaine étape exacte
Rien de nouveau côté kit — la suite se joue dans `/start PromptGuard` (construction de sa roadmap).

## Question bloquante pour la session suivante
Aucune.

---
# Session du 2026-10-08

## Décisions prises
- Nouveau projet `CreaZik_V3` (expérimentation de création de musique par IA, instrumental et vocal, modifiable intégralement) créé le 2026-10-05 via `/create_projet` : Git local + GitHub public, zone `CreaZik_V3`, sans AGENTS.md/GEMINI.md ni agents ; stack laissée vide.
- Pas de bump de version ni de `/doc_sync` : aucun fichier suivi du kit n'a changé.

## Livrables produits ou modifiés
- `DEPLOYMENTS.md` (gitignoré) : ligne CreaZik_V3 ajoutée (v5.14).
- Projet `D:\ServOMorph\CreaZik_V3` : dépôt GitHub `ServOMorph/CreaZik_V3`, protocole vibecoding posé (commit `a8b74a8`, non poussé).

## Hypothèses validées / invalidées
- VALIDE : `/create_projet` enchaîne dépôt, description GitHub et `/init_projet` sans blocage.
- EN ATTENTE : affichage de la liste des templates (étape 17) non exercé, l'utilisateur n'a pas atteint cette étape.

## Prochaine étape exacte
`/start CreaZik_V3` pour définir la stack et la roadmap du projet.

## Question bloquante pour la session suivante
Aucune.

---
# Session du 2026-10-08 (2)

## Décisions prises
- Agents `textes` (écriture limitée à `TEXTES/`, récupération via l'orchestrateur) et `modeles_llm` créés dans `D:\ServOMorph\CreaZik_V3` via `/create_agent`.
- Stockage des modèles de `modeles_llm` : `D:\AI\Musique\<modele>\` (convention `D:\AI\`, `HF_HOME=D:\HuggingFaceCache` déjà partagé) ; `D:\Modeles_IA\` proposé puis écarté.
- `webradio/tests_ace/` exclu du périmètre de `modeles_llm` (réservé aux tests du modèle ACE).
- Pas de `/doc_sync` : aucune commande ni template du kit modifié.

## Livrables produits ou modifiés
- `D:\ServOMorph\CreaZik_V3` : chartes et `_contexte/` des deux agents, `.claude/zones.md` (non commités dans ce repo).
- `AGENTS_REGISTRY.md` (gitignoré) : deux lignes ajoutées.
- `base_connaissances/ameliorations_create_agent.md` : entrée du jour et correction de périmètre.

## Hypothèses validées / invalidées
- VALIDE : `start.md` de CreaZik_V3 référence `agent_role.md` (pas de warning).
- INVALIDE : question de périmètre brute suffisante -> pivot vers présentation de l'arborescence avant choix.
- EN ATTENTE : comportement réel des deux agents au premier `/start`.

## Prochaine étape exacte
`/start textes` ou `/start modeles_llm` depuis `D:\ServOMorph\CreaZik_V3`.

## Question bloquante pour la session suivante
Aucune.

---

# Session du 2026-10-10

## Décisions prises
- Agent `jeux` créé dans `Appli_TSA_SDI_TDAH/JEUX` via `/create_agent` (alias `jeux`, parent racine) : jeux pour TSA/SDI/TDAH, 5 jeux simples proposés avant développement.
- Jeux non branchés sur l'application pendant le développement ; test via `run_jeux.py` (racine, périmètre d'écriture étendu) ; `src/` et `IA-TSA` en lecture seule.
- Message de mise à jour pour la zone parente copié dans le presse-papier.
- Pas de `/doc_sync` : aucune commande ni template du kit modifié.

## Livrables produits ou modifiés
- `Appli_TSA_SDI_TDAH` : `JEUX/agent_role.md`, `JEUX/_contexte/`, `.claude/zones.md` (non commités dans ce repo).
- `AGENTS_REGISTRY.md` (gitignoré) : ligne `jeux` ajoutée.
- `base_connaissances/ameliorations_create_agent.md` : entrée du jour.

## Hypothèses validées / invalidées
- VALIDE : `start.md` d'Appli référence `agent_role.md` (pas de warning).
- EN ATTENTE : faisabilité de `run_jeux.py` sans toucher `src/` ; emplacement des données de recherche du projet.

## Prochaine étape exacte
`/start jeux` depuis `D:\ServOMorph\Appli_TSA_SDI_TDAH`.

## Question bloquante pour la session suivante
Aucune.

---

# Session du 2026-10-12 (suite)

## Décisions prises
- Vol de focus : correctif `focus_fiable.ps1` appliqué aux 4 scripts de clic/saisie ; test réel reporté par l'utilisateur (section ajoutée à `tests_manuels.md`).
- `check_kit.py` : regex de version tolérante au gras Markdown ; `/init_projet` prescrit désormais une méthode de substitution Python littérale (kit v5.18).

## Livrables produits ou modifiés
- `skills/chatgpt-orchestrateur/scripts/focus_fiable.ps1` (nouveau) + `cliquer_fenetre`, `coller_et_envoyer`, `copier_reponse`, `defiler_fenetre` : modifiés, non validés en réel.
- `scripts/check_kit.py`, `.claude/commands/init_projet.md` + miroir `templates/`, `tests_manuels.md`, `CHANGELOG.md` v5.18, `README.md`, `Protocole_start_close_context.md` : mis à jour.

## Hypothèses validées / invalidées
- VALIDE : `check_kit.py` passant avec README effectivement contrôlé (`v5.18`).
- EN ATTENTE : efficacité du correctif de focus (cause présumée, non confirmée) ; effet parasite possible de la touche Alt sur la barre de menus Chrome.

## Prochaine étape exacte
Exécuter le test de focus (`tests_manuels.md`), puis trancher le port des correctifs `backup_project.py` et la mise à jour du guide `initialiser_un_projet.md`.

## Question bloquante pour la session suivante
Aucune.

---
# Session du 2026-10-13 (2)

## Décisions prises
- Agent `shorts` créé dans `SérénIATech_dev/Communication/SHORTS` (alias `shorts`), lecture étendue à tout le dépôt hors données sensibles, écriture limitée à son dossier ; ligne « Zone parente » retirée (aucune zone racine dans `zones.md`, Communication sans `team.md`).

## Livrables produits ou modifiés
- `SérénIATech_dev/Communication/SHORTS/{agent_role.md,_contexte/contexte.md,_contexte/signals.md}` : créés ; `.claude/zones.md` de SérénIATech_dev : ligne `shorts` ajoutée (hors dépôt du kit).
- `AGENTS_REGISTRY.md` (local, hors git) : ligne ajoutée. `base_connaissances/ameliorations_create_agent.md` : entrée du jour.

## Hypothèses validées / invalidées
- EN ATTENTE : `/start shorts` jamais lancé ; chargement de la charte non testé.

## Prochaine étape exacte
Lancer `/start shorts` depuis `SérénIATech_dev`, puis l'état des lieux des Shorts. Priorités P1 ci-dessus inchangées.

## Question bloquante pour la session suivante
Aucune.

---

# Session du 2026-10-14

## Décisions prises
- Agent `espace_l-invariable` créé dans `SérénIATech_dev/Gestion clients/Clients/Espace_L-Invariable` (parent `gestion-clients`, lecture du dépôt hors données sensibles, écriture limitée à son dossier) ; renommage en majuscules reporté (dossier verrouillé, `clients.dossier` en base).
- `clip_promo/diffusion` en écriture partagée avec `shorts` ; charte `shorts` complétée (parent `communication`) ; 2 actions L'Invariable migrées de `gestion-clients` vers l'agent.
- `/create_agent` : P1 à P6 implémentées (parent englobant, remontée du projet cible, migration d'actions, références avant renommage, données sensibles, lecture étendue) ; kit v5.20.

## Livrables produits ou modifiés
- `create_agent.md`, `create_team.md`, `templates/agent_role_TEMPLATE.md`, `CHANGELOG.md`, `README.md`, `Protocole_start_close_context.md`, `base_connaissances/ameliorations_create_agent.md` : modifiés. Hors dépôt : chartes et `_contexte/` d'`espace_l-invariable` et `shorts`, `zones.md` et `signals.md` de `gestion-clients` (SérénIATech_dev).

## Hypothèses validées / invalidées
- INVALIDE : « zone parente non déterminée » pour shorts/espace_l-invariable -> parent englobant dans `zones.md`.
- EN ATTENTE : processus verrouillant le dossier (deux `http.server`, ports 8765/8781, non vérifiés) ; commande modifiée non exercée en réel.

## Prochaine étape exacte
Lever le verrou et renommer le dossier (action ci-dessus), puis `/start espace_l-invariable` depuis `SérénIATech_dev`. Priorités P1 inchangées.

## Question bloquante pour la session suivante
Aucune.

---

# Session du 2026-10-14

## Décisions prises
- `/close` attribue chaque élément à sa zone propriétaire (3-bis) et contrôle le statut Git des signaux avant d'annoncer un commit (13) ; `/start` signale les éléments mal classés (4c) sans les déplacer ; kit v5.21.
- Déploiement par `/update` dans `SérénIATech_dev` (blocs SPECIFICITES PROJET préservés, `create_memory.md` et `CLAUDE.md` mis à jour par la procédure standard).
- Roadmap `roadmap_actions_ouvertes_luna.md` laissée à la racine de `SérénIATech_dev` et étape 4c inchangée : « on ne change rien » (décision de l'utilisateur).

## Livrables produits ou modifiés
- `.claude/commands/start.md`, `close.md` et leurs templates, `Protocole_start_close_context.md`, `CHANGELOG.md`, `README.md`, `tests_manuels.md` : modifiés. Hors dépôt kit : `SérénIATech_dev/.claude/` (4 fichiers, commit d'update) ; `DEPLOYMENTS.md` (local, gitignoré).

## Hypothèses validées / invalidées
- VALIDE : miroir kit/template identique hors bloc, `check_kit.py` et 14 tests passent, commandes installées identiques aux templates (comparaison refaite après un faux positif).
- EN ATTENTE : comportement réel des étapes 3-bis, 4c, 13 (scénarios non rejoués) ; limite connue : 4c ne contrôle pas une roadmap posée à la racine.

## Prochaine étape exacte
L'utilisateur rejoue les scénarios dans `SérénIATech_dev` (nouvelle session, prompt de guidage fourni) puis transmet les divergences au kit.

## Question bloquante pour la session suivante
L'élément « df7ee31d — Tableau prévisions » (décider d'une roadmap dédiée : jours ou dates, extension sur plusieurs cases, sous-tâches) a été mentionné sans être traité : de quel projet ou zone vient-il ?

---

# Session du 2026-10-17

## Décisions prises
- Projet `REA` créé via `/create_projet` (Git local, sans GitHub) puis `/init_projet` : alias `REA`, objectif « Utiliser REA (https://github.com/morluto/rea) », stack « À définir », `AGENTS.md` et `GEMINI.md` demandés, aucun agent, aucun template.

## Livrables produits ou modifiés
- `D:\ServOMorph\REA` : dépôt créé, commits `b753cfc` (init) et `ef8ed53` (protocole, kit v5.21). `AGENTS.md` et `GEMINI.md` créés mais non commités.
- `DEPLOYMENTS.md` (local, gitignoré) : ligne REA ajoutée au tableau des projets. Aucun fichier du kit versionné modifié, pas de bump `CHANGELOG.md`.

## Hypothèses validées / invalidées
- VALIDE : substitution Windows de `/init_projet` exercée sur un projet réel (aucun `{{` résiduel, `{{RACINE}}` en `D:\ServOMorph\REA`).
- INVALIDE : `init_projet.md` étape 7 (« ajouter une ligne ») ne précise pas le tableau cible ; l'ajout en fin de fichier est tombé dans le tableau des templates, déplacé à la main.
- INVALIDE : l'étape 5 de `init_projet.md` ne stage pas `AGENTS.md`/`GEMINI.md` quand ils sont demandés.

## Prochaine étape exacte
Lancer `/start REA` dans `D:\ServOMorph\REA` et y renseigner la stack ; corriger les deux écarts de `init_projet.md` (actions P2 ci-dessus).

## Question bloquante pour la session suivante
L'élément « df7ee31d — Tableau prévisions » (décider d'une roadmap dédiée : jours ou dates, extension sur plusieurs cases, sous-tâches) a été mentionné sans être traité : de quel projet ou zone vient-il ?

---

# Session du 2026-10-17 (2)

## Décisions prises
- Projet `IA_Eco-Responsable` créé via `/create_projet` (Git local + dépôt GitHub public `ServOMorph/IA_Eco-Responsable`) puis `/init_projet` : alias = nom du projet, objectif « Interface open source pour installer et lancer des IA locales (chat, image) en un clic, adaptées à la machine de l'utilisateur, pensée pour les novices », stack « À définir », `AGENTS.md` demandé, `GEMINI.md` refusé, aucun agent, aucun template.
- Les noms proposés en amont (Hearth, Atelier, Nestor...) n'ont pas été retenus : l'utilisateur a imposé `IA_Eco-Responsable`.

## Livrables produits ou modifiés
- `D:\ServOMorph\IA_Eco-Responsable` : dépôt créé, commits `6e5d208` (init) et `075aaf5` (protocole, kit v5.21), poussés sur `origin/main` (contrôlé par `git log origin/main`). `AGENTS.md` commité.
- `DEPLOYMENTS.md` (local, gitignoré) : ligne IA_Eco-Responsable ajoutée au tableau des projets. Aucun fichier du kit versionné modifié hors signaux/contexte, pas de bump `CHANGELOG.md`.

## Hypothèses validées / invalidées
- VALIDE : `/create_projet` avec GitHub public, avec `gh repo edit` pour la description, de bout en bout (dépôt créé, description appliquée, push contrôlé).
- INVALIDE : les écarts de `init_projet.md` étapes 5 (staging `AGENTS.md`) et 7 (tableau cible de `DEPLOYMENTS.md`) se sont reproduits à l'identique ; contournés à la main, toujours non corrigés dans le kit.

## Prochaine étape exacte
Lancer `/start IA_Eco-Responsable` dans `D:\ServOMorph\IA_Eco-Responsable`, définir la stack et cadrer le MVP (2 modèles, filtrage matériel 8 Go RAM / 8 Go VRAM) ; corriger les deux écarts de `init_projet.md` (action P2 ci-dessus).

## Question bloquante pour la session suivante
L'élément « df7ee31d — Tableau prévisions » (décider d'une roadmap dédiée : jours ou dates, extension sur plusieurs cases, sous-tâches) a été mentionné sans être traité : de quel projet ou zone vient-il ?

---

# Session du 2026-10-22

## Décisions prises
- Projet `creation_llm` créé via `/create_projet` (Git local + dépôt GitHub public `ServOMorph/creation_llm`, description « Création d'un LLM from scratch sur mon PC ») puis `/init_projet` : alias = nom du projet, stack « À définir », sensibles « Aucun », `AGENTS.md` et `GEMINI.md` demandés (lecture de la numérotation décalée des réponses), aucun agent, aucun template.

## Livrables produits ou modifiés
- `D:\ServOMorph\creation_llm` : dépôt créé, commits `5df09ec` (init) et `d343b1e` (protocole, kit v5.21). Le commit du protocole n'est pas poussé sur `origin/main`.
- `DEPLOYMENTS.md` (local, gitignoré) : ligne creation_llm ajoutée au tableau des projets. Aucun fichier du kit versionné modifié hors signaux/contexte, pas de bump `CHANGELOG.md`.

## Hypothèses validées / invalidées
- VALIDE : `/create_projet` avec GitHub public de bout en bout.
- INVALIDE : les écarts de `init_projet.md` étapes 5 et 7 persistent (contournés : `AGENTS.md`/`GEMINI.md` stagés à la main, ligne `DEPLOYMENTS.md` insérée dans le bon tableau).
- EN ATTENTE : la numérotation de Q1-Q9 de `/init_projet` (Q4 sautée dans l'énoncé) a provoqué une réponse décalée de l'utilisateur ; interprétation faite sans confirmation.

## Prochaine étape exacte
Lancer `/start creation_llm` dans `D:\ServOMorph\creation_llm`, définir la stack, pousser le commit du protocole ; corriger les écarts de `init_projet.md` (action P1 ci-dessus).

## Question bloquante pour la session suivante
L'élément « df7ee31d — Tableau prévisions » (décider d'une roadmap dédiée : jours ou dates, extension sur plusieurs cases, sous-tâches), mentionné le 2026-10-17 sans être traité : de quel projet ou zone vient-il ?

---

# Session du 2026-10-26

## Décisions prises
- `DOCUMENTATION/` pour `SérénIATech_dev` : création différée jusqu'à l'évaluation du mécanisme dans `Appli_TSA_SDI_TDAH` (décision utilisateur, tests manuels reportés à plus tard).

## Livrables produits ou modifiés
- `D:\ServOMorph\Appli_TSA_SDI_TDAH\tests_manuels.md` : section « Évaluation DOCUMENTATION » (5 questions, seuil 4/5) ajoutée, non commitée dans le dépôt d'Appli.
- Script d'analyse des sessions (scratchpad, hors dépôt) : mesure des lectures de `DOCUMENTATION/`.

## Hypothèses validées / invalidées
- INVALIDE : la consigne « Base de connaissances » de `CLAUDE.md` suffit à déclencher la consultation (0 cas sur 29 sessions locales d'Appli ; historique partiel).
- INVALIDE : la doc d'Appli est à jour (3 specs en écart avec le code ; 15 commits `src/` sans mise à jour documentaire depuis le 2026-10-12).
- EN ATTENTE : les 5 tests actifs ; décision sur les pistes de fiabilisation.

## Prochaine étape exacte
Faire corriger les specs périmées d'Appli (`/start documentation` dans Appli), passer les 5 tests de `tests_manuels.md` d'Appli, puis trancher les pistes et les décisions SérénIATech_dev (action P1 ci-dessus).

## Question bloquante pour la session suivante
L'élément « df7ee31d — Tableau prévisions » (décider d'une roadmap dédiée : jours ou dates, extension sur plusieurs cases, sous-tâches), mentionné le 2026-10-17 sans être traité : de quel projet ou zone vient-il ?

---

# Session du 2026-10-26 (2)

## Décisions prises
- v5.22 : `/close` trie les actions ouvertes (reste dans `signals.md` ce qui appelle une action ou une décision proche, plafond 20 ; le reste dans `_contexte/backlog.md`, non chargé par `/start`), retire les entrées traitées, promeut les urgentes, contrôle la péremption ; ligne de renvoi hors plafond.
- Version v5.22 (et non v6.0) : aucune migration imposée. Findings de revue de code : règle gardée en spécifique projet (le kit n'a pas d'étape générique de revue).
- Appli_TSA_SDI_TDAH applique la v5.22 à la main (pas de `/update`) ; son `close.md` générique est plus ancien (sans 3-bis ni puce étape 13/15) : réalignement complet non engagé.

## Livrables produits ou modifiés
- `.claude/commands/close.md` et `templates/.claude/commands/close.md` : étapes 4, 13, 15 (commit `0f8783b`).
- `templates/_contexte/signals.md`, `Protocole_start_close_context.md`, `DOCUMENTATION/` (guide, glossaire), `CHANGELOG.md`, `README.md`, `scripts/check_kit.py` (`backlog.md` en fichier de sortie connu) : commit `0f8783b`, poussé à la clôture.
- `tests_manuels.md` : section « /close v5.22 » ajoutée.

## Hypothèses validées / invalidées
- VALIDE : `check_kit.py` passe (exit 0). `check_docs.py` échoue sur l'écart ancien (commit `26b9cdd4`), sans lien.
- EN ATTENTE : comportement réel du nouveau tri sur un `/close` de projet (aucun test exécuté).
- INVALIDE : `Appli_TSA_SDI_TDAH` possède `_docs/protocole_vibecoding.md` (fichier absent).

## Prochaine étape exacte
Faire passer la section « /close v5.22 » de `tests_manuels.md` dans un projet à plus de 20 actions ouvertes, puis trancher l'alignement de `_docs/protocole_vibecoding.md`.

## Question bloquante pour la session suivante
L'élément « df7ee31d — Tableau prévisions » (décider d'une roadmap dédiée : jours ou dates, extension sur plusieurs cases, sous-tâches), mentionné le 2026-10-17 sans être traité : de quel projet ou zone vient-il ?

---

# Session du 2026-10-27

## Décisions prises
- `/update` v5.22 vers `SérénIATech_dev` limité à `close.md` (`start.md`, `create_memory.md`, `ollama_call.py`, `CLAUDE.md` déjà alignés ; `AGENTS.md`/`GEMINI.md` non touchés) ; permission `menage_zone.py` du frontmatter conservée à la main.
- Le report des ajouts propres à Appli (concision dans `CLAUDE.md`, garde-fou de pause Discord) n'est pas engagé.

## Livrables produits ou modifiés
- `SérénIATech_dev/.claude/commands/close.md` : v5.22, commit `61b8e47` (hors dépôt du kit).
- `DEPLOYMENTS.md` (gitignoré) : ligne `SérénIATech_dev` passée à v5.22, 2026-10-27.
- `_contexte/signals.md`, `contexte.md`, archives : mis à jour.

## Hypothèses validées / invalidées
- VALIDE : bloc `SPECIFICITES PROJET` de la cible restauré depuis `HEAD` après écrasement lors de la copie (diff tronqué à 40 lignes non relu) ; une seule paire de marqueurs.
- INVALIDE : « `/update` copie sans perte » — le frontmatter de `close.md` n'est pas protégé (action P1 ci-dessus).
- EN ATTENTE : comportement réel du tri backlog dans `SérénIATech_dev` et Appli.

## Prochaine étape exacte
Ouvrir une session sur `SérénIATech_dev` : rejouer les scénarios 2 à 6 de `/start` et `/close` puis le test « /close v5.22 » (`tests_manuels.md`).

## Question bloquante pour la session suivante
L'élément « df7ee31d — Tableau prévisions » (décider d'une roadmap dédiée : jours ou dates, extension sur plusieurs cases, sous-tâches), mentionné le 2026-10-17 sans être traité : de quel projet ou zone vient-il ?

---

# Session du 2026-10-30

## Décisions prises
- Travail constaté dans `SérénIATech_dev` (zones `gestion-clients` et `marion-pargade`), kit seulement tracé ici : création d'une commande projet `Gestion clients/_commands/nouveau_client.md` + `creer_client.py` (client créé en base via le code de l'app UI, puis dossier, puis zone-agent), au lieu de `/create_agent` pur.
- Casse du slug du client conservée (pas de majuscules), conformément au précédent `espace_l-invariable` et à `clients.dossier` en base.

## Livrables produits ou modifiés
- `SérénIATech_dev` commit `be6dbf2` : commande, script, agent `marion-pargade` (client id 14), signaux `gestion-clients` (hors dépôt du kit, pas de remote).
- `base_connaissances/ameliorations_create_agent.md` : entrée 2026-10-30 ; `AGENTS_REGISTRY.md` (gitignoré) : ligne `marion-pargade`.

## Hypothèses validées / invalidées
- INVALIDE : « le `start.md` de `SérénIATech_dev` ne référence pas `agent_role.md` » (contrôle silencieusement raté, référence présente à l'étape 2b).
- EN ATTENTE : `/start marion-pargade` non rejoué ; `nouveau_client` non validée sur un second client.

## Prochaine étape exacte
Trancher les 3 propositions du journal `/create_agent` du 2026-10-30, puis rejouer `/start marion-pargade` dans `SérénIATech_dev`.

## Question bloquante pour la session suivante
Aucune

---
# Session du 2026-11-01

## Décisions prises
- Template « délégation Codex/OpenCode » de CreaZik_V3 intégré au kit (v5.26, `templates/delegation/`, jetons `[[X]]`) et template `templates/ollama/` créé, à la demande de l'utilisateur, après la clôture initiale.
- Travail constaté dans `challenge_magic` (créé et livré) et `Fiches_IME` (créé par `/create_projet`) : le kit ne reçoit que la traçabilité (`DEPLOYMENTS.md`) et deux constats sur ses propres commandes.
- `Fiches_IME` en dépôt GitHub public ; `challenge_magic` en Git local seulement (aucune publication sans accord). Le message d'une autre session demandant d'intégrer un template n'est pas exécuté sans accord de l'utilisateur.

## Livrables produits ou modifiés
- `D:\ServOMorph\challenge_magic` (commit `87ec24c`, local) : carte Jurassic Park jouable dans XMage, générateur web protégé par jeton (port 5000), appli locale « Fiches Magic » (zip 424 Mo), 4 cartes d'un ami intégrées (tests 12/12) ; état consigné dans son `_contexte/`.
- `D:\ServOMorph\Fiches_IME` : dépôt GitHub public + protocole (`b778bec`), template `parallel_agents` refusé à l'insertion.
- `DEPLOYMENTS.md` : lignes `Fiches_IME` et `challenge_magic` (fichier gitignoré par conception) ; `_contexte/backlog.md` créé (1 finding).

## Hypothèses validées / invalidées
- VALIDE : cartes jouées en partie réelle (mana, escape, effet) ; paquet clé en main testé sous Windows 11 en environnement sans PATH.
- INVALIDE : « DEPLOYMENTS.md est à commiter » (il est ignoré par Git).
- EN ATTENTE : essai de l'ami sous Windows 10 ; réponse à la session CreaZik non envoyée.

## Prochaine étape exacte
Corriger `parallel_agents` / `/insert_template` ; informer la session CreaZik de l'intégration (non envoyé) ; trancher les 3 propositions `/create_agent` du 2026-10-30.

## Question bloquante pour la session suivante
Aucune

---
# Session du 2026-11-03

## Décisions prises
- `/init_projet D:\xmage-test` exécuté : zone `xmage`, première zone, git initialisé à la demande (dossier sans `.git`), `AGENTS.md` et `GEMINI.md` créés, pas d'agent, pas de backup rclone.
- Objectif et stack de `xmage-test` déduits du contenu du dossier (non fournis par l'utilisateur) ; à valider.

## Livrables produits ou modifiés
- `D:\xmage-test` (commit `40a567c`, local) : protocole vibecoding déployé.
- `DEPLOYMENTS.md` : ligne `xmage-test` (fichier gitignoré par conception, donc hors commit).
- Aucun fichier de commande ou de template du kit modifié : pas de bump de `CHANGELOG.md`.

## Hypothèses validées / invalidées
- VALIDE : `/init_projet` s'exécute de bout en bout sur un dossier existant sans `.git` ni `.claude/`.
- INVALIDE : « Q4 = oui implique un dépôt existant » ; l'étape 5 échouerait sans `git init`, non prévu par la commande.
- EN ATTENTE : relecture par l'utilisateur de l'objectif et de la stack de `xmage-test`.

## Prochaine étape exacte
Corriger `init_projet.md` (étapes 5 et 7 + cas Q4 = oui sans `.git`), puis trancher les 3 propositions `/create_agent` du 2026-10-30.

## Question bloquante pour la session suivante
Aucune

---

# Session du 2026-11-06 (suite : phase 2)

## Décisions prises
- Phase 1 (fondations) et phase 2 (audit du kit) de `roadmap_fondations.md` closes ; `check_docs.py` ignore désormais le frontmatter dans le contrôle append-only du journal.
- Tri des actions P1 validé par l'utilisateur : 12 actions vers le backlog, 2 doublons retirés, 1 laissée faute de `réf:` précis ; 20 actions P1 restent (plafond atteint).
- Guides DOCUMENTATION en retard confiés à l'agent `documentation` (triage dans son `signals.md`, ajouté à ce `/close`).

## Livrables produits ou modifiés
- `scripts/check_docs.py` : contrôle append-only du journal limité au corps (passe, exit 0).
- `llms.txt` : version v5.27, 9 commandes et 2 scripts de contrôle ajoutés. `README.md` : § État actuel ramené à la v5.27.
- `_contexte/backlog.md` : 14 entrées ajoutées (12 triées, détection Codex, retex de `/maintenance`).
- `roadmap_fondations.md`, `.claude/memory.md` (entrée « traçage des échanges »).

## Hypothèses validées / invalidées
- VALIDE : `check_kit.py`, `check_docs.py` et `pytest` (29 passés, 1 ignoré) passent.
- INVALIDE : retex de `/maintenance` du 2026-11-06 non transcrit avant le compactage -> refait en backlog.
- EN ATTENTE : détection d'une session Codex.

## Prochaine étape exacte
Phase 3 de `roadmap_fondations.md` : création de l'agent PEDAGOGIE par `/create_agent` (périmètre d'écriture limité à `PEDAGOGIE/`, sans publication Netlify), puis choix du parcours.

## Question bloquante pour la session suivante
Aucune
---
# Session du 2026-11-08 (suite)

## Décisions prises
- Phase 4 close sur validation de l'utilisateur ; test Gmail, Agenda et Drive reporté (connecteurs non autorisés), tracé en backlog.
- Constats de l'audit relayés à la session ouverte « Business SerenIA Tech » par `SendMessage` ; reformulation contrôlée et corrigée (patch du diff avant toute restauration, archivage au lieu de suppression), application validée par l'utilisateur dans sa session.
- Script de relevé de consommation d'abonnement abandonné par l'utilisateur ; `/usage` reste la source du quota.

## Livrables produits ou modifiés
- `roadmap_fondations.md` : phase 4 [FAIT], test des connecteurs [reporté].
- `_contexte/signals.md`, `_contexte/contexte.md`, `_contexte/backlog.md`, `README.md`, `CHANGELOG.md` (v5.30).
- `SérénIATech_dev` : aucune modification par cette session (renommage et archivage faits par la session Business, d'après son message).

## Hypothèses validées / invalidées
- VALIDE : la session « Business SerenIA Tech » n'est pas l'origine de la modification du 2026-11-07 9h11 (déclaration de cette session, non recoupée).
- INVALIDE : « perte de contenu » dans linkedin et roberto -> rangement, sauf le bloc roberto du 2026-10-20 présent seulement dans HEAD.
- EN ATTENTE : origine de la modification de 9h11 ; décision sur le bloc roberto ; test des connecteurs.

## Prochaine étape exacte
Faire `/compact`, puis choisir la phase suivante : phase 3 (PEDAGOGIE, mise de côté) ou phase 5 (analyse fonctionnelle). Aucune phase n'est commencée sans confirmation écrite.

## Question bloquante pour la session suivante
Garder ou déplacer vers `derniere_session.md` de `roberto` le bloc « Dernière session 2026-10-20 » présent seulement dans HEAD ?
---
# Session du 2026-11-09

## Décisions prises
- Phase 5 de `roadmap_fondations.md` (analyse fonctionnelle de `SérénIATech_dev`) close : rapport de 7 fonctionnalités validé par l'utilisateur, inscrit dans la roadmap.
- Indy reste le seul outil de facturation ; l'UI de `SérénIATech_dev` ne fait que le suivi.
- Prospection mail : l'e-mail à froid n'est pas le canal d'acquisition ; Sirène et la base gardées pour qualifier le pipeline, campagnes masquées, rien supprimé.

## Livrables produits ou modifiés
- `roadmap_fondations.md` : phase 5 [FAIT] avec le rapport.
- `_contexte/signals.md`, `_contexte/contexte.md`, `_contexte/archive_sessions.md`, `_contexte/archive_decisions.md`, `README.md`, `CHANGELOG.md` (v5.31), `Protocole_start_close_context.md`.
- `SérénIATech_dev` : lecture seule (code, base SQLite en lecture seule pour les volumes).

## Hypothèses validées / invalidées
- INVALIDE : « veille des appels à projets absente » -> `/veille_app_asso` existe (associations, mensuelle, septembre manquant) ; à fiabiliser.
- EN ATTENTE : transmission du rapport et du finding `Gestion clients` à la session du projet ; décision sur le bloc roberto.

## Prochaine étape exacte
Faire `/compact`, puis phase 6 (plan d'automatisation) ou phase 3 (PEDAGOGIE), sur confirmation écrite. Transmettre le rapport de phase 5 à la session du projet avec l'accord de l'utilisateur.

## Question bloquante pour la session suivante
Transmettre le rapport de phase 5 à la session « Business SerenIA Tech » ou à une autre session de `SérénIATech_dev` ?

---

# Session du 2026-11-09 (suite)

## Décisions prises
- Rapport de phase 5 relayé à la session « Business SerenIA Tech » ; sa reformulation (constats confirmés par lecture) validée depuis VibeObs.
- Ordre révisé accepté par l'utilisateur : 1 > 2 > 5 > 3, 7 en parallèle, 4 après la décision CAE / NOVA.

## Livrables produits ou modifiés
- `roadmap_fondations.md` : relais et ordre révisé ajoutés à la phase 5.
- `_contexte/signals.md`, `_contexte/archive_sessions.md`, `_contexte/contexte.md`, `README.md`, `CHANGELOG.md` (v5.32), `Protocole_start_close_context.md`.

## Hypothèses validées / invalidées
- VALIDE : contrainte CHECK de `devis`, veille de septembre manquante, lignes orphelines de Gestion clients (lecture par la session Business).
- EN ATTENTE : traçage par la session Business ; reprise par les zones ui et gestion-clients ; décision CAE.

## Prochaine étape exacte
Faire `/compact`, puis phase 6 (plan d'automatisation) ou phase 3 (PEDAGOGIE), sur confirmation écrite.

## Question bloquante pour la session suivante
Garder ou déplacer vers `derniere_session.md` de `roberto` le bloc « Dernière session 2026-10-20 » présent seulement dans HEAD ?

---

# Session du 2026-11-10

## Décisions prises
- `/telephone` devient commande par défaut de tout projet créé ou mis à jour par le kit : copie par `/init_projet` (et donc `/create_projet`) et par `/update`, contrôle d'identité à l'étape 10 de `/update`.
- Projet `creation_videos` créé via `/create_projet` (dépôt GitHub public, zone `creation_videos`, stack à définir) ; `telephone.md` copié à la main à la demande de l'utilisateur.

## Livrables produits ou modifiés
- `templates/.claude/commands/telephone.md` (nouveau), `init_projet.md` et `update.md` (kit + template), `README.md`, `llms.txt`, `CHANGELOG.md` (v5.34), `tests_manuels.md`, `_contexte/`.
- `init_projet.md` étapes 5 et 7 (AGENTS.md/GEMINI.md stagés, ligne `DEPLOYMENTS.md` dans le tableau « Projets ») : correction déjà présente dans l'arbre de travail, action de signals retirée ; `check_kit.py` passe.

## Hypothèses validées / invalidées
- VALIDE : `check_kit.py` et `check_docs.py` passent après les modifications.
- EN ATTENTE : `/init_projet` et `/update` jamais exercés avec la copie de `telephone.md` (test manuel consigné).

## Prochaine étape exacte
Jouer le test manuel de copie de `telephone.md` ; suivre la phase 5 et la phase 6 de `roadmap_fondations.md`.

## Question bloquante pour la session suivante
Aucune

---

# Session du 2026-11-10 (suite)

## Décisions prises
- Phase 6 : on attend le plan de l'utilisateur dans la session SérénIATech_dev (aucun plan constaté, aucun commit depuis le 2026-11-08).
- `parallel_agents` n'est pas un template insérable : modèles par agent consommés par `/create_parallel_team` ; retiré de la liste de `/create_projet`.

## Livrables produits ou modifiés
- `.claude/commands/create_projet.md` [TEMPLATES] 17 : `parallel_agents` exclu, renvoi vers `/create_parallel_team`.
- `llms.txt` : `parallel_agents` sorti des templates insérables.
- `init_projet.md` étapes 5 et 7 (kit + template) : correctif fait ici, commité par la session parallèle (`179d65e`).
- `_contexte/signals.md` (action `parallel_agents` retirée), `CHANGELOG.md` (v5.35), `README.md`, `_contexte/contexte.md`.

## Hypothèses validées / invalidées
- VALIDE : `check_kit.py` passe après les deux correctifs.
- EN ATTENTE : affichage réel de la liste des templates de `/create_projet` (9 entrées désormais).

## Prochaine étape exacte
Attendre le plan de la phase 6 ; sinon une action P1 du kit (règle de l'étape 9 de `/close`, frontmatter de `update.md`).

## Question bloquante pour la session suivante
Aucune

---

# Session du 2026-11-11

## Décisions prises
- `llms.txt` aligné sur la version courante du kit (v5.35 au lieu de v5.28), commit `b392ff5`.
- Entrée du backlog sur la liste des templates de `/create_projet` laissée en l'état (arrêt demandé).

## Livrables produits ou modifiés
- `llms.txt` ligne 5 : version corrigée.
- `CHANGELOG.md` (v5.36), `README.md`, `Protocole_start_close_context.md`, `_contexte/`.

## Hypothèses validées / invalidées
- VALIDE : `check_kit.py` passe (exit 0) après la correction.
- EN ATTENTE : plan de la phase 6 de SérénIATech_dev.

## Prochaine étape exacte
Attendre le plan de la phase 6 ; sinon une action P1 du kit (règle de l'étape 9 de `/close`, frontmatter de `update.md`).

## Question bloquante pour la session suivante
Aucune

---

# Session du 2026-11-11 (suite 6)

## Décisions prises
- `/update` fusionne l'`allowed-tools` : liste du kit, plus les permissions ajoutées par le projet (signalées au rapport) ; les retraits du projet ne sont pas conservés.

## Livrables produits ou modifiés
- `.claude/commands/update.md` et miroir template : étape 5 (relevé et réinjection des permissions ajoutées) et étape 10 (contrôle tolérant aux ajouts en fin de ligne) ; `check_kit.py` passe.
- `CHANGELOG.md` (v5.42), `README.md`, `llms.txt`, `Protocole_start_close_context.md` : version alignée.
- `_contexte/signals.md` : action « frontmatter de `close.md` » retirée (traitée) ; contrôle de `SérénIATech_dev` ajouté à l'action de propagation.

## Hypothèses validées / invalidées
- EN ATTENTE : fusion jamais exercée en réel, première occasion au `/update` de `SérénIATech_dev`.
- EN ATTENTE : plan de la phase 6 de SérénIATech_dev.

## Prochaine étape exacte
Étape 4 du plan : propager le kit v5.42 aux projets suivis via `/update` (action « Propager le `/start` v5.40 »), en commençant par contrôler `SérénIATech_dev`. La phase 6 de SérénIATech_dev passe avant dès que son plan est prêt.

## Question bloquante pour la session suivante
Aucune

---

# Session du 2026-11-12

## Décisions prises
- Archivage avant propagation : 11 projets déplacés dans `D:\ServOMorph\archives` (La Rev, jeux_vibecoder, Projet_de_reve, jeu_espace, Participation_GitHub, cliker, Meuniers, VertIA_v2, PromptGuard, REA, IA_Eco-Responsable), déplacés tels quels y compris leurs fichiers non commités ; notés « archivé, exclu de /update » dans `DEPLOYMENTS.md`.
- `crea_zik` : à archiver, mais dossier verrouillé (cause inconnue) ; déplacement manuel par l'utilisateur après redémarrage, exclu de `/update`. 3 lignes retirées de `DEPLOYMENTS.md` (projets absents du disque : Open_Code_Apprentissage, claude-vibecoding-kit, creazik_v2). Les 5 projets hors `D:\ServOMorph` sont tous gardés.
- `/update` : `AGENTS.md` et `GEMINI.md` absents ne sont pas créés (« non pour tous les projets ») ; section « Données sensibles » vide = « Aucun déclaré. » ; `Appli_TSA_SDI_TDAH` garde `scripts/ollama_call.py` (règle du projet) ; étapes `synthese_agents` de `jeu_zombies` déplacées dans ses blocs `SPECIFICITES PROJET` ; retrait du bridge ROBERTO d'`IA_Life` (modification du 2026-09-13) sauvegardé puis conservé.
- Les 7 projets dont une session est ouverte sont reportés (aucun message envoyé aux sessions).

## Livrables produits ou modifiés
- 22 projets en v5.42 par `/update` (un commit par dépôt, fichiers de protocole seulement) ; `Moulin du Sud` commité dans le dépôt parent `Lieux_Hybrides`.
- `DEPLOYMENTS.md` : 22 projets en v5.42, 11 archivés, `crea_zik` à archiver (fichier ignoré par Git, non commité).

## Hypothèses validées / invalidées
- VALIDE : le relevé des sessions ouvertes par le dossier de travail des processus `claude.exe` fonctionne (7 projets concernés).
- EN ATTENTE : `/start` v5.40 pas encore observé dans un projet suivi.
- EN ATTENTE : plan de la phase 6 de SérénIATech_dev.

## Prochaine étape exacte
Mettre à jour les 7 projets restants (`Nettoyage_PC`, `site_internet_ST_v3`, `creation_llm`, `VertIA_v3`, `creation_3d`, `WorldModel`, `creation_videos`) une fois leurs sessions fermées ou leur close fait (relever les sessions avant), puis observer un `/start` en réel dans un projet suivi. La phase 6 de SérénIATech_dev passe avant dès que son plan est prêt.

## Question bloquante pour la session suivante
Aucune

---

# Session du 2026-11-12 (suite)

## Décisions prises
- `/create_agent`, propositions du 2026-10-30 : (a) mode « agent client » écarté (besoin propre à SérénIATech_dev, couvert par sa commande `nouveau_client.md`) ; (b) exception aux MAJUSCULES écartée (règle stricte, cas par cas en [COLLECTE]) ; (c) implémentée.
- `_docs/protocole_vibecoding.md` du kit réaligné par copie de `Protocole_start_close_context.md` (v5.0 → v5.42) ; `/init_projet` copie déjà la version courante.
- `backup_project.py` : non-port pour `Meuniers` (archivé) ; port vers `Rayonne_Toi` reporté (copie divergente, modifications non commitées).
- Constat « `/update` ne rafraîchit pas `_docs/protocole_vibecoding.md` » rangé en backlog.

## Livrables produits ou modifiés
- `.claude/commands/create_agent.md` étape 3 : échec ou sortie vide ≠ absence, contrôle refait avec l'outil dédié.
- `_docs/protocole_vibecoding.md` : réaligné (empreinte identique à la source).
- `_contexte/backlog.md` : 1 finding ajouté.

## Hypothèses validées / invalidées
- VALIDE : relevé des sessions par l'identifiant `--resume` des processus `claude.exe` → dossier de `~/.claude/projects/` : les 7 projets restants ont toujours une session ouverte.
- EN ATTENTE : plan de la phase 6 de SérénIATech_dev.

## Prochaine étape exacte
Relever les sessions ouvertes ; mettre à jour par `/update` les projets restants dont la session est fermée (`Nettoyage_PC`, `site_internet_ST_v3`, `creation_llm`, `VertIA_v3`, `creation_3d`, `WorldModel`, `creation_videos`), puis observer un `/start` en réel dans un projet suivi. La phase 6 de SérénIATech_dev passe avant dès que son plan est prêt.

## Question bloquante pour la session suivante
Aucune

---

# Session du 2026-11-13

## Décisions prises
- Action « skill d'orchestration multi-agents avec ChatGPT » passée de P1 au backlog (`[piste]`).
- Tests réels faits sur un projet et une zone jetables, supprimés après le test (registre et `zones.md` restaurés).

## Livrables produits ou modifiés
- `_contexte/signals.md` : action `/insert_template` close ; action `/create_memory` réduite à la conversion de `/create_agent`.
- `_contexte/backlog.md` : 1 piste ajoutée (skill ChatGPT).

## Hypothèses validées / invalidées
- VALIDE : `/insert_template` ajoute la ligne au registre « Templates installés », sans doublon à la ré-insertion complète (arrêt étape 5) ni partielle (couple présent). Procédure suivie à la main, pas via la skill.
- VALIDE : `/create_memory <alias_zone>` écrit dans `<zone>/_contexte/memory.md`, crée l'en-tête, ne touche pas `.claude/memory.md`.
- EN ATTENTE : plan de la phase 6 de SérénIATech_dev.

## Prochaine étape exacte
Relever les sessions ouvertes ; mettre à jour par `/update` les projets restants dont la session est fermée (`Nettoyage_PC`, `site_internet_ST_v3`, `creation_llm`, `VertIA_v3`, `creation_3d`, `WorldModel`, `creation_videos`), puis observer un `/start` en réel dans un projet suivi. La phase 6 de SérénIATech_dev passe avant dès que son plan est prêt.

## Question bloquante pour la session suivante
Aucune

---

# Session du 2026-11-13 (suite)

## Décisions prises
- `telephone.md` installé dans les seules sessions ouvertes qui ne l'avaient pas : `VertIA_v3` ; la session « Sécurité » est exclue (décision de l'utilisateur).

## Livrables produits ou modifiés
- `D:\ServOMorph\VertIA_v3\.claude\commands\telephone.md` : créé par la session VertIA_v3, empreinte identique à celle du kit (contrôlée dans cette session).
- Aucun fichier du kit modifié hors `_contexte/`.

## Hypothèses validées / invalidées
- VALIDE : procédure « session ouverte » exercée de bout en bout (demande, reformulation contrôlée, validation, accord de l'utilisateur, exécution par la session), via `ListAgents` et `SendMessage`.
- NON VERIFIE : l'association nom de session / dossier a été supposée pour les 6 autres projets testés (`telephone.md` présent dans chacun) ; seule `VertIA_v3` a confirmé son dossier.
- EN ATTENTE : plan de la phase 6 de SérénIATech_dev ; dossier de la session « pilote-74 ».

## Prochaine étape exacte
Relever les sessions ouvertes ; mettre à jour par `/update` les projets restants dont la session est fermée (`Nettoyage_PC`, `site_internet_ST_v3`, `creation_llm`, `VertIA_v3`, `creation_3d`, `WorldModel`, `creation_videos`), puis observer un `/start` en réel dans un projet suivi. La phase 6 de SérénIATech_dev passe avant dès que son plan est prêt.

## Question bloquante pour la session suivante
Dans quel dossier tourne la session « pilote-74 » (`telephone.md` à y installer s'il est absent) ?

---

# Session du 2026-11-14

## Décisions prises
- `/init_projet` (kit + template) : l'alias de zone est proposé par défaut avec le nom du dossier projet ; la question sur la stack est supprimée (placeholder `{{STACK}}` retiré, section « Stack » de `contexte.md` initialisée à « Non définie à la création »). `/create_projet` étape 16 le reprend. Version majeure v6.0 (placeholder supprimé, règle de l'étape 9).

## Livrables produits ou modifiés
- Projet `Agent_Trader` créé par `/create_projet` : `D:\ServOMorph\Agent_Trader`, dépôt GitHub privé `ServOMorph/Agent_Trader`, protocole installé (zone `Agent_Trader`, aucun template ni agent), ligne ajoutée dans `DEPLOYMENTS.md` (gitignoré).
- `.claude/commands/init_projet.md`, `templates/.claude/commands/init_projet.md`, `.claude/commands/create_projet.md`, `templates/_contexte/contexte.md` : modifiés.
- `Protocole_start_close_context.md`, `_docs/protocole_vibecoding.md`, `README.md`, `llms.txt`, `CHANGELOG.md` (v6.0) : alignés. Contrôles `check_kit.py` et `check_docs.py` passants.
- Le travail v5.44 (journal de session) laissé non commité par la session précédente est inclus dans le même commit.

## Hypothèses validées / invalidées
- VALIDE : `/create_projet` exercé de bout en bout en réel (dépôt privé, init, aucun template).
- EN ATTENTE : le nouveau flux (alias par défaut, sans stack) n'a pas été rejoué ; test ajouté à `tests_manuels.md`.
- NON FAIT : le journal de session n'a pas été tenu pendant cette session.

## Prochaine étape exacte
Relever les sessions ouvertes ; mettre à jour par `/update` les projets restants dont la session est fermée (`Nettoyage_PC`, `site_internet_ST_v3`, `creation_llm`, `VertIA_v3`, `creation_3d`, `WorldModel`, `creation_videos`), puis observer un `/start` en réel dans un projet suivi. La phase 6 de SérénIATech_dev passe avant dès que son plan est prêt.

## Question bloquante pour la session suivante
Dans quel dossier tourne la session « pilote-74 » (`telephone.md` à y installer s'il est absent) ?

---

# Session du 2026-11-14

## Décisions prises
- Journal de session `_contexte/journal_session.md` (gitignoré, ajout seul) adopté contre les pertes dues aux `/compact` ; `signals.md`, `contexte.md` et roadmaps restent écrits par `/close` seul, qui l'intègre puis le vide.
- Diffusion aux 9 sessions ouvertes par une version unique contrôlée, appliquée après accord de l'utilisateur dans chaque session ; correctif « gitignoré » envoyé dans un second temps.
- `/update` v5.44 sur les projets sans session ouverte, un par un avec contrôles.
- Constat : une autre session du kit (création d'`Agent_Trader`, v6.0 : `/init_projet` sans question de stack) a clos le kit à 09:45 (commit `7bcd433`) en y incluant le travail v5.44 de cette session ; son bloc « Dernière session » est archivé dans `_contexte/archive_sessions.md`.

## Livrables produits ou modifiés
- Kit v5.44 (`start.md`, `close.md`, `init_projet.md`, `update.md` en kit + template ; `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` ; `.gitignore` ; `check_kit.py` ; `CHANGELOG.md` ; `README.md` ; `llms.txt` ; docs de protocole ; `tests_manuels.md`) : commités dans `7bcd433` (autre session du kit) ; ce `/close` ajoute `_contexte/` et `CHANGELOG.md`.
- 21 projets mis à jour en v5.44 ; règle appliquée dans les blocs projet de 8 sessions ouvertes sur 9.

## Hypothèses validées / invalidées
- VALIDE : `check_kit.py` et `check_docs.py` passent ; 7 contrôles du `/update` passés sur les 21 projets.
- INVALIDE : journal versionné (résidu à chaque `/close`) -> pivot vers gitignoré.
- NON VERIFIE : association nom de session / dossier ; cycle réel du journal ; correctif `.gitignore` chez Creation llm et World Model ; application chez Sécurité.
- EN ATTENTE : plan de la phase 6 de SérénIATech_dev.

## Prochaine étape exacte
Relever les sessions ouvertes ; `/update` v5.44 de `SérénIATech_dev`, puis des projets dont la session est fermée (`Nettoyage_PC`, `site_internet_ST_v3`, `creation_llm`, `VertIA_v3`, `creation_3d`, `WorldModel`, `creation_videos`, `xmage-test`) ; observer un cycle réel du journal. La phase 6 de SérénIATech_dev passe avant dès que son plan est prêt.

## Question bloquante pour la session suivante
Dans quels dossiers tournent les sessions « pilote-74 » (absente de la liste actuelle) et « agent-trader-f8 » (nouvelle) ?

---

# Session du 2026-11-14 (suite)

## Décisions prises
- `/delegation` (kit) : Codex, OpenCode gratuit, Ollama et sous-agents Haiku comme exécutants ; Claude orchestre ; sollicitations limitées (commit/push main, écriture hors projet, exécutant bloqué, irréversible) ; journal `_codex/journal_delegation.md` versionné.
- Commandes à lancement manuel : `disable-model-invocation: true` (description hors contexte du modèle, `/nom` conservé) plutôt qu'un déplacement hors de `.claude/`.
- Corrections de l'audit OpenCode appliquées par `/close` (règle « seul `/close` écrit `signals.md` »).

## Livrables produits ou modifiés
- `DOCUMENTATION/` : 4 guides alignés, 3 guides créés (`f325480`).
- Kit v6.1 (`dee116d`, `45f4f09`, `3eb5736`) : `/delegation`, lanceurs PS 5.1 corrigés, 3 findings du backlog corrigés par Codex ; v6.2 (`dfd802b`) : `/migration_canva`, `disable-model-invocation` sur 4 commandes.
- `_contexte/` : signals, backlog (3 findings retirés), contexte mis à jour par ce `/close`.

## Hypothèses validées / invalidées
- VALIDE : Codex (correctif cadré, 88 s) et OpenCode gratuit (audit, 13 anomalies exactes) utilisables ; `check_kit.py` et `check_docs.py` passent.
- INVALIDE : Ollama pour une synthèse demandant du jugement (bilan superficiel, refait) -> réservé aux textes mécaniques.
- EN ATTENTE : effet réel de `disable-model-invocation` sur `.claude/commands/` ; 5 points Canva « à vérifier ».

## Prochaine étape exacte
Tester `/migration_canva` avec les deux comptes Canva ; au `/start` suivant, constater l'absence des 4 commandes manuelles de la liste des skills. Ensuite : `/update` v5.44 de `SérénIATech_dev` et des projets à session fermée.

## Question bloquante pour la session suivante
Dans quels dossiers tournent les sessions « pilote-74 » et « agent-trader-f8 » ?

---

# Session du 2026-11-15

## Décisions prises
- Garde GPU : jeton VRAM obligatoire auprès de VertIA_v3 ; hook `PreToolUse` dans le kit ; alerte `/compact` au seuil de 600 000 tokens.
- Accès à SérénIATech_dev uniquement par demande à la session `sereniatech_dev` (gardienne), sauf zones shorts et jean-luc-dariol pour leur travail.
- Règle des trois validations avant toute écriture dans un `CLAUDE.md`, `AGENTS.md` ou `GEMINI.md` (v6.3).
- `/update` : étape 0bis, classement des actions ouvertes du projet cible avant toute mise à jour.
- Jeu TopiGzme demandé, livré, testé « ok » par l'utilisateur puis supprimé à sa demande, avec toute mention (fichiers, artifact, journaux). Aucun bilan de ce lot conservé.

## Livrables produits ou modifiés
- Kit v6.4 : `scripts/garde_vram.py`, `alerte_compact.py`, `console_distante.py`, `compact_euros.py`, `.claude/settings.json` ; `/update` et `/telephone` (kit + template) ; `/delegation` ; `DOCUMENTATION/` (protocole de test, système d'apprentissage, prises de contrôle) ; `roadmap_apprentissage.md`, `tests/apprentissage/`.
- Dashboard « VibeObs Dev » publié ; sa mise à jour avec v6.4 reste à faire.

## Hypothèses validées / invalidées
- VALIDE : `check_kit.py` et `check_docs.py` passent, miroirs kit/template identiques.
- EN ATTENTE : garde VRAM, alerte compact et `console_distante.py` non vus en conditions réelles ; cause des deux redémarrages du PC non établie ; session shorts relancée mais non vue en Remote Control.
- INVALIDE : « coupure de 27 minutes » déduite de l'heure de l'événement 6008 (approximative) -> derniers événements réels à 10:27 et 15:11.

## Prochaine étape exacte
Coller la ligne `prises_de_controle` dans `.claude/CLAUDE.md` (trois validations déjà données), relancer les sessions Remote Control tombées, puis mettre à jour le dashboard avec v6.4.

## Question bloquante pour la session suivante
Aucune

---

# Session du 2026-11-16

## Décisions prises
- Retex `/maintenance` : 7 propositions appliquées (contrôles de `check_kit.py`, renvois de `maintenance.md`, test append-only de `check_docs.py`, propositions consignées au journal), 2 écartées, la 6 reportée au backlog.
- Ligne de renvoi vers `prises_de_controle.md` écrite dans `.claude/CLAUDE.md` § Spécificités projet (kit seul), après trois validations.
- `/update` de VertIA_v3 v5.25 → v6.5 mené à bien (commit `b7230f6`) ; Moulin du Sud et World Model à reproposer après leur `/close`.
- Garde VRAM étendu à `gen_images*.py`, `gen_musique.py` et Blender ; diffusé à la zone SHORTS par hook de zone, appliqué par `shorts-c2` après accord de l'utilisateur.
- Mesure RAM/VRAM du passage en CLI différée (sessions en cours).

## Livrables produits ou modifiés
- `scripts/check_kit.py`, `scripts/garde_vram.py`, `ollama_call.py` et ses miroirs, `_codex/run_opencode.ps1` et son miroir, `.claude/commands/create_agent.md`, `maintenance.md`, `llms.txt`, `.gitignore`, `.claude/CLAUDE.md`, tests associés : commités en local.
- `_codex/journal_delegation.md`, briefs E et F, `DEPLOYMENTS.md` : commités à cette clôture.
- Hors kit : VertIA_v3 `b7230f6` ; SérénIATech_dev `2169a1a` (zone SHORTS, par `shorts-c2`).

## Hypothèses validées / invalidées
- VALIDE : essai réel OpenCode `--format json` (13 s) ; contrôles 1 à 7 du `/update` de VertIA_v3 ; blocage à blanc de `gen_images_qwen.py` par le hook de SHORTS (code 2).
- INVALIDE : motif du garde VRAM trop large (faux positifs sur `.py` et `.env.*.example`), corrigé.
- EN ATTENTE : activation réelle du hook de SHORTS (prochain lancement de la session depuis `SHORTS`) ; règle de routage de `/delegation` non écrite ; registre des artifacts toujours non exercé en réel.

## Prochaine étape exacte
Reproposer `/update` v6.5 à Moulin du Sud et World Model après leur `/close` ; relancer la session `shorts-c2` depuis `SHORTS` pour constater que le hook du garde est actif.

## Question bloquante pour la session suivante
Aucune

---

# Session du 2026-11-17

## Décisions prises
- Garde VRAM : un texte cité entre guillemets après echo/printf/Write-Host/Write-Output n'est plus analysé (substitutions `$(...)` et backticks conservées) ; faux positif constaté en session.
- `/delegation` : essai réel de l'outil exigé dans le brief quand un correctif dépend de son format de sortie (tout outil externe).
- `/create_agent` étape 10 : repli sur affichage du message si `Set-Clipboard` échoue (constaté depuis la session).
- `/update` v6.6 appliqué à World Model et Moulin du Sud, `CLAUDE.md` écrit par chaque session après trois validations.

## Livrables produits ou modifiés
- `scripts/garde_vram.py`, `tests/test_garde_vram.py` (9 cas), `.claude/commands/delegation.md` (règle + chemin VertIA réparé), `.claude/commands/create_agent.md`, `base_connaissances/ameliorations_create_agent.md` : commités.
- Hors kit : WorldModel `ba4d382`, Lieux_Hybrides `ed28cb8` ; `DEPLOYMENTS.md` et `AGENTS_REGISTRY.md` (locaux, gitignorés).

## Hypothèses validées / invalidées
- VALIDE : hook VRAM actif dans `shorts-c2` ; `/create_agent` de bout en bout sur projet jetable (supprimé) ; 4 commandes manuelles absentes de la liste des skills.
- INVALIDE : « session shorts introuvable » : elle est listée sous `shorts-c2`.
- EN ATTENTE : repli presse-papier de `/create_agent` non exercé ; la copie du garde VRAM utilisée par SHORTS (copie ou script du kit) n'a pas été vérifiée.

## Prochaine étape exacte
Analyser les actions ouvertes et déléguer celles qui s'y prêtent à des sous-agents ou à Codex (`/delegation`), en mesurant l'économie de tokens.

## Question bloquante pour la session suivante
Aucune

---

# Session du 2026-11-17 (nuit)

## Décisions prises
- Relais téléphone : VibeObs raccordé directement au pont de Roberto (option 1, au lieu du modèle B) ; il transmet les réponses de l'utilisateur mot pour mot et ne décide jamais seul (cas 3 du registre), après relecture à l'utilisateur.
- Mise en place chez Roberto par sa session sur dérogation (cas 4, verbatim) ; trois modes de session : PC (`/telephone off`), écran (`/telephone`), voix (`/telephone roberto`, activé par l'utilisateur seul).
- Tunnel du pont : ouvert par l'utilisateur seul, ni VibeObs ni aucune session ne le connaît ni ne l'ouvre ; après redémarrage du PC, relance manuelle.
- Envoi au téléphone par `send_message.py` de Roberto (UTF-8), jamais `curl` (accents corrompus sous Windows).
- Arrêt complet du relais choisi au clavier (« fin du relais » : sessions repassées en mode habituel, pont arrêté par Roberto, écoute coupée).

## Livrables produits ou modifiés
- `.claude/commands/relais_telephone.md` (nouveau), `.claude/commands/telephone.md` + `templates/.claude/commands/telephone.md` (mode roberto), `.claude/settings.json`, `.gitignore`, `scripts/check_kit.py`, `README.md`, `llms.txt`, `Protocole_start_close_context.md`, `CHANGELOG.md` (v6.9), `tests_manuels.md`, `DOCUMENTATION/30_decisions/prises_de_controle.md` (cas 3 et 4) : commités avec ce `/close`.
- Hors VibeObs : `telephone.md` installé dans VertIA_v3 (`20cfa11`, cas 1) ; 3 commits de Roberto (`df08ff1`, `a37f0c0`, `ec1601c`), non poussés.

## Hypothèses validées / invalidées
- VALIDE : relais dans les deux sens avec VertIA_v3 ; question spontanée de la session arrivée sans retenue malgré un autre mode d'autorisation ; accents corrects via `send_message.py` ; mode Manuel de l'appli coupe le micro.
- INVALIDE : écoute « persistante » (expire au bout de 30 min, à relancer) ; `curl` pour l'envoi ; transcription fiable (« Sous-titres réalisés par l'Amara.org », « wap »).
- EN ATTENTE : `/telephone off` appliqué par VertIA_v3 ; tenue hors du PC sur réseau mobile ; hook PreCompact sur un vrai `/compact` ; économie de tokens de `/delegation` non mesurée.

## Prochaine étape exacte
Faire valider à l'utilisateur les corrections de `/relais_telephone` listées dans l'action « Terminer le relais téléphone », puis diffuser `/telephone roberto` aux autres projets.

## Question bloquante pour la session suivante
Quelles corrections de `/relais_telephone` l'utilisateur valide-t-il (phrase « fin du relais », phrases parasites, « oui » net, état lu dans le fil de conversation, réponse tapée au clavier) ?

---

# Session du 2026-11-17 (soir)

## Décisions prises
- Corrections 1 à 5 de `/relais_telephone` validées une à une par l'utilisateur et écrites : arrêt « fin du relais », phrases parasites ignorées, « oui » net pour une réponse qui engage, état d'une session lu dans son fil, réponse tapée au clavier traitée comme directe (même mention).
- `telephone.md` (mode roberto) diffusé aux projets suivis non archivés par le cas 1 (copie directe, commits locaux) sans activer le mode roberto (activé par l'utilisateur seul) ; `SérénIATech_dev` exclu (gardienne hors ligne).
- Push de tous les projets sur ordre explicite de l'utilisateur : fast-forward après `git fetch`, jamais de force.

## Livrables produits ou modifiés
- `.claude/commands/relais_telephone.md` (5 corrections), `tests_manuels.md`, `CHANGELOG.md` (v6.10), `README.md`, `llms.txt`, `Protocole_start_close_context.md` : commités avec ce `/close`.
- Hors VibeObs : `telephone.md` installé dans 29 projets (28 commits locaux ; Moulin du Sud `6108874`) ; 24 dépôts poussés ; Roberto : `send_message.py` commité (`0f1d4c7`).

## Hypothèses validées / invalidées
- VALIDE : Roberto a commité `send_message.py` seul (contrôlé par `git show --stat`) ; VertIA_v3 déclare `/telephone off` appliqué (déclaration, fil non relu).
- EN ATTENTE : essais réels de la section « Relais téléphone » ; hook PreCompact sur un vrai `/compact` ; économie de tokens de `/delegation` non mesurée.

## Prochaine étape exacte
Valider en conditions réelles la section « Relais téléphone » de `tests_manuels.md` ; intégrer le commit distant d'`AutoClaude` (`git pull --rebase`) sur accord de l'utilisateur ; diffuser `telephone.md` à `SérénIATech_dev` via sa gardienne.

## Question bloquante pour la session suivante
Faut-il intégrer le commit distant d'`AutoClaude` par `git pull --rebase` (réécrit ses 3 commits locaux) ?

---

# Session du 2026-11-18

## Décisions prises
- `/update` v6.10 des projets à session ouverte inactive : VibeObs arrête la session à la demande de l'utilisateur puis met à jour ; 58 actions classées « Plus tard » en bloc sur son choix ; session active ou en attente laissée de côté.
- Test de `/migration_canva` abandonné (automatisation impossible, `playwright` hors service) puis commande supprimée du kit à la demande de l'utilisateur ; historique du `CHANGELOG.md` conservé.
- Push de `creation_videos`, des 5 projets mis à jour et d'`AutoClaude` (`git pull --rebase` sans conflit) sur accord de l'utilisateur.

## Livrables produits ou modifiés
- `.claude/commands/migration_canva.md` supprimé ; `README.md`, `llms.txt`, `CHANGELOG.md` (v7.0), `Protocole_start_close_context.md` : commités avec ce `/close`.
- Hors VibeObs : `/update` v6.10 commités et poussés pour `creation_videos` (`e58efa0`), `WorldModel` (`fe1d6c8`), `creation_llm` (`f2f898a`), `VertIA_v3` (`3058d0b`), `Appli_TSA_SDI_TDAH` (`e97c3ce`), `Roberto` (`7aea4ec`) ; `AutoClaude` poussé (`c644815`).

## Hypothèses validées / invalidées
- VALIDE : les 6 `/update` passent les 7 contrôles (Appli : seul écart la permission `Bash(git log:*)` conservée) ; `pre_push_check.py` à 0 ; l'entraînement GPU de `creation_llm` a survécu à l'arrêt de sa session.
- INVALIDE : automatiser la migration Canva par navigateur piloté -> migration faite à la main par l'utilisateur.
- EN ATTENTE : essais réels de la section « Relais téléphone » ; hook PreCompact sur un vrai `/compact` ; économie de tokens de `/delegation` non mesurée.

## Prochaine étape exacte
Valider en conditions réelles la section « Relais téléphone » de `tests_manuels.md` ; `/update` v6.10 de `creation_3d` et `site_internet_ST_v3` à la fermeture de leurs sessions ; diffuser l'update à `SérénIATech_dev` via sa gardienne.

## Question bloquante pour la session suivante
Aucune

---

# Session du 2026-11-18 (suite)

## Décisions prises
- Projet Shorts extrait de `SérénIATech_dev/Communication/SHORTS` vers `D:\ServOMorph\Shorts` sur ordre de l'utilisateur : copie en lecture seule, rôle de l'agent généralisé à tout demandeur, git local, hook `garde_vram.py` conservé.
- Aucun agent autonome lancé sur les actions ouvertes : aucune n'est réalisable sans l'utilisateur, une session tierce ou une condition externe.
- 5 entrées périmées ou faites retirées du backlog (`com_agents`/Meuniers, REA, IA_Eco-Responsable, creation_llm, agent shorts de SérénIATech_dev).

## Livrables produits ou modifiés
- `D:\ServOMorph\Shorts` : créé, commit `5b5e77f` (hors VibeObs) ; `.claude/commands/shorts.md` : chemin du jeton VRAM corrigé (un caractère de contrôle remplaçait `\v`).
- `DEPLOYMENTS.md` : ligne Shorts ; `_contexte/backlog.md` : 5 entrées retirées.
- Message envoyé à `sereniatech_dev` ; session `shorts-4c` lancée en CLI (confiance du dossier validée par l'utilisateur).

## Hypothèses validées / invalidées
- VALIDE : `garde_vram.py` bloque 4 commandes GPU sans jeton et laisse passer `echo` (test par entrée JSON simulée, aucune commande GPU réelle).
- INVALIDE : « les actions ouvertes se délèguent à des agents autonomes » -> toutes exigent l'utilisateur, une session tierce ou une condition externe.
- EN ATTENTE : réponse de `sereniatech_dev` ; cycle réel d'acquisition et de libération du jeton VRAM par `shorts` ; `/start` de `shorts-4c` ; essais réels « Relais téléphone ».

## Prochaine étape exacte
Valider en conditions réelles la section « Relais téléphone » de `tests_manuels.md` ; suivre la réponse de `sereniatech_dev` sur l'extraction de SHORTS et le `/start` de `shorts-4c` ; `/update` v6.10 de `creation_3d` et `site_internet_ST_v3` à la fermeture de leurs sessions ; diffuser l'update à `SérénIATech_dev` via sa gardienne.

## Question bloquante pour la session suivante
Aucune

---

# Session du 2026-11-19 (suite du 2026-11-18)

## Décisions prises
- Délégation à Codex bloquée par l'utilisateur (quota Plus à ménager) : interrupteur `~/.codex/delegation_bloquee.flag`, contrôle dans `run_codex.ps1` ; consigne « modèle Codex » (31 `AGENTS.md` commités) en suspens, texte final non validé.
- Relais téléphone exercé plusieurs heures : règles « jamais de silence », « réponses courtes », « points toutes les minutes » ajoutées à `relais_telephone.md` ; pont de Roberto corrigé (regroupement, coupures de 15 à 90 s, voix).
- Veille IA (chat, image, vidéo) lancée à la voix et exécutée par VertIA_v3, puis essais comparatifs sous jeton GPU ; VibeObs décide des téléchargements de 20 Go ou moins, jamais des licences ni des installations.

## Livrables produits ou modifiés
- Kit v7.1 : `delegation.md`, `relais_telephone.md`, `run_codex.ps1` (kit et template), `templates/AGENTS.md`, README de la délégation ; `_contexte/relais_idees_veille.md` et `veille_sources_fiables.md` (nouveaux).
- Hors kit : consigne dans 31 `AGENTS.md` (commits locaux) ; rapports de VertIA_v3 (`veille/`, `benchmarks/veille/rapport_resultats.md`).

## Hypothèses validées / invalidées
- VALIDE : `gpt-6.1-sol`, `gpt-6.2-sol` et `gpt-6-astra` acceptés par le binaire de l'application (0.167), `gpt-6.1-sol` refusé par le Codex npm 0.154 ; VertIA_v3 préempte `creation_llm` par le jeton (liste d'urgences, tâche interruptible).
- INVALIDE : « jeton de `creation_llm` jusqu'à 13:54 » (périmé : renouvelé, dernier relevé jusqu'au 2026-11-20 08:46).
- EN ATTENTE : correctifs de Roberto non testés sur un vrai iPhone ; décisions de l'utilisateur sur la veille et le blocage Codex.

## Prochaine étape exacte
Faire trancher le blocage Codex et les quatre décisions de la veille VertIA_v3 ; recharger l'appli iPhone et rejouer la section « Relais téléphone » de `tests_manuels.md` ; `/update` v5.37 de `SérénIATech_dev` sur accord.

## Question bloquante pour la session suivante
Lever ou garder le blocage de la délégation à Codex, et avec quel mécanisme de limite ?

---

# Session du 2026-11-19 (soir)

## Décisions prises
- Blocage Codex : politique centrale `~/.codex/politique_delegation.json` (modèle, binaire), seuils 50 % sur 5 h et 60 % sur 7 jours lus dans les rollout de Codex, verrou exclusif par appel ; wrapper déterministe plutôt qu'une session LLM gardienne.
- Mode passe-plat (`-Passe`, `_codex/garde_codex.sh`) pour les scripts shell (prompt par tube, `--search`) ; `creation_llm` branché, `modele.sh` supprimé.
- Zone `MAINTENANCE/` créée (rôle sans nom de projet suivi ; écriture sur tout le dépôt, lecture des projets de `DEPLOYMENTS.md`) pour concevoir le template « maintenance », à faire plus tard.

## Livrables produits ou modifiés
- Kit v7.2 : `_codex/run_codex.ps1`, `_codex/garde_codex.sh`, `templates/delegation/` (script, `install.ps1`), `delegation.md`, zone `MAINTENANCE/`, `zones.md`, `base_connaissances/ameliorations_create_agent.md`.
- Hors kit : `~/.codex/politique_delegation.json` ; `creation_llm` commit local `7f71e65`.

## Hypothèses validées / invalidées
- VALIDE : lecture du quota (`rate_limits`) dans les rollout ; verrou (code 4) et seuils (code 5) en profil isolé ; essais réels (tâche en lecture seule, tube avec `--search`, modèle imposé `gpt-6.1-sol`).
- INVALIDE : brancher `creation_llm` sur le wrapper existant (ni `--search` ni tube) -> mode passe-plat.
- EN ATTENTE : diffusion à `CreaZik_V3` et `VertIA_v3` ; deux appels réels simultanés ; consigne des `AGENTS.md`.

## Prochaine étape exacte
Diffuser le wrapper à `VertIA_v3` et `CreaZik_V3` (accord de chaque session), corriger la consigne « modèle Codex » des `AGENTS.md` (trois validations), puis trancher le flag ; faire trancher les quatre décisions de la veille `VertIA_v3` ; `/start maintenance` pour le template.

## Question bloquante pour la session suivante
Lever le flag de blocage de la délégation à Codex une fois le wrapper diffusé, ou le garder ?
---
# Session du 2026-11-20

## Décisions prises
- Modèle Codex imposé `gpt-6.2-sol` ; consigne « Modèle Codex » diffusée aux `AGENTS.md` (écriture directe par lot sur les projets sans session ouverte, proposition par message à `VertIA_v3` et `SérénIATech_dev`).
- `run_codex.ps1` : `-DryRun` en code 0 et verdict explicite de `-Statut` (le flag prime sur le quota), après le blocage constaté par `VertIA_v3`.
- Flag de blocage levé par l'utilisateur après le commit du kit ; il reste l'interrupteur d'urgence ; aucune notification aux autres sessions (elles le découvriront).
- Push en fast-forward des commits `AGENTS.md` et wrapper de 22 projets, sur ordre de l'utilisateur.

## Livrables produits ou modifiés
- Kit v7.4 : `_codex/run_codex.ps1`, `templates/delegation/scripts/run_codex.ps1`, `templates/AGENTS.md`, `templates/delegation/README.md`, `.claude/commands/delegation.md`, `CHANGELOG.md`, `README.md` (commits `c4882e3`, `4c805ce`, poussés).
- Hors kit : `AGENTS.md` de 28 projets plus `VertIA_v3` et `SérénIATech_dev` ; wrapper de `CreaZik_V3` et `VertIA_v3`.

## Hypothèses validées / invalidées
- VALIDE : deux appels simultanés sérialisés par le verrou ; `-DryRun` code 0 ; `-Statut` BLOQUEE puis AUTORISEE ; appel réel flag levé réussi (code 0, `gpt-6.2-sol`, 0 NativeCommandError) ; plus aucun `AGENTS.md` en `gpt-6.1-sol` dans `D:\ServOMorph` (parcours à 5 niveaux).
- EN ATTENTE : `.gitattributes` de `creation_llm` ; `VibeObs/AGENTS.md` sans la section.

## Prochaine étape exacte
Trancher le `.gitattributes` de `creation_llm` et la section « Modèle Codex » de `VibeObs/AGENTS.md` ; faire trancher les quatre décisions de la veille `VertIA_v3` ; `/start maintenance` pour le template.

## Question bloquante pour la session suivante
Aucune

---

# Session du 2026-11-20 (soir)

## Décisions prises
- Section « Modèle Codex » ajoutée à `VibeObs/AGENTS.md` après les trois validations (insérée avant « Spécificités projet »).
- Veille IA traitée par `VertIA_v3` seule ; en relais Roberto, VibeObs relaie sans garder en mémoire le contenu des sessions, sauf impact sur le kit ou template réutilisable.
- Périmètre de VibeObs validé comme base : kit de protocole (commandes, templates, `/update`, `DEPLOYMENTS.md`), zones documentation, pedagogie, maintenance, relais téléphone/Roberto et Intercom, délégation Codex/OpenCode/Ollama ; hors périmètre : travail et décisions métier des projets suivis.

## Livrables produits ou modifiés
- `AGENTS.md` : section « Modèle Codex » ajoutée (commit `28bd2a1`).
- `_contexte/contexte.md` (§ Périmètre), `_contexte/signals.md`, `CHANGELOG.md` (v7.5), `README.md`, `DOCUMENTATION/_contexte/signals.md` (action de triage) : mis à jour à la clôture.

## Hypothèses validées / invalidées
- VALIDE : `D:\ServOMorph\creation_llm\.gitattributes` n'existe pas (liste du dossier).
- EN ATTENTE : `.gitattributes` de `creation_llm` ; tri des actions ouvertes selon le périmètre ; les quatre décisions de la veille VertIA ne figurent pas dans le `signals.md` de `VertIA_v3` (session ouverte, aucune écriture) mais dans son rapport `benchmarks/veille/rapport_resultats.md`.

## Prochaine étape exacte
Trier les actions ouvertes de `signals.md` selon le périmètre (conserver, transférer, écarter), une par une ; trancher le `.gitattributes` de `creation_llm` ; `/start maintenance` pour le template.

## Question bloquante pour la session suivante
Aucune
---
# Session du 2026-11-21

## Décisions prises
- `/maintenance` définie (quarantaine `D:\_quarantaine\<date>\` avec `manifeste.md`, purge à 30 jours, refacto en analyse seule, retours et journal versionné) puis exercée pour la première fois sur le kit : lots A (chemins de `DEPLOYMENTS.md`) et B (`relais_idees_veille.md`, veille hors périmètre) exécutés ; C et D reportés en session de travail ; E noté comme écart voulu (section « Modèle Codex » propre à `AGENTS.md`) ; F transmis ; G laissé.
- Intercom agent abandonné (décision de l'utilisateur : les sessions communiquent déjà par `ListAgents` et `SendMessage`) ; `VibeObs Général` prévenu.
- Cinq améliorations de `/maintenance` retenues par l'utilisateur et appliquées (kit v7.7) ; registre des artifacts clôturé par l'utilisateur.
- Tri des actions selon le périmètre : écartées (tri du backlog v5.22 à v5.25, relance des sessions Remote Control, upload Drive d'Appli) ; relais portail IA refusé ; création de `DOCUMENTATION/` chez `SérénIATech_dev` et port `backup_project.py` transférés ; backup rclone de `SérénIATech_dev` conservé.

## Livrables produits ou modifiés
- `.claude/commands/maintenance.md`, `CHANGELOG.md`, `README.md`, `llms.txt`, `Protocole_start_close_context.md` : kit v7.7 (5 améliorations issues du premier essai réel).
- `_contexte/maintenance_historique.md` et `_contexte/maintenance_retours.md` : créés ; `_contexte/relais_idees_veille.md` : en quarantaine (`D:\_quarantaine\2026-11-21\VibeObs\`) ; `DEPLOYMENTS.md` (local, ignoré) : 2 chemins corrigés ; `MAINTENANCE/_contexte/signals.md`, `DOCUMENTATION/_contexte/signals.md` et `tests_manuels.md` : mis à jour.

## Hypothèses validées / invalidées
- VALIDE : premier essai réel de `/maintenance` : étape 0 sans erreur sans historique, quarantaine avec manifeste et origine disparue, historique créé, étape 11 posée (réponse « oui »).
- EN ATTENTE : étape 11 avec réponse « non » ; refacto à étudier non inscrit au backlog faute de validation : `CHANGELOG.md` de 98 Ko.

## Prochaine étape exacte
Confirmer le périmètre de l'abandon d'Intercom puis le retirer ; traiter les écarts reportés par la maintenance ; poursuivre le tri des actions selon le périmètre ; relever les maintenances des projets suivis puis tirer le template (`/start maintenance`).

## Question bloquante pour la session suivante
L'abandon d'Intercom couvre-t-il `INTERCOM_AGENT.md` seulement, ou aussi la messagerie `intercom/` ?

---

# Session du 2026-11-21 (soir)

## Décisions prises
- Tri des actions ouvertes selon le périmètre : écartées (upload Drive d'Appli, évaluation DOCUMENTATION d'Appli, tri du backlog v5.22 à v5.25, relance des sessions Remote Control, pousser les restes sans remote, extraction de SHORTS) ; clôturées par l'utilisateur (relais téléphone, registre des artifacts) ; transférées (port `backup_project.py` à Rayonne_Toi, `DOCUMENTATION/` de SérénIATech_dev à `sereniatech_dev`).
- Règle d'IA locale de VertIA_v3 : relais refusé, puis proposée comme règle du `CLAUDE.md` du kit (action P2, trois validations à lancer sur accord).
- Codex : `.gitattributes` `* text=auto eol=lf` créé dans `creation_llm` (non commité), `AGENTS.md` de Moulin du Sud commité (`3b41aac`), push de `Lieux_Hybrides` refusé (pas de `main` distant) et question posée dans la zone Moulin du Sud.
- Kit v8.0 : `/create_team`, son guide, `INTERCOM_AGENT.md` et `templates/team_TEMPLATE.md` supprimés (modifications d'une session de la zone kit lancée par erreur, relues et validées ici) ; backlog trié de 21 à 15 entrées.

## Livrables produits ou modifiés
- `_contexte/signals.md`, `_contexte/backlog.md`, `_contexte/contexte.md`, `tests_manuels.md`, `CHANGELOG.md` (v8.0), `README.md`, `llms.txt`, `Protocole_start_close_context.md` : mis à jour.
- `init_projet.md` (kit et template), `create_parallel_team.md`, `DOCUMENTATION/`, `scripts/check_kit.py` : modifiés par la session de la zone kit lancée par erreur, contrôlés (`check_kit.py` passe, miroir identique).
- Hors dépôt : `creation_llm/.gitattributes`, `Rayonne_Toi/_contexte/signals.md`, `Moulin du Sud/_contexte/signals.md` : écrits, non commités.

## Hypothèses validées / invalidées
- VALIDE : l'`AGENTS.md` de Moulin du Sud était suivi par Git (sous `lieux/`), contrairement au signal ; `CreaZik_V3` est à jour avec `origin/main` et sa stack est renseignée.
- EN ATTENTE : décision de l'utilisateur sur l'action de la Maintenance (écarts reportés, droits sur `DOCUMENTATION/20_guides/`) ; entrée de backlog « harmonisation `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` » et 14 suivantes ; fin de maintenance : la session Maintenance dit ne rien faire dans le dossier du kit.

## Prochaine étape exacte
Poursuivre le tri du backlog (15 entrées) à partir de l'harmonisation `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` ; instruire la règle d'IA locale de VertIA_v3 pour le `CLAUDE.md` du kit (trois validations) ; diffuser `init_projet` par `/update`.

## Question bloquante pour la session suivante
Aucune

---
# Session du 2026-11-23

## Décisions prises
- Règle d'IA locale de VertIA_v3 acceptée après les trois validations (session commencée le 2026-11-22) et écrite dans `.claude/CLAUDE.md` et `templates/.claude/CLAUDE.md`, section `## IA locale et GPU`.

## Livrables produits ou modifiés
- `.claude/CLAUDE.md`, `templates/.claude/CLAUDE.md` : section ajoutée ; `CHANGELOG.md` v8.1, `_contexte/signals.md`, `_contexte/contexte.md`, `_contexte/archive_decisions.md` : mis à jour, commités.

## Hypothèses validées / invalidées
- EN ATTENTE : diffusion de la règle par `/update` ; fonctionnement de `vertia_gen.py` non relu ; seuil de 20 appels non mesuré.
- EN ATTENTE (reporté) : compactage automatique (ligne `auto`) et non-échec du compactage, dans `tests_manuels.md` ; action de la Maintenance (`control_PC/analysis`, droits sur `DOCUMENTATION/20_guides/`) retirée des signaux sans décision consignée de l'utilisateur sur `control_PC`.
