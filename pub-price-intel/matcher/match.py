"""CLI to match offers to catalog SKUs using YAML rules."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

import pandas as pd

from .utils import load_catalog, load_offers, load_rules


def apply_rules(offers: pd.DataFrame, rules: Iterable[dict]) -> pd.DataFrame:
    offers = offers.copy()
    offers["matched_sku"] = None

    for rule_set in rules:
        venue = rule_set.get("venue")
        venue_rules = rule_set.get("rules", [])
        mask = offers["venue"].eq(venue)
        for rule in venue_rules:
            field = rule.get("field")
            contains = rule.get("contains", "").lower()
            sku = rule.get("match_sku")
            if field in offers.columns and sku:
                field_mask = offers[field].str.lower().str.contains(contains)
                offers.loc[mask & field_mask, "matched_sku"] = sku
    return offers


def match_offers(catalog_path: Path, offer_paths: Iterable[Path], rule_path: Path) -> pd.DataFrame:
    catalog = load_catalog(catalog_path)
    offers = load_offers(offer_paths)
    rules = load_rules(rule_path)
    if offers.empty:
        return pd.DataFrame(columns=["venue", "product_name", "price", "matched_sku"])
    matched = apply_rules(offers, rules.get("matching", []))
    return matched.merge(catalog, left_on="matched_sku", right_on="sku", how="left")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Match scraped offers to catalog SKUs.")
    parser.add_argument("--catalog", type=Path, default=Path("data/catalog.csv"))
    parser.add_argument("--snapshots", type=Path, nargs="*", default=[Path("data/snapshots/jdw.json")])
    parser.add_argument("--rules", type=Path, default=Path("rules/glasgow.yml"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    matched = match_offers(args.catalog, args.snapshots, args.rules)
    output_path = Path("data/matched_offers.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    matched.to_csv(output_path, index=False)
    print(f"Matched offers saved to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
