import random


def binary_symmetric_channel(binary_sequence, p):
    result = ""
    for bit in binary_sequence:
        if random.random() < p:
            result += '0' if bit == '1' else '1'
        else:
            result += bit
    return result


