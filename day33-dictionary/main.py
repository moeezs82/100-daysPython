info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info) 
# print(info.keys())
# print(info.values())

# for key in info.keys():
#   print(f"The value corresponding to the key {key} is {info[key]}")

# print(info.get('name2')) # will print none if the key is not found
# print(info['name2'])    # will throw an exception if the key is not found

print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}") 
  