class CusMath:
    def __init__(self, num) -> None:
        self.num = num

    def addToNum(self, n):
        self.num = self.num+n

    @staticmethod
    def add(a, b):
        return a+b
    
#static method can be called directly with or without any instance
result = CusMath.add(1, 2)
print(result)

inst = CusMath(5)
print(inst.add(1, 2))