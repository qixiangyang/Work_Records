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


def get_data(index, x):
    res = requests.get(url, headers=headers)
    print('线程ID：{} 任务ID：{} 请求状态：{}'.format(index, x, res.status_code))
    # time.sleep(1)
    return res.text


def get_title(index, text_info, x):
    page_dom = etree.HTML(text_info)
    title_list = page_dom.xpath('/html/body/div/div/div[1]/div/h2/a/text()')
    print('线程ID：{} 任务ID：{} 结果：{}'.format(index, x, str(title_list)))
    return title_list


def main(index, seed_list):
    print(seed_list)
    for x in seed_list:
        text_info = get_data(index, x)
        get_title(index, text_info, x)


x = list(range(101, 200))
seg = 10
ths = []

for _ in range(seg):
    th = threading.Thread(target=main, args=(_, x[_*seg: (_+1)*seg]))
    th.start()
    ths.append(th)

for th in ths:
    th.join()
