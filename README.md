# Canva Instagram Grid Cropper

A lightweight tool that takes a full-sized Canva image (3110×6750 px) designed for a 3-column Instagram grid and slices a horizontal row into 3 separate 4:5 format images for posting. Perfect for puzzle feeds or mosaic-style Instagram layouts.

This repository contains two versions of the tool organized in separate directories:

## Project Structure

- `/cli` - Contains the Python command-line version
- `/web` - Contains the browser-based web version

## Python Version (Terminal)
A command-line script for terminal usage located in the `/cli` directory.

### Features
- Supports images exported from Canva with dimensions optimized for Instagram (3110×6750 px)
- Crops a specific horizontal row (out of multiple) into 3 vertical 4:5 images
- Automatic margin handling to avoid overlap

### Usage

Make sure you have Python 3 and the required libraries installed:

```bash
cd cli
pip install -r requirements.txt
```

Then run the script like this:

```bash
python icrop.py myimage.png 2
```

This will crop the **second row** (from bottom to top) of the image and generate 3 cropped images ready to post to Instagram.

#### Output

- `imagem<row_number>-1.png` – right third of the row
- `imagem<row_number>-2.png` – center third of the row
- `imagem<row_number>-3.png` – left third of the row

## Web Version (Browser UI)

A browser-based UI available at [Instagram-Grid-Cropper](https://rodrig20.github.io/Instagram-Grid-Cropper/) located in the `/web` directory.

### Features
- No installation required
- Works directly in your browser
- Responsive UI for image processing

### Usage

1. Navigate to the `/web` directory
2. Open `index.html` in your browser, or host it on a web server
3. Upload your image file
4. Select the row number to crop
5. Download the resulting cropped images

No installation required - works directly in your browser!
