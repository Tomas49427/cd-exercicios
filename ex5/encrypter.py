import io

from PIL import Image
from crypto import make_key
from datetime import datetime
from os import path, makedirs
from crypto import xor_img_key, xor_img_key_partial


def encrypt_full(file: str) -> (str, str):
    img = Image.open(file)
    img_bytes = img.tobytes()
    key_size = len(img_bytes)
    key = make_key(key_size)
    result = xor_img_key(img_bytes, key)
    return save_encrypted(file, result, img, False, key)


def encrypt_partial(file: str, vertical_start: int, vertical_end: int, horizontal_start: int, horizontal_end: int) -> (str, str):
    img = Image.open(file)
    img_bytes = img.tobytes()
    key_size = len(img_bytes)
    key = make_key(key_size)
    result = xor_img_key_partial(img, img_bytes, key, vertical_start, vertical_end, horizontal_start,
                                 horizontal_end)
    return save_encrypted(file, result, img, True, key)


def save_encrypted(file: str, result: bytearray, img: Image, partial: bool, key: bytes) -> (str, str):
    encrypted = Image.frombytes(img.mode, img.size, bytes(result))
    dt_string = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    file_name = path.basename(file)
    partial = "partial-" if partial else ""
    if not path.exists("./encrypted/"):
        makedirs("./encrypted/")
    if not path.exists("./key/"):
        makedirs("./key/")
    encrypted.save(f'./encrypted/{dt_string} {partial}{file_name}')
    key_file = open(f'./key/{dt_string} {file_name}.bin', 'wb')
    key_file.write(key)
    key_file.close()
    encrypted.close()
    img.close()
    return f'./encrypted/{dt_string} {partial}{file_name}', f'./key/{dt_string} {file_name}.bin'
