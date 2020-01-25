cities = []

with open('AmericanAirports.csv') as cfile:
    for line in cfile.readlines():
        data = line.split(',')
        cities.append(data[2])

with open('all_cities.txt', 'w') as outfile:
    for city in cities:
        outfile.write(city + '\n')