# -*- coding: utf-8 -*-
from besttags.util import merge, limit, Tags
from besttags.apis import best_hashtags, ritetag, instatag, displaypurposes


class Manager(object):
    """This make great stuff."""

    def __init__(self, kind='simple', limit=30, weights=[], fix=[]):
        self.kind = kind
        self.limit = limit
        self.weights = weights

        if isinstance(fix, list):
            self.fix = fix
        elif isinstance(fix, str):
            self.fix = [fix]
        else:
            raise TypeError("Wrong type for 'fix', only str or list.")

        if not isinstance(self.weights, list):
            raise TypeError("The weights should be a list.")

        if not hasattr(self, self.kind):
            raise TypeError(f"The kind '{self.kind}' is not supported.")

        if self.limit < len(self.fix):
            raise ValueError("The limit cannot be lower,than the fix tags.")

    def __call__(self, *args):
        self.tags = []
        for arg in args:
            if isinstance(arg, list):
                self.tags += arg
            elif isinstance(arg, str):
                self.tags.append(arg)

        tags = getattr(self, self.kind)()

        add = []
        for f in self.fix:
            if f not in tags:
                add.append(f)

        return Tags((add + tags)[:self.limit])

    def test(self):
        tags = [self.tags for i in range(2)]
        stat = merge(tags, self.weights)
        return limit(stat, self.limit)

    def simple(self):
        tags = [best_hashtags(t) for t in self.tags]
        stat = merge(tags, self.weights)
        return limit(stat, self.limit)

    def all(self):
        tags = []
        for func in [best_hashtags, ritetag, instatag, displaypurposes]:
            for t in self.tags:
                t = func(t)
                if t:
                    tags.append(t)

        stat = merge(tags, self.weights)
        return limit(stat, self.limit)
