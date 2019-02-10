from besttags.util.db import Manager

ma = Manager()
ma.setup()
ma.add('test', ['a', 'b', 'c'])
print(ma.all())
ma.delete()
