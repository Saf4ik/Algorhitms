# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
#     -   Без использования «Решета Эратосфена»;
#     -   Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

import profile
import time
import timeit

def eratosphen(n):
    A = [False, False]+[True] * (n-2)
    for k in range(2, int(n**0.5)):
        if A[k]:
            for m in range(k**2, n, k):
                A[m] = False
    for k in range(len(A)):
        if A[k]:
            print(f'{k} - prime')



# profile.run('eratosphen(1100)')
begin = time.time()
eratosphen(1100)
end = time.time()
print(end - begin)


# В ТАКОМ ВИДЕ ПРИХОДИТ НЕ СРЕДНЕЕ, А ОБЩЕЕ ВРЕМЯ
# print(timeit.timeit("eratosphen(1100)",setup="from __main__ import eratosphen", number=100))
