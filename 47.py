"""
Имя проекта: practicum_1
Номер версии: 1.0
Имя файла: 47.py
Автор: 2020 © Ю.А. Мазкова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 10/12/2020
Дата последней модификации: 10/12/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума № 1
Дан одномерный массив числовых значений, насчитывающий N элементов. Исключить из массива элементы, принадлежащие промежутку [B; C].
#версия Python: 3.9.0
"""
import random

N = random.randint(1,25)
arr = [random.randint(-100,100) for i in range(N)]
print(arr)
B = random.randint(1,10)
print("B= " + str(B))
C = random.randint(1,10)
print("C= " + str(C))

arr[B : C] = []
print(arr)
