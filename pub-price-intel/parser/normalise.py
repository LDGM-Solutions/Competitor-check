"""Helpers to normalise scraped offer data."""

from __future__ import annotations

import re
from typing import Iterable

import pandas as pd

VOLUME_PATTERN = re.compile(r"(?P<volume>\d+)\s?ml", re.IGNORECASE)


def normalise_product_name(name: str) -> str:
    return name.strip().title()


def extract_volume(text: str) -> int | None:
    match = VOLUME_PATTERN.search(text)
    return int(match.group("volume")) if match else None


def build_dataframe(offers: Iterable[dict[str, object]]) -> pd.DataFrame:
    frame = pd.DataFrame(offers)
    frame["product_name"] = frame["product_name"].astype(str).map(normalise_product_name)
    return frame
