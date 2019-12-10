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

dat_file_tmp = './news_articles/bbc_explore_tmp.txt'
dat_file = './news_articles/express_entertainment-films.txt'

open(dat_file_tmp, 'w').close()

url = 'https://www.express.co.uk/entertainment/films'

print('searching', url)
rHead = requests.get(url)
data = rHead.text
soup = BeautifulSoup(data, "html.parser")
for link in soup.find_all('a'):
    href = link.get('href')
    if href is not None and href.startswith('/entertainment/films') and \
            href != '/entertainment/films':
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
