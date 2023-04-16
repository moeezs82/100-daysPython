import os

# Get the directory of the current script file
dir_path = os.path.dirname(os.path.realpath(__file__))

folder = os.path.join(dir_path, 'data')
if(not os.path.exists(folder)):
    os.mkdir(folder)

for i in range(100):
    day_folder = f"{folder}/Day-{i+1}"
    if not os.path.exists(day_folder):
        os.mkdir(day_folder)
    for file_name in ['corrup.txt', 'corrup.mo']:
        file_path = f"{day_folder}/{file_name}"
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                # Do nothing, just create an empty file
                # Close the file after creating it
                f.close()

# to rename
for i in range(100):
    if (os.path.exists(f"{folder}/Day-{i+1}")):
        # checking if already created tutorial-.. folder than deleting it
        if (os.path.exists(f"{folder}/tutorial-{i+1}")):
            # checking if folder containing files
            for fileName in os.listdir(f"{folder}/tutorial-{i+1}"):
                file_path = os.path.join(f"{folder}/tutorial-{i+1}", fileName)
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            os.rmdir(f"{folder}/tutorial-{i+1}")
        os.rename(f"{folder}/Day-{i+1}", f"{folder}/tutorial-{i+1}")