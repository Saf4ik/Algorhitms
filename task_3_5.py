# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.
import random as r


a = [r.randint(-100, 50) for i in range(15)]
print(a)
mn = 0
for i in a:
    if i < 0 and i < mn:
        mn = i
print(f'Минимальный элемент {mn}, его индекс {a.index(mn)}')



