# 1.5 Поле first – дробное положительное число, цена товара; 
# поле second – целое положительное число, количество единиц товара.
# Реализовать метод cost() – вычисление стоимости товара.


class table:
    def __init__(self, first, second):
        global flag 
        flag = True
        if str(first).isnumeric() == False:
            print('Не корректный ввод')
            flag = False
        else:
            self.first = float(first)
            self.second = int(second)
            
    def cost(self):
        if flag: 
            return self.first * self.second
        else:
            pass

first = input('Введите цену: ')
second = input('Введите кол-во: ')
f = table(first, second)
print(f.cost())