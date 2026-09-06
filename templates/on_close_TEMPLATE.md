# Hooks /close — zone <NOM_ZONE>

Template opt-in. Copier dans `<dossier_zone>/_contexte/on_close.md` uniquement si la zone a
besoin d'exécuter des actions propres à la clôture de session (arrêt d'un service, snapshot,
sauvegarde externe). Absence du fichier : `/close` inchangé.

Ne garder que les sections utilisées. Supprimer ce bloc d'en-tête après copie.

## Contrat

`/close` lit ce fichier et exécute la section correspondante au point d'insertion prévu :

| Section           | Déclenchée par `/close` | Moment |
|-------------------|-------------------------|--------|
| `## Pré-synthèse` | étape 2-bis             | après la résolution du dossier, avant la production de la synthèse de session |
| `## Fin`          | étape 14-ter            | après `git push` (étape 14), avant le bilan des résidus (étape 15) |

Règles :
- Le titre de section doit être exactement `## Pré-synthèse` ou `## Fin` (accents inclus).
- Une section absente = rien à faire, sans erreur.
- Toute commande de hook est **non bloquante** : en cas d'échec, `/close` signale en une ligne et
  poursuit.
- `## Fin` s'exécute **même si le `git push` de l'étape 14 a échoué** : une sauvegarde de fin de
  session ne dépend pas du push.
- Si une commande de `## Fin` modifie un fichier tracké (manifeste, index), le gitignorer ou
  l'inclure au commit de l'étape 13 — sinon chaque `/close` laisse un résidu signalé à l'étape 15.
- Pas de secret en clair : charger les variables d'environnement depuis un `.env` gitignoré, ne
  jamais afficher son contenu.

## Pré-synthèse

<!-- Exemple : snapshot d'un état externe avant la synthèse.
```bash
python chemin/vers/snapshot.py
```
Non bloquant : signaler l'échec en une ligne et poursuivre la clôture.
-->

## Fin

<!-- Exemple : arrêt d'un service local et/ou sauvegarde externe.
```bash
python chemin/vers/service_manager.py stop
```
Non bloquant. S'exécute même après un échec du push.
-->
