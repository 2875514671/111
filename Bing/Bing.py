# —*— coding: utf-8 —*—


import requests
import re
import os
import time
import json


def request_wallpaper(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text

    except requests.RequestException:
        return None


def save_to_document(urls):
    uri = 'https://cn.bing.com'
    imgs = urls['url']
    names = urls['copyright']
    cop = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9]")
    n = re.sub(r"[A-Za-z0-9\!\%\[\]\,\。]", "", names)
    name = cop.sub('', n)
    print(name)
    # 文件保存地址
    root = r"/home/ysk/PycharmProjects/Reptile/Bing/Picture"
    # root = r"E:\JetBrains\PyCharmProject\Reptile\Bing\Bing"

    img_name = name + '.jpg'
    if not os.path.exists(img_name):
        img = requests.get(uri + imgs)
        with open(root + '/' + img_name, 'wb') as f:
            time.sleep(0.5)
            f.write(img.content)
        print('图片爬取成功')
    else:
        print('爬取失败')


def main():
    url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    # idx=0是今日的壁纸数据，1 2  3  4  5...依次是昨日、前日...   数字是-1是明日的数据
    urls = json.loads(request_wallpaper(url))['images'][0]
    save_to_document(urls)


if __name__ == '__main__':
    main()
