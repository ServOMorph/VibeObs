# Signals — maintenance   (MAJ 2026-11-24)

## Actions ouvertes
<!-- ≤ 20 entrées (ligne « Backlog » exclue) ; dette et findings non urgents -> _contexte/backlog.md -->
- [P1|ouvert] Exercer le template `/maintenance` : l'insérer dans les projets suivis et lancer la maintenance de chacun.
  - Fait au 2026-11-24 : template inséré dans `D:\ServOMorph\VertIA_v3` (non commité par cette zone) ; bloc « SPÉCIFICITÉS PROJET » renseigné par la session VertIA_v3 le 2026-11-23 (limite prudente : aucun changement de comportement, refacto en analyse seule ; chemins sensibles = liste initiale plus `_orchestration/state/` et `engines/`, ajouts propres à VertIA). `/maintenance` a tourné jusqu'au rapport dans la session CLI `Maintenance VertIA_v3` (processus `claude.exe` 10556 au moment du `/close`) : 1012 tests passent, quatre lots proposés ; lot A (suivi de 3 fichiers non suivis, et sort de `regles_validation.md` dans VertIA_v3 : garder ou quarantaine) en attente de décision de l'utilisateur dans cette session. Une première session CLI (processus 13460) s'est figée et a été arrêtée.
  - Restent : décisions sur les lots A à D de VertIA_v3 ; étapes 10 (journal `maintenance_historique.md`) et 11 (amélioration de la commande) ; vérifier que les frictions sont consignées dans `maintenance_retours.md` de VertIA_v3 ; frictions déjà relevées : `du` et `grep` récursifs arrêtés par manque de mémoire (étape 3), rapport devenu illisible par `console_distante.py lire` (seule la fin de l'écran est visible) ; insérer ensuite dans `creation_llm` (session ouverte), `sereniatech_dev`, VibeObs ; relever les maintenances déjà en place dans les projets suivis ; `README.md`, `llms.txt`, `CHANGELOG.md` du kit à compléter pour le template (VibeObs Général) ; guide d'insertion de templates absent (action P2 chez Documentation).
  - fait quand: `/maintenance` a tourné de bout en bout dans au moins un projet suivi, ses frictions sont consignées et les améliorations proposées au kit.
  - réf: `templates/maintenance/`, `MAINTENANCE/regles_validation.md`, `D:\ServOMorph\VertIA_v3\.claude\commands\maintenance.md`, `DEPLOYMENTS.md` (ligne VertIA_v3, fichier ignoré par Git)
- [P1|ouvert] Après un redémarrage du PC : contrôler que le Tableau de bord démarre seul depuis D: et que `ffmpeg` répond avec le nouveau PATH ; puis mettre en quarantaine les originaux C: de `TableauDeBord` et de `ffmpeg` avec `migrer_projet.py quarantaine --confirmer`.
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

## Dernière session (2026-11-24)
# Session du 2026-11-24

## Décisions prises
- VertIA_v3 : limite maintenance/évolution prudente et chemins sensibles confirmés (2026-11-22, téléphone) ; la session VertIA_v3 a écrit le bloc projet le 2026-11-23 avec deux ajouts (`_orchestration/state/`, `engines/`).
- Session CLI figée arrêtée et relancée sur demande de l'utilisateur.

## Livrables produits ou modifiés
- `_contexte/signals.md`, `_contexte/contexte.md` : mis à jour (convertis en fins de ligne LF pour `check_kit.py`). Aucun autre fichier du kit modifié ; dans VertIA_v3, aucune écriture de cette zone.

## Hypothèses validées / invalidées
- VALIDE : `/maintenance` tourne dans VertIA_v3 jusqu'au rapport (1012 tests passent, quatre lots proposés).
- INVALIDE : envoyer Entrée ou Échap à une session CLI figée la débloque (écran inchangé) -> pivot vers arrêt du processus et relance.
- EN ATTENTE : décisions de l'utilisateur sur les lots A à D de VertIA_v3 ; redémarrage du PC pour `TableauDeBord` et `ffmpeg`.

## Prochaine étape exacte
Reprendre la session CLI `Maintenance VertIA_v3` (lire son écran, ou la relancer si elle est fermée) : obtenir les décisions sur les lots A à D, puis étapes 10 et 11, en consignant les frictions.

## Question bloquante pour la session suivante
Lot A de VertIA_v3 : valides-tu le suivi des 3 fichiers non suivis, et `regles_validation.md` de VertIA_v3 : garder dans le dépôt ou quarantaine ?
