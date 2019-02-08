from besttags.local.manager import DataManager, FileManager
import json

data = {
    "coding": {
        "programming": 0.9,
        "software": 0.6,
        "linux": 0.4,
    },
    "linux": {
        "coding": 1,
        "os": 0.5,
    },
    "python": {
        "coding": 0.2,
        "programmer": 0.6,
    },
}

#with open('besttags/data/sample.json', "w") as f:
#    json.dump(data, f, indent=4)


#best = DataManager(data=data)
#best = DataManager(data=data)
for best in [DataManager(), FileManager()]:
    result = best('python', 'linux')
    print(result)
