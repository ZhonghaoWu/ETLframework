"""Data loaders for persisting transformed frames."""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
import pandas as pd


class BaseLoader(ABC):
    @abstractmethod
    def load(self, frame: pd.DataFrame, target: Path) -> Path:
        """Persist transformed data and return destination path."""
        raise NotImplementedError


class CSVSaver(BaseLoader):
    """Save each symbol to a CSV file."""

    def load(self, frame: pd.DataFrame, target: Path) -> Path:
        target.mkdir(parents=True, exist_ok=True)
        for symbol, subset in frame.groupby("symbol"):
            file_path = target / f"{symbol}.csv"
            subset.to_csv(file_path, index=False)
        return target
