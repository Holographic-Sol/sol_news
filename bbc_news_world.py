import os
import codecs
import requests
from bs4 import BeautifulSoup
import distutils.dir_util
import datetime

time_now = str(datetime.datetime.now())
time_now = time_now.replace(':', '-')
time_now = time_now.replace('.', '')
time_now = time_now.replace(' ', '_')
tm_stamp = time_now[:13]

dat_dir = './news_articles/' + tm_stamp + '/'
distutils.dir_util.mkpath(dat_dir)

encode = u'\u5E73\u621015\u200e'

href_data = []
title_data = []
cat_title_data = []
article = []

dat_file = dat_dir + '/bbc_news-world_' + tm_stamp + '.txt'

url = 'https://www.bbc.co.uk/news/world'

print('searching', url)
rHead = requests.get(url)
data = rHead.text
soup = BeautifulSoup(data, "html.parser")
for link in soup.find_all('a'):
    href = link.get('href')
    if href is not None and href.startswith('/news/world-'):
        cat_title_data.append(href)
        # print(href)

i = 0
for cat_title_datas in cat_title_data:
    url = cat_title_data[i]
    url = 'https://www.bbc.co.uk'+url
    print('searching', url)
    rHead = requests.get(url)
    data = rHead.text
    soup = BeautifulSoup(data, "html.parser")
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is not None and href.startswith('/news/world-'):
            article.append(href)
    i += 1

i = 0
for articles in article:
    url = article[i]
    url = 'https://www.bbc.co.uk'+article[i]
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
            # print(text)
            with codecs.open(dat_file, 'a', encoding="UTF-8") as fo:
                fo.write(text+'\n')
            fo.close()
    i += 1