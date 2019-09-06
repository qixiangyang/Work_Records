"""
Description:
Author:qxy
Date: 2019-09-03 18:12
File: postgre 
"""

import psycopg2
import time
from generate_data import gen_test_data
from draw_data import gen_graph


conn = psycopg2.connect(database="wangyuebing",
                        user="postgres",
                        password="12345678",
                        host="127.0.0.1",
                        port="5432")
print("Opened database successfully")

cur = conn.cursor()


def insert_data(data_info, block, text_len):

    count = 1
    count_time = time.time()

    x_data = []
    y_data = []

    for test_data in data_info:
        sql = "insert into article_info (title, text, date) values " \
              "('%s', '%s', '%s')" % (str(test_data['title']), test_data['text'], test_data['date'])

        cur.execute(sql)
        count += 1
        # conn.commit()
        if count % block == 0:
            conn.commit()
            tmp_time = time.time()
            per_time = tmp_time - count_time
            print(count, per_time)
            count_time = time.time()
            x_data.append(count)
            y_data.append(per_time)

    conn.close()
    gen_graph(x_data, y_data, 'PostgreSQL', 'block', text_len)


if __name__ == '__main__':

    data_num = 10000000
    block_num = 100000
    text_len = 1000
    test_data_list = gen_test_data(data_num, text_len)

    time_start = time.time()
    insert_data(test_data_list, block_num, text_len)
    time_end = time.time()

    print('totally cost', time_end - time_start)

    # cur.execute("""create table article_info (
    #             id serial primary key,
    #             title text not null,
    #             text text not null,
    #             date date not null)""")
    # print('创建表成功')