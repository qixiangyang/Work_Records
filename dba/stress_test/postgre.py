"""
Description:
Author:qxy
Date: 2019-09-03 18:12
File: postgre 
"""

import psycopg2
import time
from generate_data import gen_test_data


conn = psycopg2.connect(database="wangyuebing", user="postgres",
                        password="12345678", host="127.0.0.1",
                        port="5432")

print("Opened database successfully")

cur = conn.cursor()

# cur.execute("""create table article_info (
#             id serial primary key,
#             title text not null,
#             text text not null,
#             date date not null)""")
# print('创建表成功')

# cur.execute("insert into article_info (title, text, date) values ('%s', '%s', '%s')" % ('ssss', 'sssssssss', '2019-08-02'))
# conn.commit()
# conn.close()


def insert_data(x):

    test_data_list = gen_test_data(x)
    count = 1
    count_time = time.time()

    for test_data in test_data_list:
        sql = "insert into article_info (title, text, date) values " \
              "('%s', '%s', '%s')" % (str(test_data['title']), test_data['text'], test_data['date'])

        cur.execute(sql)
        count += 1
        if count % 1000 == 0:
            conn.commit()
            tmp_time = time.time()
            per_time = tmp_time - count_time
            print(count, per_time)
            count_time = time.time()

    conn.close()


if __name__ == '__main__':

    time_start = time.time()
    insert_data(1000000)
    time_end = time.time()
    print('totally cost', time_end - time_start)