import os

# Get the directory of the current script file
dir_path = os.path.dirname(os.path.realpath(__file__))

print(f"file directory {dir_path}")

print(f"directory from you are running this program {os.getcwd()}")
os.chdir('/Learning')
print(f"directory changed to {os.getcwd()}")

for folders in os.listdir(os.getcwd()):
    print(folders)
    if (os.path.isdir(folders)):
        print("this is the directory")
        for folder in os.listdir(folders):
            print(folder)