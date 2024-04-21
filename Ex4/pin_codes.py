from SymbolSource import SymbolSource
import numpy as np


def generate_pin_codes():
    numbers = SymbolSource.SYMBOLS['NUMBERS']
    probabilities = np.ones(len(numbers)) / len(numbers)
    source = SymbolSource(probabilities, numbers)
    pin_codes = ["".join(map(chr, source.generate_sequence(np.random.randint(4, 7)))) for _ in range(10)]
    source.printSourceInfo()
    print(f'Pin codes: {pin_codes}')

    from SymbolSource import SymbolSource
    import numpy as np

def generate_pin_codes_uniform():
    # Geração de códigos PIN com distribuição uniforme
    numbers = SymbolSource.SYMBOLS['NUMBERS']
    probabilities = np.ones(len(numbers)) / len(numbers)  # Distribuição uniforme
    source = SymbolSource(probabilities, numbers)
    pin_codes = ["".join(map(chr, source.generate_sequence(np.random.randint(4, 7)))) for _ in range(10)]
    source.printSourceInfo()
    print(f'Uniform Pin codes: {pin_codes}')

def generate_pin_codes_weighted():
    # Geração de códigos PIN com distribuição ponderada
    numbers = SymbolSource.SYMBOLS['NUMBERS']
    # Probabilidades personalizadas para cada número
    probabilities = np.array([0.05, 0.05, 0.20, 0.20, 0.10, 0.02, 0.13, 0.13, 0.02, 0.10])
    source = SymbolSource(probabilities, numbers)
    pin_codes = ["".join(map(chr, source.generate_sequence(np.random.randint(4, 7)))) for _ in range(10)]
    source.printSourceInfo()
    print(f'Weighted Pin codes: {pin_codes}')

def main():
    for i in range(10):
        generate_pin_codes_uniform()
    for i in range(10):
        generate_pin_codes_weighted()

if __name__ == "__main__":
    main()

