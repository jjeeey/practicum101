"""
Имя проекта: practicum_1
Номер версии: 1.0
Имя файла: 28.py
Автор: 2020 © Ю.А. Мазкова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 10/12/2020
Дата последней модификации: 10/12/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума № 1
Составить алгоритм и программу для реализации логических операций «И» и «ИЛИ» для двух переменных.
#версия Python: 3.9.0
"""
V = int(input("Скорость автомобиля:"))
t = int(input("Температура на улице:"))
if (V > 80 and t<=0) or (V > 60 and t <= -10):
    print("Едь аккуратно, гололед")
    V = V / 2
    print("Рекомендуемая скорость езды:", V)
elif (V > 120 and t>=30) or (V > 100 and t >= 45):
    print("Едь медленно, машина может заглохнуть")
    V = V / 3
    print("Рекомендуемая скорость езды:", V)
else:
    print("Условия для езды нормальные,едь спокойно")
