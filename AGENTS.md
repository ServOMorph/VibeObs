# AGENTS.md

Instructions pour les agents non-Claude (Codex, Gemini, etc.) intervenant sur ce projet.
Ce fichier ne duplique pas `.claude/CLAUDE.md` (protocole vibecoding start/close, réservé à
Claude Code) : il ne couvre que ce qui s'applique à tout agent, indépendamment de l'outil.

## Base de connaissances

Si ce projet dispose d'un dossier `DOCUMENTATION/` à la racine avec un fichier `INDEX.md`, il
centralise la documentation métier du projet, consultable par tout agent quel que soit l'outil
utilisé. Avant d'affirmer un fait métier non disponible dans le contexte immédiat, consulter
`DOCUMENTATION/INDEX.md` (catalogue, une ligne par document) puis n'ouvrir que le(s) document(s)
pertinent(s) — jamais tout le dossier. Absence de `DOCUMENTATION/` : rien à consulter.

## Communication Intercom

Si `INTERCOM_AGENT.md` existe à la racine, le lire et l'appliquer pour tout message Intercom. Avant
chaque réponse finale, clôture de tâche ou fin de session, exécuter obligatoirement
`python intercom/intercom.py inbox --urgent`. Une urgence est traitée avant la conclusion, jamais
reportée silencieusement ; suivre alors la séquence `pause`, `ack`, puis `resume` d'INTERCOM_AGENT.md.
