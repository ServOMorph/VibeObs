# Objectif
Ajouter à `scripts/check_docs.py` un avertissement non bloquant signalant les guides de `DOCUMENTATION/` probablement en retard sur le code, avec un bruit faible. Critère : sur le dépôt actuel, l'avertissement produit au plus 5 signalements, chacun justifiable ; le code de sortie du script reste inchangé (un avertissement ne fait jamais échouer) ; tests ajoutés et passants.

## Fichiers autorisés
- `scripts/check_docs.py`
- `tests/test_check_docs.py` (créer ou compléter)
- Le miroir de `check_docs.py` dans `templates/` s'il existe (le rechercher : même contenu attendu).

## Fichiers à lire
- `scripts/check_docs.py`, `DOCUMENTATION/INDEX.md`, quelques guides de `DOCUMENTATION/20_guides/`.
- `scripts/check_kit.py` (contrôle des miroirs).

## Contexte autonome
Les documents de `DOCUMENTATION/` portent un frontmatter avec `maj` (date) et souvent une section « Sources » citant des fichiers du dépôt. Une première heuristique (comparaison large des dates) a été jugée trop bruyante le 2026-11-16. Piste attendue : ne comparer `maj` qu'aux fichiers explicitement cités dans « Sources » (ou entre backticks) du guide, via la date du dernier commit git de ces fichiers ; signaler seulement si un fichier cité a été modifié après `maj` par un commit dont le message n'est pas de type `close(` ou `update:`. Ajuster si les mesures montrent mieux.

## Étapes
1. Implémenter l'avertissement (préfixe `AVERTISSEMENT`), sans toucher aux erreurs existantes.
2. Mesurer : lancer `python scripts/check_docs.py` et noter le nombre de signalements ; ajuster l'heuristique si > 5.
3. Écrire les tests (dépôt git temporaire ou fonctions pures).
4. Aligner le miroir s'il existe, lancer `python scripts/check_kit.py`.

## Vérification
- `python -m pytest tests/test_check_docs.py -q` passe.
- `python scripts/check_docs.py` : code de sortie identique à avant la modification ; citer la sortie.
- `python scripts/check_kit.py` passe.

## Ce qu'il ne faut pas faire
- Aucun commit, aucun push. Ne pas modifier les guides de `DOCUMENTATION/`.

Terminer par le rapport STATUT / FICHIERS / VERIFS / OUVERT, 15 lignes maximum, en citant le nombre de signalements mesurés et leur liste.
