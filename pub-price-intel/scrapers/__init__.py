"""Scraper implementations for different venues."""

from .ark_html import ArkHtmlScraper
from .nicholsons_html import NicholsonsHtmlScraper
from .oneills_html import OneillsHtmlScraper
from .spoons_pdf import SpoonsPdfScraper
from .walkabout_html import WalkaboutHtmlScraper

__all__ = [
    "ArkHtmlScraper",
    "NicholsonsHtmlScraper",
    "OneillsHtmlScraper",
    "SpoonsPdfScraper",
    "WalkaboutHtmlScraper",
]
