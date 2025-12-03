# ETLframework

A lightweight, modular ETL framework for financial time series data. The framework is composed of interchangeable extractor, cleaner, transformer, and loader modules so pipelines can be assembled or swapped without changing surrounding code. A demonstration script shows how to process two asset classes (equities and crypto) into feature-rich CSV outputs.

## Features
- **Composable abstractions**: `BaseExtractor`, `BaseCleaner`, `BaseTransformer`, and `BaseLoader` define the contract for each ETL stage so implementations can be swapped independently.
- **Sample implementations**:
  - `EquityPriceExtractor` and `CryptoPriceExtractor` simulate pulling prices for equities and crypto assets.
  - `BasicCleaner` removes duplicates, orders records, and forward-fills prices per symbol.
  - `ReturnFeatureTransformer` adds percentage returns and normalized price series.
  - `CSVSaver` writes separate CSV files per symbol to a destination directory.
- **Simple orchestration**: `ETLPipeline` wires components together and exposes a `run()` helper to execute the flow end-to-end.

## Project layout
```
etl_framework/
  __init__.py              # Package exports
  extractors.py            # Data extraction interfaces and mocks
  cleaners.py              # Cleaning utilities
  transformers.py          # Feature engineering
  loaders.py               # Output persistence
  pipeline.py              # Pipeline orchestration

demo.py                    # Demonstrates equity + crypto pipelines
```

## Getting started
1. Install dependencies (only pandas is required):
   ```bash
   pip install pandas
   ```
2. Run the demonstration script to execute both pipelines and persist CSV outputs under `data/`:
   ```bash
   python demo.py
   ```

The script prints the transformed dataframes and writes per-symbol CSVs to `data/equities/` and `data/crypto/`.

## Extending the framework
- Create new extractor/cleaner/transformer/loader classes by implementing the respective base interface and pass them into `ETLPipeline`.
- Add additional asset types by creating extractors that conform to the `fetch(symbols)` interface and reusing shared cleaners/transformers/loaders.

## Example: creating a custom loader
```python
from pathlib import Path
from etl_framework import BaseLoader
import pandas as pd

class ParquetSaver(BaseLoader):
    def load(self, frame: pd.DataFrame, target: Path) -> Path:
        target.mkdir(parents=True, exist_ok=True)
        for symbol, subset in frame.groupby("symbol"):
            subset.to_parquet(target / f"{symbol}.parquet")
        return target
```
Swap `ParquetSaver` into the pipeline to persist Parquet files without touching other modules.
