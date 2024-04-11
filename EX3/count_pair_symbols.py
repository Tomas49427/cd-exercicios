import os

folder_path = "../recursos"
english_file_name = "ListaPalavrasEN.txt"
portuguese_file_name = "ListaPalavrasEN.txt"


def count_pair_symbols(file):
    # Initialize the count of symbols
    invalid_symbols = {"\n", " ", "\"", "/"}
    symbol_pair_counts = {}
    total_pair_symbols = 0

    # Iterate through each symbol in the file
    for i in range(len(file) - 1):
        # Check if it's a valid symbol
        if file[i] in invalid_symbols or file[i + 1] in invalid_symbols:
            continue

        # Increment the count of the symbol
        pair = file[i] + file[i + 1]
        if pair in symbol_pair_counts:
            symbol_pair_counts[pair] += 1
        else:
            symbol_pair_counts[pair] = 1

        # Increment the total count of symbols
        total_pair_symbols += 1

    # Calculate the probability of each symbol
    symbol_pair_probabilities = {}
    for pair, count in symbol_pair_counts.items():
        probability = count / total_pair_symbols  # Calculate the probability of each symbol
        symbol_pair_probabilities[pair] = probability

    # Print symbol value and probability
    for pair, probability in symbol_pair_probabilities.items():
        print(f"Pair: {pair}, Probability: {probability}")


def main():
    # Read the symbols inside the english file
    with open(os.path.join(folder_path, english_file_name), 'r') as file:
        print(f"Sequence symbols for {english_file_name}:")
        file_content = file.read()
        count_pair_symbols(file_content)
        print("\n")

    # Read the symbols inside the portuguese file
    with open(os.path.join(folder_path, portuguese_file_name), 'r') as file:
        print(f"Sequence symbols for {portuguese_file_name}:")
        file_content = file.read()
        count_pair_symbols(file_content)
        print("\n")


main()
