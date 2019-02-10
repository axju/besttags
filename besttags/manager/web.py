from besttags.util.func import merge_list, merge_dict, limit
from besttags.manager.basic import BasicManager
from besttags.util.apis import (best_hashtags, ritetag,
                                instatag, displaypurposes)


class WebManager(BasicManager):
    """This make great stuff."""

    def __init__(self, kind='simple', limit=30, weights=[], fix=[]):
        super(WebManager, self).__init__(limit=limit, fix=fix)
        self.kind = kind
        self.weights = weights

        if not isinstance(self.weights, list):
            raise TypeError("The weights should be a list.")

        if not hasattr(self, self.kind):
            raise TypeError(f"The kind '{self.kind}' is not supported.")

    def __call__(self, *args):
        super(WebManager, self).__call__(*args)
        tags = getattr(self, self.kind)()
        return self.get_tags(tags)

    def test(self):
        tags = [self.tags for i in range(2)]
        stat = merge_list(tags, self.weights)
        return limit(stat, self.limit)

    def simple(self):
        tags = [best_hashtags(t) for t in self.tags]
        stat = merge_list(tags, self.weights)
        return limit(stat, self.limit)

    def all(self):
        tags = []
        for func in [best_hashtags, ritetag, instatag, displaypurposes]:
            for t in self.tags:
                t = func(t)
                if t:
                    tags.append(t)

        stat = merge_list(tags, self.weights)
        return limit(stat, self.limit)

    def displaypurposes(self):
        tags = [displaypurposes(t, kind='dict') for t in self.tags]
        stat = merge_dict(tags)
        return limit(stat, self.limit)
