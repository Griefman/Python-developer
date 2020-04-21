# -*- coding: utf-8 -*-

import time


def show_time(f):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        f(*args, **kwargs)
        time_end = time.time()
        print('Начало выполнения: ', time_start, 'Завершение выполнения: ', time_end)
        print('Время выполнения: ', time_end - time_start, 'sec')
    return wrapper


@show_time
def list_creator(num):
    list_numbers = []
    for i in range(1, num + 1):
        list_numbers.append(i)
    return list_numbers


list_creator(1000000)


@show_time
def list_generator(num):
    for i in range(1, num + 1):
        yield i


list_generator(1000000)




