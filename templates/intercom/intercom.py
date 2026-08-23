#!/usr/bin/env python3
"""Messagerie inter-projets locale : file persistante, urgences et reprise."""
from __future__ import annotations
import argparse, json, os, subprocess, time, uuid
from datetime import datetime, timezone
from pathlib import Path
ROOT = Path(os.environ.get("INTERCOM_ROOT", Path(__file__).resolve().parent.parent))
BASE = ROOT / ".intercom"
CONFIG, INBOX, HANDLED, RESUME = BASE / "config.json", BASE / "inbox.jsonl", BASE / "handled.jsonl", BASE / "reprise.md"
def rows(path):
    return [] if not path.exists() else [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
def append(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as f: f.write(json.dumps(value, ensure_ascii=False) + "\n")
def cfg():
    if not CONFIG.exists(): raise SystemExit(f"Configuration absente : {CONFIG}")
    return json.loads(CONFIG.read_text(encoding="utf-8"))
def waiting():
    done = {x["id"] for x in rows(HANDLED) if "id" in x}
    return [x for x in rows(INBOX) if x.get("id") not in done]
def display(items):
    if not items: print("Aucun message en attente.")
    for x in items: print(f"[{x['priority'].upper()}] {x['id']} | de {x['sender']} | {x['created_at']}\nSujet : {x['subject']}\n{x['body']}\n")
def notify(entry, recipient):
    """Alerte Windows locale ; l'échec ne doit jamais empêcher l'envoi."""
    text = f"Intercom [{entry['priority'].upper()}] {entry['sender']} → {recipient} : {entry['subject']}"[:240]
    try:
        subprocess.run(["msg.exe", "*", text], capture_output=True, text=True, timeout=5,
                       creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    except (OSError, subprocess.TimeoutExpired):
        pass
def send(a):
    recipient = cfg().get("recipients", {}).get(a.to)
    if not recipient: raise SystemExit(f"Destinataire inconnu : {a.to}")
    target = Path(recipient["path"]).resolve()
    if not target.exists(): raise SystemExit(f"Projet destinataire introuvable : {target}")
    x = {"id": uuid.uuid4().hex[:12], "created_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"), "sender": cfg()["project"], "priority": a.priority, "subject": a.subject, "body": a.body}
    append(target / ".intercom/inbox.jsonl", x); notify(x, a.to); print(f"Message {x['id']} envoyé à {a.to} ({a.priority}).")
def ack(a):
    if a.id not in {x.get("id") for x in waiting()}: raise SystemExit(f"Message en attente introuvable : {a.id}")
    append(HANDLED, {"id": a.id, "handled_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")}); print(f"Message {a.id} marqué comme traité.")
def pause(a):
    BASE.mkdir(parents=True, exist_ok=True)
    RESUME.write_text(f"# Point de reprise intercom\n\n- Créé : {datetime.now(timezone.utc).astimezone().isoformat(timespec='seconds')}\n- Travail interrompu : {a.task}\n- Prochaine action : {a.next_action}\n- Contexte utile : {a.context}\n", encoding="utf-8")
    print(f"Point de reprise enregistré : {RESUME}")
def watch(a):
    BASE.mkdir(parents=True, exist_ok=True); INBOX.touch(exist_ok=True); pos = 0 if a.from_start else INBOX.stat().st_size; print("Écoute intercom active. Ctrl+C pour arrêter.")
    while True:
        size = INBOX.stat().st_size
        if size < pos: pos = 0
        if size > pos:
            with INBOX.open(encoding="utf-8") as f: f.seek(pos); lines = f.readlines(); pos = f.tell()
            for line in lines:
                x = json.loads(line); print(f"NOUVEAU_MESSAGE [{x['priority'].upper()}] {x['id']} de {x['sender']} : {x['subject']}", flush=True)
        time.sleep(a.interval)
def main():
    p = argparse.ArgumentParser(description=__doc__); s = p.add_subparsers(dest="action", required=True)
    x=s.add_parser("send"); x.add_argument("to"); x.add_argument("--priority", choices=("normal", "urgent"), default="normal"); x.add_argument("--subject", required=True); x.add_argument("--body", required=True); x.set_defaults(func=send)
    x=s.add_parser("inbox"); x.add_argument("--urgent", action="store_true"); x.set_defaults(func=lambda a: display([r for r in waiting() if not a.urgent or r["priority"] == "urgent"]))
    x=s.add_parser("ack"); x.add_argument("id"); x.set_defaults(func=ack)
    x=s.add_parser("pause"); x.add_argument("--task", required=True); x.add_argument("--next-action", required=True); x.add_argument("--context", required=True); x.set_defaults(func=pause)
    x=s.add_parser("resume"); x.set_defaults(func=lambda a: print(RESUME.read_text(encoding="utf-8") if RESUME.exists() else "Aucun point de reprise."))
    x=s.add_parser("watch"); x.add_argument("--interval", type=float, default=1.0); x.add_argument("--from-start", action="store_true"); x.set_defaults(func=watch)
    a=p.parse_args(); a.func(a)
if __name__ == "__main__": main()
