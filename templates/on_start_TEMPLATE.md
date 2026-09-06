# Hooks /start — zone <NOM_ZONE>

Template opt-in. Copier dans `<dossier_zone>/_contexte/on_start.md` uniquement si la zone a
besoin d'exécuter des actions propres au démarrage de session (relance d'un service, snapshot,
enchaînement d'une commande). Absence du fichier : `/start` inchangé.

Ne garder que les sections utilisées. Supprimer ce bloc d'en-tête après copie.

## Contrat

`/start` lit ce fichier et exécute la section correspondante au point d'insertion prévu :

| Section            | Déclenchée par `/start` | Moment |
|--------------------|-------------------------|--------|
| `## Pré-synthèse`  | étape 3-bis             | après le chargement `signals.md` / `contexte.md` / `roadmap`, avant l'affichage de `signals.md` |
| `## Post-synthèse` | étape 5-bis             | après l'affichage 🎉 de l'étape 5 |

Règles :
- Le titre de section doit être exactement `## Pré-synthèse` ou `## Post-synthèse` (accents inclus).
- Une section absente = rien à faire, sans erreur.
- Toute commande de hook est **non bloquante** : en cas d'échec, `/start` signale en une ligne et
  poursuit.
- Une section `## Post-synthèse` peut légitimement ne jamais rendre la main (ex. elle enchaîne une
  autre commande qui tourne en continu). C'est permis.
- Pas de secret en clair : charger les variables d'environnement depuis un `.env` gitignoré, ne
  jamais afficher son contenu.

## Pré-synthèse

<!-- Exemple : relancer un service local avant d'afficher la synthèse.
```bash
python chemin/vers/service_manager.py restart
```
Non bloquant : afficher le message retourné et poursuivre `/start` en cas d'échec.
-->

## Post-synthèse

<!-- Exemple : enchaîner automatiquement une commande de service après la synthèse.
Cette section peut ne pas rendre la main si la commande enchaînée tourne en continu.
-->
