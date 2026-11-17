# Objectif
Prototype, dans le kit seulement, d'un hook Claude Code `PreCompact` qui trace le compactage dans le journal de session et rappelle au résumé de conserver l'état de travail. Critère : script testé, branché dans `.claude/settings.json` du kit, sans effet sur les autres hooks.

## Fichiers autorisés
- `scripts/hook_precompact.py` (créer)
- `tests/test_hook_precompact.py` (créer)
- `.claude/settings.json` (ajouter l'entrée `PreCompact` uniquement)

## Fichiers à lire
- `.claude/settings.json`, `scripts/alerte_compact.py` (modèle de hook existant), `.claude/CLAUDE.md` § Journal de session.

## Contexte autonome
Journal de session : `<racine du projet>/_contexte/journal_session.md`, gitignoré, ajout seul, une ligne par événement au format `AAAA-MM-JJ HH:MM | décision|fichier|action | texte`. Règle actuelle : l'agent relit le journal après chaque `/compact`, mais un compactage (manuel ou automatique) n'est pas détectable sans hook. Faits documentés (vérifiés le 2026-11-14 dans la doc Claude Code) : le hook `PreCompact` reçoit en JSON sur stdin au moins `hook_event_name`, `trigger` (`manual` ou `auto`), `custom_instructions`, `transcript_path`, `cwd` ; sa sortie standard est ajoutée aux consignes du résumé. Le projet se trouve par `CLAUDE_PROJECT_DIR` sinon `cwd`. Comportement voulu : (1) ajouter au journal une ligne `| action | compactage <trigger> : relire ce journal` (créer `_contexte/` jamais : si le dossier est absent, ne rien écrire) ; (2) imprimer sur stdout une consigne courte demandant au résumé de conserver la tâche en cours, les fichiers modifiés non commités et la prochaine étape, et de relire `_contexte/journal_session.md` après le compactage ; (3) ne jamais faire échouer le compactage : toute erreur → code de sortie 0, rien sur stdout sauf la consigne.

## Étapes
1. Écrire le script (Python standard, encodage UTF-8 explicite).
2. Tests : entrée JSON valide, `_contexte/` absent, JSON invalide, encodage accentué.
3. Brancher dans `.claude/settings.json` en conservant `PreToolUse` et `UserPromptSubmit` à l'identique (commande `python "$CLAUDE_PROJECT_DIR/scripts/hook_precompact.py"`).

## Vérification
- `python -m pytest tests/test_hook_precompact.py -q` passe.
- `python -c "import json;json.load(open('.claude/settings.json',encoding='utf-8'))"` passe.
- `python scripts/check_kit.py` passe.
- Essai réel d'un compactage impossible ici : le signaler dans OUVERT.

## Ce qu'il ne faut pas faire
- Aucun commit, aucun push. Ne pas toucher aux templates ni aux autres hooks.

Terminer par le rapport STATUT / FICHIERS / VERIFS / OUVERT, 15 lignes maximum.
