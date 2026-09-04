#!/usr/bin/env python3
"""Client générique de l'API REST Netlify v1."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urljoin
from urllib.request import Request, urlopen

API_ROOT = "https://api.netlify.com/api/v1/"


def load_local_token() -> None:
    """Charge uniquement le token Netlify depuis .env.netlify, sans l'afficher."""
    if os.environ.get("NETLIFY_AUTH_TOKEN"):
        return
    env_file = Path.cwd() / ".env.netlify"
    if not env_file.is_file():
        return
    for line in env_file.read_text(encoding="utf-8").splitlines():
        key, separator, value = line.partition("=")
        if separator and key.strip() == "NETLIFY_AUTH_TOKEN":
            os.environ["NETLIFY_AUTH_TOKEN"] = value.strip().strip('"').strip("'")
            return


def read_body(value: str | None) -> bytes | None:
    if value is None:
        return None
    if value.startswith("@"):
        return Path(value[1:]).read_bytes()
    return value.encode("utf-8")


def request(url: str, method: str, body: bytes | None, token: str) -> tuple[int, bytes, dict[str, str]]:
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "User-Agent": "netlify-template-client/1.0",
    }
    if body is not None:
        headers["Content-Type"] = "application/json"
    response = Request(url, data=body, headers=headers, method=method)
    with urlopen(response, timeout=60) as result:
        return result.status, result.read(), dict(result.headers.items())


def main() -> int:
    parser = argparse.ArgumentParser(description="Appelle toute route de l'API REST Netlify v1.")
    endpoint = parser.add_mutually_exclusive_group(required=True)
    endpoint.add_argument("--path", help="Route v1, par exemple /sites ou /sites/<id>.")
    endpoint.add_argument("--url", help="URL complète, notamment pour un build hook.")
    parser.add_argument("--method", default="GET", help="Méthode HTTP (GET par défaut).")
    parser.add_argument("--data", help="Corps JSON ou @chemin/vers/payload.json.")
    parser.add_argument("--query", action="append", default=[], metavar="CLE=VALEUR")
    parser.add_argument("--paginate", action="store_true", help="Suit les pages Link tant qu'elles existent.")
    parser.add_argument("--output", help="Écrit la réponse brute dans ce fichier au lieu de stdout.")
    args = parser.parse_args()

    load_local_token()
    token = os.environ.get("NETLIFY_AUTH_TOKEN")
    if not token:
        parser.error("NETLIFY_AUTH_TOKEN est requis (environnement ou .env.netlify).")

    if args.url:
        url = args.url
    else:
        url = urljoin(API_ROOT, args.path.lstrip("/"))
    if args.query:
        query = {}
        for item in args.query:
            key, separator, value = item.partition("=")
            if not separator or not key:
                parser.error(f"Query invalide : {item}. Format attendu CLE=VALEUR.")
            query[key] = value
        url = f"{url}{'&' if '?' in url else '?'}{urlencode(query)}"

    body = read_body(args.data)
    pages: list[object] = []
    try:
        while True:
            _, response_body, headers = request(url, args.method.upper(), body, token)
            if args.paginate:
                pages.append(json.loads(response_body.decode("utf-8")))
                links = headers.get("Link", "")
                next_links = [part for part in links.split(",") if 'rel="next"' in part]
                if next_links and "<" in next_links[0] and ">" in next_links[0]:
                    url = next_links[0].split("<", 1)[1].split(">", 1)[0]
                    body = None
                    continue
                response_body = json.dumps(pages, ensure_ascii=False, indent=2).encode("utf-8")
            if args.output:
                Path(args.output).write_bytes(response_body)
            else:
                sys.stdout.buffer.write(response_body)
                if response_body and not response_body.endswith(b"\n"):
                    sys.stdout.buffer.write(b"\n")
            return 0
    except HTTPError as error:
        details = error.read().decode("utf-8", errors="replace")
        print(f"Netlify API HTTP {error.code}: {details}", file=sys.stderr)
    except (URLError, OSError, json.JSONDecodeError) as error:
        print(f"Appel Netlify impossible: {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
