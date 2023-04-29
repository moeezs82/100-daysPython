class Employee:
    def __init__(self, name: str, salary: int) -> None:
        self.name = name
        self.salary = salary

    def showInfo(self):
        print(f"name: {self.name} salary: {self.salary}")

    @classmethod
    def fromStr(cls, string: str):
        return cls(string.split('-')[0], int(string.split('-')[1]))

e1 = Employee("Moeez", 12000)

string = "Muneeb-12000"
e2 = Employee(string.split('-')[0], int(string.split('-')[1]))

string1 = "Najibullah-12000"
e3 =  Employee.fromStr(string1)

e1.showInfo()
e2.showInfo() 
e3.showInfo()