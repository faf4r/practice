import requests
from lxml import etree
import os

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68'
}


def getdir(htmlurl):
    r = requests.get(htmlurl, headers)
    r.encoding = 'utf-8'
    selector = etree.HTML(r.text)
    dirname = selector.xpath('//*[@id="main-wrapper"]/div[1]/h1/text()')
    return dirname[0]


def getoneurls(htmlurl):
    r = requests.get(htmlurl, headers)
    r.encoding = 'utf-8'
    selector = etree.HTML(r.text)
    urls = selector.xpath('//*[@id="main-wrapper"]/div[5]/img/@src')
    return urls


def prove(url):
    r = requests.get(url, headers)
    selector = etree.HTML(r.text)
    result = selector.xpath('/html/head/title/text()')
    if result == ['404 - ÕÒ²»µ½ÎÄ¼þ»òÄ¿Â¼¡£']:
        return False
    else:
        return True


def gethtmls():
    urls = []
    for i in range(39056, 39070):
        homeurl = f'https://www.30wt.net/love/131/20210106/{i}.html'
        urls.append(homeurl)
        print(homeurl)
        p = 2
        while True:
            pageurl = f'https://www.30wt.net/love/131/20210106/{i}_{p}.html'
            if prove(pageurl):
                urls.append(pageurl)
                print(pageurl)
                p += 1
            else:
                break
    print(urls)
    return urls



def save(dirname, url):
    r = requests.get(url, headers)
    r.encoding = 'utf-8'
    name = url.split('/')[-1]
    print('saving ', name)
    with open('./樱井宁宁/'+dirname+'/'+name, 'wb') as f:
        f.write(r.content)


if __name__ == '__main__':
    htmlurls = gethtmls()
    for htmlurl in htmlurls:
        dirname = getdir(htmlurl).split('(')[0]
        try:
            os.mkdir(r'C:\Users\Administrator\Desktop\tuacg\樱井宁宁\\'+dirname)
        except Exception as e:
            print(e)
        for url in getoneurls(htmlurl):
            save(dirname, url)
