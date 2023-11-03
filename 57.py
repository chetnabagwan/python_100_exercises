import json
from pprint import pprint

with open(r"C:\\Users\\cbagwan\Downloads\\company1.json", 'r') as file:
    d= json.loads(file.read())

pprint(d)