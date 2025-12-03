"""Composable ETL pipeline."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import pandas as pd

from .cleaners import BaseCleaner
from .extractors import BaseExtractor
from .loaders import BaseLoader
from .transformers import BaseTransformer


@dataclass
class ETLPipeline:
    extractor: BaseExtractor
    cleaner: BaseCleaner
    transformer: BaseTransformer
    loader: BaseLoader

    def run(self, symbols: Iterable[str], destination: Path) -> pd.DataFrame:
        raw = self.extractor.fetch(symbols)
        cleaned = self.cleaner.clean(raw)
        transformed = self.transformer.transform(cleaned)
        self.loader.load(transformed, destination)
        return transformed
