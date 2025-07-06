from PIL import Image
import numpy as np

def encode_lsb(image_path, message, output_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    arr = np.array(img)

    flat = arr.flatten()
    binary_message = ''.join([format(ord(c), '08b') for c in message]) + '1111111111111110'  # End-of-message marker

    if len(binary_message) > len(flat):
        raise ValueError("Message too long to encode in image.")

    for i in range(len(binary_message)):
        flat[i] = (flat[i] & 0xFE) | int(binary_message[i])


    new_arr = flat.reshape(arr.shape)
    Image.fromarray(new_arr).save(output_path)
    print(f"[✅] Message hidden in: {output_path}")
