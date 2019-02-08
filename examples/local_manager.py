from besttags.local.manager import DataManager

data = {
    'coding': {
        'programming': 0.9,
        'software': 0.6,
        'linux': 0.4,
    },
    'linux': {
        'coding': 1,
        'os': 0.5,
    },
    'python': {
        'coding': 0.2,
        'programmer': 0.6,
    },
}

best = DataManager(data=data)

result = best('python', 'linux')

print(result)