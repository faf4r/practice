import requests
import os
import time
import re
import concurrent.futures

headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36 Edg/89.0.774.57'}

def change_title(title):
    mode = re.compile(r'[\\\/\:\*\?\"\<\>\|]')
    file_name = re.sub(mode, '_', title)
    return file_name

def download(url):
    resp = requests.get(url, headers=headers)
    base_html = resp.json()
    data_list = base_html['data']

    try:
        os.mkdir('video')
    except:
        pass

    try:
        for data in data_list:
            title = change_title(data['title']) + '.mp4'
            url = data['playUrl']

            r = requests.get(url, headers=headers)
            video_data = r.content
            with open('video/'+title,'wb') as f:
                f.write(video_data)
            print('已下载：', title)
    except Exception as e:
        print(e)
        print('下载失败：',title)


if __name__ == '__main__':
    start_time = time.time()
    exe = concurrent.futures.ThreadPoolExecutor(max_workers=5)
    for page in range(1, 6):
        url = f'https://www.ku6.com/video/feed?pageNo={page}&pageSize=40&subjectId=74'
        exe.submit(download, url)
    exe.shutdown()
    end_time = time.time()
    print('共计用时：', int(end_time - start_time), '秒')

