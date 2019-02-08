# -*- coding: utf-8 -*-
from besttags.util import BasicManager


class FileManager(BasicManager):
    """This make great stuff."""

    def __init__(self, file, limit=30):
        super(FileManager, self).__init__(limit=limit)
        self.file = file

    def __call__(self, *args):
        super(FileManager, self).__call__(*args)
        return self.get_tags(args)
