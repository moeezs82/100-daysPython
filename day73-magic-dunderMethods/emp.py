from typing import Any


class Employee:
    def __init__(self, name) -> None:
        self.name = name
        self.salary = 0

    def __len__(self) -> int:
        i=0
        for c in (self.name):
            i+=1
        return i
    
    # will on print 
    def __str__(self) -> str:
        return f"The name of the employee is {self.name} using __str__()"
    
    # this is alternative to __str__
    def __repr__(self) -> str:
        return f"Employee('{self.name}')"
    
    def __call__(self, salary) -> None:
        self.salary = salary