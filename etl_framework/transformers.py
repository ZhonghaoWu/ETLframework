"""Feature engineering and transformations."""

from __future__ import annotations

from abc import ABC, abstractmethod
import pandas as pd


class BaseTransformer(ABC):
    @abstractmethod
    def transform(self, frame: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError


class ReturnFeatureTransformer(BaseTransformer):
    """Adds daily return and normalized price columns."""

    def transform(self, frame: pd.DataFrame) -> pd.DataFrame:
        transformed = frame.copy()
        transformed = transformed.sort_values(["symbol", "timestamp"]).reset_index(drop=True)
        transformed["return"] = transformed.groupby("symbol")["price"].pct_change()
        transformed["normalized_price"] = transformed.groupby("symbol")["price"].transform(
            lambda series: series / series.iloc[0]
        )
        return transformed
