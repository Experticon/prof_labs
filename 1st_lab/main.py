# Импортирование библиотеки для генерации случайных чисел
import random


def hand_input(x, type):
    if type == 1:
        n = x
        try:
            for i in range(n):
                A[i] = int(A[i])
        except ValueError:
            print("Введены неверные данные")
            exit()

        return n
    elif type == 2:
        try:
            B = list(map(int, input("Введите элементы списка в строку (целые числа): \n").split()))
            return B
        except ValueError:
            print("Введены неверные данные")
            exit()


def find_longest(size, type):
    # Самая длинная цепочка на данный момент
    long = 0
    # Самая длинная цепочка на во всём списке
    longest = 0
    # last - Индекс последнего элемента самой длинной цепочки
    last = 0
    if type == 1:
        for i in range(size):
            if A[i] % 2 == 0:
                long += 1
                if i != (size - 1):
                    continue
            # Фиксирование самой длинной цепочки
            if long > longest:
                longest = long
                if i != (size - 1):
                    last = i - 1
                else:
                    last = i
                long = 0
    elif type == 2:
        for i in range(len(A)):
            if A[i] % 2 == 0:
                long += 1
                if i != (len(A) - 1):
                    continue
            # Фиксирование самой длинной цепочки
            if long > longest:
                longest = long
                if i != (len(A) - 1):
                    last = i - 1
                else:
                    last = i
            long = 0
    return last, longest


if __name__ == '__main__':
    # Выбор ввода элементов списка
    Input_Type = int(input("Выберите тип ввода:\n 1 - Вручную, 2 - Автоматически \n"))
    Realisation_Type = int(input("Выберите реализацию:\n 1 - Без стандартной библиотеки, "
                                 "2 - Со стандартной библиотекой \n"))
    if Realisation_Type != 1 and Realisation_Type != 2:
        print("Введены неверные данные")
        exit()
    # Ручной ввод
    if Input_Type == 1:
        if Realisation_Type == 1:
            size = int(input("Введите размер списка (целое число)\n"))
            A = input("Введите элементы списка в строку (целые числа): \n").split()
            hand_input(size, Realisation_Type)
        elif Realisation_Type == 2:
            A = hand_input(0, Realisation_Type)
    # Автоматический ввод
    elif Input_Type == 2:
        size = int(input("Введите размер списка (целое число)\n"))
        try:
            A = [random.randint(1, 100) for _ in range(size)]
        except ValueError:
            print("Введены неверные данные")
            exit()
    # Ошибка ввода
    else:
        print("Введены неверные данные")
        exit()

    print("Изначальный список:")
    print(A)

    if Realisation_Type == 1:
        last, longest = find_longest(size, Realisation_Type)
    elif Realisation_Type == 2:
        last, longest = find_longest(0, Realisation_Type)

    # Удаление самой длинной цепочки в списке (Если таких несколько, удаляется самая первая попавшаяся
    for i in range(last, last - longest, -1):
        del A[i]

    print("\nКонечный список:")
    print(A)

