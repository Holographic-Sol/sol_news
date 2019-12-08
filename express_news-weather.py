import os
import codecs
import requests
from bs4 import BeautifulSoup

encode = u'\u5E73\u621015\u200e'

href_data = []
title_data = []

dat_file = './news_articles/express_news-weather.txt'

open(dat_file, 'w').close()

url = 'https://www.express.co.uk/news/weather'
print('searching', url)
rHead = requests.get(url)
data = rHead.text
soup = BeautifulSoup(data, "html.parser")
for link in soup.find_all('a'):
    href = link.get('href')
    if href is not None and href.startswith('/news/weather'):
        article_url = 'https://www.express.co.uk' + href
        print(article_url)
        href_data.append(article_url)


i = 0
for href_datas in href_data:
    url = href_data[i]
    with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
        fo.write('\n'+url)
    fo.close()
    print('searching', url)
    rHead = requests.get(url)
    data = rHead.text
    soup = BeautifulSoup(data, "html.parser")
    for row in soup.find_all('p'):
        text = row.get_text()
        if text is not None:
            with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
                fo.write(text+'\n')
            fo.close()
    i += 1
