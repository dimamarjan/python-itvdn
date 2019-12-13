# Задание 1
# Напишите итератор, который возвращает элементы заданного списка в обратном порядке (аналог
# reversed).
# Задание 2
# Перепишите решение первого задания с помощью генератора.


def my_revers(seq):
    """Генератор, возвращающий последовательность в обратном порядке"""

    idx = len(seq) - 1

    while idx >= 0:
        yield seq[idx]
        idx -= 1


def main():
    # Перевернём строку
    my_str = "УЛЫБОК ТЕБЕ ДЕД МАКАР"
    for i in my_revers(my_str):
        print(i, end="")
    print()

    # Перевернём последовательность степеней двойки
    my_seq = [1, 2, 4, 8, 16, 35, 64, 128, 256, 512, 1024]
    for i in my_revers(my_seq):
        print(i, end='  ')


if __name__ == '__main__':
    main()