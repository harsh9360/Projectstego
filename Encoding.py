### Encoding Process (stego_encode.py)

import cv2
import os
from tkinter import Tk, filedialog

def encode_message(image_path, message, password, output_path="encoded_image.jpg"):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return
    
    d = {chr(i): i for i in range(255)}
    n, m, z = 0, 0, 0
    
    for char in message:
        img[n, m, z] = d[char]
        n, m = n + 1, m + 1
        z = (z + 1) % 3
    
    cv2.imwrite(output_path, img)
    print("Message encoded successfully!")
    os.system(f"start {output_path}")  # Opens the image (Windows only)

if __name__ == "__main__":
    Tk().withdraw()
    img_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not img_path:
        print("No image selected!")
    else:
        secret_msg = input("Enter secret message: ")
        passcode = input("Enter a passcode: ")
        encode_message(img_path, secret_msg, passcode)



