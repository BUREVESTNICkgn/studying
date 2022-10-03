class OperOnDegrees:
    
    def __init__(self, qwe):
        self.qwe = qwe

    def __add__(self, other):
        return OperOnDegrees(self.qwe + other.qwe)
    
    def get(self):
        return self.qwe
    
a = OperOnDegrees(5)
b = OperOnDegrees(12)

c = a + b

print(c.get())