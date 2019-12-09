# -*- coding: utf-8 -*-


import requests
import re
import os
import time


def get_parse_page(pn, name):

    for i in range(int(pn)):
        print('正在获取第{}页'.format(i + 1))

        url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%s&pn=%d' % (name, i * 20)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400'
        }

        response = requests.get(url, headers=headers)

        html = response.content.decode()

        results = re.findall('"objURL":"(.*?)",', html)
        print(results)
        save_to_txt(results, name, i)


def save_to_txt(results, name, i):
    j = 0

    if not os.path.exists('./' + name):
        os.makedirs('./' + name)

    for result in results:
        print("正在保存第{}个".format(j))

        try:
            pic = requests.get(result, timeout=10)
            time.sleep(1)
        except:
            print('当前图片无法下载')
            j += 1
            continue

        file_full_name = './' + name + './' + str(i) + '-' + str(j) + '.jpg'
        with open(file_full_name, 'wb') as f:
            f.write(pic.content)

        j += 1


if __name__ == '__main__':
    name = input("请输入要下载的关键词： ")
    pn = input('你想下载前几页(一页60张图片)： ')
    get_parse_page(pn, name)
