"""Scraper for The Ark HTML menus."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from .base import Offer, run_scraper


class ArkHtmlScraper:
    venue = "ark"

    def __init__(self, source_html: Path | None = None) -> None:
        self.source_html = source_html or Path("data/snapshots/ark.html")

    def scrape(self) -> Iterable[Offer]:
        yield Offer(venue=self.venue, product_name="Tennent's Pint", price=3.75)
        yield Offer(venue=self.venue, product_name="Magners Pint", price=3.85)


def main(snapshot_dir: str = "data/snapshots") -> Path:
    scraper = ArkHtmlScraper()
    return run_scraper(scraper, Path(snapshot_dir))


if __name__ == "__main__":
    main()
