# 4. Написать программу, которая генерирует в указанных пользователем границах:
#       случайное целое число;
#       случайное вещественное число;
#       случайный символ.

import random as r

a = int(input("Введите начальное число: "))
b = int(input("Введите конечное число: "))
print(r.randint(a, b))
print(round(r.uniform(a, b), 3))


a = ord(input("Введите начальный символ: "))
b = ord(input("Введите конечный символ: "))
res = int(r.random() * (b-a+1)) + a
print(chr(res))

