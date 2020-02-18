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

