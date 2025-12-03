"""Data cleaning utilities."""

from __future__ import annotations

from abc import ABC, abstractmethod
import pandas as pd


class BaseCleaner(ABC):
    @abstractmethod
    def clean(self, frame: pd.DataFrame) -> pd.DataFrame:
        """Prepare raw data frame for transformations."""
        raise NotImplementedError


class BasicCleaner(BaseCleaner):
    """A minimal cleaner that demonstrates standard steps."""

    def clean(self, frame: pd.DataFrame) -> pd.DataFrame:
        cleaned = frame.copy()
        cleaned = cleaned.drop_duplicates()
        cleaned = cleaned.sort_values(["symbol", "timestamp"]).reset_index(drop=True)
        cleaned["price"] = cleaned["price"].astype(float)
        cleaned["price"] = cleaned.groupby("symbol")["price"].ffill()
        return cleaned
