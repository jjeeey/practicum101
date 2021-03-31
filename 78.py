"""
Имя проекта: practicum_1
Номер версии: 1.0
Имя файла: 78.py
Автор: 2020 © Ю.А. Мазкова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 20/03/2021
Дата последней модификации: 20/03/2021
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума № 1
Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Разделить элементы каждой строки на элемент этой строки с наибольшим значением.
#версия Python: 3.9.0
"""
import random

N = 6
M = 5

L = 3


def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(0, 9))

    return col


def get_matrix(row, column):
    matrix = []
    for i in range(0, row):
        matrix.append(get_row(column))

    return matrix


def print_matrix(matrix):
    i = 0
    while i < len(matrix):
        j = 0
        row = matrix[i]
        while j < len(row):
            column = row[j]
            print(column, end=' ')
            j += 1

        print()
        i += 1


A = get_matrix(N, M)
print("Исходная матрица:")
print_matrix(A)

i = 0
while i < len(A):
    j = 0
    max_element = max(A[i])
    while j < len(A[i]):
        A[i][j] /= max_element
        A[i][j] = round(A[i][j], 1)
        j += 1

    i += 1

print("Модифицированная матрица:")
print_matrix(A)
