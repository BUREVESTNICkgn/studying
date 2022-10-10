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
        new1 = OperOnDegrees(self.degree, self.minute)
        new1.degree += other.degree
        new1.minute += other.minute
        return new1
        # d = other.getMin
        # return OperOnDegrees(self.degree + d)

    def getMin(self):
        return float(self.degree)

    def __sub__(self, other):
        pass

    def transfer(self):
        while self.minute >= 60:
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
        self.degree = int(degree)
        self.minute = int(minute)
        # if str(degree).isnumeric() == False or str(minute).isnumeric() == False:  # noqa: E712
        #     flag = False
        # else:
        #     self.degree = int(degree)
        #     self.minute = int(minute)
        #     # self.degree_op = int(degree_op)
        #     # self.minute_op = int(minute_op)
        
    def __add__(self, other):
        new = Angle(self.degree, self.minute)
        new.degree += other.degree
        new.minute += other.minute
        return self.transfer(new.degree, new.minute)
    
    def __sub__(self, other):
        new = Angle(self.degree, self.minute)
        new.degree -= other.degree
        new.minute -= other.minute
        return self.transfer(new.degree, new.minute)

    def decimal_degrees(self):
        return math.degrees(self.radian())

    def radian(self):
        rad1 = self.degree * math.pi / 180
        rad2 = self.minute * math.pi / 10800
        return rad1 + rad2

    def re_dd(self):
        degrees = math.trunc(self.decimal_degrees())
        minutes = math.trunc(abs((self.decimal_degrees() - degrees)) * 60)
        return degrees, minutes

    def transfer(self, degree_t = 0, minute_t = 0):
        while abs(minute_t) >= 60:
            order_minute = minute_t // 60
            minute_t = minute_t - (order_minute * 60)
            degree_t += order_minute
        return degree_t, minute_t
    
    def sin(self):
        """
        sin(<rad>)
        
        """
        return math.sin(self.radian())
    
    def plus(self, degree_op: int, minute_op: int):
        a = self.degree + degree_op
        b = self.minute + minute_op
        return self.transfer(a, b)
    
    def minus(self, degree_op: int, minute_op: int):
        a = self.degree - degree_op
        b = self.minute - minute_op
        return self.transfer(a, b)
    
    def get(self):
        return self.degree, self.minute
    
    # def comparison(self, degree_op, minute_op):
    #     if self.radian():
    #     pass
    

class Triangle(Angle):
    def __init__(self, degree, minute, length):
        super().__init__(degree, minute)
        self.length = length
    
        
        
        


a = input('A: ')
b = input('B: ')
s = Angle(a, b)
print(f'Перевод к стандартному виду: {s.transfer()}')
print(f'Перевод в радинаы: {s.radian()}')
print(f'Перевод в десятичные градусы: {s.decimal_degrees()}')
print(f'Перевод из DD в DM: {s.re_dd()}')
print(f"Синус угла {a}°{b}': {s.sin()}")
f = Angle(45, 45)
h = Angle(90, -560)
y = f + h
print(y)
print(s.plus(5, 7))
print(s.minus(5, 7))


"""
https://en.wikipedia.org/wiki/Decimal_degrees

"""
