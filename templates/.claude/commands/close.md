---
description: Clôture la session d'une zone — synthèse, mise à jour du contexte, commit
argument-hint: <zone>
model: sonnet
allowed-tools: Bash(git status:*), Bash(git diff:*), Bash(git add:*), Bash(git commit:*), Bash(git push:*), Bash(git check-ignore:*), Bash(git ls-files:*), Bash(git rev-parse:*), Bash(git show:*), PowerShell(python *backup_file.py*)
---

# /close <zone>

## Zones valides et dossiers réels

Lire `.claude/zones.md` pour obtenir la table des alias → dossiers réels.


## Procédure

1. Lire l'argument fourni ($ARGUMENTS).
   - Si absent : utiliser le working directory courant comme dossier cible (zone implicite).
   - Si présent mais non reconnu dans la table ci-dessus :
     répondre "Erreur : zone inconnue. Zones valides : <liste des alias>"
     et s'arrêter.
   - Si présent et reconnu : résoudre le dossier via la table.

2. Résoudre le dossier réel via la table (ou utiliser le working directory si pas d'argument).

2-bis. **Hook de zone — Pré-synthèse.** Si `<dossier>/_contexte/on_close.md` existe : le charger et
   exécuter les instructions de sa section « Pré-synthèse » si elle est présente. Rien à faire sinon.
   Non bloquant : en cas d'échec d'une commande du hook, le signaler en une ligne et poursuivre la
   clôture. Contrat des sections : `on_close_TEMPLATE.md` du kit.

3. Produire une synthèse de session (< 25 lignes) au format suivant :

```
# Session du AAAA-MM-JJ

## Décisions prises
- [décision actée, 1 ligne]

## Livrables produits ou modifiés
- [fichier] : [statut]

## Hypothèses validées / invalidées
- VALIDE : ...
- INVALIDE : ... -> pivot vers ...
- EN ATTENTE : ...

## Prochaine étape exacte
[1-3 lignes]

## Question bloquante pour la session suivante
[1 question, ou "Aucune"]
```

3-bis. **Attribution par zone.** Avant d'écrire le moindre signal, déterminer la zone propriétaire de
   chaque action, décision et point d'attention de la session. Critère : la zone dont le dossier
   (table de `.claude/zones.md`) contient les fichiers concernés ; en cas d'égalité, celle dont le
   `agent_role.md` couvre le sujet.
   - **Zone racine** : ne garde que les tâches de coordination réellement transversales (roadmap
     commune, arbitrage entre zones, décision valable pour plusieurs zones). Une action métier
     d'une zone n'est jamais recopiée à la racine, même « pour mémoire » ; une action transversale
     la mentionne au plus par un champ `réf:`.
   - **Zone fermée ≠ travail réalisé** : si l'essentiel du travail ou des éléments à reporter
     appartient à une autre zone que celle passée en argument, le dire en une ligne (« /close <A>
     lancé, travail constaté dans <B> ») et traiter explicitement la destination de chaque
     élément ; ne jamais les écrire dans la zone fermée par défaut.
   - **Droits d'écriture** : lire le `agent_role.md` de la zone fermée (s'il existe), sections
     « Peut écrire » et « Ne doit pas toucher ». Écriture dans le `_contexte/` d'une autre zone
     permise seulement si ces droits ou une autorisation explicite de l'utilisateur la couvrent
     (une zone sans `agent_role.md` n'a pas de restriction propre). Sinon : ne pas écrire chez
     l'autre zone, conserver l'élément dans le `signals.md` de la zone fermée sous la mention
     `[à transférer vers <alias>]`, et le lister dans le bilan de l'étape 15.
   - **Session touchant plusieurs zones** : la synthèse de l'étape 3 décrit la zone fermée. Pour
     chaque autre zone concernée, ne mettre à jour que ses actions et points d'attention
     (jamais sa section « Dernière session », jamais son `contexte.md` sans demande), et lister
     chaque fichier de signal touché pour l'étape 13.
   - **Pas de doublon, pas de perte** : avant d'ajouter une action dans le `signals.md` d'une
     zone, le lire ; si une action de même objet ou de même `réf:` existe, la mettre à jour
     (`fait quand:`, `réf:`, priorité, état) au lieu d'en ajouter une. Un transfert se fait en
     deux temps : écrire à la destination, relire pour constater la présence, puis seulement
     retirer l'élément de la source. Si l'écriture à la destination échoue, l'élément reste à la
     source.

4. Mettre à jour `<dossier>/_contexte/signals.md` :
   - Lire le fichier existant. Reporter tout élément non résolu **appartenant à cette zone**
     (attribution de l'étape 3-bis) ; ne jamais supprimer un élément d'une autre zone sans
     l'avoir transféré selon 3-bis.
   - **Rotation des sessions :** Si le nombre de blocs `# Session du` dépasse 1 (seuil) :
     - Déplacer toutes les sessions sauf la plus récente vers `<dossier>/_contexte/archive_sessions.md` (append only, préfixer par `---` si le fichier existe déjà).
     - Conserver uniquement la dernière session dans `signals.md`.
   - Écraser la section "Dernière session" avec la synthèse de l'étape 3 (date du jour dans le titre).
   - Mettre à jour les priorités [P1/P2] sur les actions ouvertes.
   - Supprimer les entrées "Contexte chaud" périmées. Ajouter les nouvelles informations volatiles.
   - Sections sans contenu : omettre entièrement le titre (le recréer seulement si elle redevient non vide).
   - **Invariant :** chaque action ouverte doit comporter :
     - `fait quand: <critère observable en 1 ligne>` — condition concrète permettant de clore l'action
     - `réf: <fichier(s) ou contexte clé>` — où trouver le contexte nécessaire
     Si le contexte est introuvable dans la session, écrire `réf: [à préciser]` plutôt qu'omettre le champ.

5. Mettre à jour `<dossier>/_contexte/contexte.md` :
   - Réécrire intégralement la section "État actuel" (5 lignes max).
   - Ajouter les décisions actées à "Décisions structurantes" (append only, 5 lignes max par entrée — le détail va dans `archive_decisions.md` ou le commit).
   - Si la liste dépasse 10 entrées : archiver les plus anciennes dans `_contexte/archive_decisions.md`.
   - Ne pas toucher à "Objectif" sauf décision explicite. Ne pas toucher à "Stack" sauf changement technique.
   - Si rien n'a changé : ne pas toucher au fichier.

6. Si une `roadmap*.md` existe dans `<dossier>` : vérifier qu'elle reflète fidèlement l'état après
   session (statuts des tâches et phases). Mettre à jour si périmée.
   Invariant : ce que lira le prochain `/start` doit être vrai.

7. Base de connaissances (`DOCUMENTATION/`), si la zone fermée n'est pas `documentation` elle-même :
   - Si `<racine du projet>/DOCUMENTATION/INDEX.md` n'existe pas (pas d'agent documentaire sur ce
     projet) : ignorer cette étape.
   - Sinon : évaluer si la session a produit une information utile aux autres zones du projet
     (décision transversale, référence externe stable, donnée métier durable) — pas une info propre
     à cette seule zone.
   - Si oui : proposer à l'utilisateur l'entrée à ajouter/mettre à jour dans `DOCUMENTATION/`
     (fichier concerné + ligne d'`INDEX.md`) et attendre confirmation avant d'écrire — cette zone
     n'a pas la main sur le dossier d'une autre zone.
   - Si oui : ajouter aussi une action de triage dans `DOCUMENTATION/_contexte/signals.md`, sans
     modifier les documents de connaissance. Utiliser le format `[P2|ouvert|source=<alias>]`, avec
     `fait quand:` (décision documentaire prise) et `réf:` (fichier ou décision source). Ne pas
     créer de doublon si une action portant la même référence est déjà ouverte.
   - Si `DOCUMENTATION/_contexte/signals.md` a été modifié : l'inclure au commit de l'étape 13.
   - Si non : ne rien faire, ne pas le mentionner dans le bilan.

8. Mettre à jour `README.md` à la racine du projet :
   - Refléter l'état actuel du projet (section "État actuel" de `contexte.md`).
   - Ne pas modifier les sections stables (objectif, stack, structure) sauf changement explicite.
   - Si le README n'existe pas encore : le créer avec les sections standard (objectif, stack, structure, état actuel).

9. Bumper la version dans `CHANGELOG.md` :
   - Lire la dernière entrée de `CHANGELOG.md` pour extraire la version actuelle (ex: `v2.2`).
   - Si `CHANGELOG.md` n'existe pas : le créer avec l'en-tête `# Changelog` et une première entrée
     `## v0.1 — AAAA-MM-JJ` (pas de calcul de bump), puis passer à l'étape 10.
   - Déterminer le type de bump à partir de la synthèse de l'étape 3 :
     - **major** si : structure de `_contexte/` modifiée, placeholder renommé ou supprimé, commande supprimée
     - **minor** dans tous les autres cas
   - Calculer la prochaine version : minor → incrémenter le chiffre après le point ; major → incrémenter le chiffre avant le point et remettre le minor à 0.
   - Ajouter en tête de `CHANGELOG.md` une nouvelle entrée :
     ```
     ## vX.Y — AAAA-MM-JJ

     ### [Ajouté / Modifié / Corrigé]
     - [reprendre les livrables produits ou décisions actées de l'étape 3]
     ```
   - Ne pas modifier les entrées existantes.

10. Avant de committer, si `scripts/check_kit.py` existe à la racine du projet, exécuter le
   contrôle d'intégrité mécanique (sinon passer directement à l'étape 12) :
   ```bash
   python scripts/check_kit.py
   ```
   **Règle :** un écart signalé bloque le commit tant qu'il n'est pas traité ou explicitement écarté.

   Si le contrôle passe (exit code 0) : continuer à l'étape 12.
   Si le contrôle échoue (exit code 1) :
   - Lister les écarts détectés
   - Traiter chaque écart ou le consigner explicitement comme "écart connu à corriger en Phase X"
   - Ne pas committer tant que des écarts non consignés persistent

12. Relire les étapes 3 à 9 une par une et confirmer explicitement que chacune
   a été exécutée (pas seulement planifiée). Si une étape a une commande associée (script de build,
   régénération de vue, etc.) et qu'elle n'a pas encore été lancée dans cette session, l'exécuter
   maintenant, avant le commit — jamais après.

13. Effectuer un commit git :
    - Pour chaque fichier de signal modifié pendant la session (zone fermée et autres zones de
      l'étape 3-bis), contrôler son statut Git avant toute annonce de commit :
      ```bash
      git check-ignore -v <fichier>             # exit 0 = ignoré
      git ls-files --error-unmatch <fichier>    # exit 1 = non suivi
      ```
      Fichier ignoré : il ne peut pas être commité ; ne pas le forcer (`git add -f`), le signaler
      dans le bilan. Fichier non suivi et non ignoré : l'ajouter. Si le fichier est dans un autre
      dépôt Git que le dossier de travail (`git rev-parse --show-toplevel`), committer dans ce
      dépôt-là ou le signaler. Ne jamais annoncer « commit réussi » pour un fichier absent de
      `git show --name-only HEAD` après le commit.
    ```bash
    git diff --name-only          # vérifier tous les fichiers modifiés pendant la session
    git status                    # confirmer l'état du repo
    git add <dossier>/_contexte/ CHANGELOG.md [autres fichiers modifiés identifiés ci-dessus]
    git commit -m "close(<alias>): session AAAA-MM-JJ — <résumé 1 ligne>"
    ```
    - Le résumé reprend la première décision actée, ou la prochaine étape si aucune décision.
    - En cas de doute sur ce qu'il faut stager : préférer un commit légèrement trop large
      plutôt qu'un commit partiel laissant le repo dans un état incohérent.
    - Ne pas inclure de fichiers sans lien avec la session.
    - Si une commande de génération a modifié des fichiers après le commit (cas non censé
      survenir avec l'étape 12, mais à vérifier via `git status` après coup) : les inclure dans
      ce même commit, jamais dans un commit séparé.

14. Exécuter `git push` :
    ```bash
    git push
    ```
    Si le projet n'a pas de remote configuré, ignorer cette étape silencieusement. Si le push
    échoue (pas de remote tracking, conflit, réseau, etc.) : afficher l'erreur telle quelle dans
    le bilan de l'étape 15, ne pas tenter de résolution automatique (pas de force push, pas de
    pull/rebase automatique).

14-ter. **Hook de zone — Fin.** Si `<dossier>/_contexte/on_close.md` existe et contient une section
    « Fin » : l'exécuter maintenant. Rien à faire sinon. Non bloquant. S'exécute même si le `git
    push` de l'étape 14 a échoué : une sauvegarde de fin de session ne dépend pas du push.

15. Afficher un bilan des résidus non commités :
    ```bash
    git status --short
    ```
    S'il reste des fichiers non commités : ajouter à la synthèse finale une ligne
    "résidus non commités : N fichiers". Pas d'action automatique — uniquement rendre visible.
    Ajouter aussi, si présents : les fichiers de signal ignorés par Git (non commités), les
    éléments marqués `[à transférer vers <alias>]` et tout écart de zone traité à l'étape 3-bis.

16. Afficher en fin de réponse en grand format : ✌️😎

<!-- SPECIFICITES PROJET : DEBUT (préservé par /update, ne pas toucher hors de ce bloc) -->
<!-- Convention : toute règle liée à une étape précise de la Procédure ci-dessus doit la
     référencer explicitement par son numéro (ex: "Étape 6 : ..."), plutôt que compter sur la
     position physique de cette zone (toujours en fin de fichier). -->
<!-- SPECIFICITES PROJET : FIN -->
