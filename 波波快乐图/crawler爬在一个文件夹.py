from requests import get
from os import mkdir
from re import findall
from time import sleep
from datetime import datetime
import get_urls
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'}
urls_ = get_urls.urls_list()


s = datetime.now()

for url_ in urls_: # 主循环
    start = datetime.now()
    try: # 请求网址并得到图片链接列表
        r = get(url_, headers=headers, timeout=1)
        urls = findall('<img alt=".*?" src="(.*?)".*?>',r.text)

        # 用于计数显示
        all_ = len(urls)
        if all_:
            print('共找到',all_,'条url')
        c = 1
        
    except Exception as m:
            print(m)


    # 开始循环下载本页图片
    try:    
        for url in urls:
            r_url = get(url,headers=headers, timeout=3)
            # 确认文件名
            file_name = url.split('/')[-1]    
            f = open(file_name, "wb")
            f.write(r_url.content)
            f.close()
            # 计数显示
            print('\r已下载'+str(c)+'/'+str(all_), end='')
            c += 1
    except:
            print('一个图片下载失败')

        
    end = datetime.now()

    print('\n程序运行完毕，共用时：', (end-start).seconds, '秒')


l = datetime.now()
print('共用时：', (l-s).seconds, '秒')
