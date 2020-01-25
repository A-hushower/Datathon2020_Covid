import json

with open('TPE.json') as jfile:
    data = json.load(jfile)

cities = []
with open('cities.txt') as cities_file:
    for line in cities_file.readlines():
        cities.append(line[:-1])

with open('TPE2.txt','w') as outfile:
    for flight in data['schedule']:
        title = flight['thread']['title']
        for city in cities:
            if city in title:
                outfile.write(city + '\n')


                
        