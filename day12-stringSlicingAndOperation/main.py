fruit = "Mango"

print("first three chars", fruit[0:3]) # including 0 and excluding 4 index
print("first three chars", fruit[:3]) # 0 is default in start
print("first three chars", fruit[1:]) # n is default in end
print("first three chars", fruit[:]) 

print("length of", fruit, len(fruit))


# nagative 
print("first three chars", fruit[0:len(fruit)-3])
print("first three chars", fruit[0:-3]) # len(name) is default in end at start in negative case
print("first three chars", fruit[-1:-3]) # 5-1=4 and 5-3=2, 4 to 2 makes no sence
print("first three chars", fruit[-4:-1]) # 5-4=1 and 5-1=4, 1 to 4 will print