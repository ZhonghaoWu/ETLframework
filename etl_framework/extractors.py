"""Data extractors for the ETL framework."""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Iterable, List

import pandas as pd


class BaseExtractor(ABC):
    """Abstract base class for all extractors."""

    @abstractmethod
    def fetch(self, symbols: Iterable[str]) -> pd.DataFrame:
        """Return a DataFrame with columns: symbol, timestamp, price."""
        raise NotImplementedError


class _StaticTimeSeriesExtractor(BaseExtractor):
    """Common extractor for demonstration using static data."""

    def __init__(self, price_rows: List[dict]):
        self.price_rows = price_rows

    def fetch(self, symbols: Iterable[str]) -> pd.DataFrame:
        symbols_set = set(symbols)
        rows = [row for row in self.price_rows if row["symbol"] in symbols_set]
        frame = pd.DataFrame(rows)
        frame["timestamp"] = pd.to_datetime(frame["timestamp"], utc=True)
        return frame


class EquityPriceExtractor(_StaticTimeSeriesExtractor):
    """Mock extractor that simulates equity prices."""

    def __init__(self) -> None:
        # Normally this would call an external service. For demo purposes we
        # provide static daily close prices.
        super().__init__(
            [
                {"symbol": "AAPL", "timestamp": datetime(2024, 6, 3), "price": 194.03},
                {"symbol": "AAPL", "timestamp": datetime(2024, 6, 4), "price": 195.10},
                {"symbol": "AAPL", "timestamp": datetime(2024, 6, 5), "price": 197.12},
                {"symbol": "MSFT", "timestamp": datetime(2024, 6, 3), "price": 420.21},
                {"symbol": "MSFT", "timestamp": datetime(2024, 6, 4), "price": 421.90},
                {"symbol": "MSFT", "timestamp": datetime(2024, 6, 5), "price": 423.07},
            ]
        )


class CryptoPriceExtractor(_StaticTimeSeriesExtractor):
    """Mock extractor that simulates crypto prices."""

    def __init__(self) -> None:
        super().__init__(
            [
                {"symbol": "BTC-USD", "timestamp": datetime(2024, 6, 3), "price": 69750.01},
                {"symbol": "BTC-USD", "timestamp": datetime(2024, 6, 4), "price": 70320.24},
                {"symbol": "BTC-USD", "timestamp": datetime(2024, 6, 5), "price": 69510.92},
                {"symbol": "ETH-USD", "timestamp": datetime(2024, 6, 3), "price": 3810.10},
                {"symbol": "ETH-USD", "timestamp": datetime(2024, 6, 4), "price": 3895.44},
                {"symbol": "ETH-USD", "timestamp": datetime(2024, 6, 5), "price": 3920.07},
            ]
        )
