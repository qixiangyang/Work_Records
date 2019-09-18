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
gevent.monkey.patch_socket()


def hello(i):
    url = 'http://httpbin.org/ip'
    print("{}: {}".format(i, requests.get(url).text))


b = timeit.default_timer()
tasks = [gevent.spawn(hello, i) for i in range(50)]
gevent.joinall(tasks)
e = timeit.default_timer()
print(e - b)