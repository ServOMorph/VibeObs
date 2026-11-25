# Roadmap — Roberto : commande du PC à la manette et à la voix

Créée le 2026-11-25, réorganisée à chaque instruction de l'utilisateur selon l'urgence (décision du 2026-11-25).
Développement dans `Roberto/lot_dictee/` (cas 5 de `DOCUMENTATION/30_decisions/prises_de_controle.md`) ; aucun lot envoyé à Roberto sans accord de l'utilisateur ; insertion par la session Roberto après son accord.

## Mapping manette (NSW Wired Controller, mesuré le 2026-11-25)
A = 2, B = 1, X = 3, Y = 0 (fonctions supprimées) ; − = 8, + = 9, maison = 12, capture = 13 ; croix = hat 0 ; stick gauche horizontal = axe 0 (supposé, non mesuré).

## Phase 1 — Mains libres : dictée et envoi [FAIT]
- [validé] B : dictée Win+H ; X : Entrée ; F12 au clavier (repli crochet clavier).
- [validé 2026-11-25] B défectueux, retiré : X maintenu = dictée, relâché = coupure ; A = Entrée, et pendant la dictée coupe puis Entrée ; croix droite.
- [validé sans essai séparé, déclaration de l'utilisateur 2026-11-25] Bouton souris MANETTE active/désactivée dans l'interface.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 2 — Retour vocal [FAIT]
- Annonce vocale (SAPI, `parler.py`) à la fin de chaque demande traitée.
- Fait : voix Piper (Jessica), un message à la fois, statut toutes les 30 s, bouton de capture (13) = voix on/off.
- Fait : lecture vocale automatique des réponses par hook Stop (`lecture_reponse.py`), validée à l'oreille ; bouton maison (12) = messages de 30 s on/off, validé.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 3 — Changement de session [FAIT]
- Calibrage des chats (A sur chaque position), `sessions.json`.
- Y : fonctions supprimées le 2026-11-25 (bouton grisé dans l'interface). [validé] stick gauche gauche/droite = session voisine.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 4 — Interface de pilotage [FAIT]
- Page HTML sombre, serveur à rechargement automatique, demi-écran droit sans défilement.
- Grande manette annotée, boutons du test courant en surbrillance, tests validés à la manette (croix, A).
- Fait : image de fond VertIA (7 %), console manette dans la page, bouton de capture « V », libellés reliés, bouton souris MANETTE.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 4 bis — Commandes vocales [FAIT]
- Bouton de fonction « + » (indice 9) maintenu : « Roberto, ouvre WhatsApp », relâcher = exécution (fenêtre au premier plan, lancement si absente), annonce vocale.
- Commandes dans `commandes.json` ; d'autres commandes à ajouter sur demande.
- Mode conversation (bouton − ) : écoute continue, faster-whisper, envoi au chat « vibe obs » ; phrases recollées (3 s) ; transcription : beam 5 + vocabulaire.
- Retiré : stick droit pour les tests (doublon de la croix) ; écoute permanente « vendredi ».

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 5 — Intégration dans Roberto [FAIT]
- Fait le 2026-11-25 : lot validé par l'utilisateur, relu et commité par la session Roberto (`b933637`, `b77282e`) ; `demarrer.py`, `README.md` du lot, commande `/manette` et hook Stop créés chez Roberto (cas 6, intégration autonome). Chantier repris par la session Roberto : VibeObs n'y travaille plus.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 6 — Template réutilisable [TODO]
- Extraire le système en template du kit pour d'autres projets. Idée seulement, non décidée : à lancer sur demande explicite de l'utilisateur (touche le kit).

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.
