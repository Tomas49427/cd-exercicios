from PIL.Image import Image
from os import urandom


def make_key(size: int) -> bytes:
    return urandom(size)


def xor_img_key(img_bytes: bytes, key: bytes) -> bytearray:
    result = bytearray(len(img_bytes))
    for i in range(len(img_bytes)):
        result[i] = (key[i] ^ img_bytes[i])
    return result


def xor_img_key_partial(img: Image, img_bytes: bytes, key: bytes, vertical_start: int, vertical_end: int,
                        horizontal_start: int, horizontal_end: int) -> bytearray:
    bytes_per_pixel = 4 if img.mode == 'RGBA' else 3 if img.mode == 'RGB' else 1
    result = bytearray(len(img_bytes))
    for i in range(len(img_bytes)):
        current_index = i / bytes_per_pixel
        if vertical_start <= current_index / img.height + 1 <= vertical_end and horizontal_start <= current_index % img.width + 1 <= horizontal_end:
            result[i] = (key[i] ^ img_bytes[i])
        else:
            result[i] = (img_bytes[i])
    return result
