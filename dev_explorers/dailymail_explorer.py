import requests
from bs4 import BeautifulSoup

url = 'https://www.dailymail.co.uk/news'
print('searching', url)
rHead = requests.get(url)
data = rHead.text
soup = BeautifulSoup(data, "html.parser")

for link in soup.find_all('a'):
    href = link.get('href')
    if href is not None:
        print(href)

