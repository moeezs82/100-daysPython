class Person:
    def __init__(self, name, occupation, netWorth):
        self.name = name
        self.occupation = occupation
        self.netWorth = netWorth
    
    def info(self):
        return f"{self.name} is a {self.occupation} has net worth of {self.netWorth}"
    

moeez = Person("Moeez", "Developer", 100000)
print(moeez.info())