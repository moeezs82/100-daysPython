import os

# Get the directory of the current script file both are same but above one is preferable
current_dir = os.path.dirname(os.path.realpath(__file__))
# current_dir = os.path.dirname(__file__)

# READING A FILE

# f = open(f'{current_dir}\myfile.txt', 'r')
# # print(f)
# text = f.read()
# print(text)
# f.close()

# WRITING A FILE

f = open(f'{current_dir}\myfile.txt', 'a')
f.write('Hello, world!')
f.close()

# if we are using with then it automatically closes the file
with open(f'{current_dir}\myfile.txt', 'a') as f:
  f.write(" Hey I am inside with")