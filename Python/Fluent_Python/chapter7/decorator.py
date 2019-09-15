"""
Description:
Author:qxy
Date: 2019-07-06 10:20
File: decorator 
"""


# def make_averager():
#     val_list = []
#
#     def avg(val):
#          val_list.append(val)
#          tatal = sum(val_list)
#          return tatal / len(val_list)
#
#     return avg
#
#
# avg = make_averager()
# avg(10)
# avg(11)
#
# print(avg.__doc__)


import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factotial(n):
    return 1 if n < 2 else n * factotial(n-1)


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(123)')
    snooze(.123)
    print('*' * 40, 'Calling factotial(6)')
    factotial(6)

