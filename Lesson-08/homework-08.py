# -*- coding: utf-8 -*-

import time


def show_time(f):
    def wrapper():
        time_start = time.time()
        f()
        time_end = time.time()
        print('Время выполнения: ', time_end - time_start, 'sec')

    return wrapper()


@show_time
def list_generator():
    return [i for i in range(1, 1000000 + 1)]


@show_time
def list_creator():
    list_numbers = []
    for i in range(1, 1000000 + 1):
        list_numbers.append(i)
    return list_numbers
