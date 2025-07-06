from PIL import Image
import numpy as np

def decode_lsb(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    arr = np.array(img)
    flat = arr.flatten()

    bits = [str(flat[i] & 1) for i in range(len(flat))]
    binary_message = ''.join(bits)

    chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    message = ""
    for c in chars:
        if c == '11111111' or c == '11111110':
            break
        message += chr(int(c, 2))
    print("[🔓] Hidden Message:", message)
    return message
