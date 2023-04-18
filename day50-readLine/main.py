import os

current_dir = os.path.dirname(os.path.realpath(__file__))

# f = open(f"{current_dir}\myFile.txt")
# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         break
f = open(f"{current_dir}\marks.txt")
i=0
while True:
    i+=1
    line = f.readline()
    if not line:  # we are spliting line below and as last line is empty
        break
    m1 = int(line.split(',')[0])
    m2 = int(line.split(',')[1])
    m3 = int(line.split(',')[2])
    print(f'Marks of student: {i} in maths is: {m1*2}')
    print(f'Marks of student: {i} in English is: {m2*2}')
    print(f'Marks of student: {i} in sst is: {m3*2}')

with open(f'{current_dir}/newFile.txt', 'w') as f:
    lines = ['line 1\n', 'line 2\n', 'line 3\n', 'line 4\n', 'line 5\n']
    f.writelines(lines)

lines = ['line 1', 'line 2', 'line 3', 'line 4', 'line 5']
with open(f'{current_dir}/newFile2.txt', 'w') as f:
    for line in lines:
        f.write(line+'\n')