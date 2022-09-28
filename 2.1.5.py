class table:
    def __init__(self, first, second):

        self.first = first
        self.second = second

    def cost(self):
        return self.first * self.second

first = float(input('Введите левую границу диапазона: '))
second = int(input('Введите правую границу диапазона: '))
f = table(first, second)
print(f.cost())