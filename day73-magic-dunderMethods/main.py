from emp import Employee

e = Employee("Moeez Rajput")
print(len(e))
# print(e) # we changed the print for employee objects using __str__ or __repr__ method first check for __str__

print(str(e))
print(repr(e))
e(50000) # setting salary using __call__ method
print(e.salary)