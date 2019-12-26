

"""
当在 "try...finally" 语句的 try 中执行 return, break 或 continue 后, finally 子句依然会执行.
函数的返回值由最后执行的 return 语句决定. 由于 finally 子句一定会执行, 所以 finally 子句中的 return 将始终是最后执行的语句.
"""


def some_func():
    try:
        print(1)
        return 'from_try'
    finally:
        print(2)
        return 'from_finally'


if __name__ == '__main__':
    some_func()


