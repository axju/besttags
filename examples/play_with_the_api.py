from besttags import Manager
from besttags.apis import best_hashtags, ritetag, instatag, displaypurposes

#print(best_hashtags('coding'))
#print(ritetag('coding'))
#print(instatag('love'))
#print(displaypurposes('love'))

best = Manager(kind='all', fix=['fullstackhero'])
print(best('computer', 'instagood'))
