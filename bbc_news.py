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
cat_title_data = []
article = []

dat_file_tmp = './news_articles/bbc_news-world_tmp.txt'
dat_file = './news_articles/bbc_news-world.txt'

url = 'https://www.bbc.co.uk/news/world'

print('searching', url)
rHead = requests.get(url)
data = rHead.text
soup = BeautifulSoup(data, "html.parser")
for link in soup.find_all('a'):
    href = link.get('href')
    if href is not None and href.startswith('/news/world-'):
        # article_url = 'https://www.express.co.uk' + href
        # print(article_url)
        # if article_url not in href_data:
        #     href_data.append(article_url)
        cat_title_data.append(href)
        # print(href)
print(len(cat_title_data))

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
            # article_url = 'https://www.express.co.uk' + href
            # print(article_url)
            # if article_url not in href_data:
            #     href_data.append(article_url)
            # cat_title_data.append(href)
            # print(href)
            article.append(href)
    i += 1

open(dat_file_tmp, 'w').close()

i = 0
for articles in article:
    url = article[i]
    url = 'https://www.bbc.co.uk'+article[i]
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
            # print(text)
            with codecs.open(dat_file_tmp, 'a', encoding="UTF-8") as fo:
                fo.write(text+'\n')
            fo.close()
    i += 1

if i is len(href_data):
    shutil.copy(dat_file_tmp, dat_file)
    os.remove(dat_file_tmp)
