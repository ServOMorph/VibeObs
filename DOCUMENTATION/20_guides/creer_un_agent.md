---
type: guide
description: Créer un agent (zone à rôle) avec /create_agent
tags: guide, agent, create_agent
maj: 2026-11-14
---

# Créer un agent

Commande : `/create_agent <chemin_projet_cible> <dossier> [rôle] [parent=<alias_equipe>]` — s'exécute toujours depuis le kit, jamais copiée dans les projets cibles. Référence : [`../../_docs/protocole_vibecoding.md`](../../_docs/protocole_vibecoding.md) (section /create_agent).

## Ce que c'est

Un agent = une zone à rôle : charte `agent_role.md` (rôle, périmètre d'écriture, invariants) + `_contexte/` propre, enregistrée dans `zones.md` du projet cible, pilotable par /start et /close. L'option `parent=` l'ajoute à une équipe existante et met à jour son `team.md`.

## Phases

| Phase | Contenu |
|---|---|
| [PREFLIGHT] | Résout l'argument (dossier normalisé en MAJUSCULES, alias en minuscules) ; chemin non initialisé : remonte jusqu'au premier `.claude/zones.md` et propose ce projet ; vérifie que start.md du projet cible charge la charte (sinon avertit et demande confirmation ; une lecture en échec ne vaut jamais absence) ; zone parente = zone englobante la plus proche dans `zones.md` (à défaut la racine) ; repère les actions du `signals.md` du parent citant le dossier et, si la casse change, les références fonctionnelles au nom du dossier (code, configs, bases) |
| [COLLECTE] | Une question groupée unique : rôle durable (jamais inventé par défaut), périmètre d'écriture (`{{ECRITURE_ETENDUE}}`) et de lecture (`{{LECTURE_ETENDUE}}`), confirmation du mode et du projet déduit, migration des actions du parent, mise à jour des références au renommage ; lit la section « Données sensibles » du `CLAUDE.md` cible (`{{DONNEES_SENSIBLES}}`) ; analyse la stack seulement si le résultat sera utilisé |
| [ECRITURE] | Écrit tous les fichiers d'un coup — mode création (nouvel alias, contrôle d'unicité avant écriture dans zones.md) ou conversion (alias déjà présent : complète sans toucher zones.md ni un signals.md existant, sauf chemin mis à jour après renommage de casse). Migration acceptée : actions recopiées chez l'agent, remplacées chez le parent par une ligne `[info]`. Renommage de casse sous Windows en deux temps ; renommage refusé (verrou) : aucun processus terminé, report tracé en action P2 |
| [SORTIE] | Propose une seule fois de copier dans le presse-papier un message de mise à jour pour l'agent racine du projet cible — jamais écrit dans les fichiers du projet cible ; récapitule et recommande Opus pour [AUDIT] |
| [AUDIT] | Analyse à froid de la commande elle-même — jamais automatique, Opus imposé, sur demande explicite seulement |

## Effets de bord

- Charte générée depuis `templates/agent_role_TEMPLATE.md` ; depuis le 2026-09-16, un périmètre
  étendu (`{{ECRITURE_ETENDUE}}`) se répercute automatiquement dans les Invariants (« Ne jamais
  committer hors de ») — plus besoin de patch manuel (P14)
- Chaque création alimente `ameliorations_create_agent.md` (racine du kit) et `AGENTS_REGISTRY.md` (hors git)
- Les commandes kit-only restent dans `.claude/commands/` du kit, absentes de `templates/`

## Après création

L'agent est une zone : il se pilote via `/start <alias>` / `/close <alias>`. Sa zone parente (ligne « Zone parente » de la charte) est la zone englobante résolue au [PREFLIGHT], pas forcément la racine. Son verdict évolue dans AGENTS_REGISTRY.md selon le retour d'expérience. Cas particulier : agent dont le dossier est la racine du projet (alias sans ligne dans zones.md) — signalé au registre, ligne "Zone parente" omise de la charte.
