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
    # 返回的url链接加密，不知道怎么破解，有时间再说
    names = (json.loads(urls))['works_name']
    cop = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9]")
    n = re.sub(r"[A-Za-z0-9\!\%\[\]\,\。]", "", names)
    name = cop.sub('', n)
    print(name)
    # 文件保存地址
    root = r"D:\JetBrains\PycharmProjects\Reptile\Wallpaper\Wallpaper"

    img_name = name + '.jpg'
    if not os.path.exists(img_name):
        """
        2020-06-12 添加 headers 解决图片下载失败
        根据请求图片地址发现抱错{"code":"40310014","msg":"invalid Referer header"}，
        参照大佬的描述 https://www.jianshu.com/p/46c127a699f7
        请求头中添加 Referer，解决此问题
        """
        # 2020-06-12 根据请求图片地址发现抱错{"code":"40310014","msg":"invalid Referer header"}，请求头中添加 Referer
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/83.0.4103.97 Safari/537.36 ",
                   "Referer": "https://wallpaper.wispx.cn/"
                   }
        img = requests.get(imgs, headers=headers)
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
    for i in range(6):
        main()
