"""
Description:
Author:qxy
Date: 2019-09-13 10:43
File: a_mock_test 
"""
import requests
import mock
from unittest import mock


def send_request(url):
    r = requests.get(url)
    return r.status_code


def visit_ustack():
    return send_request('http://www.ustack.com')


