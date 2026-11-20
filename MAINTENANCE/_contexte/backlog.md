# Backlog — maintenance

- [dette] Environnement virtuel `argos-translate` de `participation_github_v2` : chemins d'origine remplacés dans `pyvenv.cfg` et les scripts d'activation lors de la migration, mais environnement jamais testé sur D:. Peut-être à recréer.
  - fait quand: `activate` fonctionne depuis D: et `python -c "import argostranslate"` réussit, ou l'environnement est recréé.
  - réf: `D:\ServOMorph\participation_github_v2\repos_suivis\argos-translate\env`
- [dette] La copie D: de TableauDeBord garde des chemins vers `Agents_IA_V2`, `IA_V5` et `auto_copier_coller` (config des lanceurs, aide au diagnostic) ; `Agents_IA_V2` et `IA_V5` sont introuvables sur C: et D:.
  - fait quand: les lanceurs concernés démarrent ou sont retirés de `config/paths.json`.
  - réf: `D:\ServOMorph\TableauDeBord\config\paths.json`
- [dette] `lancer_sur_bureau.py` et `balayer_chemins.py` n'ont aucun test automatisé (seulement un essai réel chacun) ; seul `migrer_projet.py` est couvert (12 tests).
  - fait quand: des tests pytest couvrent le repérage de fenêtres et le motif de recherche, ou la décision de ne pas les tester est actée.
  - réf: `MAINTENANCE/scripts/lancer_sur_bureau.py`
- [dette] `.env.example` de `Lieux_Hybrides` cite encore le chemin C: de pifpafpof ; fichier non lu (règle sur les `.env`), à corriger par l'utilisateur.
  - fait quand: le chemin du fichier pointe vers `D:\ServOMorph\pifpafpof`.
  - réf: `D:\ServOMorph\Lieux_Hybrides\.env.example`
- [piste] Migrer `site_internet_Sereniatech_V2` (reste sur C:, l'utilisateur a interdit d'y toucher le 2026-11-20 ; mode de déploiement par GitHub supposé, non confirmé).
  - fait quand: l'utilisateur demande la migration, ou décide de laisser le site sur C:.
  - réf: `C:\Users\raph6\Documents\ServOMorph\site_internet_Sereniatech_V2`
- [piste] Un lanceur du dossier Démarrage de Windows pointe vers un autre dossier sur C: (`Documents\SerenIATech\SérénIATech_dev`, hors `ServOMorph`) : même risque si ce dossier est déplacé un jour.
  - fait quand: l'utilisateur décide de le migrer ou de le laisser sur C:.
  - réf: `C:\Users\raph6\Documents\SerenIATech\SérénIATech_dev\launch_ui.bat`
