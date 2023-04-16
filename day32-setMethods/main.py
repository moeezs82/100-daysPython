cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities1.union(cities2)
print(cities3)
print(cities1, cities2)

cities1.update(cities2)
print(cities1)

# same functionality as maths intersection, intersection_update, symectric_difference, symmetric_difference_update, difference, difference_update, isdisjoint, issupperset, issubset

cities2.add("Helsinki")
cities1.update({"Karachi", "Lahore"})
cities2.remove('Seoul') # this will raise an exception if item not present and .discard("Seoul") will not
print(cities1, cities2)

# pop()
# This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

# del
# del is not a method, rather it is a keyword which deletes the set entirely.

# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)

# clear():
# This method clears all items in the set and prints an empty set.

# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")