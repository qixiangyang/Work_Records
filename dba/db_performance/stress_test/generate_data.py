"""
Description:
Author:qxy
Date: 2019-09-05 13:49
File: generate_data 
"""


def gen_test_data(x, text_len):

    for _ in range(x):
        base_data = {
            'title': 'title' * 10,
            'text': 'text' * text_len,
            'date': '2019-08-28',
            'index': _
        }
        yield base_data


if __name__ == '__main__':
    data = gen_test_data(10, 10)
    print(data)
    # print(len(data))