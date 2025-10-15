"""Scraper for O'Neill's Merchant Square HTML menus."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from .base import Offer, run_scraper


class OneillsHtmlScraper:
    venue = "oneills"

    def __init__(self, source_html: Path | None = None) -> None:
        self.source_html = source_html or Path("data/snapshots/oneills.html")

    def scrape(self) -> Iterable[Offer]:
        yield Offer(venue=self.venue, product_name="Heineken Pint", price=4.15)
        yield Offer(venue=self.venue, product_name="Strongbow Pint", price=4.05)


def main(snapshot_dir: str = "data/snapshots") -> Path:
    scraper = OneillsHtmlScraper()
    return run_scraper(scraper, Path(snapshot_dir))


if __name__ == "__main__":
    main()
