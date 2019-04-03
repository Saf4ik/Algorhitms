# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


res = [0 for x in range(8)]
for num in range(2,100):
    for digit in range(2, 10):
        if num % digit == 0:
            res[digit - 2] += 1

for i in range(len(res)):
    print(f'{i+2} - {res[i]}')