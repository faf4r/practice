import requests
import re
from datetime import datetime

start = datetime.now()

text = open('#imgurls.txt', mode='r')
urls = re.findall('<img src="(.*?)">', text.read())
text.close()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'}
if len(urls):
    print('共找到', len(urls), '张图片')

i = 1
for url in urls:
    img = requests.get(url, headers=headers)
    f = open(str(i)+'.jpg', 'wb')
    f.write(img.content)
    f.close()
    print('\r已下载'+str(i)+'/'+str(len(urls)), end='')
    i += 1


end = datetime.now()

print('\n程序运行完成，共用时：', (end-start).seconds, '秒')
