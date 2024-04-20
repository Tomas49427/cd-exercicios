from PIL import Image
from datetime import datetime
from os import path, makedirs
from crypto import xor_img_key, xor_img_key_partial


def decrypt_full(file: str, key_path: str) -> str:
    img = Image.open(file)
    img_bytes = img.tobytes()
    key = open(key_path, 'rb').read()
    result = xor_img_key(img_bytes, key)
    return save_decrypted(file, result, img)


def decrypt_partial(file: str, key_path: str, vertical_start: int, vertical_end: int, horizontal_start: int,
                    horizontal_end: int) -> str:
    img = Image.open(file)
    img_bytes = img.tobytes()
    key = open(key_path, 'rb').read()
    result = xor_img_key_partial(img, img_bytes, key, vertical_start, vertical_end,horizontal_start, horizontal_end)
    return save_decrypted(file, result, img)


def save_decrypted(file: str, result: bytearray, img: Image) -> str:
    decrypted = Image.frombytes(img.mode, img.size, bytes(result))
    file_name = path.basename(file)
    if not path.exists("./decrypted/"):
        makedirs("./decrypted/")
    decrypted.save(f'./decrypted/{file_name}')
    decrypted.close()
    img.close()
    return f'./decrypted/{file_name}'
