# -*- coding: utf-8 -*-

from besttags.__about__ import __author__,  __email__, __version__
from besttags.analyzer.web import WebAnalyzer
from besttags.analyzer.local import DataAnalyzer, FileAnalyzer

__all__ = [
    'WebAnalyzer', 'DataAnalyzer', 'FileAnalyzer',
    '__author__', '__email__', '__version__'
]
