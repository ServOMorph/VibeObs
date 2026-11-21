# Signals — maintenance   (MAJ 2026-11-20)

## Actions ouvertes
<!-- ≤ 20 entrées (ligne « Backlog » exclue) ; dette et findings non urgents -> _contexte/backlog.md -->
- [P1|ouvert] Définir le périmètre de la maintenance et les règles de validation (sécurité d'abord) avant toute roadmap : racines concernées, types d'éléments, exclusions absolues, actions autorisées par type, fréquence, purge de la quarantaine, contrôle de VertIA avant tout appel Ollama. Aligner `agent_role.md`, resté en lecture seule sur les autres projets alors que l'utilisateur a décidé le 2026-11-19 d'élargir à la lecture, l'écriture et la suppression (projets et PC).
  - Fusionnée le 2026-11-20 avec « Créer le template maintenance » (demande de VibeObs Général, confiée à cette zone) : maintenance complète d'un projet, fichiers et code, kit sans oubli pour des projets propres, à insérer dans les projets suivis (`creation_llm`, `sereniatech_dev`, `vertia`, VibeObs, d'autres ensuite). `/maintenance` du kit réécrite en socle générique v7.6 (12 étapes, quarantaine, refacto en analyse seule, journal, amélioration de la commande), non commitée. Restent : relever les maintenances déjà en place dans les projets suivis, trancher le délai de purge de la quarantaine (fixé à 30 jours pour le kit), tirer le template de la commande. 2026-11-21 (racine) : premier essai réel de `/maintenance` sur le kit ; la commande passe en v7.7 avec cinq améliorations (`allowed-tools` `du` et `grep`, étape 3 éléments ignorés volumineux, étape 9 en-tête de `manifeste.md`, suppression non commitée signalée et action « transférer à la session propriétaire », bloc kit étape 4 lecture des chemins de `DEPLOYMENTS.md`), à généraliser dans le template ; détail dans `_contexte/maintenance_retours.md` de la racine.
  - fait quand: les règles sont écrites et validées par l'utilisateur, `agent_role.md` reflète les droits décidés, le template de base est défini (périmètre complet de la maintenance) et inséré dans au moins un projet suivi, avec ses contrôles exercés.
  - réf: `MAINTENANCE/agent_role.md`, `_contexte/contexte.md` (décisions 2026-11-19 et 2026-11-20), `.claude/commands/maintenance.md`, `DOCUMENTATION/20_guides/maintenance_du_kit.md`, `DEPLOYMENTS.md`
- [P1|ouvert] Après un redémarrage du PC : contrôler que le Tableau de bord démarre seul depuis D: et que `ffmpeg` répond avec le nouveau PATH ; puis mettre en quarantaine les originaux C: de `TableauDeBord` et de `ffmpeg` avec `migrer_projet.py quarantaine --confirmer`.
  - fait quand: `C:\Users\raph6\Documents\ServOMorph` ne contient plus que `site_internet_Sereniatech_V2` et `manifeste.md` est complété.
  - réf: `MAINTENANCE/scripts/migrer_projet.py`, `D:\_quarantaine\2026-11-20\manifeste.md`
- [P1|ouvert] Corriger le chemin `ffmpeg` C: de `ace_worker_reference.py` de VertIA_v3 en passant par sa session (ouverte, validation dans sa session) ; bloque la quarantaine de l'original `ffmpeg`.
  - fait quand: le fichier pointe vers `D:\ServOMorph\ffmpeg`, accord de la session VertIA_v3 tracé.
  - réf: `D:\ServOMorph\VertIA_v3\_codex\reference\ace_worker_reference.py`
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

## Dernière session (2026-11-20)
<!-- Écrasé intégralement par /close. Synthèse < 25 lignes. -->
# Session du 2026-11-20

## Décisions prises
- Droits élargis par l'utilisateur (lecture, écriture, suppression dans les autres projets et sur le PC) ; toute suppression passe par la quarantaine `D:\_quarantaine\<date>\` avec `manifeste.md`, validation par lot ; GitHub : guidage seul ; scripts Python au maximum ; Ollama après contrôle de VertIA.
- Migration des projets de `C:\...\ServOMorph` vers `D:\ServOMorph` : copie vérifiée par SHA-256, chemins corrigés, original en quarantaine. Ordre du 2026-11-20 : ne pas toucher au site `site_internet_Sereniatech_V2`.

## Livrables produits ou modifiés
- `MAINTENANCE/scripts/migrer_projet.py` (+ `tests/test_migrer_projet.py`, 12 tests passés), `lancer_sur_bureau.py`, `balayer_chemins.py` : créés.
- 11 projets et 1 doublon (`whisper`) en quarantaine ; `Schumfl.txt` déplacé ; `nul` supprimé ; `TableauDeBord` et `ffmpeg` copiés sur D: (originaux gardés) ; PATH utilisateur, raccourci Démarrage et `PROJETS.md` mis à jour ; chemin `ffmpeg` corrigé dans CreaZik_V3 et Shorts.
- Outil `D:\_outils\venv_bureaux` (pyvda) : Tableau de bord relancé sur le bureau « Accueil », interface dans Chrome (profil ServO Morph).

## Hypothèses validées / invalidées
- VALIDE : la chaîne copier, vérifier, corriger les chemins, quarantaine a traité 12 éléments sans écart ; `nul` supprimé via `[IO.File]::Delete` sur chemin `\\?\`.
- INVALIDE : `Remove-Item` suffit pour `nul` ; `run.py` ouvrait l'interface dans Chrome (navigateur par défaut : Firefox, corrigé) ; les dépendances de `pifpafpof` étaient connues avant son déplacement (Lieux_Hybrides et password_manager_pro pointaient vers son `.env`, corrigé après coup).
- EN ATTENTE : démarrage automatique du Tableau de bord et `ffmpeg` après redémarrage ; test de `idle_game_auto_claude` sur D:.

## Prochaine étape exacte
Redémarrer le PC, contrôler le Tableau de bord et `ffmpeg`, mettre leurs originaux en quarantaine (actions P1), puis définir le périmètre et les règles de validation.

## Question bloquante pour la session suivante
Quelles racines, en plus de `D:\ServOMorph`, entrent dans le périmètre de la maintenance ?
