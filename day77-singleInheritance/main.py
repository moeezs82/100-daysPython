class Animal:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by Animal")

class Dog(Animal):
    def __init__(self, name, species, breed) -> None:
        super().__init__(name, species)
        self.breed = breed

    def make_sound(self):
        print('Bark!')

class Cat(Animal):
    def __init__(self, name, species, breed) -> None:
        super().__init__(name, species)
        self.breed = breed
    def make_sound(self):
        print("Meow!")

dog = Dog("Ash", "Dog", "Husky")
dog.make_sound()
cat = Cat("Puffy", "Cat", "Persian")
cat.make_sound()

animal = Animal("Dog", "Dog")
animal.make_sound()