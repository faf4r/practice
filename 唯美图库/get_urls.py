from requests import get
from re import findall
headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36 Edg/89.0.774.57'}
url = 'https://www.smmv.net/'


# 访问网页查看最新链接
def get_latest_num():
    r = get(url=url, headers=headers)
    latest_url = findall('<a class="media-content" href="(.*?)" target="_blank">', r.text)[0]
    latest = latest_url.split('/')[-1].split('.')[0]
    return int(latest)


# 从1开始下载可用链接，耗时较久
def get_urls():
    start = 1
    end = get_latest_num() + 1
    for i in range(start, end): # 开始循环选择
        print('\r正在下载urls...  请勿打断该过程', end='')
        url = 'https://www.smmv.net/{}.html'.format(str(i))
        try:# 筛选可用第url
            r = get(url=url, headers=headers, timeout=1)
            urls = findall('<img alt=".*?" src="(.*?)".*?>', r.text)
            if len(urls):
                f = open('urls.txt', 'a+')
                f.write(url+'\n')
                f.close()
            else:
                pass
        except Exception as e:
            print(e)
    print('下载完成')


# 查询已有链接
def had_num():
    f = open('urls.txt', 'r')
    list_ = f.read().split('\n')
    num = list_[-2].split('/')[-1].split('.')[0]
    return int(num)


# 更新已有链接，如果没有，将进行下载
def update():
    try:
        f = open('urls.txt', 'r')
        start = had_num() +1
        end = get_latest_num() + 1
        if start < end:
            for i in range(start, end):
                url = 'https://www.smmv.net/{}.html'.format(str(i))
                try:
                    r = get(url=url, headers=headers, timeout=1)
                    urls = findall('<img alt=".*?" src="(.*?)".*?>', r.text)
                    if len(urls):
                        f = open('urls.txt', 'a+')
                        f.write(url+'\n')
                        f.close()
                    else:
                        pass
                except Exception as w:
                    print(W)

            print('更新完成')
        else:
            print('已是最新版本')
    except:
            print('无urls.txt文件，正在为您下载...')
            get_urls()


# 服务于主程序，模块最终目的，返回一个urls列表已供遍历
def urls_list():
    try:
        f = open('urls.txt','r')
        list_ = f.read().split('\n')
        return list_
    except:
        print('无urls.txt文件，正在为您下载...')
        get_urls()
        urls_list()


# 直接运行该文件将更新，没有就下载
if __name__ == '__main__':
    update()
