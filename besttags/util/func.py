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
    n = float(len(tags))
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
