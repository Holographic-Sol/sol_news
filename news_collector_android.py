import os
import subprocess
import distutils.dir_util
import time

print('[1] once')
print('[2] loop')
user_input = input('Would you like to run once or loop? ')
if user_input is '2':
    user_input_2 = input('Please enter in minutes the time interval between each loop: ')
    if user_input_2.isdigit():
        print('loop will be every:', user_input_2, 'minutes.')
        user_input_2 = int(user_input_2)
        user_input_2 = user_input_2 * 60

flag = False
xcmd_process = []

dat_dir = './news_articles'
distutils.dir_util.mkpath(dat_dir)

crawler = ['somersetlive_somerset-news.py',
           'sky_news-world.py',
           'bbc_news_world.py',
           'express_news-world.py',
           'express_news-uk.py',
           'techradar_uk-news.py',
           'express_news-politics.py',
           'express_news-science.py',
           'express_news-weather.py',
           'express_science-technology.py',
           'techradar_uk-pro.py',
           'express_entertainment-gaming.py',
           'express_news-nature.py',
           'express_news-weird.py',
           'dailymail_news.py',
           'metro_news-technology.py',
           'metro_news-uk.py',
           'metro_news-weird.py',
           'metro_news-world.py',
           'express_entertainment-films.py']


def funk1():
    var = crawler[0]
    cmd = 'python ' + var
    print('running command:', cmd)
    xcmd = subprocess.Popen(cmd, shell=True)
    xcmd_pid = xcmd.pid
    xcmd_process.append(xcmd_pid)
    print('subprocess PID :', xcmd_pid)


def funk2():
    var = crawler[1]
    cmd = 'python ' + var
    print('running command:', cmd)
    xcmd = subprocess.Popen(cmd, shell=True)
    xcmd_pid = xcmd.pid
    xcmd_process.append(xcmd_pid)
    print('subprocess PID :', xcmd_pid)


def funk3():
    var = crawler[2]
    cmd = 'python ' + var
    print('running command:', cmd)
    xcmd = subprocess.Popen(cmd, shell=True)
    xcmd_pid = xcmd.pid
    xcmd_process.append(xcmd_pid)
    print('subprocess PID :', xcmd_pid)
def funk4():
    var = crawler[3]
    cmd = 'python ' + var
    print('running command:', cmd)
    xcmd = subprocess.Popen(cmd, shell=True)
    xcmd_pid = xcmd.pid
    xcmd_process.append(xcmd_pid)
    print('subprocess PID :', xcmd_pid)


def funk5():
    var = crawler[4]
    cmd = 'python ' + var
    print('running command:', cmd)
    xcmd = subprocess.Popen(cmd, shell=True)
    xcmd_pid = xcmd.pid
    xcmd_process.append(xcmd_pid)
    print('subprocess PID :', xcmd_pid)


def funk6():
    var = crawler[5]
    cmd = 'python ' + var
    print('running command:', cmd)
    xcmd = subprocess.Popen(cmd, shell=True)
    xcmd_pid = xcmd.pid
    xcmd_process.append(xcmd_pid)
    print('subprocess PID :', xcmd_pid)


def funk7():
    var = crawler[6]
    cmd = 'python ' + var
    print('running command:', cmd)
    xcmd = subprocess.Popen(cmd, shell=True)
    xcmd_pid = xcmd.pid
    xcmd_process.append(xcmd_pid)
    print('subprocess PID :', xcmd_pid)


def funk8():
    var = crawler[7]
    cmd = 'python ' + var
    print('running command:', cmd)
    xcmd = subprocess.Popen(cmd, shell=True)
    xcmd_pid = xcmd.pid
    xcmd_process.append(xcmd_pid)
    print('subprocess PID :', xcmd_pid)


def funk9():
    var = crawler[8]
    cmd = 'python ' + var
    print('running command:', cmd)
    xcmd = subprocess.Popen(cmd, shell=True)
    xcmd_pid = xcmd.pid
    xcmd_process.append(xcmd_pid)
    print('subprocess PID :', xcmd_pid)

def funk10():
    var = crawler[9]
    cmd = 'python ' + var
    print('running command:', cmd)
    xcmd = subprocess.Popen(cmd, shell=True)
    xcmd_pid = xcmd.pid
    xcmd_process.append(xcmd_pid)
    print('subprocess PID :', xcmd_pid)


def funk11():
    var = crawler[10]
    cmd = 'python ' + var
    print('running command:', cmd)
    xcmd = subprocess.Popen(cmd, shell=True)
    xcmd_pid = xcmd.pid
    xcmd_process.append(xcmd_pid)
    print('subprocess PID :', xcmd_pid)


def funk12():
    var = crawler[11]
    cmd = 'python ' + var
    print('running command:', cmd)
    xcmd = subprocess.Popen(cmd, shell=True)
    xcmd_pid = xcmd.pid
    xcmd_process.append(xcmd_pid)
    print('subprocess PID :', xcmd_pid)


def funk13():
    var = crawler[12]
    cmd = 'python ' + var
    print('running command:', cmd)
    xcmd = subprocess.Popen(cmd, shell=True)
    xcmd_pid = xcmd.pid
    xcmd_process.append(xcmd_pid)
    print('subprocess PID :', xcmd_pid)


def funk14():
    var = crawler[13]
    cmd = 'python ' + var
    print('running command:', cmd)
    xcmd = subprocess.Popen(cmd, shell=True)
    xcmd_pid = xcmd.pid
    xcmd_process.append(xcmd_pid)
    print('subprocess PID :', xcmd_pid)


def funk15():
    var = crawler[14]
    cmd = 'python ' + var
    print('running command:', cmd)
    xcmd = subprocess.Popen(cmd, shell=True)
    xcmd_pid = xcmd.pid
    xcmd_process.append(xcmd_pid)
    print('subprocess PID :', xcmd_pid)


def funk16():
    var = crawler[15]
    cmd = 'python ' + var
    print('running command:', cmd)
    xcmd = subprocess.Popen(cmd, shell=True)
    xcmd_pid = xcmd.pid
    xcmd_process.append(xcmd_pid)
    print('subprocess PID :', xcmd_pid)


def funk17():
    var = crawler[16]
    cmd = 'python ' + var
    print('running command:', cmd)
    xcmd = subprocess.Popen(cmd, shell=True)
    xcmd_pid = xcmd.pid
    xcmd_process.append(xcmd_pid)
    print('subprocess PID :', xcmd_pid)


def funk18():
    var = crawler[17]
    cmd = 'python ' + var
    print('running command:', cmd)
    xcmd = subprocess.Popen(cmd, shell=True)
    xcmd_pid = xcmd.pid
    xcmd_process.append(xcmd_pid)
    print('subprocess PID :', xcmd_pid)


if user_input is '1':
    funk1()
    funk2()
    funk3()
    funk4()
    funk5()
    funk6()
    funk7()
    funk8()
    funk9()
    funk10()
    funk11()
    funk12()
    funk13()
    funk14()
    funk15()
    funk16()
    funk17()
    funk18()
    while flag is False:
        i = 0
        for xcmd_processs in xcmd_process:
            foo = str(xcmd_process[i])
            bar = "/proc/"+foo
            if os.path.exists(bar) is True:
                p3 = subprocess.Popen(["ps -o cmd= {}".format(xcmd_process[i])], stdout=subprocess.PIPE, shell=True)
                found_pid_name = str(p3.communicate()[0])
                pass
            elif not os.path.exists(bar):
                del xcmd_process[i]
                if len(xcmd_process) is 0:
                    flag = True
            i += 1

elif user_input is '2':
    while True:
        funk1()
        funk2()
        funk3()
        funk4()
        funk5()
        funk6()
        funk7()
        funk8()
        funk9()
        funk10()
        funk11()
        funk12()
        funk13()
        funk14()
        funk15()
        funk16()
        funk17()
        funk18()
        while flag is False:
            i = 0
            for xcmd_processs in xcmd_process:
                foo = str(xcmd_process[i])
                bar = "/proc/" + foo
                if os.path.exists(bar) is True:
                    p3 = subprocess.Popen(["ps -o cmd= {}".format(xcmd_process[i])], stdout=subprocess.PIPE, shell=True)
                    found_pid_name = str(p3.communicate()[0])
                    pass
                elif not os.path.exists(bar):
                    del xcmd_process[i]
                    if len(xcmd_process) is 0:
                        flag = True
                i += 1
        print('-- sleeping:', user_input_2)
        time.sleep(user_input_2)
