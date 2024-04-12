import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
import os
import helper

def load_image(path):
    return Image.open(path)


def interactive_crop(image_path):
    image = load_image(image_path)
    fig, ax = plt.subplots()
    ax.imshow(image)

    coords = []

    def onselect(eclick, erelease):
        x1, y1, x2, y2 = int(eclick.xdata), int(eclick.ydata), int(erelease.xdata), int(erelease.ydata)
        coords[:] = [min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)]
        plt.close(fig)  # Fecha a figura após a seleção

    rectangle_selector = RectangleSelector(
        ax, onselect,
        useblit=True,
        minspanx=5, minspany=5, spancoords='pixels',
        interactive=True
    )
    plt.show()
    return tuple(coords)


def generate_key(length):
    """ Gera uma chave aleatória de bytes. """
    return np.random.bytes(length)


def apply_vernam_cipher(byte_data, key):
    """ Aplica a cifra de Vernam usando XOR nos bytes. """
    byte_array = np.frombuffer(byte_data, dtype=np.uint8)
    key_array = np.frombuffer(key, dtype=np.uint8)
    ciphered_bytes = np.bitwise_xor(byte_array, key_array).tobytes()
    return ciphered_bytes


def extract_and_cipher(image, crop_coords, key):
    x, y, w, h = crop_coords
    cropped_image = image.crop((x, y, x + w, y + h))
    cropped_bytes = cropped_image.tobytes()
    ciphered_bytes = apply_vernam_cipher(cropped_bytes, key)
    ciphered_image = Image.frombytes('RGB', (w, h), ciphered_bytes)
    return ciphered_image


def patch_image(original, patched, position):
    x, y = position
    original.paste(patched, (x, y))
    return original


def encrypt_area(image_path, output_path, key_path, coords_path):
    coords = interactive_crop(image_path)
    image = load_image(image_path)
    key = generate_key(coords[2] * coords[3] * 3)  # Assuming RGB image
    ciphered_image = extract_and_cipher(image, coords, key)
    patched_image = patch_image(image, ciphered_image, (coords[0], coords[1]))
    patched_image.save(output_path)

    with open(key_path, 'wb') as key_file:
        key_file.write(key)

    with open(coords_path, 'w') as coords_file:
        coords_file.write(','.join(map(str, coords)))


if __name__ == "__main__":
   # img_path = helper.get_resources_path() + "color_images/barries.tif"
    img_path = "original_image.jpg"
    key_path = "encryption_key.bin"
    encrypted_img_path = "encrypted_image.jpg"
    coords_path = "coords.txt"
    encrypt_area(img_path, encrypted_img_path, key_path, coords_path)


