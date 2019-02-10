from besttags import DataAnalyzer, FileAnalyzer
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


#best = DataAnalyzer(data=data)
#best = DataAnalyzer(data=data)
for best in [DataAnalyzer(), FileAnalyzer()]:
    result = best('python', 'linux')
    print(result)
