# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.


a = [[0 for i in range(5)] for j in range(4)]
for cols in range(len(a)):
    s = 0
    for rows in range(4):
        a[cols][rows] = int(input("Input number: "))
        s += a[cols][rows]
    a[cols][-1] = s
for i in a:
    print(i)
