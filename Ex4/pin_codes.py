from SymbolSource import SymbolSource
import numpy as np


def generate_pin_codes():
    numbers = SymbolSource.SYMBOLS['NUMBERS']
    probabilities = np.ones(len(numbers)) / len(numbers)
    source = SymbolSource(probabilities, numbers)
    pin_codes = ["".join(map(chr, source.generate_sequence(np.random.randint(4, 7)))) for _ in range(10)]
    source.printSourceInfo()
    print(f'Pin codes: {pin_codes}')

def main():
    generate_pin_codes()


main()
