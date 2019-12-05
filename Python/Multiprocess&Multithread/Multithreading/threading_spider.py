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
from queue import Queue

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


def main(index, task_id_list_seg):

    for x in task_id_list_seg:
        text_info = get_data(index, x)
        get_title(index, text_info, x)


task_id_list = list(range(101, 200))
seg = 10
ths = []

for _ in range(seg):
    th = threading.Thread(target=main, args=(_, task_id_list[_*seg: (_+1)*seg]))
    th.start()
    ths.append(th)

for th in ths:
    th.join()

"""
对待爬取的url种子进行分片，然后每个线程取特定的分片里的数据。
This is work, 但是需要更加 Pythonic 的方式。就是使用队列，。
deque 是线程安全的。勘误不是
deque.Queue 是线程安全的
参考地址：https://juejin.im/post/5b129a1be51d45068a6c91d4
deque 双向队列
Queue 先进先出队列 FIFO
"""


class SpiderTest:
    url = 'https://qixiangyang.cn/'
    headers = {'cookie': 'test_thread'}

    def __init__(self, id_list, nums):
        self.id_list = id_list
        self.nums = nums
        self.q = Queue(len(id_list))

    def get_url(self):
        for _ in self.id_list:
            self.q.put(_)

    def get_data(self, index, x):
        res = requests.get(self.url, headers=self.headers)
        print('线程ID：{} 任务ID：{} 请求状态：{}'.format(index, x, res.status_code))
        return res.text

    @staticmethod
    def get_title(index, text_info, x):
        page_dom = etree.HTML(text_info)
        title_list = page_dom.xpath('/html/body/div/div/div[1]/div/h2/a/text()')
        print('线程ID：{} 任务ID：{} 结果：{}'.format(index, x, str(title_list)))
        return title_list

    def get_info(self, t_num):
        while not self.q.empty():
            x = self.q.get()
            text_info = self.get_data(t_num, x)
            self.get_title(t_num, text_info, x)

    def run(self):
        self.get_url()
        ths = []
        for _ in range(self.nums):
            th = threading.Thread(target=self.get_info, args=(_,))
            th.start()
            ths.append(th)
        for th in ths:
            th.join()


start = time.time()

url_id = list(range(101, 200))
a = SpiderTest(url_id, 20)
a.run()

end = time.time()
print('总共花费时间:', end - start)