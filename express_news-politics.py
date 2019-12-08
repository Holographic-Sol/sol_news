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
from bs4 import BeautifulSoup
import distutils.dir_util
import shutil

dat_dir = './news_articles/'
distutils.dir_util.mkpath(dat_dir)

encode = u'\u5E73\u621015\u200e'

href_data = []
title_data = []

dat_file_tmp = './news_articles/express_news-politics_tmp.txt'
dat_file = './news_articles/express_news-politics.txt'

open(dat_file_tmp, 'w').close()

url = 'https://www.express.co.uk/news/politics'
print('searching', url)
rHead = requests.get(url)
data = rHead.text
soup = BeautifulSoup(data, "html.parser")
for link in soup.find_all('a'):
    href = link.get('href')
    if href is not None and href.startswith('/news/politics') and \
            href != '/entertainment/politics':
        article_url = 'https://www.express.co.uk' + href
        print(article_url)
        if article_url not in href_data:
            href_data.append(article_url)


i = 0
for href_datas in href_data:
    url = href_data[i]
    with codecs.open(dat_file_tmp, 'a', encoding="UTF-8") as fo:
        fo.write('\n'+url)
    fo.close()
    print('searching', url)
    rHead = requests.get(url)
    data = rHead.text
    soup = BeautifulSoup(data, "html.parser")
    for row in soup.find_all('p'):
        text = row.get_text()
        if text is not None:
            with codecs.open(dat_file_tmp, 'a', encoding="UTF-8") as fo:
                fo.write(text+'\n')
            fo.close()
    i += 1

if i is len(href_data):
    shutil.copy(dat_file_tmp, dat_file)
    os.remove(dat_file_tmp)
