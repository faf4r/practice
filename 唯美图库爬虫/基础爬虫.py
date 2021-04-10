import requests
import os
import re
import time
from datetime import datetime

'''
网址必须有效才行
'''

url = 'https://www.smmv.net/902.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'}

start = datetime.now()
try:
    r = requests.get(url, headers=headers)
    urls = re.findall('<img alt=".*?" src="(.*?)".*?>',r.text)
    
    dir_name = re.findall('<h1 class="post-title h3">(.*?)</h1>', r.text)
    print('目录名称：',dir_name)
    
    all_ = len(urls)
    if all_:
        print('共找到',all_,'条url')
    c = 1
    
except Exception as m:
        print(m)
        
try:
    os.mkdir(dir_name[0])
except Exception as e:
    print(e)
    
for url in urls:
    r_url = requests.get(url,headers=headers)
    
    file_name = url.split('/')[-1]    
    f = open(dir_name[0]+'/'+file_name, "wb")
    f.write(r_url.content)
    f.close()
    
    print('\r已下载'+str(c)+'/'+str(all_), end='')
    c += 1
    time.sleep(1)
    
end = datetime.now()

print('\n程序运行完毕，共用时：', (end-start).seconds, '秒')
