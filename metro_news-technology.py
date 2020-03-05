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

date_today = datetime.date.today().strftime('%Y-%m-%d')

encode = u'\u5E73\u621015\u200e'

href_data = []
title_data = []

dat_file = dat_dir + '/metro_news-tech_' + tm_stamp + '.txt'

url = 'https://www.metro.co.uk/news/tech'
print('searching', url)
rHead = requests.get(url)
data = rHead.text
soup = BeautifulSoup(data, "html.parser")
for link in soup.find_all('a'):
    href = link.get('href')
    dt = date_today.replace('-', '/')
    search_str_today = 'https://metro.co.uk/'+dt
    search_str_yesterday = 'https://metro.co.uk/'+dt
    idx = search_str_yesterday.rfind('/')
    search_str_yesterday = search_str_yesterday[:idx]
    if href is not None and href.startswith(search_str_today) or \
            href is not None and href.startswith(search_str_yesterday):
        print(href)
        if href not in href_data:
            href_data.append(href)

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

