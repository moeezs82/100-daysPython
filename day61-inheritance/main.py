class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"the name of employee: {self.id} is {self.name}")

class Programmer(Employee):
    def __init__(self, name, id, languages: list = []):
        super().__init__(name, id)
        self.languages = languages
    def showLanguage(self):
        if(len(self.languages)):
            print(f"{self.name} has expertise over {self.languages}")
        else:
            print("The default language is Python")

moeez = Employee("Moeez", 24)
moeez.showDetails()

moeezProgrammer = Programmer("moeez", 12, ['php', 'python', 'javaScript'])
moeezProgrammer.showLanguage()
