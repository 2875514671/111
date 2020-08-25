# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from time import sleep
import os


def request_wallpaper(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def html_href(html):
    soup = BeautifulSoup(html, 'html.parser')
    imgs = soup.find_all('img')
    get_imgs = []
    for img in imgs:
        i = img.get('data-src')
        if i is None:
            pass
        else:
            get_imgs.append(i)
    return get_imgs


def save_imgs(imgs):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/83.0.4103.97 Safari/537.36 ",
               "Referer": "https://wallhaven.cc"
               }
    for img in imgs:
        img_name = img[-10:]
        if not os.path.exists(img_name):
            save_img = requests.get(img, headers=headers)
            root = r"E:\Jetbrains\Projects\Reptile\Wallhaven\Wallhaven"
            with open(root + '\\' + img_name, 'wb') as f:
                sleep(1)
                f.write(save_img.content)
            print(img_name, '图片爬取成功')
        else:
            print('爬取失败')


def main():
    url = 'https://wallhaven.cc/latest'
    html = request_wallpaper(url)
    imgs = html_href(html)
    save_imgs(imgs)


if __name__ == '__main__':
    main()