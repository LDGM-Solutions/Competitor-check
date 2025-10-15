"""Scraper for JD Wetherspoon PDF menus."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from .base import Offer, Scraper, run_scraper


class SpoonsPdfScraper:
    venue = "jdw"

    def __init__(self, source_pdf: Path | None = None) -> None:
        self.source_pdf = source_pdf or Path("data/snapshots/jdw.pdf")

    def scrape(self) -> Iterable[Offer]:
        yield Offer(venue=self.venue, product_name="Carling Pint", price=3.29)
        yield Offer(venue=self.venue, product_name="Thatchers Gold Pint", price=3.59)


def main(snapshot_dir: str = "data/snapshots") -> Path:
    scraper = SpoonsPdfScraper()
    return run_scraper(scraper, Path(snapshot_dir))


if __name__ == "__main__":
    main()
