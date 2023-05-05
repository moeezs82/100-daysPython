import os
from PIL import Image

# Get the directory of the current script file
cur_dir = os.path.dirname(os.path.realpath(__file__))

def images_to_pdf(images_path, pdf_path):
    rgb_images = []

    if os.path.exists(images_path):
        print("exists")

    target_files = []
    for path, subdirs, files in os.walk(images_path):
        for name in files:
            if name.lower().endswith((".jpeg", ".png", ".jpg")):
                target_files.append(os.path.join(path, name))

    for image in target_files:
        if os.path.isfile(image) and image.endswith((".jpeg", ".png", ".jpg")):
            print(image)
            image_open = Image.open(image)
            rgb_images.append(image_open.convert('RGB'))
    # here we start with first array and at append we exclude that
    rgb_images[0].save(pdf_path, save_all=True, append_images=rgb_images[1:])
            

# Example usage:
images_path = os.path.join(cur_dir, 'images')
pdf_path = f'{cur_dir}/output.pdf'

images_to_pdf(images_path, pdf_path)
