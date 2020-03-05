# -*- coding: utf-8 -*-

# Проверка числа на простоту


def prime_num(n):
    if n == 1:
        return False
    for i in range(2, n + 1):
        if n % i == 0 and i == n:
            return True
        elif n % i == 0 and i != n:
            return False


# выводит список всех делителей числа
def get_divisors(n):
    lst_divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst_divisors.append(i)
    return lst_divisors


# выводит самый большой простой делитель числа
def get_max_prime(n):
    lst_max_prime = []
    lst_divs = get_divisors(n)
    for i in lst_divs:
        if prime_num(i):
            lst_max_prime.append(i)
    return max(lst_max_prime)

# Тест №1 - Проверка числа на простоту (истинные значения)


def test_1():
    dct_in = {'7': True, '101': True, '997': True}
    dct_out = {}
    for key in dct_in.keys():
        bool_out = prime_num(int(key))
        dct_out[key] = bool_out
    if dct_in == dct_out:
        print('Test #1 OK')
    else:
        print('Test #1 is failed')


# Тест №2 - Проверка числа на простоту (ложные значения)


def test_2():
    dct_in = {'4': False, '100': False, '500': False}
    dct_out = {}
    for key in dct_in.keys():
        bool_out = prime_num(int(key))
        dct_out[key] = bool_out
    if dct_in == dct_out:
        print('Test #2 OK')
    else:
        print('Test #2 is failed')


test_1()
test_2()


