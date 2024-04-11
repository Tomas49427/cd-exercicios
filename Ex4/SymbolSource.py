import numpy

class SymbolSource:
    def __init__(self, probabilities, symbols_allowed):
        # Verificar se a FMP é válida
        self.probabilities = numpy.array(probabilities)
        self.symbols = numpy.random.choice(symbols_allowed, size=len(probabilities), replace=False)

        # calcular a entropia da fonte
        self.entropy = -numpy.sum(self.probabilities * numpy.log2(self.probabilities))

    def generate_sequence(self, n):
        # Gerar uma sequência de símbolos de acordo com a FMP
        return numpy.random.choice(self.symbols, size=n, p=self.probabilities)

    def calculate_sequence_entropy(self, sequence):
        # Calcular a entropia de uma sequência de símbolos
        _, counts = numpy.unique(sequence, return_counts=True)
        probabilities = counts / len(sequence)
        return -numpy.sum(probabilities * numpy.log2(probabilities))

    def printSourceInfo(self):
        print(f'Entropia da fonte: {self.entropy:.2f} bits/símbolo')
        print('Símbolos e probabilidades associadas:')
        for i in range(len(self.symbols)):
            symbol_char = chr(self.symbols[i])
            print(f'Símbolo: {self.symbols[i]} [{symbol_char}] - Probabilidade: {self.probabilities[i]:.2f}')


    # Enum para símbolos permitidos
    SYMBOLS = {
        'NUMBERS': numpy.arange(48, 58),  # 0 - 9
        'UPPER_CASE': numpy.arange(65, 91),  # A - Z
        'LOWER_CASE': numpy.arange(97, 123),  # a - z
        'SPECIAL_CHARS_1': numpy.arange(33, 48),  # ! " # $ % & ' ( ) * + , - . /
        'SPECIAL_CHARS_2': numpy.arange(58, 65),  # : ; < = > ? @
        'EURO_MILLIONS': numpy.concatenate((numpy.arange(1, 51), numpy.arange(1, 13))),  # Euro Millions numbers + stars
    }

