import os
from json import load as json_load
from besttags.util.func import merge_dict, limit
from besttags.manager.basic import BasicManager

from besttags.data.sample import SAMPLE_DATA
SAMPLE_JSON = os.path.join(os.path.dirname(__file__), '../data/sample.json')


class BasicLocalManager(BasicManager):
    """This make great stuff."""

    def __call__(self, *args):
        super(BasicLocalManager, self).__call__(*args)
        stat = merge_dict([self.get_tag_relation(tag) for tag in self.tags])
        tags = limit(stat, self.limit)
        return self.get_tags(tags)

    def get_tag_relation(self, tag):
        return None


class DataManager(BasicLocalManager):
    """This make great stuff."""

    def __init__(self, data=SAMPLE_DATA, limit=30, fix=[]):
        super(DataManager, self).__init__(limit=limit, fix=fix)
        self.data = data

    def get_tag_relation(self, tag):
        tags = self.data.get(tag)
        tags[tag] = 1
        return tags


class FileManager(DataManager):

    def __init__(self, filename=SAMPLE_JSON, limit=30, fix=[]):
        with open(filename, "r") as read_file:
            data = json_load(read_file)
        super(FileManager, self).__init__(data=data, limit=limit, fix=fix)
