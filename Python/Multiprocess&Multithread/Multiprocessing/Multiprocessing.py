"""
Description:
Author:qxy
Date: 2019-07-09 15:01
File: Multiprocessing 
"""

import os, time, random
from multiprocessing import Process, Pool, Queue
import subprocess


# print("Process %s is running" % (os.getpid()))
#
# pid = os.fork()
# if pid == 0:
#     print("i am child process %s and my parent process is %s" % (os.getpid(), os.getppid()))
#
# else:
#     print('i %s just create a child process %s' % (os.getpid(), pid))

"""
Process 方法
"""

# def run_proc(name):
#     print("Run child process %s (%s)" % (name, os.getpid()))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test', ))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')

"""
Pool 方法
"""


# def long_time_tast(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_tast, args=(i, ))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')


"""
subproces 子进程方法
"""

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)


"""
进程间通信
"""
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))

    pw.start()
    pr.start()
    pw.join()

    pr.terminate()
