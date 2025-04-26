from skimage.io import imread, imsave
import os

def load_image():
    
    path = input("Enter the path to the image file: ").strip()
    if not os.path.exists(path):
        print("Error: File does not exist.")
        return None
    try:
        image = imread(path)
        print("Image loaded successfully.")
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def save_image(image, filename="processed_image.png"):
    
    try:
        imsave(filename, image)
        print(f"Image saved as {filename}")
    except Exception as e:
        print(f"Error saving image: {e}")
