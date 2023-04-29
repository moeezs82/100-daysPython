class ParentClass:
    def parentMethod(self):
        print("This is parent class method")

class ChildClass(ParentClass):
    def childMethod(self):
        print("This is child class method")
        super().parentMethod()

class_object = ChildClass()
class_object.childMethod()
class_object.parentMethod()

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, langs: list = []):
        super().__init__(name, id)
        self.langs = langs

    
moeez = Programmer("Moeez", 234, ['python', 'php', 'javascript'])
