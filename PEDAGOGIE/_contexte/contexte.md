# Contexte — pedagogie

## Objectif (immuable sauf décision explicite)
Produire et tenir à jour un parcours pédagogique complet qui permet à une personne de reconstruire VibeObs from scratch, à l'image de sa propre pratique. À chaque `/start`, analyser le kit (CHANGELOG, commandes, templates) pour repérer les nouveautés depuis la dernière session et les intégrer au parcours. Livrables, calqués sur les ressources Claude Code de SérénIATech publiées sur Netlify : page de cours HTML unique prête pour Netlify (`index.html`, `assets/`, `_headers` et `robots.txt` en noindex), fiches de PP selon le gabarit, modèle générique sans donnée personnelle, journal de retex.

## Stack / contraintes techniques (stable, rarement modifié)
- Page de cours : HTML statique unique, modèle `D:\ServOMorph\site_internet_ST_v3\dist_ressources_claudecode` (`index.html`, `assets/css`, `assets/fonts`, `_headers` avec `X-Robots-Tag: noindex, nofollow, noarchive`, `robots.txt` en `Disallow: /`).
- Fiches de PP : Markdown, selon `C:\Users\raph6\Documents\SerenIATech\SérénIATech_dev\Gestion clients\Clients\Marion-Pargade\parcours\modele_generique\gabarit_fiche_PP.md` ; la page de cours fait référence, les fiches la suivent.
- Vocabulaire : « PP » = phase pédagogique.
- Organisation prévue : `PEDAGOGIE/modele_generique/` (gabarit, fiches), `page_cours/` (source), `dist/` (prêt pour Netlify), `journal_retex.md`.
- Source du contenu : kit VibeObs (`CHANGELOG.md`, `.claude/commands/`, `templates/`).

## État actuel (réécrit intégralement à chaque /close)
Agent créé et lancé le 2026-11-06. Parcours non encore choisi, aucun livrable de contenu produit.

## Décisions structurantes (append only — 10 entrées max, 5 lignes max/entrée, archiver au-delà)
- 2026-11-06 : Initialisation du protocole vibecoding.
- 2026-11-06 : écriture limitée à `PEDAGOGIE/`, aucune publication par l'agent (`dist/` préparé, l'utilisateur publie) ; lecture étendue sans `instance_marion/` ni secrets.
