# 2. Компьютер загадывает число от 1 до n. У пользователя k попыток отгадать.
# После каждой неудачной попытки компьютер сообщает меньше или больше загаданное число.
# В конце игры текст с результатом (или “Вы угадали”, или “Попытки закончились”).

import random as r

print("Угадайте число от 0 до 100")
answer = int(r.randint(0, 100))
#print(answer)
userAnswer = int(input("Введите число: "))
maxTrycount = 7
tryCount = 0
while maxTrycount - tryCount != 0:
    tryCount += 1
    if userAnswer == answer:
        print("Вы угадали")
        break
    elif userAnswer > answer:
        if tryCount == maxTrycount:
            print("Слишком большое. Вы проиграли")
            break
        else:
            print(f"Слишком большое. У вас осталось {maxTrycount - tryCount} попыток.")
    else:
        if tryCount == maxTrycount:
            print("Слишком маленькое. Вы проиграли")
            break
        else:
            print(f"Слишком маленькое. У вас осталось {maxTrycount - tryCount} попыток.")
    userAnswer = int(input("Попробуйте еще раз. Введите число: "))