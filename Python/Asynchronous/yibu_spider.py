"""
Description:
Author:qxy
Date: 2019/11/29 5:21 下午
File: yibu_spider 
"""

import asyncio
import aiohttp
import time
from lxml import etree

start = time.time()


async def get_data(url):
    """
    使用 aiohttp 请求数据
    """

    session = aiohttp.ClientSession()
    response = await session.get(url=url)
    page_text = await response.text()
    await session.close()
    return page_text


def parse_page(page_text):
    """
    使用 lxml 解析数据，由于 lxml 不支持协程的写法，所以使用了普通函数的写法
    """

    page_dom = etree.HTML(page_text)
    title_list = page_dom.xpath('/html/body/div/div/div[1]/div/h2/a/text()')
    return title_list


async def main(index):

    """
    主函数
    """
    url = 'https://qixiangyang.cn/'  # 放我的弱小的服务器吧，换个别的目标 Q_Q
    result = await get_data(url)
    title_list = parse_page(result)
    print('请求index', index, '结果:', str(title_list))


tasks = [asyncio.ensure_future(main(_)) for _ in range(100)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('总共花费时间:', end - start)