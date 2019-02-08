# -*- coding: utf-8 -*-
from random import shuffle


def merge_list(tags, weights=None):
    """
    tags: a list of tags-lists
    weights: alist of weights, the sum shuld be 1
    """
    if not weights:
        weights = [1.0/len(tags) for i in range(len(tags))]

    stat = {}
    for i, tag in enumerate(tags):
        for t in tag:
            stat[t] = stat.get(t, 0) + weights[i]

    return stat


def merge_dict(tags):
    """
    Marge a list of tags-dict.
    """
    n = len(tags)
    stat = {}
    for tag in tags:
        for t, v in tag.items():
            stat[t] = stat.get(t, 0) + v/n
    return stat


def limit(s, n=30):
    """
    get a dict wir tags as keys and the importent as the value.
    sorted the element and return a list of tags oth the langth n
    """
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


class BasicManager(object):

    def __init__(self, limit=30, fix=[]):
        self.limit = limit

        if isinstance(fix, list):
            self.fix = fix
        elif isinstance(fix, str):
            self.fix = [fix]
        else:
            raise TypeError("Wrong type for 'fix', only str or list.")

        if self.limit < len(self.fix):
            raise ValueError("The limit cannot be lower,than the fix tags.")

    def __call__(self, *args):
        self.tags = []
        for arg in args:
            if isinstance(arg, list):
                self.tags += arg
            elif isinstance(arg, str):
                self.tags.append(arg)

    def get_tags(self, tags):
        add = []
        for f in self.fix:
            if f not in tags:
                add.append(f)

        return Tags((add + tags)[:self.limit])
