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
