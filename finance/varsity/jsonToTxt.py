import json

with open('varsity.json', 'r') as j:
    d = json.load(j)

with open('varsity.txt', 'a') as t:
    for module in d:
        for chapter in d[module]:
            t.write((f'{chapter}${d[module][chapter]}${module}\n'))
