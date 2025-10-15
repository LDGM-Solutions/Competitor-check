"""Command line interface to orchestrate scraping, parsing, and matching."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from matcher.match import match_offers
from parser.normalise import build_dataframe
from scrapers.spoons_pdf import main as run_spoons
from scrapers.nicholsons_html import main as run_nicholsons

SNAPSHOT_DIR = Path("data/snapshots")


def scrape() -> list[Path]:
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    return [
        run_spoons(str(SNAPSHOT_DIR)),
        run_nicholsons(str(SNAPSHOT_DIR)),
    ]


def parse(snapshot_paths: list[Path]) -> pd.DataFrame:
    offers = []
    for path in snapshot_paths:
        if path.exists():
            offers.extend(pd.read_json(path).to_dict(orient="records"))
    return build_dataframe(offers)


def match(snapshot_paths: list[Path]) -> Path:
    matched = match_offers(Path("data/catalog.csv"), snapshot_paths, Path("rules/glasgow.yml"))
    output_path = Path("data/matched_offers.csv")
    matched.to_csv(output_path, index=False)
    return output_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Pub price intelligence CLI")
    parser.add_argument("command", choices=["scrape", "parse", "match", "run"], help="Which stage to execute")
    args = parser.parse_args()

    if args.command == "scrape":
        paths = scrape()
        print("Snapshots saved:", ", ".join(str(path) for path in paths))
    elif args.command == "parse":
        frame = parse(scrape())
        print(frame.head())
    elif args.command == "match":
        output = match(scrape())
        print(f"Matched offers written to {output}")
    elif args.command == "run":
        paths = scrape()
        frame = parse(paths)
        output = match(paths)
        print(f"Pipeline completed with {len(frame)} offers. Output: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
