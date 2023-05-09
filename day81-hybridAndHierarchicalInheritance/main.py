# hybrid inheritance
class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def show_details(self):
    print("Name:", self.name)
    print("Age:", self.age)
    
class Person(Human):
  def __init__(self, name, age, address):
    Human.__init__(self, name, age)
    self.address = address
    
  def show_details(self):
    Human.show_details(self)
    print("Address:", self.address)
    
class Program:
  def __init__(self, program_name, duration):
    self.program_name = program_name
    self.duration = duration
    
  def show_details(self):
    print("Program Name:", self.program_name)
    print("Duration:", self.duration)
    
class Student(Person, Program):
  def __init__(self, name, age, address, program):
    Person.__init__(self, name, age, address)
    self.program = program
    
  def show_details(self):
    Person.show_details(self)
    print(f"Program: {self.program}")

s1 = Student("Muneeb", 21, "this is address", "BSC")

s1.show_details()
# end hybrid inheritance

# Hierarchical Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print("Name:", self.name)

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print("Species: Dog")
        print("Breed:", self.breed)

class Cat(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name)
        self.color = color

    def show_details(self):
        Animal.show_details(self)
        print("Species: Cat")
        print("Color:", self.color)

dog = Dog("Max", "Golden Retriever")
dog.show_details()
cat = Cat("Luna", "Black")
cat.show_details()