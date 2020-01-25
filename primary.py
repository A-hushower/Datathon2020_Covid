import collections

PPL_PER_FLIGHT = 250
risks = dict()

with open('chinese_airports/risks.txt') as risksfile:
    for line in risksfile.readlines():
        code, risk = line.split(', ')
        risk = risk[:-1]
        risks[code] = float(risk)

us_risks = collections.defaultdict(float)

for chi_city in risks:
    chi_risk = risks[chi_city]
    us_risk = PPL_PER_FLIGHT * chi_risk / (10 ** 12)

    with open('chinese_airports/{0}.txt'.format(chi_city)) as schedule:
        lines = schedule.readlines()
        cities = [line.replace('\n','') for line in lines]
        for city in cities:
            us_risks[city] += us_risk

print(dict(us_risks))


