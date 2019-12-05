# -*- coding: utf-8 -*-

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
    imgs = (json.loads(urls))['url']
    names = (json.loads(urls))['works_name']
    cop = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9]")
    n = re.sub(r"[A-Za-z0-9\!\%\[\]\,\。]", "", names)
    name = cop.sub('', n)
    print(name)
    # 文件保存地址
    root = r"E:\Jetbrains\PycharmProjects\Reptile\Wallpaper\Wallpaper"

    img_name = name + '.jpg'
    if not os.path.exists(img_name):
        img = requests.get(imgs)
        with open(root + '/' + img_name, 'wb') as f:
            time.sleep(0.5)
            f.write(img.content)
        print('图片爬取成功')
    else:
        print('爬取失败')


def main():
    url = 'https://wallpaper.wispx.cn/api/find?rand=1'
    urls = request_wallpaper(url)
    save_to_document(urls)


if __name__ == '__main__':
    for i in range(5):
        main()
