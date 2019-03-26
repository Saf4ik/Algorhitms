# 10. Дан файл  с логинами и паролями. Найдите топ10 самых популярных паролей.

import operator


def parse_passwords(data):
    res = []
    for i in data.split("\n"):
        res.append(i.split(";")[1])
    return res


def count_passwords(passwords):
    passwords_count = dict()
    for p in passwords:
        if p in passwords_count:
            passwords_count[p] +=1
        else:
            passwords_count[p] = 1
    return passwords_count


def sort_by_values(dictionary):
    return sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)


filename = input("Input filename: ")
top = int(input("Input top N: "))


with open(filename) as f:
    d = sort_by_values(count_passwords(parse_passwords(f.read())))
    for i in d[:top]:
        print(i)