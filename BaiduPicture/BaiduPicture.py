# -*- coding: utf-8 -*-


import requests
import os
import re
import time


def request_get_Pictururl(url, headers):
    try:
        response = requests.request('get', url=url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def save_to_txt(results, name, i):
    # i = 0

    if not os.path.exists('./' + name):
        os.makedirs('./' + name)

    for result in results:
        print("正在保存第{}个".format(i))

        try:
            pic = requests.get(result, timeout=10)
            time.sleep(0.5)
        except:
            print('当前图片无法下载')
            i += 1
            continue

        file_full_name = './' + name + './' + str(i) + '-' + str(i) + '.ipg'
        with open(file_full_name, 'wb') as f:
            f.write(pic.content)
        i += 1


def main(pn, name):
    for i in range(int(pn)):
        print('正在获取第{}页'.format(i + 1))

        url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%s&pn=%d' % (
            name, i * 20)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400'}

        html = request_get_Pictururl(url, headers)

        results = re.findall('"objURL":"(.*?)",', html)

        save_to_txt(results, name, i)


if __name__ == '__main__':
    name = input("请输入要下载的关键词： ")
    pn = input('你想下载前几页(一页60张图片)： ')
    main(pn, name)