import numpy as np
from PIL import Image
import argparse


parser = argparse.ArgumentParser(description="Script to crop image from Canva for new 4:5 Instagram posts.")

parser.add_argument('image_file', type=str, help="Image to crop")
parser.add_argument('row_number', type=int, help="Row Number (top to bottom)")
args = parser.parse_args()


full_image = np.array(Image.open(args.image_file))
row_number = args.row_number

width = 1000
height = 1350
margin = 60
# 3036

row_image = full_image[height*(row_number-1):height*row_number,:,:]
row_image = row_image[:,:3060,:]

print(row_image.shape)

for i in range(3):
    img_to_save = Image.fromarray(row_image[:,(i*width):((i+1)*width)+margin,:])
    img_to_save.save(f'imagem{i+1}.png')
