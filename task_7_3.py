# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
#    Медианой называется элемент ряда, делящий его на две равные части:
#         в одной находятся элементы, которые не меньше медианы,
#         в другой – не больше медианы.
#    Задачу можно решить без сортировки исходного массива.
#    Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

import random as r


def merge(A:list, B:list):
    C = [0]*(len(A) + len(B))
    i = k = n = 0
    while i <(len(A)) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
        else:
            C[n] = B[k]
            k += 1
        n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1; n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1; n += 1
    return C


def merge_sort(A:list):
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    left = A[:mid]
    right = A[mid:]

    merge_sort(left)
    merge_sort(right)
    C = merge(left, right)
    for i in range(len(A)):
        A[i] = C[i]
    return A

m = int(input("Input m: "))

arr = [r.randint(0,30) for i in range(2*m+1)]
s = merge_sort(arr)
print(s)
print(s[len(s) // 2])