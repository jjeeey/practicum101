"""
Имя проекта: practicum_1
Номер версии: 1.0
Имя файла: 44.py
Автор: 2020 © Ю.А. Мазкова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 10/12/2020
Дата последней модификации: 10/12/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума № 1
Дан одномерный массив числовых значений, насчитывающий N элементов. Добавить столько элементов, чтобы элементов с положительными и отрицательными значениями стало бы поровну.
#версия Python: 3.9.0
"""
import random
N = random.randint(0,15)
arr = [random.randint(-90,190) for i in range(N)]
print(arr)
plus = 0
minus = 0
for i in range(N):
    if arr[i] >0:
        plus+=1
if plus > minus:
    for i in range(minus , plus):
        arr.append(random.randint(-90,-5))
elif plus < minus:
    for i in range(plus , minus):
        arr.append(random.randint(3,15))
print("Номер плюс: " + str(plus))
print("Номер минус: " + str(minus))
print(arr)
