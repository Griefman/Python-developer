# -*- coding: utf-8 -*-
'''
Домашнее задание:

LIGHT:

1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);

2. Напишите функцию вывода самого частого имени из списка на выходе функции F;

3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.

PRO:

LIGHT +

4.  В файле с логами найти дату самого позднего лога (по метке времени): https://drive.google.com/open?id=1pKGu-u2Vvtx4xK8i2ZhOzE5rBXyO4qd8
'''
import random
from functools import reduce
# 1
names_lst = ['Misha', 'Peter', 'Maxim', 'Ilia', 'Oksana', 'Pavel', 'Olga', 'Tatiana', 'Angelina', 'Angela', 'Lubov',
             'Tamara', 'Svetlana', 'Valentina', 'Vera', 'Vadim', 'Ludmila', 'Nina', 'Ira', 'Antonina']
random_names_lst = []

N = 100


def random_names(names, n):
    for i in range(1, n + 1):
        random_names_lst.append(random.choice(names))
    return random_names_lst


print(random_names(names_lst, N))

dct = {}

# 2
def freq_name(lst):
    for name in lst:
        if name in dct:
            dct[name] += 1
        else:
            dct[name] = 1
    count = max(dct.values())
    freq_names = []
    for key, value in dct.items():
        if value == count:
            freq_names.append(key)
    print(freq_names)


freq_name(random_names_lst)

# 3
symbol_dct = {}


def rarely_name(lst):
    for word in lst:
        if word[0] in symbol_dct:
            symbol_dct[word[0]] += 1
        else:
            symbol_dct[word[0]] = 1

    freq_symbol = []
    count = min(symbol_dct.values())
    for key, value in symbol_dct.items():
        if value == count:
            freq_symbol.append(key)
    print(freq_symbol)


rarely_name(random_names_lst)

# 4
log_file = open('log.txt', 'r', encoding='UTF-8')
log_lst = []
for log in log_file:
    log_lst.append(log)
late_log = reduce(lambda a, b: a if a > b else b, log_lst)
print(late_log)
log_file.close()
