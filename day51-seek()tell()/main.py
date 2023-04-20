import os

current_dir = os.path.dirname((__file__))
print(current_dir)
with open(f'{current_dir}/file.txt', 'r') as f:
    # Move to the 10th byte in the file
    f.seek(10)

    # will tell how many bytes we have read or after how many bytes we have to read
    print(f.tell())

    # Read the next 5 bytes
    data = f.read(5)
    print(data)


with open(f'{current_dir}/file.txt', 'r') as f:
    # Read the first 10 bytes
    data = f.read(10)
    # Save the current position
    current_position = f.tell()
    # Seek to the saved position
    f.seek(current_position)

with open(f'{current_dir}/sample.txt', 'w') as f:
    f.write('Hello World!')
    # truncate whole file except first five words(bytes)
    f.truncate(5)
with open(f'{current_dir}/sample.txt', 'r') as f:
    print(f.read())
