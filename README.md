# Canva Instagram Grid Cropper

A lightweight Python script that takes a full-sized Canva image (3240x7560 px) designed for a 3-column Instagram grid and slices a horizontal row into 3 separate 4:5 format images for posting. Perfect for puzzle feeds or mosaic-style Instagram layouts.

## 🔧 Features

- Supports images exported from Canva with dimensions optimized for Instagram (3240×7560 px)
- Crops a specific horizontal row (out of multiple) into 3 vertical 4:5 images
- Automatic margin handling to avoid overlap
- Saves output images as `imagem1.png`, `imagem2.png`, and `imagem3.png`


## 🚀 Usage

Make sure you have Python 3 and the required libraries installed:

```bash
pip install numpy pillow
```

Then run the script like this:

```bash
python main.py myimage.png 2
```

This will crop the **second row** (from top to bottom) of the image and generate 3 cropped images ready to post to Instagram.

## 🧠 Example

If you designed a 3x5 Canva grid (3 columns, 5 rows = 3240×6750 px), you can use this tool to extract each row for separate posting. Just call the script once per row, changing the row number accordingly.

## 📁 Output

- `imagem1.png` – left third of the row
- `imagem2.png` – center third of the row
- `imagem3.png` – right third of the row
