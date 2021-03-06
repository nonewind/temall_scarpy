# Author : ziheng_wind
# Email : wn345361049@163.com
# github : https://github.com/Zhangziheng1/temall_scarpy
# -*- coding: utf-8 -*-

"""
封装的方糖，key可以更换成自己的key，
url：http://sc.ftqq.com/3.version
发送消息非常简单，只需要向以下URL发一个GET或者POST请求：

https://sc.ftqq.com/__YOUR_KEY__.send

接受两个参数：

text：消息标题，最长为256，必填。
desp：消息内容，最长64Kb，可空，支持MarkDown。

"""

import requests


def shuju(text,desp):
    url = "https://sc.ftqq.com/__YOUR_KEY__.send"
    data = {
        'text':text,
        'desp':desp
    }
    
    req = requests.post(url,data=data)
    print(req)


if __name__ == "__main__":
    pass