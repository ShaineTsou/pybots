# the converter is given command like this
# Usage: 'python3 [convertName].py [folder/] [new_folder/]'
import os
import sys
from PIL import Image

# Grab second and third command line arguments
image_folder = sys.argv[1]
new_folder = sys.argv[2]

# If the new_folder doesn't exist, create one
if not os.path.isdir(new_folder):
    os.mkdir(new_folder)

# Loop through the folder and convert jpg images to png
# Save new png images to the new folder
for filename in os.listdir(image_folder):
    root, ext = os.path.splitext(filename)

    if ext == '.jpg':
        try:
            with Image.open(f'{image_folder}{filename}') as img:
                # You should check where the user actually input a folder name with a slash
                img.save(f'{new_folder}{root}.png', 'png')

        except OSError as err:
            print('cannot convert', filename)
            print(err)
