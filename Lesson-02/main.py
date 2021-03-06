# Задачи на циклы и оператор условия------
# ----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
for i in range(1, 6):
    print(i, i * '0', end="\n")

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
count = 0
for i in range(1, 11):
    n = int(input())
    if n == 5:
        count += 1
print(count)


'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
sum = 0
for i in range(1,101):
    sum += i
print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
mult = 1
for i in range(1, 11):
    mult *= i
print(mult)
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
integer_number = 2129
while integer_number > 0:
    print(integer_number % 10)
    integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
integer_number = 2129
result = 0
while integer_number > 0:
    result += integer_number % 10
    integer_number //= 10
print(result)
'''
Задача 7
Найти произведение цифр числа.
'''
integer_number = 2129
result = 1
while integer_number > 0:
    result *= integer_number % 10
    integer_number //= 10
print(result)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = 213413
while integer_number > 0:
    if integer_number % 10 == 5:
        print('Yes')
        break
    integer_number = integer_number // 10
else:
    print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
integer_number = 213413
max_number = 0
while integer_number > 0:
    current_number = integer_number % 10
    if current_number > max_number:
        max_number = current_number
    integer_number = integer_number // 10
print(max_number)

'''
Задача 10
Найти количество цифр 5 в числе
'''
integer_number = 213451355
count = 0
while integer_number > 0:
    if integer_number % 10 == 5:
        count += 1
    integer_number = integer_number // 10
print(count)
