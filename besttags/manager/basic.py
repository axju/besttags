from besttags.util.cls import Tags


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
