# Signals — maintenance   (MAJ 2026-11-22)

## Actions ouvertes
<!-- ≤ 20 entrées (ligne « Backlog » exclue) ; dette et findings non urgents -> _contexte/backlog.md -->
- [P1|ouvert] Exercer le template `/maintenance` : l'insérer dans les projets suivis et lancer la maintenance de chacun.
  - Fait au 2026-11-22 : `agent_role.md` aligné (périmètre = projet où la maintenance est lancée), `MAINTENANCE/regles_validation.md` validé par l'utilisateur, `templates/maintenance/` créé (commit `238ac84`) et documenté (commit `60c631e`), template inséré dans `D:\ServOMorph\VertIA_v3` (`.claude/commands/maintenance.md`, `regles_validation.md`, `_contexte/maintenance_retours.md`, non commité), bloc « SPÉCIFICITÉS PROJET » renseigné, limite maintenance/évolution et chemins sensibles à confirmer. La session CLI `Maintenance VertIA_v3` a été fermée avant la confiance du dossier : `/maintenance` n'a pas tourné.
  - Restent : lancer `/maintenance` sur VertIA_v3 (session CLI, écran lu par `console_distante.py`, frictions notées dans `maintenance_retours.md`), insérer ensuite dans `creation_llm` (session ouverte), `sereniatech_dev`, VibeObs ; relever les maintenances déjà en place dans les projets suivis ; `README.md`, `llms.txt`, `CHANGELOG.md` du kit à compléter pour le template (VibeObs Général) ; guide d'insertion de templates absent (action P2 chez Documentation).
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

## Dernière session (2026-11-22)
# Session du 2026-11-22

## Décisions prises
- Périmètre : la racine d'une maintenance est le projet où elle est lancée. Règles de validation validées (fréquence mensuelle, purge à 30 jours, quarantaine D:).
- Template inséré dans VertIA_v3 selon le README du template (commande dans `.claude/commands/`), l'insertion standard ne convenant pas.

## Livrables produits ou modifiés
- `MAINTENANCE/agent_role.md`, `MAINTENANCE/regles_validation.md`, `templates/maintenance/` : commités (`238ac84`).
- `VertIA_v3` : template maintenance et chemin `ffmpeg` corrigé, non commités ; `DEPLOYMENTS.md` : ligne ajoutée (fichier ignoré par Git).

## Hypothèses validées / invalidées
- VALIDE : l'insertion du template exige un placement manuel (commande, règles, retours) ; `/insert_template` copie tout sous `VibeObs/`.
- INVALIDE : `/exit` envoyé par `console_distante.py` ferme une session (elle y répond comme à un message).
- EN ATTENTE : exercice réel de `/maintenance` sur VertIA_v3 ; redémarrage du PC pour `TableauDeBord` et `ffmpeg`.

## Prochaine étape exacte
Relancer la session CLI `Maintenance VertIA_v3` (`/maintenance`), valider la confiance du dossier, suivre l'écran, noter les frictions.

## Question bloquante pour la session suivante
Quelle limite maintenance/évolution et quels chemins sensibles déclarer pour VertIA_v3 ?
