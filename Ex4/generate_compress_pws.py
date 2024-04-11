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

generate_and_compress_passwords(source)

compression_ratio = generate_and_compress_passwords(source)
print(f"Taxa de compressão: {compression_ratio:.2f}")