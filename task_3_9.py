# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random as r


a = [[r.randint(1,9) for i in range(5)] for j in range(4)]
for i in a:
    print(i)
b = []

for i in range(1):
    for j in range(5):
        mn = min(a[i][j], a[i+1][j], a[i+2][j], a[i+3][j])
        b.append(mn)
print(f'Минимальные элементы столбцов: {b}')
print(f'Среди них максимальный: {max(*b)}')