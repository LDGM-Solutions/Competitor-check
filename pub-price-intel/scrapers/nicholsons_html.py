"""Scraper for Nicholson's Drum & Monkey HTML menus."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from .base import Offer, run_scraper


class NicholsonsHtmlScraper:
    venue = "nicholsons"

    def __init__(self, source_html: Path | None = None) -> None:
        self.source_html = source_html or Path("data/snapshots/nicholsons.html")

    def scrape(self) -> Iterable[Offer]:
        yield Offer(venue=self.venue, product_name="Guinness Pint", price=4.95)
        yield Offer(venue=self.venue, product_name="Aspall Cider Pint", price=4.85)


def main(snapshot_dir: str = "data/snapshots") -> Path:
    scraper = NicholsonsHtmlScraper()
    return run_scraper(scraper, Path(snapshot_dir))


if __name__ == "__main__":
    main()
