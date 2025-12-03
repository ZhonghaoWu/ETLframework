"""
A lightweight, modular ETL framework for financial time series data.
"""

from .extractors import BaseExtractor, EquityPriceExtractor, CryptoPriceExtractor
from .cleaners import BaseCleaner, BasicCleaner
from .transformers import BaseTransformer, ReturnFeatureTransformer
from .loaders import BaseLoader, CSVSaver
from .pipeline import ETLPipeline

__all__ = [
    "BaseExtractor",
    "EquityPriceExtractor",
    "CryptoPriceExtractor",
    "BaseCleaner",
    "BasicCleaner",
    "BaseTransformer",
    "ReturnFeatureTransformer",
    "BaseLoader",
    "CSVSaver",
    "ETLPipeline",
]
