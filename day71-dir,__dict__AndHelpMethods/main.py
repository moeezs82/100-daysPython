x=[1,2,3]
# dir(): The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object.
print(dir(x))

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

p = Person("Moeez", 23)
# __dict__: The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection.
print(p.__dict__)

# help(): The help() function is used to get help documentation for an object, including a description of its attributes and methods.
print(help(Person))