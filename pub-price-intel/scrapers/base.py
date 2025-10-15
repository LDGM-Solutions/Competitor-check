"""Common helpers for scraper implementations."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Protocol

from playwright.sync_api import sync_playwright


@dataclass
class Offer:
    venue: str
    product_name: str
    price: float

    def to_dict(self) -> dict[str, str | float]:
        return {
            "venue": self.venue,
            "product_name": self.product_name,
            "price": self.price,
        }


class Scraper(Protocol):
    venue: str

    def scrape(self) -> Iterable[Offer]:
        ...


def save_offers(offers: Iterable[Offer], output_path: Path) -> None:
    data = [offer.to_dict() for offer in offers]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def run_scraper(scraper: Scraper, snapshot_dir: Path) -> Path:
    output = snapshot_dir / f"{scraper.venue}.json"
    offers = list(scraper.scrape())
    save_offers(offers, output)
    return output


def launch_browser() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        browser.close()
