# -*- coding: utf-8 -*-
from besttags.util import BasicManager, merge_list, limit


class DataManager(BasicManager):
    """This make great stuff."""

    def __init__(self, data, limit=30, fix=[]):
        super(DataManager, self).__init__(limit=limit, fix=fix)
        self.data = data

    def __call__(self, *args):
        super(DataManager, self).__call__(*args)
        stat = merge_list([self.get_tag_relation(tag) for tag in self.tags])
        tags = limit(stat, self.limit)
        return self.get_tags(tags)

    def get_tag_relation(self, tag):
        return self.data.get(tag)
