# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
#    Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

import random as r

n = int(input("Input len of sequence: "))
m = int(input("Input searchin' number: "))
A = [r.randint(0, 9) for x in range(n)]
print(A)

count = 0
for i in A:
    if i == m:
        count +=1
print(f"Digit: {m} meets {count} times")