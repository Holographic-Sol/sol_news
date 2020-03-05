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

dat_file = dat_dir + '/express_news-nature_' + tm_stamp + '.txt'

url = 'https://www.express.co.uk/news/nature'
print('searching', url)
rHead = requests.get(url)
data = rHead.text
soup = BeautifulSoup(data, "html.parser")
for link in soup.find_all('a'):
    href = link.get('href')
    if href is not None and href.startswith('/news/nature') and \
            href != '/entertainment/nature':
        article_url = 'https://www.express.co.uk' + href
        print(article_url)
        if article_url not in href_data:
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

