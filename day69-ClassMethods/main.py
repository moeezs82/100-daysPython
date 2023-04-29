class Employee:
    company = "Test Company"
    # these are instancees method 
    def show(self): 
        print(f"the name is {self.name} and company is {self.company}")

    @classmethod
    def changeCompany(cls, newName):
        cls.company = newName

e1 = Employee()
e1.name = "Moeez"
e1.show()

Employee.changeCompany("Tesla")
e1.show()
# or 
e1.changeCompany("Apple")
e1.show()