# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
#     -   Без использования «Решета Эратосфена»;
#     -   Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.


import time

def is_prime(n):
    res = []
    for i in range(2, n+1):
        # for j in res:
        #     if i % j == 0:
        #         break
        # else:
        #     res.append(i)
        for j in res:
            if j > int(i**0.5)+1:
                res.append(i)
                break
            elif i % j == 0:
                break
        else:
            res.append(i)
    return res
n = 1100
begin = time.time()



x = is_prime(n)
print(x)
end = time.time()
print(end - begin)