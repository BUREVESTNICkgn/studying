"""

1.26 Создать класс Angle для работы с углами на плоскости, 
задаваемыми величиной в градусах и минутах.
Обязательно должны быть реализованы:
перевод в радианы✓, приведение к диапазону 0-360✓, 
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
            self.degree = int(degree)
            self.minute = int(minute)
    def decimal_degrees(self):
        return self.degree + self.minute / 60
    def radian(self):
        rad1 = self.degree * math.pi / 180 
        rad2 = self.minute * math.pi / 10800
        return rad1 + rad2
    def re_dd(self):
        degrees = math.trunc(self.decimal_degrees())
        minutes = math.trunc((self.decimal_degrees() - degrees) * 60)
        return degrees, minutes
    def sin(self):
        return math.sin(self.radian())

a = input('A: ')
b = input('B: ')
s = Angle(a, b)
print(s.radian())
print(s.decimal_degrees())
print(s.re_dd())
print(s.sin())

"""
https://en.wikipedia.org/wiki/Decimal_degrees

"""