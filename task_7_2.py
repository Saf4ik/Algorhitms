# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.


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

arr = [round(r.uniform(0, 50), 2) for i in range(10)]
print(arr)
print(merge_sort(arr))