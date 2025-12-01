# Canva Instagram Grid Cropper

A lightweight Python script that takes a full-sized Canva image (3110×6750 px)designed for a 3-column Instagram grid and slices a horizontal row into 3 separate 4:5 format images for posting. Perfect for puzzle feeds or mosaic-style Instagram layouts.

## Features

- Supports images exported from Canva with dimensions optimized for Instagram(3110×6750 px)
- Crops a specific horizontal row (out of multiple) into 3 vertical 4:5 images
- Automatic margin handling to avoid overlap


## Usage

Make sure you have Python 3 and the required libraries installed:

```bash
pip install -r requirements.txt
```

Then run the script like this:

```bash
python main.py myimage.png 2
```

This will crop the **second row** (from bottom to top) of the image and generate 3 cropped images ready to post to Instagram.

## Output

- `imagem<row_number>-1.png` – right third of the row
- `imagem<row_number>-2.png` – center third of the row
- `imagem<row_number>-3.png` – left third of the row
