"""
Description:
Author:qxy
Date: 2019-07-09 16:48
File: Coroutine 
"""

import asyncio
import requests


async def test1():
    print('1')
    # await asyncio.sleep(1)  # asyncio.sleep(1)返回的也是一个协程对象
    await test2()
    print('2')


async def test2():
    print('3')
    print('4')

# a = test1()
# b = test2()

# try:
#     a.send(None)
# except StopAsyncIteration as e:
#     print(e.value)
#     pass
#
# try:
#     b.send(None)
# except StopAsyncIteration as e:
#     print(e.value)
#     pass

# loop =asyncio.get_event_loop()
# loop.run_until_complete(test1())


"""爬虫测试"""

import asyncio
import aiohttp
import time


async def task_req():
    # 耗时0.1483309268951416s
    async with aiohttp.ClientSession() as session:
        async with session.get('http://baidu.com') as resp:
            print(resp.status)


async def for_req():
    # 耗时2.0457730293273926
    async with aiohttp.ClientSession() as session:
        for i in range(100):
            async with session.get('https://baidu.com') as resp:
                pass
                # print(resp.status)


def sync_req():
    # 耗时 11.768546104431152
    for i in range(100):
        requests.get('https://baidu.com')


if __name__ == '__main__':
    s = time.time()
    # 第一组
    # sync_req()
    # 第二组
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(task_req()) for i in range(100)]
    loop.run_until_complete(asyncio.wait(tasks))
    t = time.time()
    print(print(t - s))
    # 第三组
    loop.run_until_complete(for_req())

    print(time.time() - s)
