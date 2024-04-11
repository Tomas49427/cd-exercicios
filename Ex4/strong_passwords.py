from SymbolSource import SymbolSource
import numpy


def generate_strong_passwords(source, n):
    source.printSourceInfo()

    for x in range(n):
        password = "".join(map(chr, source.generate_sequence(numpy.random.randint(8, 13))))
        print(password)


def main():
    symbols = numpy.concatenate([SymbolSource.SYMBOLS['NUMBERS'], SymbolSource.SYMBOLS['UPPER_CASE'], SymbolSource.SYMBOLS['LOWER_CASE'], SymbolSource.SYMBOLS['SPECIAL_CHARS_1'], SymbolSource.SYMBOLS['SPECIAL_CHARS_2']])

    probabilities = numpy.ones(len(symbols)) / len(symbols)
    source = SymbolSource(probabilities, symbols)

    generate_strong_passwords(source, 10)

main()