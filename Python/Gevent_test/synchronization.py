"""
Description:
Author:qxy
Date: 2019/9/18 10:16 上午
File: tongbu 
"""

import requests
import timeit



def sss():
    url = 'http://httpbin.org/ip'
    for i in range(50):
        print("{}: {}".format(i, requests.get(url).text))


if __name__ == '__main__':
    b = timeit.default_timer()
    sss()
    e = timeit.default_timer()
    print(e - b)


