class Shape:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__(radius, radius)
        self.radius = radius
    
    def area(self):
        # as area of circle is pi*r2 and we already pass radius on shape whose area method is returning multiplication of 2 sides
        return 3.14*super().area()
    
rec = Shape(4,6)
print(rec.area())

cir = Circle(3)
print(cir.area())

