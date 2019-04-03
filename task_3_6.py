# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.


import random as r
a = [r.randint(1,99) for x in range(10)]
print(a)
low = min(a)
top = max(a)
ilow = a.index(low)
itop = a.index(top)

summa = 0
for i in range(ilow+1, itop):
    summa += a[i]

print(summa)