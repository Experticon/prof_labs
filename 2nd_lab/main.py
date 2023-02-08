import sys
import numpy as np
import random


def find_result(mtx):
    # Переворачиваем матрицу (столбцы и строки меняются местами)
    reverse_mtx = mtx.transpose()
    # Создаём матрицу с абсолютными значениями
    abs_mtx = np.abs(reverse_mtx)
    # Суммируем элементы столбцов (ныне строк)
    sums = np.sum(abs_mtx, axis=1)
    # Находим индекс столбца с максимальной суммой
    row_idx = np.argmax(sums)
    # Находим минимальное число в абсолютной матрице по индексу столбца
    result = np.min(abs_mtx[row_idx])
    return result


def output_result(N, M, mtx, el):
    # Открытие и запись файла
    my_file = open("output.txt", "w")
    my_file.write("Количество строк: " + str(N) + "\n")
    my_file.write("Количество столбцов: " + str(M) + "\n")
    my_file.write("Начальная матрица:\n" + str(mtx) + "\n")
    my_file.write("Результат: " + str(el) + "\n")
    # Закрытие файла
    my_file.close()


if __name__ == '__main__':

    # Генерирует строки и столбцы матрицы
    N = random.randint(1, 100)
    M = random.randint(1, 100)

    # mtx = np.random.random((N, M))

    # генерирует элементы матрицы в пределах заданного размера
    mtx = np.random.randint(100, size=(N, M))

    # Вывод без сокращений
    np.set_printoptions(threshold=sys.maxsize)

    # Находим минимальный элемент в матрице в столбце с максимальной суммой
    el = find_result(mtx)
    output_result(N, M, mtx, el)
