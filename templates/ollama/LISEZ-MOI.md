# Ollama — déléguer les tâches répétitives à un modèle local

Ce template fournit le lanceur `ollama_call.py` et la section de consignes à ajouter au `CLAUDE.md` d'un projet. Le modèle tourne sur la machine : le prompt ne quitte pas le PC.

## Contenu

| Fichier | Rôle |
| --- | --- |
| `ollama_call.py` | Envoie un prompt unique à Ollama local (`http://localhost:11434/api/generate`) et écrit la réponse sur la sortie standard en UTF-8. Bibliothèque standard uniquement. |
| `CLAUDE_SECTION.md` | Section « Délégation Ollama » à copier dans le `CLAUDE.md` du projet. |

`ollama_call.py` est une copie de `templates/ollama_call.py` du kit (celle que `/init_projet` et `/update` déploient). Les deux fichiers doivent rester identiques : toute correction se fait dans les deux.

## Prérequis

- Ollama installé et démarré (service local sur le port 11434).
- Le modèle choisi téléchargé : `ollama pull gemma4:e4b` pour le modèle par défaut, ou un autre modèle via `OLLAMA_MODEL`.
- Python 3.

## Utilisation

```powershell
python ollama_call.py "Rédige un message de commit pour : ..."
$env:OLLAMA_MODEL = "qwen2.5-coder:7b"; python ollama_call.py "..."
```

- Modèle par défaut : `gemma4:e4b`. Changer de modèle avec la variable d'environnement `OLLAMA_MODEL`.
- Un seul prompt par appel, sans historique ni flux : la réponse complète s'affiche à la fin.
- Code de sortie 1 et message sur la sortie d'erreur si Ollama est arrêté, si le modèle est absent, si la réponse est vide ou si le délai est dépassé.

## Limites constatées

- Le délai d'attente du lanceur est de 60 secondes. Sur ce PC, le premier appel après un moment sans usage a pris plus de 60 secondes (chargement du modèle en mémoire) et un essai a échoué par dépassement du délai ; l'appel suivant a répondu en environ 3 secondes. Relancer la commande si le premier appel échoue par délai.
- Les modèles locaux se trompent : relire la sortie avant de l'utiliser, surtout pour du code. Réserver Ollama aux tâches répétitives et cadrées (messages de commit, brouillons de posts, changelogs, données de test, digest de logs).

## Vérifier l'installation

```powershell
python ollama_call.py "Réponds uniquement par le mot OK."
```

La commande doit afficher `OK`. Sinon, lire le message d'erreur : connexion impossible (Ollama non démarré), modèle introuvable (`ollama pull`), ou délai dépassé (relancer).

## Insertion dans un projet

`/insert_template <projet> ollama` copie ces fichiers dans `<projet>/VibeObs/ollama/`. Pour l'utiliser comme dans les projets du kit, copier `ollama_call.py` à la racine du projet et ajouter `CLAUDE_SECTION.md` au `CLAUDE.md`.
