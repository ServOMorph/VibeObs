# Roadmap — Fondations VibeObs et vitrine SérénIATech

Créée le 2026-11-05. But : asseoir les bases pour gagner du temps plus tard, pas aller vite.
Toute nouvelle demande de l'utilisateur est rangée ici (cf. `/telephone`, § Chaque nouvelle demande).

## Cadre
- Travail depuis un téléphone : mode `/telephone`, questions une par une, réponse en un clic.
- Archivage, jamais de suppression. Préparation seule : toute action sortante validée par l'utilisateur.
- Données sensibles : lecture autorisée, traitement local (Ollama), rien vers un service externe.
- Un rapport par phase, validation de l'utilisateur entre chaque phase.
- Phase 3 (agent PEDAGOGIE) retirée le 2026-11-09 sur décision de l'utilisateur ; conservée dans `_contexte/backlog.md`.

## Phase 1 — Fondations du pilotage [FAIT]
- [fait] Questions une par une (mémoire projet).
- [fait] Commande `/telephone` (format court, choix en un clic, rangement dans ce planning).
- [fait] Règle des sessions ouvertes enregistrée (mémoire projet) ; exercée avec site et creation_llm. Conflit de traçage tranché (l'agent de la session ouverte trace dans son propre `signals.md`). Détection Codex : en backlog.
- Retex du mode téléphone : premières corrections intégrées à la commande.
- Gate : règle des sessions validée et enregistrée, mode téléphone utilisé sur une session complète.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 2 — Audit et nettoyage du kit [FAIT]
- [fait] `comptes_google.json` retiré du suivi Git et ignoré (historique public non réécrit, décision de l'utilisateur).
- [fait] Lot A archivé (`list`, `note_conception_pause_agents.md`) ; `PEDAGOGIE/` conservé.
- [fait] Lots B à F de la maintenance du 2026-11-05 (4 roadmaps archivées, `reprise_multicompte` et `discord_com/` hors Git).
- [fait] `signals.md` ramené à 20 actions P1 (12 actions vers le backlog, 2 doublons retirés). `check_docs.py` corrigé (frontmatter exclu du contrôle append-only).
- [fait] `llms.txt`, README, CHANGELOG. Guides DOCUMENTATION en retard : triage confié à l'agent `documentation` (`DOCUMENTATION/_contexte/signals.md`).
- [fait] Retex de `/maintenance` : à refaire, propositions perdues au compactage ; en backlog.
- Gate : `check_kit.py` et `check_docs.py` passent, rapport de phase validé.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 4 — Audit de SérénIATech_dev [FAIT]
- Audit et nettoyage, mêmes règles que la phase 2. Constater la prise en charge de Gmail, Agenda et Drive.
- [fait] Lot C `zones.md` réparé ; lot B `.gitignore` (résidus d'outils, pyc, tessdata, runtime Discord, médias `short3_bloc_note`).
- [fait] Lot A : travail non commité sauvegardé par 13 commits `sauvegarde(<zone>)` ; lot D racine ; lot E `VertIA` détaché ; lot F 2 roadmaps terminées archivées.
- [reporté] Gmail, Agenda, Drive : connecteurs claude.ai non autorisés ; test reporté sur décision de l'utilisateur (2026-11-08), entrée de `_contexte/backlog.md`, à lever avant la phase 6.
- [fait] Constats transmis à la session ouverte « Business SerenIA Tech » (reformulation contrôlée, application validée par l'utilisateur dans sa session) ; suivi dans `_contexte/signals.md`.
- Gate : rapport validé par l'utilisateur le 2026-11-08.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 5 — Analyse fonctionnelle [FAIT]
- Fonctionnalités manquantes à ajouter, puis nouvelles à créer dans SérénIATech_dev.
- [fait] Inventaire du code (2026-11-09, lecture seule) : devis utilisés (13, dernier le 2026-11-03 ; 7 envoyés, 0 « validé ») ; 3 factures UI pour une facturation officielle dans Indy ; prospection mail jamais utilisée (4 725 entreprises, 0 prospect, 0 e-mail, scanner IMAP coupé) ; comptabilité absente de l'UI ; Agenda branché pour l'Intérim seul, Gmail par IMAP, Drive par rclone ; `/veille_app_asso` mensuelle (rapports 06, 07, 08, 10 ; septembre manquant).
- [fait] Décisions de l'utilisateur : Indy reste le seul outil de facturation, l'UI ne fait que le suivi ; l'e-mail à froid n'est pas le canal d'acquisition, module gardé et recentré (rien supprimé).
- Rapport validé, dans l'ordre de réalisation :
  1. Devis : date de validité, statuts refusé/expiré, alerte de relance dans Orga.
  2. Suivi des paiements Indy dans l'UI : numéro Indy, échéance, alerte d'impayé.
  3. Tableau de bord du chiffre d'affaires mensuel (devis envoyés, signés, encaissés), appuyé sur 1 et 2.
  4. Totaux SAP / hors SAP par client et par an (attestations fiscales, déclaration NOVA).
  5. Provenance des contacts dans `pipeline_contacts` (canal ou post d'origine).
  6. Prospection : Sirène et base entreprises gardées pour qualifier le pipeline, campagnes masquées.
  7. `/veille_app_asso` rendue régulière avant toute extension.
- Hors liste : finding sur `Gestion clients/_contexte/signals.md` (lignes `fait quand:` orphelines) à transmettre à la session du projet ; Gmail (IMAP) et Agenda déjà branchés en local, piste pour la phase 6.
- [fait] Rapport relayé à la session « Business SerenIA Tech » (2026-11-09) ; reformulation contrôlée et validée. Ordre révisé, accepté par l'utilisateur : 1 > 2 > 5 > 3 ; 7 en parallèle (un rapport par mois, décision explicite sur septembre) ; 4 bloquée jusqu'à la décision CAE / NOVA n°4317140. Risques retenus : recréation de la table `devis` (contrainte CHECK) avec sauvegarde de `sereniatech.db` et test sur copie ; saisie manuelle des données Indy. Fonctionnalités 1, 2, 3, 5, 6 à implémenter par les zones ui et gestion-clients, 7 par la zone business.
- Gate : rapport validé par l'utilisateur le 2026-11-09.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 6 — Plan d'automatisation [EN COURS]
- [en cours] Menée par l'utilisateur dans la session SérénIATech_dev (décision du 2026-11-09) ; le kit ne lance rien. Le test des connecteurs claude.ai (phase 4) reste en backlog.
- Clients, facturation et comptabilité, communication, pilotage. Outils : Gmail, Agenda, Drive, Discord, réseaux sociaux, YouTube.
- Gate : plan validé.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.
