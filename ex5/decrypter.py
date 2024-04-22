from PIL import Image
from datetime import datetime
from os import path, makedirs
from crypto import xor_img_key, xor_img_key_partial


# Decrypts the entire image by XORing its bytes with the provided key
def decrypt_full(file: str, key_path: str) -> str:
    img = Image.open(file)
    img_bytes = img.tobytes()
    key = open(key_path, 'rb').read()
    result = xor_img_key(img_bytes, key)
    return save_decrypted(file, result, img)


# Decrypts a portion of the image by XORing its bytes with the provided key, based on specified ranges
def decrypt_partial(file: str, key_path: str, vertical_start: int, vertical_end: int, horizontal_start: int,
                    horizontal_end: int) -> str:
    img = Image.open(file)
    img_bytes = img.tobytes()
    key = open(key_path, 'rb').read()
    result = xor_img_key_partial(img, img_bytes, key, vertical_start, vertical_end, horizontal_start, horizontal_end)
    return save_decrypted(file, result, img)


# Saves the decrypted image to disk, returning the path of the saved file
def save_decrypted(file: str, result: bytearray, img: Image) -> str:
    decrypted = Image.frombytes(img.mode, img.size, bytes(result))
    file_name = path.basename(file)
    if not path.exists("./decrypted/"):
        makedirs("./decrypted/")
    decrypted.save(f'./decrypted/{file_name}')
    decrypted.close()
    img.close()
    return f'./decrypted/{file_name}'
