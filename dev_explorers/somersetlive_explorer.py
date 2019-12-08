import requests
from bs4 import BeautifulSoup

url = 'https://www.somersetlive.co.uk/news/somerset-news/'
print('searching', url)
rHead = requests.get(url)
data = rHead.text
soup = BeautifulSoup(data, "html.parser")

for link in soup.find_all('a'):
    href = link.get('href')
    if href is not None:
        print(href)
