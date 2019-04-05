# 4. Определить, какое число в массиве встречается чаще всего.
import operator
import random as r

def sort_by_values(dictionary):
    return sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)


def count_numbers(array):
    count_numbers = dict()
    for n in array:
        if n in count_numbers:
            count_numbers[n] +=1
        else:
            count_numbers[n] = 1
    return count_numbers

a = [r.randint(1, 10) for i in range(r.randint(20, 30))]
print(a)

d = sort_by_values(count_numbers(a))
for i in d:
    print(f'Число {i[0]} встречается {i[1]} раз')





