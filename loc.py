
with open('2014_us_cities.csv') as cities_file:
    lines = cities_file.readlines()

lines.pop(0)
my_lines = []

cities = dict()
unchecked = []
with open('sec_res.txt') as results:
    for line in results.readlines():
        name, risk = line.split(',')
        risk = risk.replace('\n','')
        cities[name] = risk
        unchecked.append(name)

for line in lines:
    city, pop, lat, lon = line.split(',')
    while city[-1] == ' ':
        city = city[:-1]
    if city in unchecked:
        print(city)
        my_line = ','.join([city, cities[city], lat, lon])
        my_lines.append(my_line)
        unchecked.remove(city)

with open('map_data.csv','w') as map_file:
    map_file.writelines(my_lines)