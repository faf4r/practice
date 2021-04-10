from requests import get
from re import findall
import requests
import re
import time
import os
from PIL import Image
# Written by TMF,reedited by LZB
st = input('the number we start:')
end = input('the number we end:')
time_start = time.time()  # Update1

# 删除已有urls.txt，避免重复下载
if (os.path.exists("urls.txt")):
    os.remove("urls.txt")
else:
    pass
print('searching...')
for i in range(int(st), int(end)+1):
    f = open('urls.txt', 'a+')
    url = 'https://www.smmv.net/'+str(i)+'.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(HTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'}

    try:
        r1 = get(url, headers=headers, timeout=1)
        urls = findall('<img alt=".*?" src="(.*?)".*?>', r1.text)

        all_ = len(urls)
        if all_:
            f.write(url+'\n')
            print('available url found:'+str(i))
        else:
            print('a url fail to run:'+str(i))

    except Exception as m:
        print(m)
    f.close()

time_end = time.time()
print('total time used:', time_end-time_start, 's')

# show images to bobo
def show(directory_name):
    for filename in os.listdir(r"./"+directory_name):
        img=Image.open(directory_name + "/" + filename)
        img.show()

# Update2
response = input('do you want to download the pictures right now?''\npress y if you want''\npress any key to quit')
if response == 'y':
    fp = open('urls.txt', 'r')
    urls_ = fp.read().split('\n')
    fp.close()

    for url_ in urls_:
        # url = 'https://www.smmv.net/'+str(i)+'.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                          'Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'}

        time_start = time.time()
        try:
            r2 = requests.get(url_, headers=headers, timeout=3)
            urls = re.findall('<img alt=".*?" src="(.*?)".*?>', r2.text)

            dir_name = re.findall('<h1 class="post-title h3">(.*?)</h1>', r2.text)
            try:
                os.mkdir(dir_name[0])
            except Exception as e:
                print(e)
            c = 1

            print('catalogue：', dir_name)

            all_ = len(urls)
            if all_:
                print('total', all_, 'pictures were found')
            for url in urls:
                r_url = requests.get(url, headers=headers)

                file_name = url.split('/')[-1]
                f = open(dir_name[0] + '/' + file_name, "wb")
                f.write(r_url.content)
                f.close()

                print('\rdownloaded' + str(c) + '/' + str(all_), end='')
                c += 1


        except Exception as m:
            print(m)


    time_end = time.time()

    print('\nprogramme ended,total time used：', time_end-time_start, 'seconds')
    last = input('\npress Enter to quit\npress y to show images to bobo')
    if last == 'y':
        for dir in os.listdir(r"./"):
            try:
                show(dir)
            except:
                pass
    else:
        exit()

else:
    exit()
