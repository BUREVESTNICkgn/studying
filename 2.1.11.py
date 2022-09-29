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
        if str(first).isnumeric() == False or str(second).isnumeric() == False:
            flag = False
        else:
            self.first = float(first)
            self.second = float(second)
            
    def root(self):
        if flag: 
            if self.second != 0:
                return self.second/self.first 
            else:
                return print('Коэф равен нулю')
        else:
            return print('Не корректный ввод')

# y = input('y: ')
a = input('A: ')
b = input('B: ')
s = equation(a, b)
print(s.root())