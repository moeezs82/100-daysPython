a = None
b = None

print(a is b) # exact location of object in memory
print(a is None) # exact location of object in memory
print(a == b) # value

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b) # false
print(a == b) # true

# In these cases, a and b are both pointing to the same object in memory, so is and == both return True.
# 
# For mutable objects such as lists and dictionaries, is and == can behave differently. In general, you should use == when you want to compare the values of two objects, and use is when you want to check if two objects are the same object in memory.