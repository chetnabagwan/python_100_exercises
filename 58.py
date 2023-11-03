import json

with open(r"C:\\Users\\cbagwan\Downloads\\company1.json", 'r+') as file:
    d = json.loads(file.read())
    d['employees'].append(dict(firstname = 'Albert',lastname = 'Bert'))
    file.seek(0)
    json.dump(d, file ,indent = 4)
    # file.seek(0)
    file.truncate()


