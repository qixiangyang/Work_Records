"""
Description:
Author:qxy
Date: 2019-09-05 15:22
File: draw_data 
"""

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import datetime


def gen_graph(x_data, y_data, db_name, insert_type, text_len):

    date = datetime.date.today().strftime('%Y-%m-%d')
    # print(date)

    plt.figure(dpi=300)
    plt.plot(x_data, y_data)
    plt.title('time flow with data increase')
    plt.ylabel("time, unit:s")
    plt.xlabel("data volume")
    plt.savefig('{}-{}-{}-{}.png'.format(db_name, insert_type, date, str(text_len)))


if __name__ == '__main__':
    x = [0, 1000, 2000, 3000, 4000]
    y = [0.13, 0.144, 0.1353, 0.15, 0.1662]
    func_name = ''
    insert_type = ''
    text_len = 1000
    gen_graph(x, y, func_name, insert_type, text_len)