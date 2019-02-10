from json import load as json_load
from besttags.util.func import merge_dict, limit
from besttags.util.db import Manager
from besttags.analyzer.basic import BasicAnalyzer

from besttags.data.sample import SAMPLE_DATA
from besttags.defaults import SAMPLE_JSON, SAMPLE_DB


class BasicLocalAnalyzer(BasicAnalyzer):
    """This make great stuff."""

    def __call__(self, *args):
        super(BasicLocalAnalyzer, self).__call__(*args)
        stat = merge_dict([self.get_tag_relation(tag) for tag in self.tags])
        tags = limit(stat, self.limit)
        return self.get_tags(tags)

    def get_tag_relation(self, tag):
        return None


class DataAnalyzer(BasicLocalAnalyzer):
    """This make great stuff."""

    def __init__(self, data=SAMPLE_DATA, limit=30, fix=[]):
        super(DataAnalyzer, self).__init__(limit=limit, fix=fix)
        self.data = data

    def get_tag_relation(self, tag):
        tags = self.data.get(tag)
        tags[tag] = 1
        return tags


class FileAnalyzer(DataAnalyzer):

    def __init__(self, filename=SAMPLE_JSON, limit=30, fix=[]):
        with open(filename, "r") as read_file:
            data = json_load(read_file)
        super(FileAnalyzer, self).__init__(data=data, limit=limit, fix=fix)


class DBAnalyzer(BasicLocalAnalyzer):
    """This make great stuff."""

    def __init__(self, filename=SAMPLE_DB, limit=30, fix=[]):
        super(DBAnalyzer, self).__init__(limit=limit, fix=fix)
        self.manager = Manager(filename)

    def get_tag_relation(self, tag):
        tags = self.manager.get(tag)
        tags[tag] = 1
        return tags
