import requests
from bs4 import BeautifulSoup as BS

rBrest = requests.get('https://yandex.by/pogoda/brest')
html = BS(rBrest.content, 'html.parser')
for el in html.select('.fact__basic'):
	titleBrest = el.select('.fact__temp > .temp__value')

rMinsk = requests.get('https://yandex.by/pogoda/minsk')
html = BS(rMinsk.content, 'html.parser')
for el in html.select('.fact__basic'):
	titleMinsk = el.select('.fact__temp > .temp__value')

rMogilev = requests.get('https://yandex.by/pogoda/mogilev')
html = BS(rMogilev.content, 'html.parser')
for el in html.select('.fact__basic'):
	titleMogilev = el.select('.fact__temp > .temp__value')

rVitebsk = requests.get('https://yandex.by/pogoda/vitebsk')
html = BS(rVitebsk.content, 'html.parser')
for el in html.select('.fact__basic'):
	titleVitebsk = el.select('.fact__temp > .temp__value')

rGomel = requests.get('https://yandex.by/pogoda/gomel')
html = BS(rGomel.content, 'html.parser')
for el in html.select('.fact__basic'):
	titleGomel = el.select('.fact__temp > .temp__value')

rGrodno = requests.get('https://yandex.by/pogoda/grodno')
html = BS(rGrodno.content, 'html.parser')
for el in html.select('.fact__basic'):
	titleGrodno = el.select('.fact__temp > .temp__value')
