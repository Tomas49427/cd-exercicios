import math
import os
import matplotlib.pyplot as plt


# PIL ver mais tarde
def count_symbols(file_content):
    # Initialize the count of symbols
    symbol_counts = {}
    total_symbols = 0

    # Iterate through each character in the file
    for symbol in file_content:
        # Increment the count of the symbol
        if symbol in symbol_counts:
            symbol_counts[symbol] += 1
        else:
            symbol_counts[symbol] = 1

        # Increment the total count of symbols
        total_symbols += 1

    # Calculate the probability of each symbol
    symbol_probabilities = {}
    symbol_value = {}
    for symbol, count in symbol_counts.items():
        probability = count / total_symbols  # Calculate the probability of each symbol
        symbol_probabilities[symbol] = probability
        symbol_value[symbol] = -math.log2(probability)  # Calculate the value of the symbol using the formula -log2(p)

    # Print symbol value and probability
    for symbol, value in symbol_value.items():
        print(f"Symbol: {symbol}, Value: {value}, Probability: {symbol_probabilities[symbol]}")

    # Calculate the entropy
    entropy = 0  # Initialize entropy

    # Iterate through each symbol probability
    for probability in symbol_probabilities.values():
        # Calculate contribution to entropy and add it
        entropy += probability * -math.log2(probability)

    # Print the entropy
    print(f"Entropy: {entropy}")

    # Histogram for each symbol
    for symbol, count in symbol_counts.items():
        plt.bar(symbol, count)

    plt.xlabel('Symbol')
    plt.ylabel('Frequency')
    plt.title('Symbol Frequencies Histogram')
    plt.show()


def main():
    folder_path = "../recursos/TestFilesCD"
    # List all files in the directory
    file_list = os.listdir(folder_path)

    for file_name in file_list:
        # Read the content of each file
        with open(os.path.join(folder_path, file_name), 'rb') as file:
            file_content = file.read()
            count_symbols(file_content)


main()
