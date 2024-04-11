import numpy
import string
import random
from zipfile import ZipFile
import os
from SymbolSource import SymbolSource

#simbolos permitidos na geração da sequência
numbers = numpy.arange(48, 58) # 0 - 9
upper_case = numpy.arange(65, 91) # A - Z
lower_case = numpy.arange(97, 123) # a - z
special_chars = numpy.arange(33, 48) # ! " # $ % & ' ( ) * + , - . /
special_chars_2 = numpy.arange(58, 65) # : ; < = > ? @

# Aqui, garantimos que todos os arrays sejam concatenados corretamente
symbols_allowed = numpy.concatenate((numbers, upper_case, lower_case)).astype(int)

# Exemplo de uso para um alfabeto com 5 símbolos e uma FMP específica
defined_probabilities = [0.20, 0.20, 0.20, 0.20, 0.20]  # soma deve ser = 1

# Gerar sequência de probabilidades aleatórias, soma das probabilidades = 1
random_probabilities = numpy.random.dirichlet(numpy.ones(20),size=1)[0]

# Criar uma fonte de símbolos com a FMP definida acima e os símbolos permitidos
source = SymbolSource(random_probabilities, symbols_allowed)

# Gerar uma sequência de símbolos de acordo com a FMP
sequence_size = 1000
sequence = source.generate_sequence(sequence_size)

# Calcular entropia da fonte e da sequência gerada
entropy_source = source.entropy
entropy_sequence = source.calculate_sequence_entropy(sequence)

print(f'Entropia da fonte: {entropy_source:.2f} bits/símbolo')
print(f'Entropia da sequência: {entropy_sequence:.2f} bits/símbolo')

# Mostrar os símbolos permitidos escolhidos (como inteiros) e as probabilidades associadas
print('Símbolos e probabilidades associadas:')
for i in range(len(source.symbols)):
    symbol_char = chr(source.symbols[i])
    print(f'Símbolo: {source.symbols[i]} [{symbol_char}] - Probabilidade: {source.probabilities[i]:.2f}')


print(f'Sequence: {sequence}')


# Funções geradoras de símbolos




