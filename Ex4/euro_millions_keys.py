from SymbolSource import SymbolSource
import numpy



def generate_euro_millions_keys():
    numbers = SymbolSource.SYMBOLS['EURO_MILLIONS']
    probabilities = numpy.ones(len(numbers)) / len(numbers)
    source = SymbolSource(probabilities, numbers)
    keys = [source.generate_sequence(5), source.generate_sequence(2)]
    print(f'Keys: {keys}')
    print (f'Entropy: {source.entropy:.2f} bits/symbol')

def main():
    for i in range(10):
        generate_euro_millions_keys()

main()
