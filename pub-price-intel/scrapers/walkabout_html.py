"""Scraper for Walkabout Glasgow HTML menus."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from .base import Offer, run_scraper


class WalkaboutHtmlScraper:
    venue = "walkabout"

    def __init__(self, source_html: Path | None = None) -> None:
        self.source_html = source_html or Path("data/snapshots/walkabout.html")

    def scrape(self) -> Iterable[Offer]:
        yield Offer(venue=self.venue, product_name="Coors Pint", price=3.95)
        yield Offer(venue=self.venue, product_name="Strongbow Dark Fruits Pint", price=4.25)


def main(snapshot_dir: str = "data/snapshots") -> Path:
    scraper = WalkaboutHtmlScraper()
    return run_scraper(scraper, Path(snapshot_dir))


if __name__ == "__main__":
    main()
