# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке
# и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "Error: ZeroDivision"
    return a / b


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


while True:
    a = input("Input operators: ")
    if a == "0":
        print("See you later")
        break
    if a not in operations:
            print("Error: WrongSign(allowed: +, -, *, / and 0 for exit)")
            continue
    b = int(input("Input first number: "))
    c = int(input("Input second number: "))

    print(operations[a](b, c))