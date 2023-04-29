# All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.
class Employee:
    def __init__(self, name, salary: int) -> None:
        self.name = name
        self.__salary = salary  # An indication of private variable
    def myInfo(self):
        print(f"name is {self.name} and salary is {self.__salary}")

    def __salaryUpdate(self):
        print(f"current salary is {self.__salary} will be updated next month")

moeez = Employee("Moeez", 50000)
print(moeez.name)
# print(moeez.__salary)  # can not be accessed
print(moeez._Employee__salary)

moeez.myInfo()

moeez._Employee__salaryUpdate()

