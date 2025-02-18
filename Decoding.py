### Decoding Process (stego_decode.py)

import cv2
from tkinter import Tk, filedialog

def decode_message(image_path, original_message_length, password):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return
    
    c = {i: chr(i) for i in range(255)}
    message = ""
    n, m, z = 0, 0, 0
    
    for _ in range(original_message_length):
        message += c[img[n, m, z]]
        n, m = n + 1, m + 1
        z = (z + 1) % 3
    
    print("Decrypted message:", message)

if __name__ == "__main__":
    Tk().withdraw()
    img_path = filedialog.askopenfilename(title="Select an Encoded Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not img_path:
        print("No image selected!")
    else:
        msg_length = int(input("Enter original message length: "))
        passcode = input("Enter the passcode: ")
        decode_message(img_path, msg_length, passcode)
