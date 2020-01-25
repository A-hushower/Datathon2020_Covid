import requests
import json
import csv
import collections
import secret


apikey = secret.KEY
station = 'DTW'
lang = 'en_RU'
transport_types = 'plane'

url = 'https://api.rasp.yandex.net/v3.0/schedule/?'
url += 'apikey=' + apikey
url += '&system=iata'
url += '&station=' + station
url += '&offset=300'
url += '&date=2020-01-25'
url += '&lang=' + lang
url += '&transport_types=' + transport_types

r = requests.get(url)
data = r.json()
print(data['pagination']['total'])

cities = []
with open('all_cities.txt') as cities_file:
    for line in cities_file.readlines():
        cities.append(line[:-1])

while 'Detroit' in cities:
    cities.remove('Detroit')


with open('us_airports/DTW.txt','a') as outfile:
    for flight in data['schedule']:
        title = flight['thread']['title']
        for city in cities:
            if city in title:
                outfile.write(city + ',')