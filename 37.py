"""
Имя проекта: practicum_1
Номер версии: 1.0
Имя файла: 37.py
Автор: 2020 © Ю.А. Мазкова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 10/12/2020
Дата последней модификации: 10/12/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума № 1
Дан одномерный массив числовых значений, насчитывающий N элементов. Сумму элементов массива и количество положительных элементов поставить на первое и второе место.
#версия Python: 3.9.0
"""
import numpy as np
import array
import random
N = int(input("Введите количество элементов массива:"))
A = [random.randint(-20, 20) for i in range(0, N)]
print(A)
B = 0
cym = np.sum(A)
C = np.size(A)
for i in range(N):
    if A[i] >= 0:
        B += A[i]
(A.insert(0, B))
(A.insert(1, C))
print(A)
