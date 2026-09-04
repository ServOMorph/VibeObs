# Contexte commun — communication Intercom

Ce protocole est indépendant de l'agent utilisé. Les scripts `intercom/intercom.py` et les fichiers
`.intercom/` sont la source de vérité.

## Correspondant actuel

- Projet local : `VibeObs`
- Correspondant : `meuniers` (`D:/ServOMorph/Meuniers`)
- Envoi : `python intercom/intercom.py send meuniers --priority normal --subject "Sujet" --body "Message"`

## Contrôle obligatoire en fin de tâche

Avant toute réponse finale, clôture de tâche ou fin de session, exécuter :

```powershell
python intercom/intercom.py inbox --urgent
```

S'il n'y a aucune urgence, terminer normalement. S'il y en a une, ne pas conclure encore :

1. enregistrer le travail courant avec `pause` (tâche, prochaine action, contexte) ;
2. lire la file complète avec `inbox`, traiter l'urgence et faire `ack <id>` ;
3. lire `resume`, reprendre ou terminer le travail initial, puis seulement répondre.

Les messages `normal` restent en file jusqu'à leur traitement et leur `ack`.
