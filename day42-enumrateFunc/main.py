marks = [12, 56, 32, 98, 12,  45, 1, 4]
name = "Moeez Rajput"

# index = 0
# for mark in marks:
#   print(mark)
#   if(index == 3):
#     print("Moeez, awesome!")
#   index +=1

for index, item in enumerate(name):
  print(f"{item} is at index: {index}")

for index, mark in enumerate(marks, start=1): # start will tell where to start index by defult 1
  print(mark)
  if(index == 3):
    print("Moeez, awesome!")