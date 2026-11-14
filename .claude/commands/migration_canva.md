---
disable-model-invocation: true
description: Guide pas à pas pour copier des dossiers Canva d'un compte vers un autre (utilisateur novice)
---

# /migration_canva

## Principe

Tu n'as aucun accès à Canva. L'utilisateur fait chaque clic ; tu donnes une seule action à la fois et
tu tiens le suivi. Canva ne transfère rien en bloc entre comptes : on **partage** depuis le compte source,
puis on **fait une copie** dans le compte destination. Seule la copie appartient au compte destination.
Ce qui arrive à cette copie si l'original est supprimé n'a pas été trouvé dans l'aide : à vérifier pendant le test (Étape 6).

## Limites (aide Canva)

- Une copie se fait **design par design** entre deux comptes distincts. La copie groupée d'un dossier n'existe qu'entre équipes.
- Partager un design ne relie pas les deux comptes.
- Un abonnement Canva Pro ne se transfère pas. Les éléments Pro, le kit de marque et les polices dans une copie sur compte gratuit : non trouvé, à vérifier pendant le test.
- Les images et vidéos importées dans un dossier partagé : non trouvé, à vérifier pendant le test (Étape 4).
- Si le bouton « Partager » est grisé, l'administrateur d'équipe a peut-être bloqué l'envoi hors équipe.
- Une copie ne reprend pas l'historique des versions de l'original.

## Règles

- Un message = une action. 3 lignes au plus, vocabulaire simple, le nom exact du bouton entre
  « guillemets ». Finir par « Réponds ok quand c'est fait » ou par une question `AskUserQuestion`.
- Ne jamais affirmer ce qu'affiche l'écran de l'utilisateur : lui demander ce qu'il voit.
- Si l'utilisateur ne trouve pas un bouton : lui demander de décrire l'écran ou d'envoyer une
  capture, puis adapter l'instruction. Ne jamais inventer un nom de menu.
- Ne jamais demander l'e-mail du compte source ni aucun mot de passe.
- Aucune suppression pendant la migration. Les originaux restent intacts.
- Suivi : tenir `migration_canva_suivi.md` dans le dossier courant (une ligne par dossier : nom,
  nombre d'éléments à l'origine, nombre de copies vérifiées, statut `à faire | partagé | copié | vérifié | problème`).
  Ni e-mail ni lien dans ce fichier. Le relire après chaque `/compact` et à la reprise.

## Étape 0 — Reprise

Si `migration_canva_suivi.md` existe : afficher les dossiers non `vérifié` et reprendre au premier.

## Étape 1 — Deux fenêtres

1. Ouvrir Canva dans le navigateur habituel, connecté au compte **source** (celui qu'on vide).
2. Ouvrir une fenêtre de navigation privée (Ctrl+Maj+N), aller sur canva.com, se connecter au compte
   **destination**.
Toujours rappeler dans quelle fenêtre agir : « Fenêtre SOURCE » ou « Fenêtre DESTINATION ».

## Étape 2 — Ce qu'on copie

1. Fenêtre SOURCE : cliquer « Projets ». Demander la liste des noms de dossiers affichés, recopiés tels quels
   (libellés exacts à confirmer à l'écran).
2. Demander lesquels migrer (tous, ou une liste).
3. Pour chaque dossier retenu : l'ouvrir, demander le nombre d'éléments affiché et s'il contient des
   images ou vidéos importées (pas seulement des designs).
4. Écrire le fichier de suivi, l'afficher en tableau court, demander validation.

## Étape 3 — Partager (dossier par dossier)

Fenêtre SOURCE, sur le dossier : « Partager » (ouvrir le dossier, ou survoler le dossier puis « ⋯ » / « + »
selon l'écran) → saisir l'e-mail du compte destination → accès « Peut modifier » → « Envoyer ».
Avant l'envoi, demander à l'utilisateur de relire l'adresse lettre par lettre.
Partager un dossier par e-mail à un compte hors équipe : non trouvé dans l'aide, à vérifier pendant le test.
Statut → `partagé`.

## Étape 4 — Copier (dossier par dossier)

Fenêtre DESTINATION :
1. Créer un dossier vide du même nom dans « Projets » (libellé à confirmer à l'écran).
2. Ouvrir le dossier partagé (« Partagé avec vous » dans l'aide en anglais, ou lien reçu par e-mail).
3. Pour chaque design, un par un : l'ouvrir → « Fichier » → « Faire une copie ».
   Déplacer ensuite la copie dans le nouveau dossier (libellé à confirmer à l'écran).
4. Images et vidéos importées : non trouvé dans l'aide, à vérifier pendant le test. Si elles ne sont pas
   copiées, les télécharger dans la fenêtre SOURCE puis les importer dans la fenêtre DESTINATION
   (dans le nouveau dossier).
Statut → `copié`.

## Étape 5 — Vérifier (dossier par dossier)

Fenêtre DESTINATION, dans le nouveau dossier :
1. Le nombre d'éléments est-il égal au nombre noté à l'étape 2 ?
2. Ouvrir 2 designs au hasard : pages, images et textes présents ? Filigrane ou élément bloqué
   (contenu Pro, kit de marque, polices) ? Noter tout écart en `problème`.
Égalité et aucun écart : statut → `vérifié`.

## Étape 6 — Preuve finale

Quand tous les dossiers sont `vérifié` : Fenêtre SOURCE, retirer le partage d'un dossier (« Partager »
→ remettre le partage sur « Non partagé » ou supprimer l'accès du compte destination). Fenêtre DESTINATION :
le nouveau dossier doit toujours contenir ses copies. Si oui, retirer les autres partages ; si non, revenir à l'étape 4 pour ce dossier.
Ce test est la seule preuve que la copie survit au retrait du partage : le faire avant toute suppression.

## Étape 7 — Bilan

Afficher : dossiers vérifiés / total, éléments copiés / total, problèmes avec leur cause. Conseiller de
garder les originaux quelques semaines. Un design supprimé reste 30 jours dans la corbeille ; une image ou
vidéo sortie de la corbeille ne peut plus être restaurée. Ne proposer aucune suppression ; si l'utilisateur la demande
lui-même, la guider dossier par dossier, une confirmation par dossier, après l'étape 6 seulement.
