from besttags import WebAnalyzer as Analyzer

# The tags you are interested in.
tags = ['coder', 'programmers', 'python']

# The simple one-liner.
# It will save the best hashtags for the given tags in a file.
Analyzer()(tags).save('best_hashtags.txt')

# You can change the default settings and add additional tags
Analyzer(limit=10, fix=['fullstackhero'])(tags).save('10_best_hashtags.txt')

# Use print() to show the tages
print(Analyzer()(tags))

# Use the Analyzer to create an object, which you can use multiple times. It is
# callable and allows a list or single strings.
best = Analyzer(fix=['fullstackhero'])
best('computer', 'instagood')
best(['coder', 'programmers', 'python'])

# The result is a class, with some basic functions. So you can iterate it and
# get the length.
result = best('coder', 'programmers', 'python')

print(len(result))

for tag in result:
    print(tag)

print(result)

result.save('best_hashtags.txt')
