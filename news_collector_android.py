import subprocess

crawler = ['somersetlive_somerset-news.py',
           'express_news-world.py',
           'express_news-uk.py',
           'techradar_uk-news.py',
           'express_news-politics.py',
           'express_news-science.py',
           'express_news-weather.py',
           'express_science-technology.py',
           'techradar_uk-pro.py'
           'express_entertainment-gaming.py',
           'express_news-nature.py',
           'express_news-weird.py',
           'dailymail_news.py',
           'metro_news-technology.py',
           'metro_news-uk.py',
           'metro_news-weird.py',
           'metro_news-world.py',
           'express_entertainment-films.py']

i = 0
for crawlers in crawler:
    cmd = 'python '+crawler[i]
    print('running command:', cmd)
    xcmd = subprocess.Popen(cmd, shell=True)
    i += 1
