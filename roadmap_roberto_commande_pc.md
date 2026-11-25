# Roadmap — Roberto : commande du PC à la manette et à la voix

Créée le 2026-11-25, réorganisée à chaque instruction de l'utilisateur selon l'urgence (décision du 2026-11-25).
Développement dans `Roberto/lot_dictee/` (cas 5 de `DOCUMENTATION/30_decisions/prises_de_controle.md`) ; aucun lot envoyé à Roberto sans accord de l'utilisateur ; insertion par la session Roberto après son accord.

## Mapping manette (NSW Wired Controller, mesuré le 2026-11-25)
A = 2, B = 1, X = 3, Y = 0 ; croix = hat 0 ; stick gauche horizontal = axe 0 (supposé, non mesuré).

## Phase 1 — Mains libres : dictée et envoi [EN COURS]
- [validé] B : dictée Win+H ; X : Entrée ; F12 au clavier (repli crochet clavier).
- [à tester] B défectueux, retiré (2026-11-25) : X maintenu = dictée, relâché = coupure ; A = Entrée, et pendant la dictée coupe puis Entrée ; croix droite = test validé.
- [à tester] Bouton souris MANETTE active/désactivée dans l'interface (2026-11-25) : désactivée, la manette est ignorée.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 2 — Retour vocal [EN COURS, urgence haute]
- Annonce vocale (SAPI, `parler.py`) à la fin de chaque demande traitée.
- Fait : voix Piper (Jessica), un message à la fois, statut toutes les 30 s, bouton de capture (13) = voix on/off.
- Ensuite : lecture vocale des réponses de la boucle agentique ; réponses courtes sans outil à clarifier avec l'utilisateur.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 3 — Changement de session [EN COURS]
- Calibrage des chats (A sur chaque position), `sessions.json`.
- [à tester] Y maintenu : dire le nom, relâcher = clic ; stick gauche gauche/droite = session voisine.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 4 — Interface de pilotage [EN COURS]
- Page HTML sombre, serveur à rechargement automatique, demi-écran droit sans défilement.
- Grande manette annotée, boutons du test courant en surbrillance, tests validés à la manette (croix, A).
- Fait : image de fond VertIA (7 %), console manette dans la page, bouton de capture « V », libellés reliés, bouton souris MANETTE.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 4 bis — Commandes vocales [EN COURS]
- Bouton de fonction « + » (indice 9) maintenu : « Roberto, ouvre WhatsApp », relâcher = exécution (fenêtre au premier plan, lancement si absente), annonce vocale.
- Commandes dans `commandes.json` ; d'autres commandes à ajouter sur demande.
- Mode conversation (bouton − ) : écoute continue, faster-whisper, envoi au chat « vibe obs » ; phrases recollées (3 s) ; transcription : beam 5 + vocabulaire.
- Retiré : stick droit pour les tests (doublon de la croix) ; écoute permanente « vendredi ».

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 5 — Intégration dans Roberto [TODO]
- Lot présenté à l'utilisateur, puis à Roberto sur son accord ; insertion après accord dans la session Roberto.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

## Phase 6 — Template réutilisable [TODO]
- Extraire le système en template du kit pour d'autres projets.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.
