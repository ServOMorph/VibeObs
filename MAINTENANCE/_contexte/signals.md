# Signals — maintenance   (MAJ 2026-11-25)

## Actions ouvertes
<!-- ≤ 20 entrées (ligne « Backlog » exclue) ; dette et findings non urgents -> _contexte/backlog.md -->
- [P1|ouvert] Exercer le template `/maintenance` : l'insérer dans les projets suivis et lancer la maintenance de chacun.
  - Fait au 2026-11-25 : template inséré dans `D:\ServOMorph\VertIA_v3`, bloc « SPÉCIFICITÉS PROJET » renseigné (limite prudente ; chemins sensibles complétés). `/maintenance` a tourné jusqu'au rapport (1012 tests passent, quatre lots). Lot A validé et confirmé par la session VertIA_v3 : 3 fichiers en `git add`, non commités (état constaté le 2026-11-25), `regles_validation.md` gardé dans le dépôt. Les 53 dossiers `.tmp*` et `.codex-test*` ont été supprimés le 2026-11-25 par script administrateur (journal de VertIA_v3) ; lien avec le lot B non établi. Aucune session `Maintenance VertIA_v3` ne tourne depuis le redémarrage du PC (2026-11-25 22:34).
  - Restent : relancer `/maintenance` pour les lots restants (B non confirmé, C et D sans trace de décision dans le journal de VertIA_v3) ; étape 10 (`maintenance_historique.md` non trouvé) et étape 11 (amélioration de la commande) ; `_contexte/maintenance_retours.md` de VertIA_v3 est vide : consigner les frictions relevées : `du` et `grep` récursifs arrêtés par manque de mémoire (étape 3) ; rapport illisible par `console_distante.py lire` (seule la fin de l'écran est visible) ; session listée hors ligne par `ListAgents` alors que son processus tournait (contrôler les processus `claude.exe` avant de relancer, un doublon a été lancé puis arrêté). Ensuite : insérer dans `creation_llm`, `sereniatech_dev`, VibeObs ; relever les maintenances déjà en place dans les projets suivis ; `README.md`, `llms.txt`, `CHANGELOG.md` du kit à compléter pour le template (VibeObs Général) ; guide d'insertion de templates absent (action P2 chez Documentation).
  - fait quand: `/maintenance` a tourné de bout en bout dans au moins un projet suivi, ses frictions sont consignées et les améliorations proposées au kit.
  - réf: `templates/maintenance/`, `MAINTENANCE/regles_validation.md`, `D:\ServOMorph\VertIA_v3\.claude\commands\maintenance.md`, `DEPLOYMENTS.md` (ligne VertIA_v3, fichier ignoré par Git)
- [P1|ouvert] Après un redémarrage du PC : contrôler que le Tableau de bord démarre seul depuis D: et que `ffmpeg` répond avec le nouveau PATH ; puis mettre en quarantaine les originaux C: de `TableauDeBord` et de `ffmpeg` avec `migrer_projet.py quarantaine --confirmer`.
  - PC redémarré le 2026-11-25 à 22:34 : contrôles à faire, aucun effectué à ce jour.
  - Chemin `ffmpeg` de `VertIA_v3\_codex\reference\ace_worker_reference.py` corrigé le 2026-11-22 (session VertIA_v3 hors ligne), non commité.
  - fait quand: `C:\Users\raph6\Documents\ServOMorph` ne contient plus que `site_internet_Sereniatech_V2` et `manifeste.md` est complété.
  - réf: `MAINTENANCE/scripts/migrer_projet.py`, `D:\_quarantaine\2026-11-20\manifeste.md`
- [P2|ouvert] Tester `idle_game_auto_claude` depuis D: (branche Godot, 6 modifications non commitées, aucun remote) ; original en quarantaine.
  - fait quand: l'utilisateur confirme que le jeu démarre, ou décide de le supprimer (purge de la quarantaine validée).
  - réf: `D:\ServOMorph\idle_game_auto_claude`, `D:\_quarantaine\2026-11-20\manifeste.md`
- [P2|ouvert] Corriger les chemins C: restants cités ailleurs (balayage du 2026-11-20 : 88 fichiers dans 23 projets) : `DEPLOYMENTS.md` et `AGENTS_REGISTRY.md` (kit), notes `brief.md` et `signals.md` de Shorts (passer par leur zone), `CLAUDE.md` d'Accueil Handicap (Lieux_Hybrides) et de « Pourquoi j'ai pas le droit » (trois validations). Logs et données historiques exclus.
  - fait quand: `balayer_chemins.py D:\ServOMorph <ancienne racine C:> --ignorer pifpafpof` ne liste plus que des logs, de l'historique ou des données voulues.
  - réf: `MAINTENANCE/scripts/balayer_chemins.py`, `DEPLOYMENTS.md`, `AGENTS_REGISTRY.md`
- [P2|ouvert] Retrouver `Agents_IA_V2` (cité par 12 projets de D: et par `PROJETS.md`, absent de C: et D:) : décider recréation ou références mortes.
  - fait quand: emplacement retrouvé, ou références jugées mortes et traitées.
  - réf: `D:\ServOMorph\PROJETS.md`
- [P2|ouvert] Revérifier les 5 lignes périmées de la section C: de `PROJETS.md` (`Agents_IA_V2`, `Affichage_Legal_Entreprise`, `Fine_Tuning`, `gestion-repas-symphonie-equitable`, `Bot Lilo`), non modifiées lors du patch du 2026-11-20.
  - fait quand: section C: de `PROJETS.md` conforme au contenu réel de C:.
  - réf: `D:\ServOMorph\PROJETS.md`
- Backlog : 6 entrées (dette 4, piste 2) — `_contexte/backlog.md`

## Dernière session (2026-11-25)
# Session du 2026-11-25

## Décisions prises
- Lot A de VertIA_v3 : suivre les 3 fichiers non suivis et garder `regles_validation.md` dans le dépôt (confirmé dans la session VertIA_v3).
- Maintenance relancée puis doublon arrêté ; l'ancienne session, qui gardait le rapport, conservée.

## Livrables produits ou modifiés
- `_contexte/signals.md`, `_contexte/contexte.md`, `_contexte/archive_sessions.md` : mis à jour. Aucun autre fichier du kit modifié par cette zone.

## Hypothèses validées / invalidées
- INVALIDE : session « hors ligne » dans `ListAgents` = session fermée (le processus tournait) -> contrôler les processus avant de relancer.
- EN ATTENTE : lots B à D de VertIA_v3 ; contrôles après redémarrage pour `TableauDeBord` et `ffmpeg`.

## Prochaine étape exacte
Après le redémarrage du 2026-11-25 : contrôler que le Tableau de bord démarre seul depuis D: et que `ffmpeg` répond ; puis relancer `/maintenance` dans VertIA_v3 pour les lots restants et les étapes 10 et 11.

## Question bloquante pour la session suivante
Aucune
