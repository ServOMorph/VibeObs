---
description: Active la délégation à Codex, OpenCode et Ollama comme sous-agents pour économiser les tokens de Claude
argument-hint: [chemin du projet, défaut : dossier courant]
---

# /delegation

## Objectif

Faire exécuter par des outils moins coûteux en tokens Claude les tâches qui n'ont pas besoin de
Claude, et journaliser chaque délégation pour améliorer le routage. Claude reste orchestrateur :
il rédige le brief, lit le rapport (15 lignes), relit le diff, décide et committe.

## 1. Activation (une fois par projet)

1. Projet = argument, sinon dossier courant.
2. Si `<projet>/_codex/run_codex.ps1` est absent : installer le template du kit
   (`<kit>/templates/delegation/install.ps1 -Projet <projet>`), puis relire `_codex/PREAMBULE.md` et
   `opencode.json`.
3. Contrôler les exécutants, sans appel de modèle payant :
   - `codex login status` (doit indiquer une connexion) ;
   - `opencode models` (le modèle gratuit retenu doit figurer dans la liste) ;
   - `ollama list` (au moins un modèle local).
   Exécutant absent : le noter, router sans lui. Ne jamais lancer de connexion sans l'utilisateur.
4. Créer `_codex/journal_delegation.md` s'il est absent (en-tête du § 4).

## 2. Routage

| Tâche | Exécutant | Pourquoi |
|---|---|---|
| Texte fourni en entrée : résumé, digest de logs, message de commit, reformulation, classement | Ollama (`python ollama_call.py`, `OLLAMA_MODEL=qwen2.5:7b`, ou `gemma4:12b-32k` pour un texte long) | Local, gratuit, aucune donnée sortante ; pas d'outils |
| Lecture ou recherche dans le dépôt, audit de cohérence, petite édition délimitée | OpenCode gratuit (`_codex/run_opencode.ps1`) | Gratuit ; ni web, ni bash hors liste, ni accès hors dépôt |
| Correctif multi-fichiers, revue de code, analyse lourde | Codex (`_codex/run_codex.ps1`, `-Sandbox read-only` pour une revue) — **SUSPENDU tant que `~/.codex/delegation_bloquee.flag` existe** : router vers OpenCode ou un sous-agent Claude | Quota ChatGPT (formule Plus, quota à ménager), pas Claude ; sandbox |
| Web, documentation Claude Code, navigateur, contexte de la conversation | Sous-agent Claude, modèle `haiku` sauf besoin | Seul à avoir ces outils |
| Décision, arbitrage, échange avec l'utilisateur, commit | Claude principal | Responsabilité |

Règles :
- GPU (Ollama ou tout modèle local) : jeton VRAM obligatoire, géré par la session VertIA_v3 (`D:\ServOMorph\VertIA_v3\_orchestration\vram_lock.py acquire <session> --gb <Go> --minutes <min> --wait` en arrière-plan, `release` après déchargement ; protocole `D:\ServOMorph\VertIA_v3\_orchestration\protocole.md` § GPU). Session absente de la liste autorisée du script : demander l'accès à VertIA_v3 par message, et router la tâche hors Ollama en attendant.
- Brief autonome au format `templates/delegation/BRIEF_TEMPLATE.md`, périmètre de fichiers explicite.
- Correctif qui dépend du format de sortie d'un outil externe (CLI, API) : le brief exige un essai
  réel de l'outil et la citation de sa sortie dans le rapport ; à défaut, Claude fait l'essai avant
  d'accepter le diff.
- Jamais deux exécutants sur les mêmes fichiers. Une tâche qui écrit dans le kit tourne dans un
  worktree Git (`git worktree add`), jamais dans l'arbre principal.
- Aucun secret ni donnée sensible dans un brief envoyé à Codex ou OpenCode.
- Blocage Codex (décision de l'utilisateur du 2026-11-19) : tant que le fichier `~/.codex/delegation_bloquee.flag` existe, aucune délégation à Codex, y compris par appel direct de `codex exec` ; `run_codex.ps1` sort en code 3. Ne lever le blocage (supprimer le fichier) que sur demande de l'utilisateur.
- Modèle Codex : `gpt-6.1-sol` uniquement, jamais `astra`. Une session qui utilise Codex vérifie le modèle affiché en tête de `log.txt` (ligne `model:`) ; le changement se fait par `-m <modèle>` (testé le 2026-11-18, Codex 0.167 : `gpt-6.1-sol` accepté, `gpt-6.1-astra` refusé par le compte ChatGPT).
- Lire seulement `rapport.md` ; ouvrir `log.txt` uniquement en cas d'échec. Un code de sortie nul ne
  prouve rien : contrôler STATUT, OUVERT et le diff.
- Échec d'un exécutant : une seule relance avec brief corrigé, puis bascule vers l'exécutant suivant
  (Ollama → OpenCode → Codex → sous-agent Claude), tracée au journal.

## 3. Sollicitations de l'utilisateur

Seulement pour : commit ou push sur la branche principale, écriture hors du projet, exécutant bloqué
(connexion, quota), action irréversible. Tout le reste est décidé par Claude et tracé au journal.

## 4. Journal

`_codex/journal_delegation.md`, une ligne par délégation, en ajout seul :

```
| Date heure | Tâche | Exécutant / modèle | Durée | Brief (car.) | Rapport (car.) | Statut | Retouche Claude | Note |
|---|---|---|---|---|---|---|---|---|
```

`Retouche Claude` : aucune, mineure, refaite. `Note` : pourquoi ce routage, ce qui a coincé. En fin
de lot, ajouter un bilan de 5 lignes : ce qui a marché, ce qui a échoué, règle de routage à changer.
