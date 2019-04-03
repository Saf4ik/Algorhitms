# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random as r
a = [r.randint(1,99) for x in range(10)]
print(a)
low = min(a)
top = max(a)
ilow = a.index(low)
itop = a.index(top)
a[ilow], a[itop] = a[itop], a[ilow]
print(a)