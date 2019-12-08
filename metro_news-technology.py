##                GNU General Public License version 3                          ##
##    Sony Bravia Remote by Benjamin Jack Cullen Copyright (C) 2017             ##
##                                                                              ##
##    This program is free software: you can redistribute it and/or modify      ##
##    it under the terms of the GNU General Public License as published by      ##
##    the Free Software Foundation, either version 3 of the License, or         ##
##    (at your option) any later version.                                       ##
##                                                                              ##
##    This program is distributed in the hope that it will be useful,           ##
##    but WITHOUT ANY WARRANTY; without even the implied warranty of            ##
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the              ##
##    GNU General Public License for more details.                              ##
##                                                                              ##
##    You should have received a copy of the GNU General Public License         ##
##    along with this program.  If not, see <http://www.gnu.org/licenses/>.     ##

import os
import codecs
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import distutils.dir_util

dat_dir = './news_articles/'
distutils.dir_util.mkpath(dat_dir)

date_today = datetime.today().strftime('%Y-%m-%d')

encode = u'\u5E73\u621015\u200e'

href_data = []
title_data = []

dat_file = './news_articles/metro_news-tech.txt'

open(dat_file, 'w').close()

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
