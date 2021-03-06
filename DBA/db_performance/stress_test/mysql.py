"""
Description:
Author:qxy
Date: 2019-09-03 18:11
File: mysql 
"""

import MySQLdb
import time
from generate_data import gen_test_data
from draw_data import gen_graph


conn = MySQLdb.connect(
     host="localhost",    # 主机名
     user="root",         # 用户名
     passwd="12345678",  # 密码
     db="test")        # 数据库名称

cur = conn.cursor()


def insert_data(data_info, block, text_len, data_num):

    count = 1
    count_time = time.time()

    x_data = []
    y_data = []

    for test_data in data_info:
        sql = "insert into article_info (title, text, date) values " \
              "('%s', '%s', '%s')" % (str(test_data['title']), test_data['text'], test_data['date'])

        cur.execute(sql)
        count += 1
        conn.commit()
        if count % block == 0:
            # conn.commit()
            tmp_time = time.time()
            per_time = tmp_time - count_time
            print(count, per_time)
            count_time = time.time()
            x_data.append(count)
            y_data.append(per_time)

    conn.close()
    gen_graph(x_data, y_data, 'MySQL', 'one_by_one', text_len, data_num)


if __name__ == '__main__':

    data_num = 50000
    block_num = 5000
    text_len = 1000
    test_data_list = gen_test_data(data_num, text_len)

    time_start = time.time()
    insert_data(test_data_list, block_num, text_len, data_num)
    time_end = time.time()

    print('totally cost', time_end - time_start)
    # cur.execute("""create table article_info (
    #             id int PRIMARY KEY AUTO_INCREMENT,
    #             title char not null,
    #             text text(2000) not null,
    #             date date not null)""")
    # print('创建表成功')

