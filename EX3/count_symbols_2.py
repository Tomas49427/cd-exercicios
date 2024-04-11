import os

folder_path = "../recursos"
english_file_name = "ListaPalavrasEN.txt"
portuguese_file_name = "ListaPalavrasEN.txt"


def count_symbols_2(file):
    # Initialize the count of symbols
    invalid_symbols = {"\n", " ", "\"", "/"}
    symbol_counts = {}
    total_symbols = 0

    # Iterate through each character in the file
    for symbol in file:
        # Check if it's a valid character
        if symbol in invalid_symbols:
            continue

        # Increment the count of the symbol
        if symbol in symbol_counts:
            symbol_counts[symbol] += 1
        else:
            symbol_counts[symbol] = 1

        # Increment the total count of symbols
        total_symbols += 1

    # Calculate the probability of each symbol
    symbol_probabilities = {}
    for symbol, count in symbol_counts.items():
        probability = count / total_symbols  # Calculate the probability of each symbol
        symbol_probabilities[symbol] = probability

    # Print symbol value and probability
    for symbol, probability in symbol_probabilities.items():
        print(f"Symbol: {symbol}, Probability: {probability}")


def main():
    # Read the symbols inside the english file
    with open(os.path.join(folder_path, english_file_name), 'r') as file:
        print(f"Symbols for {english_file_name}:")
        file_content = file.read()
        count_symbols_2(file_content)
        print("\n")

    # Read the symbols inside the portuguese file
    with open(os.path.join(folder_path, portuguese_file_name), 'r') as file:
        print(f"Symbols for {portuguese_file_name}:")
        file_content = file.read()
        count_symbols_2(file_content)
        print("\n")


main()
