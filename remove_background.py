import os
import sys
from rembg import remove
from PIL import Image
from tqdm import tqdm

# Define your input and output directories
input_dir = 'uploads'  # Ensure this directory exists and contains your images
output_dir = 'images/output'  # Will be created if it doesn't exist

# Check if input directory exists
if not os.path.exists(input_dir):
    print(f"Error: The input directory '{input_dir}' does not exist.")
    sys.exit(1)

# Create the output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Gather all image files
files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

if not files:
    print(f"No image files found in '{input_dir}'. Please add some images and try again.")
    sys.exit(0)

print(f"Found {len(files)} images in '{input_dir}' to process.")

# Process each image
for filename in tqdm(files, desc="Removing Background"):
    input_path = os.path.join(input_dir, filename)
    output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.png')

    try:
        with Image.open(input_path) as img:
            # Convert image to RGBA to allow transparency
            img = img.convert("RGBA")

            # Use rembg to remove the background
            result = remove(img)

            # Save the processed image as PNG with transparency
            result.save(output_path, "PNG")

    except Exception as e:
        print(f"Error processing {filename}: {e}")

print("Background removal completed!")

print(f"Processed images can be found in '{output_dir}'.")
