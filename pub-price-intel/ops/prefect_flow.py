"""Prefect flow for orchestrating the scraping and matching pipeline."""

from __future__ import annotations

from pathlib import Path

from prefect import flow, task

from scrapers.spoons_pdf import main as run_spoons
from scrapers.nicholsons_html import main as run_nicholsons
from matcher.match import match_offers


@task
def scrape_offers() -> list[Path]:
    snapshot_dir = Path("data/snapshots")
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    return [
        run_spoons(snapshot_dir),
        run_nicholsons(snapshot_dir),
    ]


@task
def match(snapshot_paths: list[Path]) -> Path:
    output = match_offers(Path("data/catalog.csv"), snapshot_paths, Path("rules/glasgow.yml"))
    output_path = Path("data/matched_offers.csv")
    output.to_csv(output_path, index=False)
    return output_path


@flow
def competitor_price_flow() -> Path:
    snapshots = scrape_offers()
    return match(snapshots)


if __name__ == "__main__":
    competitor_price_flow()
