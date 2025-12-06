#!/usr/bin/env python3
import sys
import numpy as np
from PIL import Image
from concurrent.futures import ThreadPoolExecutor


def help_msg(status):
    print("Instagram Grid Cropper")
    print("Usage:")
    print("  python main.py image.png                    # Crop all rows and all columns")
    print("  python main.py image.png row_number          # Crop all columns from specific row")
    print("  python main.py image.png row_number column_number  # Crop specific column from specific row")
    print("  python main.py --help or -h                  # Show this help message")
    sys.exit(status)

# Parse arguments based on number of arguments provided
if len(sys.argv) == 2 and (sys.argv[1] == '--help' or sys.argv[1] == '-h'):
    help_msg(0)
elif len(sys.argv) == 2:
    # python main.py image.png
    image_file = sys.argv[1]
    row_number = None  # This signals to process all rows
    specific_column = None
elif len(sys.argv) == 3:
    # python main.py image.png row_number
    image_file = sys.argv[1]
    row_number = int(sys.argv[2])
    specific_column = None
elif len(sys.argv) == 4:
    # python main.py image.png row_number column_number
    image_file = sys.argv[1]
    row_number = int(sys.argv[2])
    specific_column = int(sys.argv[3])
else:
    help_msg(1)


# Validate inputs
if specific_column is not None and (specific_column < 1 or specific_column > 3):
    raise ValueError("Column number must be between 1 and 3")

# Default values
cell_height = 1350
cell_width = 1080
total_cols = 3
margin = 65

full_image = np.array(Image.open(image_file))
image_height, image_width = full_image.shape[:2]

# Validate that image dimensions are correct
if image_height % cell_height != 0:
    raise ValueError(f"Image height ({image_height}) must be a multiple of {cell_height}")
if image_width != 3110:
    raise ValueError(f"Image width ({image_width}) must be exactly 3110")

# Calculate number of rows based on image height and cell height
total_rows = image_height // cell_height

# Validate row number if specified
if row_number is not None and (row_number < 1 or row_number > total_rows):
    raise ValueError(f"Row number must be between 1 and {total_rows} for this image")

# Determine which rows to process
if row_number is None:
    rows_to_process = range(1, total_rows + 1)
else:
    rows_to_process = [row_number]


# Function to save a single image
def save_image_task(img_array, filename):
    img = Image.fromarray(img_array)
    img.save(filename)


# Collect all image tasks to be saved
save_tasks = []

# Process each row
for current_row in rows_to_process:
    row_number_idx = current_row - 1

    # Calculate the starting and ending y-coordinates for the selected row
    start_y = image_height - cell_height * (row_number_idx + 1)
    end_y = image_height - cell_height * row_number_idx

    row_image = full_image[start_y:end_y, :, :]

    # Process each specified column
    start_point = 0
    for i in range(total_cols):
        # Determine current column number (from right to left as per original logic: 3, 2, 1)
        current_col_num = total_cols - i

        # Check if this column should be processed
        if specific_column is None or current_col_num == specific_column:
            end_point = start_point + cell_width
            img_to_save = row_image[:, start_point:end_point, :]
            filename = f"imagem{current_row}-{current_col_num}.png"

            # Add to save tasks
            save_tasks.append((img_to_save, filename))

        start_point = end_point - margin

# Execute all save tasks in parallel using ThreadPoolExecutor
with ThreadPoolExecutor() as executor:
    futures = [executor.submit(save_image_task, img_array, filename) for img_array, filename in save_tasks]

    # Wait for all tasks to complete
    for future in futures:
        future.result()