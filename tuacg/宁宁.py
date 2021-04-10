import requests
from lxml import etree

htmlurl = 'https://www.30wt.net/love/131/20210106/39057.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68'
}


def geturls(htmlurl):
    r = requests.get(htmlurl, headers)
    selector = etree.HTML(r.text)
    urls = selector.xpath('//*[@id="main-wrapper"]/div[5]/img/@src')
    return urls


def save(url):
    r = requests.get(url, headers)
    name = url.split('/')[-1]
    with open('./樱井宁宁/'+name, 'wb') as f:
        f.write(r.content)


if __name__ == '__main__':
    for url in geturls(htmlurl):
        save(url)
