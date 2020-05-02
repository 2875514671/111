# —*— coding: utf-8 —*—


import requests
import json


def request_wallpaper(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text

    except requests.RequestException:
        return None


def ImgContent(urls):
    uri = 'https://cn.bing.com'
    # 2020.05.02 添加 verify=False 取消 SSL验证
    img = requests.get(uri + urls['url'], verify=False)
    return img.content  # 返回图片二进制


def ShiciText(Shici_url):
    responses = requests.get(Shici_url)
    Shici = json.loads(responses.text)['hitokoto']
    return Shici


def SendWeiBo(urls):
    # 发表文字/图片微博的接口
    url = "https://api.weibo.com/2/statuses/share.json"
    # 构建POST参数
    text = ShiciText(Shici_url) + 'https://www.baidu.com'
    payload = {
        "access_token": "2.00wcHRWGKwWgLBfd3d9cbdbcqI3hYB",
        "status": text
    }
    files = {
        "pic": ImgContent(urls)
    }
    r = requests.post(url, data=payload, files=files)
    print(r.text)


if __name__ == '__main__':
    Image_url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    # idx=0是今日的壁纸数据，1 2  3  4  5...依次是昨日、前日...   数字是-1是明日的数据
    Shici_url = 'https://v1.hitokoto.cn/?c=i'
    urls = json.loads(request_wallpaper(Image_url))['images'][0]
    SendWeiBo(urls)
