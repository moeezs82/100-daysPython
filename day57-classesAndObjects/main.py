class Person:
    name = "Moeez"
    occupation = "Developer"
    netWorth = 1000000

    def info(self):
        return f"{self.name} is a {self.occupation} has net worth of {self.netWorth}"
    
moeez = Person
print(moeez.name)
print(moeez.info(moeez))

muneeb = Person()
muneeb.name = "Muneeb"
muneeb.occupation = "Autocad Engineer"
print(muneeb.info())


