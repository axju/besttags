# -*- coding: utf-8 -*-

from besttags.__about__ import __author__,  __email__, __version__
from besttags.manager.web import WebManager
from besttags.manager.local import DataManager, FileManager

__all__ = [
    'WebManager', 'DataManager', 'FileManager',
    '__author__', '__email__', '__version__'
]
