---
description: Charge le contexte d'une zone en début de session
argument-hint: [zone] [--complet]
model: haiku
---

# /start [zone] [--complet]

## Zones valides et dossiers réels

Lire `.claude/zones.md` pour obtenir la table des alias → dossiers réels.


## Procédure

1. Lire l'argument fourni ($ARGUMENTS).
   - Si `--complet` y figure : le retirer de l'argument et activer le mode complet (étape 4).
   - Si absent : utiliser le working directory courant comme dossier cible (zone implicite).
   - Si présent mais non reconnu dans la table ci-dessus :
     répondre "Erreur : zone inconnue. Zones valides : <liste des alias>"
     et s'arrêter.
   - Si présent et reconnu : résoudre le dossier via la table.

2. Vérifier que `<dossier>/_contexte/signals.md` et `<dossier>/_contexte/contexte.md` existent.
   Si absents : proposer d'initialiser la structure `_contexte/` pour cette zone (créer
   `contexte.md` et `signals.md` vides) et s'arrêter.

2b. Si `<dossier>/agent_role.md` existe : le charger et l'afficher intégralement,
    avant `signals.md`. Ce fichier n'existe que pour les zones-agents ; une zone
    racine classique n'en a pas.

2c. Si `<dossier>/_contexte/memory.md` existe : le charger (mémoire propre à cette
    zone, écrite via `/create_memory <alias_zone> <contenu>`).

3. Charger dans l'ordre :
   1. `_contexte/signals.md` — actions ouvertes, blocages, dernière session (priorité absolue)
   2. `_contexte/contexte.md` — contexte stable
   3. `roadmap*.md` — si un fichier correspondant existe dans `<dossier>`, le charger
   4. `_contexte/journal_session.md` — si présent et non vide, le charger (session précédente non close)

   > **Économie tokens :** si `signals.md` suffit à répondre à la question immédiate,
   > `contexte.md` peut être chargé à la demande plutôt que systématiquement.
   > En cas de doute : le charger.

3-bis. **Hook de zone — Pré-synthèse.** Si `<dossier>/_contexte/on_start.md` existe : le charger et
   exécuter les instructions de sa section « Pré-synthèse » si elle est présente. Rien à faire si le
   fichier est absent ou si cette section n'y figure pas. Non bloquant : en cas d'échec d'une
   commande du hook, le signaler en une ligne et poursuivre `/start`. Contrat des sections :
   `on_start_TEMPLATE.md` du kit.

4. Afficher `signals.md`, toujours mot pour mot (sans résumé ni reformulation) :
   - **Par défaut** : recopier les sections « Prochaine étape exacte » et « Question bloquante pour
     la session suivante » de la dernière session. Le reste du fichier est donné sur demande de
     l'utilisateur. Si l'une des deux sections est absente : afficher le contenu intégral, comme en
     mode complet.
   - **Mode complet** (`--complet`) : afficher le contenu intégral de `signals.md`.
   Si `_contexte/journal_session.md` est non vide : l'afficher mot pour mot sous le titre « Journal non
   intégré », avant la ligne de compteurs, et signaler en une ligne que le `/close` précédent n'a pas eu
   lieu ou n'a pas intégré le journal.
   Dans tous les cas, terminer par une ligne de compteurs :
   `Actions ouvertes : N (dont P1 : x) · Backlog : B · Phase en cours : <titre>`.
   N = actions de premier niveau des sections d'actions ouvertes (la ligne de renvoi du backlog
   n'est pas une action) ; « dont P1 » seulement si une section P1 existe ; « Backlog : B » (B =
   nombre de la ligne de renvoi du backlog) seulement si cette ligne existe ; « Phase en cours »
   seulement si une roadmap est active. Une partie sans objet est retirée de la ligne avec son
   séparateur, jamais remplacée par « omis » ou « aucune ».

4b. Lire les fichiers `réf:` des seules actions dont l'objet est cité dans « Prochaine étape
    exacte », y compris en mode complet ou en affichage intégral. Les autres `réf:`
    sont lues quand l'utilisateur ou la tâche en cours en a besoin. Si une action semble ambiguë
    mais qu'une `réf:` existe, lire la référence en priorité plutôt que de demander des précisions.

    Ajouter ensuite, en une ligne chacun : la phase en cours si roadmap active, et le point
    d'attention immédiat.

4c. **Contrôle de classement.** Après l'affichage de l'étape 4, analyser l'intégralité de
    `signals.md` (jamais la seule partie affichée) et repérer les éléments manifestement mal classés :
    - une action dont tous les `réf:` pointent dans le dossier d'une autre zone de `zones.md` ;
    - à la racine, une action métier d'une zone (non transversale) ;
    - une action dont l'objet ou la `réf:` figure aussi dans le `signals.md` de la zone
      propriétaire.
    Les éléments déjà marqués `[à transférer vers <alias>]` ne sont pas détaillés : leur transfert
    est déjà tracé. Les compter dans une seule ligne « N élément(s) en attente de transfert
    (déjà marqués) ».
    Pour chaque autre candidat, lire effectivement `<dossier de la zone propriétaire>/_contexte/signals.md`
    (dossier résolu par `zones.md`) avant de conclure sur le doublon : « oui » si l'objet ou une
    `réf:` y figure, « non » sinon. Écrire « non vérifiable » seulement si ce fichier n'existe pas
    après vérification de son chemin ; indiquer alors le chemin testé.
    Lister les candidats dans un bloc « Éléments possiblement mal classés » : élément, zone
    probable, doublon constaté oui/non. Ne rien déplacer ni supprimer : le reclassement se fait par
    `/close` (étape 3-bis) sur décision de l'utilisateur. Aucun candidat ni élément marqué : ne
    pas afficher le bloc.

5. Afficher en fin de réponse : 🎉🎉🎉

5-bis. **Hook de zone — Post-synthèse.** Si `<dossier>/_contexte/on_start.md` existe et contient une
   section « Post-synthèse » : l'exécuter maintenant, juste après l'affichage de l'étape 5. Rien à
   faire sinon. Non bloquant. Un hook Post-synthèse peut légitimement ne pas rendre la main
   (enchaînement d'une autre commande) — c'est permis.

<!-- SPECIFICITES PROJET : DEBUT (préservé par /update, ne pas toucher hors de ce bloc) -->
<!-- Convention : toute règle liée à une étape précise de la Procédure ci-dessus doit la
     référencer explicitement par son numéro (ex: "Étape 3 : ..."), plutôt que compter sur la
     position physique de cette zone (toujours en fin de fichier). -->
<!-- SPECIFICITES PROJET : FIN -->
