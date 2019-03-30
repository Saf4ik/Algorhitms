# 4.Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

n = int(input("Input number of elements: "))
A = [1, -0.5] + [0]*(n-2)
for i in range(2, len(A)):
    A[i] = A[i-2] / 4
print(sum(A))


# n = int(input("Input number of elements: "))
# A = [1, -0.5] + [0]*(n-2)
# summa = 0.5
# for i in range(2, len(A)):
#     A[i] = A[i-2] / 4
#     summa += A[i]
# print(summa)