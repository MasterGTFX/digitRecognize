from PIL import Image
import numpy as np
import csv


def convert_grayscale_to_pixels(grayscaleArray):
    temp_array = np.array(grayscaleArray[1:]).reshape((28, 28))
    pixels = np.zeros((28, 28), dtype=(int, 3))
    for ix, iy in np.ndindex(temp_array.shape):
        pixels[ix, iy] = (int(temp_array[ix, iy]), int(temp_array[ix, iy]), int(temp_array[ix, iy]))
    return pixels


def save_picture(grayscaleArray):
    pixels = convert_grayscale_to_pixels(grayscaleArray)
    # Convert the pixels into an array using numpy
    array = np.array(pixels, dtype=np.uint8)

    # Use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image.save('new.png')


with open('data/train_data.csv', 'r') as csv_data:
    reader = csv.reader(csv_data)
    which = 16
    for row in reader:
        which -= 1
        if which <= 0:
            save_picture(row)
            break
