"""Demonstration of the modular ETL framework."""

from pathlib import Path

from etl_framework import (
    BasicCleaner,
    CryptoPriceExtractor,
    CSVSaver,
    ETLPipeline,
    EquityPriceExtractor,
    ReturnFeatureTransformer,
)


def run_equity_pipeline():
    pipeline = ETLPipeline(
        extractor=EquityPriceExtractor(),
        cleaner=BasicCleaner(),
        transformer=ReturnFeatureTransformer(),
        loader=CSVSaver(),
    )
    return pipeline.run(["AAPL", "MSFT"], destination=Path("data/equities"))


def run_crypto_pipeline():
    pipeline = ETLPipeline(
        extractor=CryptoPriceExtractor(),
        cleaner=BasicCleaner(),
        transformer=ReturnFeatureTransformer(),
        loader=CSVSaver(),
    )
    return pipeline.run(["BTC-USD", "ETH-USD"], destination=Path("data/crypto"))


if __name__ == "__main__":
    equity_frame = run_equity_pipeline()
    crypto_frame = run_crypto_pipeline()

    print("Equity data:\n", equity_frame)
    print("\nCrypto data:\n", crypto_frame)
