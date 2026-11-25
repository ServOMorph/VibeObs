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
