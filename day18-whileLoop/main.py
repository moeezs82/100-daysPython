# i = int(input("Enter the number: "))
# print(i)
# while(i<=38):
#   i = int(input("Enter the number: "))
#   print(i)

# print("Done with the loop")

# count = 5
# while (count > 0):
#   print(count)
#   count = count - 1
# else:
#   print("I am inside else")

while True:
  number = int(input("To Exit this loop Enter a -ve number or 0: "))
  print(number)
  if not number > 0:
    break
