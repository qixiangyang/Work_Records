"""
Description:
Author:qxy
Date: 2019-09-03 18:11
File: mongo_test 
"""
import pymongo
import time
from generate_data import gen_test_data
from draw_data import gen_graph


client = pymongo.MongoClient(host='localhost', port=27017)
db = client.insert_test

db_insert = db.insert_test_db


def insert_data(data_info, block, text_len, data_len):

    count = 1
    count_time = time.time()

    x_data = []
    y_data = []
    data_list = []

    for test_data in data_info:
        count += 1
        # data_list.append(test_data)
        db_insert.insert_one(test_data)

        if count % block == 0:
            # print(data_list)
            # db_insert.insert_many(data_list)
            tmp_time = time.time()
            per_time = tmp_time - count_time
            print(count, per_time)
            count_time = time.time()

            data_list = []
            x_data.append(count)
            y_data.append(per_time)

    gen_graph(x_data, y_data, 'Mongo', 'one_by_one', text_len, data_len)


if __name__ == '__main__':

    data_num = 50000
    block_num = 5000
    text_len = 1000
    test_data_list = gen_test_data(data_num, text_len)

    time_start = time.time()
    insert_data(test_data_list, block_num, text_len, data_num)
    time_end = time.time()

    print('totally cost', time_end - time_start)



