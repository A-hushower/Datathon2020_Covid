import plotly
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('large_cities.csv')
df.head()
df['text'] = df['name'] + '<br>Risk ' + df['risk'].astype(str) + ' per mln'

fig = go.Figure()

fig.add_trace(go.Scattergeo(
    locationmode = 'USA-states',
    lon = df['lon'],
    lat = df['lat'],
    text = df['text'],
    marker = dict(
        size = df['risk'] * (10 ** 12),
        color = 'crimson',
        line_color='rgb(40,40,40)',
        line_width=0.5,
        sizemode = 'area'
    ),
    name = 'High risk cities'))

sf = pd.read_csv('small_cities.csv')
sf.head()
sf['text'] = sf['name'] + '<br>Risk ' + sf['risk'].astype(str) + ' per mln'

fig.add_trace(go.Scattergeo(
    locationmode = 'USA-states',
    lon = sf['lon'],
    lat = sf['lat'],
    text = sf['text'],
    marker = dict(
        size = 5,
        color = 'orange',
        line_color='rgb(40,40,40)',
        line_width=0.5,
        sizemode = 'area'
    ),
    name = 'Low risk cities'))

fig.update_layout(
        title_text = 'US cities infection risk<br>(Click legend to toggle traces)',
        showlegend = True,
        geo = dict(
            scope = 'usa',
            landcolor = 'rgb(217, 217, 217)',
        )
    )

plotly.offline.plot(fig, filename='us_risks.html') 
#fig.show()

'''
with open('map_data.txt') as map_file:
    lines = map_file.readlines()

cities = []
risks = []
lats = []
lngs = []
for line in lines:
    city, risk, lat, lng = line.split(',')
    cities.append(city)
    risks.append(float(risk))
    lats.append(float(lat))
    lng = lng.replace('\n','')
    lngs.append(float(lng))'''
