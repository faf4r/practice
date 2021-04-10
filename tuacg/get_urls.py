import requests
from lxml import etree

demo_url = 'https://www.tuacg.com/download?post_id=792&index=0&i=1'  # i=0:百度网盘, i=1:萌盘
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68',
    'referer': 'https://www.tuacg.com/download?post_id=792&index=0&i=1',
    'cookie': 'b2_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3LnR1YWNnLmNvbSIsImlhdCI6MTYxNzQ1NjUxOCwibmJmIjoxNjE3NDU2NTE4LCJleHAiOjE2MTg2NjYxMTgsImRhdGEiOnsidXNlciI6eyJpZCI6IjQ0ODMifX19.IAEu06N1T2OzNDD6X83u7L2wWEWPP8ZuPnCwojtx4JI; wordpress_logged_in_3128f388d9ecc702138fc5e6e2beeda9=4483.516.a0b5dd434cb4de1f3da93df9c39659f9%7C1618061323%7CDYjAtU28rTKp47Z7yn5rNFnV6gaVl99bw2wQ388bmWB%7C1f41bb2d4620b7cc94b183504325762eb3536401cc5508219448e8fcc40bf4d5; wp_xh_session_3128f388d9ecc702138fc5e6e2beeda9=02e3165536c3e963fa311d3a9c67f955%7C%7C1618136679%7C%7C1618133079%7C%7C6620e41c0b45742aba727ce14af9b66d; PHPSESSID=kidnuu0ht77ggmmiq7nmhie109',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3LnR1YWNnLmNvbSIsImlhdCI6MTYxNzQ1NjUxOCwibmJmIjoxNjE3NDU2NTE4LCJleHAiOjE2MTg2NjYxMTgsImRhdGEiOnsidXNlciI6eyJpZCI6IjQ0ODMifX19.IAEu06N1T2OzNDD6X83u7L2wWEWPP8ZuPnCwojtx4JI'
}


def demo(url):
    r = requests.get(url, headers=headers)
    try:
        selector = etree.HTML(r.text)
        result = selector.xpath('/html/body/@id')
        if result[0] == 'error-page':
            print('error url:', url)
        else:
            pass
    except Exception:
        print('available url:', url)
        save(url)


def save(url):
    with open('urls.txt', 'a+') as f:
        f.write(url+'\n')


if __name__ == '__main__':
    for i in range(0, 1000):
        url = f'https://www.tuacg.com/download?post_id={i}&index=0&i=1'
        demo(url)
