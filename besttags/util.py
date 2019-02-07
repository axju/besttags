# -*- coding: utf-8 -*-
from random import shuffle


def merge(tags, weights=None):
    """
    tags: a list of tags
    weights: alist of weights, the sum shuld be 1
    """
    if not weights:
        weights = [1.0/len(tags) for i in range(len(tags))]

    stat = {}
    for i, tag in enumerate(tags):
        for t in tag:
            stat[t] = stat.get(t, 0) + weights[i]

    return stat


def limit(s, n=30):
    # first shuffel the data
    keys = list(s.keys())
    shuffle(keys)
    s = {key: s[key] for key in keys}

    # now sort them
    sort = [i[0] for i in sorted(s.items(), key=lambda k: k[1], reverse=True)]
    return sort[:n]


class Tags(object):
    """Make it easy to format the tags"""

    def __init__(self, tags):
        self.tags = tags

    def __str__(self):
        return ' '.join([f'#{t}' for t in self.tags])

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        for tag in self.tags:
            yield tag

    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))
