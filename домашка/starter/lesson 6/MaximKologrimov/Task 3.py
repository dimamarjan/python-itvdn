# Задание 3
# Пусть на каждую ступеньку лестницы можно стать с предыдущей или переступив через одну.
# Определите, сколькими способами можно подняться на заданную ступеньку.

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

x = int(input('На какую ступеньку нужно подняться: '))
print('Кол-во способов подняться на заданную ступеньку:', fib(x))