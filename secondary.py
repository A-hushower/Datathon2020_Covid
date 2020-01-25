import collections

PPL_PER_FLIGHT = 250
risks = {'New York': 6.586435050569999e-09, 'San Francisco': 2.872816640719999e-09, 'Los Angeles': 5.755180895545e-09, 'Boston': 1.7003598941375002e-09, 'Chicago': 5.597806508605e-09, 'Dallas': 5.0744505597e-10, 'Seattle': 1.30555377084e-09, 'Houston': 9.154625757500001e-10, 'Detroit': 3.40377426995e-10, 'Honolulu': 3.40377426995e-10}

names = dict()

with open('us_airports/names.txt') as us_airports:
    lines = us_airports.readlines()
    for line in lines:
        code, name = line.split(' - ')
        name = name.replace('\n','')
        names[code] = name

sub_risks = collections.defaultdict(float)

for hub_code in names:
    hub_name = names[hub_code]
    hub_risk = risks[hub_name]
    sub_risk = PPL_PER_FLIGHT * hub_risk / (10 ** 12)
    
    with open('us_airports/{0}.txt'.format(hub_code)) as schedule:
        sub_cities = schedule.read().split(',')
        for sub_city in sub_cities:
            sub_risks[sub_city] += sub_risk

for city in risks:
    sub_risks[city] += risks[city]

sub_risks = dict(sub_risks)

with open('sec_res.txt','w') as sec_res:
    for city, risk in sorted(sub_risks.items(), key=lambda p:p[1], reverse=True):
        sec_res.write(city + ',' + str(risk) + '\n')

