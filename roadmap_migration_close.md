# Roadmap — Migration `close.md` vers le mécanisme SPECIFICITES

Objectif : rendre `/update all` non destructeur pour `close.md` d'Appli_TSA_SDI_TDAH (et des
projets à `close.md` forké), en alignant le corps générique sur le kit et en déplaçant tout
comportement projet dans le bloc `SPECIFICITES PROJET`.
Créée le : 2026-09-06

Contexte : `start.md` d'Appli_TSA_SDI_TDAH a été migré (corps générique = `templates/` verbatim,
blocs projet en SPECIFICITES avec références d'étapes). `close.md` a été laissé de côté car son
corps générique kit porte des étapes kit-only qui planteraient un `/close` côté projet.

---

## Phase 1 — Assainir `templates/close.md` du kit [FAIT]
- [x] Étape 10 (`python scripts/check_kit.py`) : rendue conditionnelle « uniquement si
      `scripts/check_kit.py` existe à la racine du projet, sinon passer directement à l'étape 12 ».
- [x] Autres étapes du corps générique vérifiées génériques : rotation de sessions (étape 4), base
      de connaissances `DOCUMENTATION/` (étape 7, gardée par « si `INDEX.md` n'existe pas : ignorer »),
      bump `CHANGELOG.md`/README (étapes 8-9). Renvois « étape 11 » -> « étape 12 » corrigés.
- [x] Répercuté à l'identique dans `.claude/commands/close.md` et `templates/.claude/commands/close.md`
      (contrôle 1 de `check_kit.py`).
- [x] Gate : `check_kit.py` exit 0 ; relecture confirmant qu'un `/close` sans `scripts/check_kit.py`
      ne référence aucune commande inexistante.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer. Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## Phase 2 — Migrer `close.md` d'Appli_TSA_SDI_TDAH [FAIT]
- [x] Corps générique = `templates/.claude/commands/close.md` du kit, verbatim (diff vide hors
      SPECIFICITES, contrôle Python `HEAD IDENTIQUE`). Frontmatter aligné (`PowerShell(python *backup_file.py*)`).
- [x] Blocs projet déplacés en SPECIFICITES, chacun référençant son numéro d'étape kit :
  - Substitution `<contexte>` + branches (main / sync-marie : `_contexte/branches/sync-marie` +
    restrictions release/deploy / `agent/<alias>` : commit limité aux livrables `agent_role.md`,
    pas de merge/rebase/deploy/main / autre : stop).
  - Relevé final `inbox` gateway à « Étape 3 (avant) » (zones `design`/`discord` : `ack` ; racine : rien).
  - `statut.md` zone-agent -> parent déclaré dans `agent_role.md` (Étape 6 après).
  - README (Étape 8) + `CHANGELOG.md` (Étape 9) restreints à `main`.
  - Flux Marie sous « Étape 6 (ajouts) » : `manualTestsCatalog.ts`, routage tests manuels
    (`tests_manuels.md` vs catalogue in-app), `COMMUNICATION/Marie/a_transmettre.md`, `WHATS_NEW`
    de `E01Welcome.tsx`, cohérence `[discord-auto]`.
  - Étape 13 : `git add <contexte>/` ; push agent-branch conditionné.
  - Hooks : `2-bis` (Pré-synthèse) / `14-ter` (Fin) — remplacent `2-ter` / `11bis`.
- [x] Gate : diff corps générique == kit ; README/CHANGELOG/WHATS_NEW verrouillés sur `main` et
      commit sur `<contexte>/` -> un `/close` sur `agent/*` ne produit aucune écriture ni commit sur
      `main` ; sur `main`, `<contexte>` = `<dossier>/_contexte` -> comportement inchangé.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer. Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## Phase 3 — Rejouer `/update` sur Appli_TSA_SDI_TDAH [FAIT]

**Préalable d'ordre (bloquant)** : `/update` (cible unique) fait deux commits git dans le repo cible
(`backup:` puis `update:`) et `git add .claude/commands/`. Ne lancer qu'après :
1. `/close` du kit (commit des templates assainis + hooks).
2. `/close` d'Appli_TSA_SDI_TDAH (commit de la migration cible).
Sinon `/update` embarque du travail cible non lié sous des messages kit trompeurs, et estampille
`DEPLOYMENTS.md` avec une version kit périmée.

- [x] Préalable : migration Phase 2 non commitée dans la cible récupérée (commit `eef53e1` :
      `close.md`/`start.md`/`discord_loop.md`/`on_close.md`) avant `/update`.
- [x] `/update D:\ServOMorph\Appli_TSA_SDI_TDAH` depuis le kit (commit cible `00166dd`, poussé).
- [x] Vérifié : `start.md`/`close.md` non touchés (déjà byte-identiques au kit), une seule paire de
      marqueurs SPECIFICITES par fichier, `_contexte/` et `zones.md` intacts (git diff vide), commit
      cible limité aux fichiers protocole. `create_memory.md` → version scopée par zone.
- [x] Écart assumé : helper Ollama conservé dans `scripts/ollama_call.py` (pas de copie racine),
      documenté dans `CLAUDE.md` § Spécificités projet ; `AGENTS.md`/`GEMINI.md` non touchés.
- [x] Ligne d'Appli_TSA_SDI_TDAH dans `DEPLOYMENTS.md` → `v5.4 | 2026-09-06`.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer. Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

**Roadmap achevée (3/3).** Proposer l'archivage à l'utilisateur (accord explicite requis).
