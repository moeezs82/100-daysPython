class Vector:
    def __init__(self, i, j, k) -> None:
        self.i = i
        self.j = j
        self.k = k

    def __str__(self) -> str:
        return f"({self.i})i + ({self.j})f + ({self.k})k"
    
    def __add__(self, other) -> 'Vector':
        new_i = self.i + other.i
        new_j = self.j + other.j
        new_k = self.k + other.k
        return Vector(new_i, new_j, new_k)
    def __sub__(self, other) -> 'Vector':
        new_i = self.i - other.i
        new_j = self.j - other.j
        new_k = self.k - other.k
        return Vector(new_i, new_j, new_k)
    # check for other operator overload in python docs like for * we have __mul__
    
v1 = Vector(2, 5, 7)
v2 = Vector(3, 4, 1)

v3 = v1+v2
v4 = v2-v1

print(v3)
print(v4)
