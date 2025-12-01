import numpy as np
from PIL import Image
import argparse


parser = argparse.ArgumentParser(
    description="Script to crop image from Canva for new 4:5 Instagram posts."
)

parser.add_argument("image_file", type=str, help="Image to crop")
parser.add_argument("row_number", type=int, help="Row Number (bottom to top)")
args = parser.parse_args()


full_image = np.array(Image.open(args.image_file))
row_number = args.row_number - 1

margin_horizontal = 65
height = 1350
width = 1080
visble_width = width - margin_horizontal

row_image = full_image[
    full_image.shape[0]
    - height * (row_number + 1) : full_image.shape[0]
    - height * (row_number),
    :,
    :,
]

start_point = 0
for i in range(3):
    end_point = start_point + width
    img_to_save = Image.fromarray(row_image[:, start_point:end_point, :])
    img_to_save.save(f"imagem{row_number}-{3-i}.png")

    start_point = end_point - margin_horizontal
