import subprocess
import barcode
import os
from PIL import Image
from barcode.writer import ImageWriter
from config import BARCODE_FILE

def check_internet():
    try:
        # Connect to Google's public DNS server
        print("checking internet connection......")
        # Ping Google's public DNS server (8.8.8.8)
        subprocess.run(["ping", "-c", "1", "8.8.8.8"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

    
def generate_barcode(data):
    """Generates a Code-128 barcode."""
    try:
        # Generate barcode
        code128 = barcode.get('code128', data, writer=ImageWriter())
        file_path = code128.save(BARCODE_FILE)
        print(f"Barcode successfully saved to {file_path}")
        return file_path
    except barcode.errors.IllegalCharacterError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    
def resize_image(image_path, target_width):
    """
    Resizes the image to fit the target width while maintaining aspect ratio.
    """
    with Image.open(image_path) as img:
        # Calculate the new height to maintain aspect ratio
        aspect_ratio = img.height / img.width
        new_height = int(target_width * aspect_ratio)
        
        # Resize the image
        resized_img = img.resize((target_width, new_height), Image.Resampling.LANCZOS)
        return resized_img

def poweroff():
    os.system("sudo poweroff")