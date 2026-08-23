---
description: Installe le mécanisme de communication hiérarchique agent↔coordinateur↔orchestrateur
argument-hint: "<chemin_projet_cible>"
model: sonnet
---

# /create_com_agents <chemin_projet_cible>

## Objectif

Installer, dans un projet déjà initialisé (`.claude/zones.md` présent), un mécanisme de
communication hiérarchique agent↔coordinateur↔orchestrateur, sans communication latérale :

- chaque zone-agent (dossier avec `agent_role.md`) maintient `_contexte/statut.md` — état
  courant, écrasé (pas append), mis à jour à chaque `/close` de cette zone ;
- chaque zone-agent maintient `_contexte/messages.md` — boîte de réception, écrite
  directement par l'orchestrateur en session (pas de commande dédiée pour "envoyer"), lue
  et purgée au `/start` de la zone destinataire ;
- chaque coordinateur (dossier avec `team.md`) agrège les `statut.md` de ses membres directs à son
  propre `/start`, puis remonte son propre état ;
- la zone racine agrège uniquement les coordinateurs directement rattachés à elle. Sans `team.md`,
  le comportement historique est conservé : elle agrège tous les agents directs.

Cette commande vit dans le kit et n'est jamais copiée dans les projets cibles : elle
s'exécute toujours depuis le kit, projet cible en argument. Elle ne modifie que `start.md`
et `close.md` du projet cible — jamais `zones.md`/`agent_role.md` (le mécanisme reste dans
le périmètre déjà déclaré de chaque zone : "peut mettre à jour son propre `_contexte/` via
`/start` et `/close`").

## [PREFLIGHT] — résolution, aucune écriture

1. Résoudre `<chemin_projet_cible>` (même règle que `/create_agent` : gérer les chemins avec
   espaces par test de préfixes croissants jusqu'à trouver `.claude/zones.md`).
2. Vérifier `<projet_cible>/.claude/zones.md`, `.claude/commands/start.md`,
   `.claude/commands/close.md` existent. Un seul manque → s'arrêter, projet pas initialisé
   via `/init_projet`.
3. Vérifier si le mécanisme est déjà installé : chercher le marqueur `<!-- COM_AGENTS -->`
   dans `start.md` et `close.md`. Présent dans les deux → informer "Mécanisme déjà installé
   dans ce projet." et s'arrêter, sauf si l'utilisateur demande explicitement une
   réinstallation. Présent dans un seul des deux fichiers (état incohérent) : signaler et
   demander comment procéder plutôt que corriger silencieusement.
4. Lister les zones de `zones.md`. Pour chacune sauf la racine, vérifier la présence de
   `agent_role.md` dans son dossier → zone-agent. Si `team.md` existe, valider sa table « Membres
   directs » : alias présents dans `zones.md`, chemins cohérents et aucun membre dupliqué. Un écart
   bloque l'écriture, car la hiérarchie serait ambiguë. Pour chaque zone-agent, vérifier si
   `_contexte/statut.md` existe déjà :
   - Absent : rien à signaler, sera créé au premier `/close` de cette zone après
     installation.
   - Présent et conforme au format de l'étape 5 (mêmes libellés de champs) : rien à
     signaler.
   - Présent mais non conforme (champs différents, format libre) : le signaler
     nommément (fichier + champs détectés) et proposer une conversion au nouveau format
     lors de l'écriture — jamais un écrasement silencieux.

## [ECRITURE] — toutes les écritures groupées

5. `close.md` du projet cible — nouvelle étape native, insérée après l'étape de mise à jour
   de la roadmap (juste avant la mise à jour du README) :

   ```
   <étape suivante>bis. <!-- COM_AGENTS --> Si `<dossier>/agent_role.md` existe (zone-agent) :
      mettre à jour `_contexte/statut.md` (créer si absent, écraser entièrement s'il existe)
      avec l'état de fin de session déjà produit aux étapes précédentes — ne pas relire les
      fichiers pour ça. Format :
      ```
      Roadmap active : <nom du fichier roadmap*.md actif, ou "aucune">
      Phase en cours : <libellé de la phase EN COURS, ou "aucune">
      Avancement : <1 ligne, résumé de la synthèse de session>
      Bloqué : <non, ou oui + raison en 1 ligne>
      Prochaine action : <1 ligne, reprise de "Prochaine étape exacte">
      Mis à jour : AAAA-MM-JJ
      Destinataire : <alias de la zone parente, ou "aucun" pour la racine>
      ```
   ```

   Numéroter cette étape en cohérence avec les étapes existantes du `close.md` cible (ex.
   étape 6bis si l'étape roadmap est la 6), sans renuméroter les étapes suivantes — suivre
   la même convention que `synthese_agents.md` dans jeu_zombies (bis plutôt que
   renumérotation complète, sauf si le projet cible a déjà une convention de renumérotation
   stricte, auquel cas la respecter).

6. `start.md` du projet cible — deux nouvelles étapes natives, **toutes deux regroupées tôt
   dans la procédure, immédiatement après l'étape de chargement de charte (2b, chargement
   `agent_role.md`)** — jamais après un paragraphe de synthèse existant (étape 4b ou
   équivalent) : une étape conditionnelle placée après un pavé de texte narratif est
   régulièrement sautée en exécution réelle (constaté lors du pilote Roberto2 2026-08-12 :
   l'étape de synthèse `statut.md` placée après la synthèse `signals.md` a été omise, alors
   que la même étape placée juste après 2b, adjacente et courte, a été exécutée
   correctement) :

   ```
   2c. <!-- COM_AGENTS --> Si `<dossier>/_contexte/messages.md` existe et n'est pas vide :
       l'afficher intégralement, avant `signals.md`, puis le vider.

   2d. <!-- COM_AGENTS --> OBLIGATOIRE : si le dossier résolu est un coordinateur (`team.md`) ou
       la racine du projet, déterminer ses membres **directs**. Pour un coordinateur, utiliser la
       table de son `team.md`. Pour la racine, ne retenir que les équipes dont `team.md` déclare la
       racine comme zone parente ; si aucun `team.md` n'existe, conserver le mode historique et
       retenir chaque zone-agent. Lire `_contexte/statut.md` s'il existe, produire une synthèse
       condensée par membre (phase, avancement, blocage), puis proposer 2 à 4 actions concrètes.
       Fichier absent : l'ignorer silencieusement. Une zone simple n'agrège jamais.
   ```

   Adapter la numérotation aux étapes réellement présentes dans le `start.md` cible (ne pas
   supposer qu'il a exactement 2b comme le kit — vérifier avant d'insérer), mais toujours
   les placer immédiatement après le chargement de charte, jamais après une étape de
   synthèse narrative.

7. Pour chaque zone-agent signalée en [PREFLIGHT] avec un `statut.md` non conforme : ne pas
   le convertir automatiquement. Le signaler dans le récapitulatif final (étape 8) comme
   action manuelle restante.

## [SORTIE]

8. Un seul récapitulatif :
   - Fichiers modifiés (`start.md`, `close.md` du projet cible, liens cliquables, chemin
     absolu) — préciser que `statut.md`/`messages.md` eux-mêmes ne sont pas créés
     maintenant : `statut.md` apparaît au premier `/close` d'une zone-agent après
     installation, `messages.md` seulement quand un message y est écrit.
   - Liste des zones-agents avec un `statut.md` ad hoc non conforme détecté en [PREFLIGHT]
     (le cas échéant), à convertir manuellement.
   - Confirmation : "✅ Mécanisme de communication installé dans <projet_cible>. Prochain
     `/close <agent>` mettra à jour son `statut.md` ; prochain `/start <racine>` agrégera
     les statuts des zones-agents."

<!-- SPECIFICITES PROJET : DEBUT (préservé par /update, ne pas toucher hors de ce bloc) -->
<!-- Convention : toute règle liée à une phase précise de la Procédure ci-dessus doit la
     référencer explicitement par son ancre ([PREFLIGHT]/[ECRITURE]/[SORTIE]), plutôt que
     par un numéro d'étape ou la position physique de cette zone. -->
<!-- SPECIFICITES PROJET : FIN -->
