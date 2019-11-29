"""
Description:
Author:qxy
Date: 2019/9/18 10:25 上午
File: gevent_test 
"""
import requests
import gevent
import gevent.monkey
# 这里将socket变成异步
import timeit
from lxml import etree
gevent.monkey.patch_socket()


def hello(i):
    url = 'https://www.baidu.com/'
    data = requests.get(url)
    text = etree.HTML(data.text).xpath('//*[@id="bottom_layer"]/div/div/span/span[2]/text()')
    print("{}: {}: {}".format(i, data.status_code, str(text)))


b = timeit.default_timer()
tasks = [gevent.spawn(hello, i) for i in range(100)]
gevent.joinall(tasks)
e = timeit.default_timer()
print(e - b)