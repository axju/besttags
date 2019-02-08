# -*- coding: utf-8 -*-
from besttags.util import BasicManager


class DataManager(BasicManager):
    """This make great stuff."""

    def __init__(self, data, limit=30, fix=[]):
        super(DataManager, self).__init__(limit=limit, fix=fix)
        self.data = data

    def __call__(self, *args):
        super(DataManager, self).__call__(*args)
        return self.get_tags(args)
