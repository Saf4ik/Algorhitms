# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def oddAndEven(number):
    oddCount = 0
    for i in number:
        if int(i) % 2 == 0:
            oddCount += 1
    return oddCount


n = input("Input positive integer: ")
res = oddAndEven(n)
print(f"Odd digits: {res}, even digits: {len(n) - res}")