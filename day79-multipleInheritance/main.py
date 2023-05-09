class Employee:
    def __init__(self, name) -> None:
        self.name = name

    def show(self):
        print(f"the name is {self.name}")

class Programmer:
    def __init__(self, language) -> None:
        self.language = language

    def show(self):
        print(f"the language of programmer is {self.language}")

class ProgrammerEmployee(Employee, Programmer):
    def __init__(self, name, language) -> None:
        Programmer.__init__(self, language)
        Employee.__init__(self, name)
    
# mro method resolution order first come first
print(ProgrammerEmployee.mro())

prog_emp = ProgrammerEmployee("Moeez", "Python")
prog_emp.show()