# Usage: 'python3 thumbnail-creator.py [folder/] [new_folder/] [min_height_px]'
import os
import sys
from PIL import Image

# Grab command line arguments
image_folder = sys.argv[1]
new_folder = sys.argv[2]
min_height = int(sys.argv[3])


# If the new_folder doesn't exist, create one
if not os.path.isdir(new_folder):
    os.mkdir(new_folder)

# Loop through the folder and create thumbnail image for each jpg image or png image
# Save new png images to the new folder
for filename in os.listdir(image_folder):
    root, ext = os.path.splitext(filename)

    if ext == '.png' or '.jpg':
        try:
            with Image.open(f'{image_folder}{filename}') as img:
                print(f'Original size of {filename}: {img.size}')

                # thumbnail modifies the file in place, so make a copy first
                thumbnail_img = img

                # Make the thumnail based on fixed height value
                quotient_of_w_and_h = img.size[0] / img.size[1]
                thumbnail_img.thumbnail(
                    (quotient_of_w_and_h * min_height, min_height))

                # Save the file to the new folder
                thumbnail_img.save(f'{new_folder}thumbnail-{root}.png', 'png')
                print(f'Thumbnail size of {filename}: {thumbnail_img.size}')

        except OSError as err:
            print('cannot create thumbnail', filename)
            print(err)
