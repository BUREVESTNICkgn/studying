"""

1.26 Создать класс Angle для работы с углами на плоскости, 
задаваемыми величиной в градусах и минутах.
Обязательно должны быть реализованы:
перевод в радианы✓, приведение к диапазону 0-360✓, 
увеличение и уменьшение угла на заданную величину,
получение синуса✓, сравнение углов.

"""

import math
import PyQt5

"""

class OperOnDegrees:
    def __init__(self, degree, minute):
        self.degree = int(degree)
        self.minute = int(minute)
        pass

    def __add__(self, other):
        # new1 = OperOnDegrees(self.degree, self.minute)
        # new2 = OperOnDegrees(self.degree, self.minute)
        # new1.degree += other.degree
        # new1.minute += other.minute
        # return new1, new2
        d = other.getMin
        return OperOnDegrees(self.degree + d)

    def getMin(self):
        return float(self.degree)

    def __sub__(self, other):
        pass

    def transfer(self):
        if self.minute >= 60:
            order_minute = self.minute // 60
            self.minute = self.minute - (order_minute * 60)
            self.degree += order_minute
        return self.degree, self.minute

    def dif(self):
        pass

""" 

class Angle:
    """
    Данный класс позволяет рабоать с градусами и минутами (DM), радианами
    десятичными градусами (DD), а так же вычеслять синус

    """

    def __init__(self, degree, minute):
        global flag
        flag = True
        if str(degree).isnumeric() == False or str(minute).isnumeric() == False:  # noqa: E712
            flag = False
        else:
            self.degree = int(degree)
            self.minute = int(minute)
            # self.degree_op = int(degree_op)
            # self.minute_op = int(minute_op)

    def decimal_degrees(self):
        return math.degrees(self.radian())

    def radian(self):
        rad1 = self.degree * math.pi / 180
        rad2 = self.minute * math.pi / 10800
        return rad1 + rad2

    def re_dd(self):
        degrees = math.trunc(self.decimal_degrees())
        minutes = math.trunc((self.decimal_degrees() - degrees) * 60)
        return degrees, minutes

    def transfer(self):
        if self.minute >= 60:
            order_minute = self.minute // 60
            self.minute = self.minute - (order_minute * 60)
            self.degree += order_minute
        return self.degree, self.minute
    
    def sin(self):
        """sin(rad)"""
        return math.sin(self.radian())
    
    def plus(self, degree_op, minute_op):
        return self.degree + int(degree_op), self.minute + int(minute_op)
    
    def minus(self, degree_op, minute_op):
        return self.degree - int(degree_op), self.minute - int(minute_op)
        


a = input('A: ')
b = input('B: ')
# c = input('С: ')
# d = input('D: ')
s = Angle(a, b)
# gg = OperOnDegrees(a, b)
# print(gg.transfer())
print(s.transfer())
print(s.radian())
print(s.decimal_degrees())
print(s.re_dd())
# print(s.re2_dd())
print(s.sin())
# f = OperOnDegrees(a, b)
# h = OperOnDegrees(c, d)
# print(f + h)
print(s.plus(5, 7))

"""
https://en.wikipedia.org/wiki/Decimal_degrees

"""
