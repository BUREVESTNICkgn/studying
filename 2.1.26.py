"""

1.26 Создать класс Angle для работы с углами на плоскости, 
задаваемыми величиной в градусах и минутах.
Обязательно должны быть реализованы:
перевод в радианы, приведение к диапазону 0-360, 
увеличение и уменьшение угла на заданную величину,
получение синуса, сравнение углов.

"""

import math

class Angle:
    def __init__(self, degree, minute):
        global flag 
        flag = True
        if str(degree).isnumeric() == False or str(minute).isnumeric() == False:
            flag = False
        else:
            self.degree = degree
            self.minute = minute

    def radian(self):
        if flag:
            