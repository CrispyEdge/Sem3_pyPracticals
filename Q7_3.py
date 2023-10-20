class Numbers:
    MULTIPLIER = 5
    def __init__(self, x, y):
        self.x=x
        self.y=y
    
    def add(self):
        return self.x + self.y
    
    @classmethod
    def multiply(cls, a):
        return cls.MULTIPLIER * a
    @staticmethod
    def subtract(b, c):
        return b-c
    
    @property
    def value(self):
        return (self.x, self.y)
    @value.setter
    def value(self, d):
        self.x = d[0]
        self.y = d[1]
        
    @value.deleter
    def value(self):
        self.x = None
        self.y = None
    
    
    
ob = Numbers(10, 20)
print("add", ob.add())
print("Multiply", Numbers.multiply(10))
print("Subtract", Numbers.subtract(40,20))

ob.value = (200, 300)
print(ob.value)
del ob.value
print(ob.value)

