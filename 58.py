"""
Имя проекта: practicum_1
Номер версии: 1.0
Имя файла: 58.py
Автор: 2020 © Ю.А. Мазкова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 10/12/2020
Дата последней модификации: 10/12/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума № 1
Задана строка символов, в которой встречается символ «.». Поставить после каждого такого символа системное время ПК.
#версия Python: 3.9.0
"""
from datetime import datetime
M = 3
list_strings = []
for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())
now = str(datetime.now())
for string in list_strings:
    print(string.replace('.', '.' + now))
