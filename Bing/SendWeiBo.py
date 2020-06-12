# —*— coding: utf-8 —*—


import requests
import datetime

# 第一步 获取code
"""
code获取方法
url = https://api.weibo.com/oauth2/authorize?
client_id=AppKey
redirect_uri=https://api.weibo.com/oauth2/default.html
CodeUrl = https://api.weibo.com/oauth2/authorize?client_id=AppKey&redirect_uri='https://api.weibo.com/oauth2/default.html&response_type=code
请求CodeUrl之后会转到http://www.example.com/response&code=CODE,记录下该url中的CODE
"""


# 第二步 获取Token
# def GetToken():
#     url_get_token = "https://api.weibo.com/oauth2/access_token"
#     # 构建POST参数
#     payload = {
#         "client_id": "1088808918",  # 申请应用时分配的AppKey
#         "client_secret": "8eef7420e3622bdae046730b273efe7d",  # 申请应用时分配的AppSecret
#         "grant_type": "authorization_code",  # 请求的类型，填写authorization_code
#         "code": 'fbc842b345d14d86da156f32be020bc9',  # 第一部获取的code
#         "redirect_uri": "https://api.weibo.com/oauth2/default.html" # 回调地址
#     }
#     # POST请求
#     r = requests.post(url_get_token, data=payload)
#     # 输出响应信息
#     print(r.text)


def SendWeiBo():
    # 发表文字/图片微博的接口
    url = "https://api.weibo.com/2/statuses/share.json"
    # 构建POST参数
    payload = {
        "access_token": "2.00wcHRWGKwWgLBfd3d9cbdbcqI3hYB",  # 第二步获取的Token
        "status": "图片名称是中文还不能发 https://www.baidu.com"
    }
    # today = str(datetime.date.today()).replace("-", "")
    # picture = "/home/ysk/PycharmProjects/Reptile/Bing/Picture/" + today + '.jpg'
    picture = 'https://cn.bing.com/th?id=OHR.JoanNYC_ZH-CN1501350561_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp'
    img = requests.get(picture)
    files = {
        "pic": open(img.content, "rb")
    }
    r = requests.post(url, data=payload, files=files)
    print(r.text)


if __name__ == '__main__':
    print(SendWeiBo())