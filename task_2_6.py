# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.

import random as r

print("Угадайте число от 0 до 100")
answer = int(r.randint(0, 100))
#print(answer)
userAnswer = int(input("Введите число: "))
maxTrycount = 10
tryCount = 0
while maxTrycount - tryCount != 0:
    tryCount += 1
    if userAnswer == answer:
        print("Вы угадали")
        break
    elif userAnswer > answer:
        if tryCount == maxTrycount:
            print(f"Слишком большое. Вы проиграли. Правильный ответ: {answer}")
            break
        else:
            print(f"Слишком большое. У вас осталось {maxTrycount - tryCount} попыток.")
    else:
        if tryCount == maxTrycount:
            print(f"Слишком маленькое. Вы проиграли. Правильный ответ: {answer}")
            break
        else:
            print(f"Слишком маленькое. У вас осталось {maxTrycount - tryCount} попыток.")
    userAnswer = int(input("Попробуйте еще раз. Введите число: "))