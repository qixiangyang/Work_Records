"""
Description:
Author:qxy
Date: 2019/11/27 1:42 下午
File: threading 爬虫 
"""

import threading
import requests
import time
from lxml import etree


url = 'https://qixiangyang.cn/'

headers = {'cookie': 'test_thread'}


def get_data(index):
    res = requests.get(url, headers=headers)
    print(index, res.status_code)
    time.sleep(1)
    return res.text


def get_title(index, text_info):
    page_dom = etree.HTML(text_info)
    title_list = page_dom.xpath('/html/body/div/div/div[1]/div/h2/a/text()')
    print(index, title_list)
    return title_list


def main(index):
    text_info = get_data(index)
    get_title(index, text_info)


ths = []
for _ in range(10):
    th = threading.Thread(target=main, args=(_,))
    th.start()
    ths.append(th)

for th in ths:
    th.join()
