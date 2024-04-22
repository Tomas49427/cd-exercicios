import strong_passwords
import os
from zipfile import ZipFile
import numpy
from SymbolSource import SymbolSource

def generate_and_compress_passwords(source, n=1000, filename="passwords.zip"):

    # Gerar senhas fortes
    passwords = strong_passwords.generate_strong_passwords(source, n)
    passwords = list(passwords)
    txt_filename = "passwords.txt"
    with open(txt_filename, "w") as f:
        f.write("\n".join(passwords))

    # Comprimir o arquivo de texto
    with ZipFile(filename, 'w') as zipf:
        zipf.write(txt_filename)

    # Remover o arquivo de texto
    os.remove(txt_filename)

    # Calcular e retornar a taxa de compressão
    original_size = sum(len(password) for password in passwords) + n - 1  # +n-1 para os caracteres de nova linha
    compressed_size = os.path.getsize(filename)
    compression_ratio = compressed_size / original_size

    return compression_ratio

symbols = numpy.concatenate([SymbolSource.SYMBOLS['NUMBERS'], SymbolSource.SYMBOLS['UPPER_CASE'], SymbolSource.SYMBOLS['LOWER_CASE'], SymbolSource.SYMBOLS['SPECIAL_CHARS_1'], SymbolSource.SYMBOLS['SPECIAL_CHARS_2']])
probabilities = numpy.ones(len(symbols)) / len(symbols)
source = SymbolSource(probabilities, symbols)
num_passwords = 1000
filename = "passwords.zip"
generate_and_compress_passwords(source, num_passwords, filename)

compression_ratio = generate_and_compress_passwords(source)
print(f"Taxa de compressão: {compression_ratio:.2f}")



def generate_strong_passwords(source, n):
    passwords = []
    for _ in range(n):
        password_length = numpy.random.randint(8, 13)
        password = "".join(map(chr, source.generate_sequence(password_length)))
        passwords.append(password)
    return passwords

def generate_and_compress_passwords(source, n=1000, filename="passwords.zip"):
    passwords = generate_strong_passwords(source, n)
    txt_filename = "passwords.txt"
    with open(txt_filename, "w") as f:
        f.write("\n".join(passwords))

    with ZipFile(filename, 'w') as zipf:
        zipf.write(txt_filename)

    os.remove(txt_filename)
    original_size = sum(len(password) for password in passwords) + n - 1
    compressed_size = os.path.getsize(filename)
    compression_ratio = compressed_size / original_size
    return compression_ratio, source.entropy

def main():
    symbols = numpy.concatenate([numpy.arange(48, 58), numpy.arange(65, 91),
                                 numpy.arange(97, 123), numpy.arange(33, 48), numpy.arange(58, 65)])

    # Uniform distribution
    uniform_probabilities = numpy.ones(len(symbols)) / len(symbols)
    uniform_source = SymbolSource(uniform_probabilities, symbols)
    uniform_compression_ratio, uniform_entropy = generate_and_compress_passwords(uniform_source, 1000, "uniform_passwords.zip")
    uniform_source.printSourceInfo()
    print(f"Uniform Distribution - Compression Ratio: {uniform_compression_ratio:.2f}, Entropy: {uniform_entropy:.2f} bits/symbol")

    # Dirichlet distribution
    dirichlet_probabilities = numpy.random.dirichlet(numpy.ones(len(symbols)) * 0.5)
    dirichlet_source = SymbolSource(dirichlet_probabilities, symbols)
    dirichlet_compression_ratio, dirichlet_entropy = generate_and_compress_passwords(dirichlet_source, 1000, "dirichlet_passwords.zip")
    dirichlet_source.printSourceInfo()
    print(f"Dirichlet Distribution - Compression Ratio: {dirichlet_compression_ratio:.2f}, Entropy: {dirichlet_entropy:.2f} bits/symbol")

if __name__ == "__main__":
    main()

