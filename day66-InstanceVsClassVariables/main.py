class Employee:
    companyName = "Apple" # class variable as it is directly associated with class
    numOfEmployees = 0 
    def __init__(self, name) -> None:
        # these are instances variable as these will be different for each instance
        self.name = name
        self.raise_amount = 0.2 
        Employee.numOfEmployees+=1

    def showDetails(self):
        print(f"name of the employee is: {self.name} and the raise amount in {self.companyName} is: {self.raise_amount}")


emp1 = Employee("Moeez")
emp1.raise_amount = 0.4
# although companyName is class property but it wil check if instance created its own property for that then it will use that otherwise class variable will use
emp1.companyName = "Apple US"
emp1.showDetails()
# is equivalent to
# Employee.showDetails(emp1)

# we can also change the class variable it self
Employee.companyName = "Samsung"

emp2 = Employee("Muneeb")
emp2.showDetails()

print(Employee.numOfEmployees)