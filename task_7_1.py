# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).


import random as r


def bubble_sort(A):
    for bypass in range(1,len(A)):
        is_sorted = True
        for k in range(0,len(A)-bypass):
            if A[k] > A[k+1]:
                is_sorted = False
                A[k], A[k+1] = A[k+1], A[k]
        if is_sorted:
            break
    return A


arr = [r.randint(-100,100) for i in range(15)]
# arr = [1, 2, 3, 4, 5]
print(arr)
print(bubble_sort(arr))
