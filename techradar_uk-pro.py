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

dat_file = dat_dir + '/techradar_uk-pro_' + tm_stamp + '.txt'

url = 'https://www.techradar.com/uk/pro/security'
print('searching', url)
rHead = requests.get(url)
data = rHead.text
soup = BeautifulSoup(data, "html.parser")

for link in soup.find_all('a'):
    href = link.get('href')
    exclude = ['https://www.techradar.com/uk/pro',
               'https://www.techradar.com/uk/rsstoolkit',
               'https://www.techradar.com/uk/pro/news',
               'https://www.techradar.com/uk/pro/reviews',
               'https://www.techradar.com/uk/pro/insights',
               'https://www.techradar.com/uk/vpn/best-vpn',
               'https://www.techradar.com/uk/pro/security',
               'https://www.techradar.com/uk/news/about-us',
               'https://www.techradar.com/uk/advertise-with-us',
               'https://www.techradar.com/uk',
               'https://www.techradar.com/uk/news',
               'https://www.techradar.com/uk/news/internet',
               'https://www.techradar.com/uk/news/computing',
               'https://www.techradar.com/uk/digital-transformation',
               'https://www.techradar.com/uk/news/digital-home',
               'https://www.techradar.com/uk/pro/mobile-industry',
               'https://www.techradar.com/uk/news/vpn',
               'https://www.techradar.com/uk/news/gaming',
               'https://www.techradar.com/uk/news/disney-plus-shows-movies-sign-up']
    if href is not None and href.startswith('https://www.techradar.com/uk') and href not in exclude:
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

