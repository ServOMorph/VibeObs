"""Valeur indicative, au tarif API, des tokens retirés du contexte par /compact.

Sous abonnement Pro/Max, aucun euro n'est réellement économisé : c'est du quota.
Le calcul suppose que les tokens retirés auraient été relus depuis le cache à chaque tour suivant.
Prix de lecture du cache (USD par million de tokens), tarif API au 2026-11-03.
"""

import argparse
import sys

PRIX_CACHE_USD_PAR_M = {
    "opus": 0.20,
    "sonnet": 0.10,
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tokens", type=int, help="tokens économisés affichés par /compact")
    parser.add_argument("--modele", choices=sorted(PRIX_CACHE_USD_PAR_M), default="opus")
    parser.add_argument("--tours", type=int, default=20, help="nombre de tours restants dans la session")
    parser.add_argument("--taux", type=float, required=True, help="taux de change : 1 USD = X EUR")
    args = parser.parse_args()
    if args.tokens < 0 or args.tours < 0 or args.taux <= 0:
        print("ERREUR: tokens et tours positifs, taux strictement positif", file=sys.stderr)
        return 1
    usd = args.tokens / 1_000_000 * PRIX_CACHE_USD_PAR_M[args.modele] * args.tours
    eur = usd * args.taux
    print(f"{args.tokens} tokens x {args.tours} tours ({args.modele}) : {usd:.2f} USD = {eur:.2f} EUR (équivalent API, indicatif)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
