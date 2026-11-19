#!/usr/bin/env bash
# Passe-plat gardé : remplace l'appel direct `codex <args>` des scripts shell.
# Usage : garde_codex.sh [options codex...] exec [options...] [-]
# Le prompt envoyé sur l'entrée standard est transmis tel quel.
dir="$(cd "$(dirname "$0")" && pwd)"
script="$dir/run_codex.ps1"
command -v cygpath >/dev/null 2>&1 && script="$(cygpath -w "$script")"
encoded="$(printf '%s\0' "$@" | base64 | tr -d '\n')"
exec powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$script" -Passe -ArgsB64 "$encoded"
