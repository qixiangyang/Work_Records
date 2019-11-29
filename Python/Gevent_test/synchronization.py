"""
Description:
Author:qxy
Date: 2019/9/18 10:16 上午
File: tongbu 
"""

import requests
import timeit
import lxml
from lxml import etree


def sss():
    url = 'https://www.baidu.com/'
    for i in range(100):
        data = requests.get(url)
        text = etree.HTML(data.text).xpath('//*[@id="bottom_layer"]/div/div/span/span[2]/text()')
        print("{}: {}: {}".format(i, data.status_code, str(text)))


if __name__ == '__main__':
    b = timeit.default_timer()
    sss()
    e = timeit.default_timer()
    print(e - b)


