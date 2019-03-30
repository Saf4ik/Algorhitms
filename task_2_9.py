# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
#    Вывести на экран это число и сумму его цифр.


n = int(input("Input positive integer or 0 for exit:"))
maxS = 0
maxM = 0
while n != 0:
    m = n
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    if s > maxS:
        maxS = s
        maxM = m
    n = int(input("Input positive integer or 0 for exit:"))
print(f"Number {maxM}, has a maximum sum of digits: {maxS}")