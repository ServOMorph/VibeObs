# Objectif
Corriger deux défauts de l'outillage de délégation, dans le worktree courant uniquement.
1. `ollama_call.py` : le délai HTTP est fixé à 60 s, inférieur au chargement à froid mesuré (82 s pour `qwen2.5:7b`). Le rendre paramétrable par la variable d'environnement `OLLAMA_TIMEOUT` (secondes, nombre positif), valeur par défaut 180. Valeur invalide (non numérique, nulle ou négative) : message `ERREUR:` sur stderr et code 1, sans appel réseau. Le message de délai dépassé doit citer la valeur utilisée et la variable `OLLAMA_TIMEOUT`.
2. `run_opencode.ps1` : `rapport.md` ne garde que le premier bloc du message final (15 lignes max, arrêt à la ligne `OUVERT:`) ; une liste d'anomalies écrite par OpenCode autour du rapport est restée dans `log.txt` seulement. Faire en sorte que `rapport.md` contienne le message final complet de l'agent (rapport STATUT/FICHIERS/VERIFS/OUVERT inclus, avec les lignes de détail qui le suivent ou le précèdent dans ce message), débarrassé des séquences ANSI et du bruit de la CLI. Garder le repli `STATUT: ECHEC` si aucune ligne `STATUT:` n'est trouvée.

## Fichiers autorisés
- `ollama_call.py`, `templates/ollama_call.py`, `templates/ollama/ollama_call.py` (trois copies à garder identiques)
- `tests/test_ollama_call.py`
- `_codex/run_opencode.ps1`, `templates/delegation/scripts/run_opencode.ps1` (deux copies à garder identiques)
- Toute ligne de documentation du dépôt qui affirme le délai de 60 s (à lister dans FICHIERS)

## Fichiers à lire
- Les fichiers autorisés ci-dessus.
- Exemple réel de log OpenCode tronqué : le dossier le plus ancien correspondant à `D:\ServOMorph\VibeObs\_codex\runs\*_oc_D_audit*` contenant un `log.txt` de plus de 2 000 caractères (lecture seule, ne rien y écrire).

## Contexte autonome
Dépôt public du kit VibeObs. Les copies sous `templates/` sont des miroirs des fichiers racine. PowerShell 5.1 doit rester supporté (pas d'opérateurs `??`, `?:`, `&&`). Aucun appel réel à Ollama ni à OpenCode : les tests doivent simuler le réseau.

## Étapes
1. Modifier `ollama_call.py`, puis recopier à l'identique dans les deux miroirs.
2. Ajouter dans `tests/test_ollama_call.py` des tests : délai par défaut 180, délai lu depuis `OLLAMA_TIMEOUT`, valeur invalide refusée sans appel réseau.
3. Analyser le log réel indiqué, puis corriger l'extraction du rapport dans `_codex/run_opencode.ps1` et recopier dans le miroir.
4. Chercher dans le dépôt (`rg "60 s|60s|timeout=60"`) les mentions documentaires du délai et les mettre à jour si elles décrivent ce script.

## Vérification
- `python -m pytest tests/test_ollama_call.py -q` : tout passe.
- `python scripts/check_kit.py` : passe.
- Comparaison des miroirs (`fc` ou équivalent) : identiques.
- Rejouer l'extraction corrigée sur une copie du log réel (dans un dossier temporaire hors dépôt) et indiquer dans VERIFS le nombre de lignes obtenues contre 15 avant.

## Ce qu'il ne faut pas faire
- Aucun changement hors périmètre, commit, push, génération ni redémarrage non demandé.
- Ne lancer ni Ollama, ni OpenCode, ni aucun modèle local.
- Ne pas modifier `_codex/run_codex.ps1` ni `PREAMBULE.md`.

Terminer par le rapport STATUT / FICHIERS / VERIFS / OUVERT, 15 lignes maximum.
