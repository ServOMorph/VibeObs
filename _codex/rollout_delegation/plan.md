# Diffusion de /delegation — plan

Décision utilisateur (2026-11-14, session VibeObs) : VertIA est le premier testeur ; puis une version testable par 3 sessions, puis davantage. Les retours viennent directement à VibeObs ; l'utilisateur ne valide pas les étapes, VibeObs gère le processus en autonomie. Tout échange entre agents et toute commande lancée sont tracés dans `journal_echanges.md` (verbatim pour les messages).

## Phases
1. [EN PAUSE 2026-11-14 23:45, demande utilisateur] VertIA_v3 : comparaison avec son existant, correctif des lanceurs, adoption de `delegation.md`, un lot réel tracé dans son `_codex/journal_delegation.md`. Sortie : retours intégrés au kit, version v1 de la commande.
2. [TODO] 3 sessions pilotes (choix selon usage réel : sessions de code actives) : installation par message, un lot réel chacune, retours.
3. [TODO] Diffusion générale : `delegation.md` dans `templates/.claude/commands/`, déployé par `/init_projet` et `/update`.

## Règles du processus
- VibeObs n'écrit jamais dans un autre projet : il propose par message, la session concernée applique.
- Chaque message envoyé ou reçu est copié dans `journal_echanges.md` avec date, émetteur, destinataire.
- Chaque commande lancée par VibeObs pour ce processus y est notée (commande, résultat en une ligne).
- Un retour qui contredit la commande est corrigé dans le kit avant la phase suivante.
