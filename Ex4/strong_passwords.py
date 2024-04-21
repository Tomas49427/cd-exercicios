from SymbolSource import SymbolSource
import numpy


def generate_strong_passwords(source, n):
    source.printSourceInfo()
    passwords = []

    for x in range(n):
        password = "".join(map(chr, source.generate_sequence(numpy.random.randint(8, 13))))
        #print(password)
        passwords.append(password)

    return passwords


def generate_and_save_passwords(source, n, filename="passwords.txt"):
    passwords = []
    for x in range(n):
        password = "".join(map(chr, source.generate_sequence(numpy.random.randint(8, 13))))
        passwords.append(password)

    with open(filename, "w") as f:
        f.write("\n".join(passwords))

def main():
    symbols = numpy.concatenate([SymbolSource.SYMBOLS['NUMBERS'], SymbolSource.SYMBOLS['UPPER_CASE'], SymbolSource.SYMBOLS['LOWER_CASE'], SymbolSource.SYMBOLS['SPECIAL_CHARS_1'], SymbolSource.SYMBOLS['SPECIAL_CHARS_2']])

    probabilities = numpy.ones(len(symbols)) / len(symbols)
    source = SymbolSource(probabilities, symbols)
    generate_strong_passwords(source, 10)
    # #source_file = "passwords.txt"
    #generate_and_save_passwords(source, 1000, source_file)


main()