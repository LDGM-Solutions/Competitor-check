"""Utility functions for offer matching."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd
import yaml


def load_catalog(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def load_offers(paths: Iterable[Path]) -> pd.DataFrame:
    frames = [pd.read_json(path) for path in paths if path.exists()]
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()


def load_rules(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)
