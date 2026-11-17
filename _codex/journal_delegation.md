# Journal de délégation — VibeObs

| Date heure | Tâche | Exécutant / modèle | Durée | Brief (car.) | Rapport (car.) | Statut | Retouche Claude | Note |
|---|---|---|---|---|---|---|---|---|
| 2026-11-14 23:2x | D audit suivi | OpenCode / deepseek-v4.1-flash-free | 1 s | - | - | ECHEC | aucune | Lanceur : $PSScriptRoot vide en valeur par défaut de param sous PS 5.1 ; relancé avec -Root explicite. Bug template à corriger. |
| 2026-11-14 23:3x | B doc Claude Code | sous-agent Claude / haiku (claude-code-guide), 51k tokens Haiku | 49 s | 900 | 2600 | OK | aucune | Web requis : seul un sous-agent Claude convient. Résultat : disable-model-invocation retire la description du contexte ; PreCompact (stdout = consignes du résumé) + SessionStart matcher compact (réinjection) utilisables pour le journal. |
| 2026-11-14 23:3x | A vérif Canva + correction brouillon | sous-agent Claude / haiku, 62k tokens Haiku | 66 s | 1900 | 2900 | PARTIEL | aucune | WebFetch canva.com en 403 : faits tirés des extraits WebSearch seulement ; 3 points non trouvés laissés « à vérifier pendant le test ». |
| 2026-11-14 23:3x | C correctifs kit (3 findings backlog) | Codex CLI (binaire appli) / workspace-write, worktree | 88 s | 3300 | 900 | OK | mineure | Diff propre, miroirs identiques, check_kit OK. OUVERT signalé honnêtement (contrôle 6 hors périmètre du brief) : complété par Claude. Leçon : brief trop étroit, inclure les contrôles liés. |
| 2026-11-14 23:4x | D audit suivi (relance) | OpenCode / deepseek-v4.1-flash-free | 127 s | 2100 | 380 (+2600 dans log) | OK | aucune | 13 anomalies précises fichier:ligne, dont 2 contradictions rclone réelles. Bug lanceur : rapport.md ne garde que le 1er bloc, la liste est dans log.txt. Bon rapport qualité/coût. |
| 2026-11-14 23:5x | Bilan du journal | Ollama / qwen2.5:7b | 82 s froid (échec timeout 60 s x2), 12 s chaud | 1500 | 520 | PARTIEL | refaite | Délai fixe de 60 s de ollama_call.py < chargement à froid : préchauffer le modèle ou rendre le délai paramétrable. Bilan exact mais superficiel ; « règle de routage » proposée hors sujet. |

## Bilan du lot 2026-11-14 (rédigé par Claude)
- Marché : Codex pour un correctif multi-fichiers cadré (88 s, diff propre) ; OpenCode gratuit pour un audit en lecture (13 anomalies exactes) ; sous-agents Haiku pour le web et la doc Claude Code.
- Échoué : lanceurs sous PowerShell 5.1 ($PSScriptRoot vide en défaut de param, corrigé) ; rapport OpenCode tronqué (liste dans log.txt) ; Ollama à froid au-delà de 60 s ; canva.com en 403 pour WebFetch.
- Routage à changer : Ollama réservé aux textes courts et mécaniques (commit, reformulation), pas aux synthèses qui demandent du jugement ; brief Codex à élargir aux contrôles liés aux passages modifiés.
- Coût Claude : briefs ~7 000 car. et rapports lus ~4 000 car., contre la lecture complète de 5 commandes et 3 fichiers de suivi évitée (estimation, non mesurée).
- À faire : corriger la capture du rapport OpenCode ; délai Ollama paramétrable ; mesurer les tokens réels (usage des sous-agents disponible, Codex/OpenCode non).

## Lot 2026-11-15

| Date heure | Tâche | Exécutant / modèle | Durée | Brief (car.) | Rapport (car.) | Statut | Retouche Claude | Note |
|---|---|---|---|---|---|---|---|---|
| 2026-11-15 21:0x | E délai Ollama paramétrable + rapport OpenCode complet | Codex CLI 0.154.0 / gpt-6.1-sol medium, workspace-write, worktree `codex/delegation-fix` | 235 s | 3100 | 900 | OK | aucune | 9 fichiers, miroirs identiques, 32 tests OK. Passage d'OpenCode en `--format json` : schéma d'événements présumé par Codex, non couvert par son rejeu (log texte) ; validé par Claude sur un essai réel OpenCode (13 s, message final complet). |
| 2026-11-15 21:0x | F retex /maintenance (propositions) | Codex CLI 0.154.0 / gpt-6.1-sol medium, read-only | 86 s | 2000 | 2900 | OK | aucune | 10 propositions sourcées fichier:ligne ; source de la 1re contrôlée par Claude (check_kit.py:98). `rg` indisponible dans la sandbox, repli Select-String. |
| 2026-11-15 21:0x | G exercice /create_agent sur projet jetable | sous-agent Claude / general-purpose, 66k tokens | 97 s | 2600 | 2700 | PARTIEL | aucune | Cœur OK ; étapes 8-9 et copie CLAUDE.md sautées (interdictions du brief). Écart {{STACK}} confirmé par Claude. Bloqué par le garde VRAM sur un `cp` d'un fichier dont le nom contient le runtime local. |
| 2026-11-15 21:1x | Essai réel du lanceur OpenCode corrigé | OpenCode / deepseek-v4.1-flash-free | 13 s | 250 | 450 | OK | aucune | Vérification du chemin JSON du correctif E. |

## Bilan du lot 2026-11-15 (rédigé par Claude)
- Marché : Codex gpt-6.1-sol pour un correctif cadré (diff propre, documentation liée mise à jour d'elle-même) et pour une analyse en lecture seule sourcée ; sous-agent pour exécuter une commande du kit de bout en bout.
- Échoué : aucun échec d'exécutant ; une hypothèse non vérifiée par Codex (schéma JSON OpenCode) attrapée à la relecture.
- Routage à changer : exiger dans le brief Codex un essai réel quand le correctif dépend du format de sortie d'un outil externe gratuit.
- Bloquant transverse : le garde VRAM bloque toute commande contenant le nom du runtime local (lecture, diff, copie, pytest ciblé), faux positif à corriger.
- Coût Claude : briefs ~7 700 car., rapports lus ~7 000 car., diff relu hors miroirs (estimation, non mesurée).

## Lot 2026-11-17

| Date heure | Tâche | Exécutant / modèle | Durée | Brief (car.) | Rapport (car.) | Statut | Retouche Claude | Note |
|---|---|---|---|---|---|---|---|---|
| 2026-11-17 14:15 | H audit des réf: signals + backlog | OpenCode / deepseek-v4.1-flash-free | 265 s | 1870 | 890 | OK | aucune | 96 réf., 0 morte ; 1 entrée backlog probablement faite (délai Ollama : essai à froid non tracé). Liste bien dans rapport.md (correctif E confirmé). |
| 2026-11-17 14:15 | I audit DEPLOYMENTS vs projets | Codex / read-only | 332 s | 2250 | 6530 | PARTIEL | aucune | 41 projets lus ; 5 versions indéterminables ; nombreux dépôts en avance sur l'amont (commits d'update non poussés). Lecture hors dépôt : seul Codex convient. |
| 2026-11-17 14:15 | J fusion backup_project.py Rayonne_Toi (préparation) | Codex / read-only | 96 s | 2360 | 2630 | OK | aucune | Diff testé par git apply --check (LF), load_config conservé ; non appliqué (modifs non commitées de Rayonne_Toi). |
| 2026-11-17 14:15 | K avertissement guides périmés check_docs | Codex / workspace-write, worktree codex/check-docs-avert | 233 s | 2220 | 1000 | OK | aucune | 3 avertissements mesurés, code de sortie inchangé, 21 tests. Échec check_kit en worktree = fichiers gitignorés absents (non-régression). |
| 2026-11-17 14:15 | L hook PreCompact (prototype kit) | Codex / workspace-write, worktree codex/precompact-hook | 128 s | 2650 | 640 | OK | aucune | 11 tests ; essai réel de compactage non fait. Même faux échec check_kit en worktree. |

## Bilan du lot 2026-11-17 (rédigé par Claude)
- Marché : 5 tâches en parallèle en environ 5,5 min, aucune relance ; rapports exploitables sans ouvrir log.txt.
- Échoué : rien côté exécutants ; check_kit en worktree signale à tort les fichiers gitignorés (à documenter dans le brief type).
- Routage à changer : préciser dans les briefs en worktree que check_kit échoue sur DEPLOYMENTS.md / AGENTS_REGISTRY.md / _archives/local absents.
- Coût Claude : briefs ~11 350 car. écrits, rapports ~11 700 car. lus, 2 diffs relus (~270 lignes) ; lecture évitée : 41 projets, 2 historiques git, implémentation et tests. Économie non mesurée en tokens (pas de relevé /cost avant/après).
