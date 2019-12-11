"""
Description:
Author:qxy
Date: 2019/12/11 10:35 下午
File: celery_test 
"""

from celery import Celery

app = Celery('task', broker='amqp://guest@localhost//',
             backend='redis://localhost:6379/0')


@app.task
def add(x, y):
    return x + y


if __name__ == '__main__':
    app


