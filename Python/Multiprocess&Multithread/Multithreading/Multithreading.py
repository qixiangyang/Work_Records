
"""
Description:
Author:qxy
Date: 2019-07-09 14:21
File: Multithreading 
"""

# from time import ctime, sleep
# import threading
#
#
# def music(func):
#     for i in range(2):
#         print("I was listening to %s! %s" % (func, ctime()))
#         print(sleep(1))
#
#
# def movie(func):
#     for i in range(2):
#         print("I was at the %s! %s" %(func, ctime()))
#         sleep(5)
#
#
# threads = []
# t1 = threading.Thread(target=music, args=('爱情买卖',))
# threads.append(t1)
#
# t2 = threading.Thread(target=movie, args=('阿凡达',))
# threads.append(t2)
#
#
# if __name__ == '__main__':
#     for i in threads:
#         i.setDaemon(True)
#         i.start()
#     i.join()
#
#     print("all over %s" % ctime())


"""
廖雪峰教程
"""

import time, threading


# def loop():
#     print('thread %s is running...' % (threading.current_thread().name))
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
#
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

balance = 0


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def rum_thread(n):
    for i in range(10000000):
        change_it(n)


t1 = threading.Thread(target=change_it, args=(5,))
t2 = threading.Thread(target=change_it, args=(8,))

t1.start()
t2.start()
t1.join()
t2.join()

print(balance)
