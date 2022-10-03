"""
1.11 Линейное уравнение у = Ах + В. Поле first – дробное число, коэффициент А; 
поле second – дробное число, коэффициент В. 
Реализовать метод root() – вычисление корня линейного уравнения. 
Метод должен проверять неравенство коэффициента В нулю.

"""
class equation:
    def __init__(self, first, second):
        global flag 
        flag = True
        if self.isfloat(first) == False or self.isfloat(second) == False:
            flag = False
        else:
            self.first = float(first)
            self.second = float(second)
            
    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
            
    def root(self):
        if flag: 
            if self.second != 0:
                return -self.second/self.first 
            else:
                return print('Коэф равен нулю')
        else:
            return print('Не корректный ввод')

# y = input('y: ')
a = input('A: ')
b = input('B: ')
s = equation(a, b)
print(s.root())