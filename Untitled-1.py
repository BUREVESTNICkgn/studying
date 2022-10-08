class OperOnDegrees:
    
    # def __init__(self, qwe):
    #     self.qwe = qwe

    # def __add__(self, other):
    #     return OperOnDegrees(self.qwe + other.qwe)
    

    def __init__(self, degree, minute):
        self.degree = int(degree)
        self.minute = int(minute)
        pass

    def __add__(self, other):
        new1 = OperOnDegrees(self.degree, self.minute)
        new1.degree += other.degree
        new1.minute += other.minute
        return new1
    
    def get(self):
        return self.degree, self.minute
    
a = OperOnDegrees(5, 4)
b = OperOnDegrees(12, 5)

c = a + b

print(c.get())