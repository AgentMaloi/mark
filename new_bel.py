import requests
from bs4 import BeautifulSoup as BS

url = 'https://news.tut.by/daynews/'

rBel = requests.get(url)
print("News status code: ")
print(rBel.status_code)
html = BS(rBel.text, 'html.parser')

news = []
new_news = []
news_links = []

news = html.find_all('a', class_='entry__link')

for el in range(len(news)):
    news_links.append(news[el].get('href'))
    if news[el].find('span', class_='entry-head _title'):
        new_news.append(news[el].text)

print(news_links[0])
