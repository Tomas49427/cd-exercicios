import os

folder_path = "../resources"
english_file_name = "ListaPalavrasEN.txt"
portuguese_file_name = "ListaPalavrasPT.txt"


# EX 3, b
def count_pair_symbols(file):
    # Initialize the count of symbols
    invalid_symbols = {"\n", "'", " ", "-", "\"", "/"}
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

    return symbol_pair_counts


def main():
    # Read the symbols inside the english file
    with open(os.path.join(folder_path, english_file_name), 'r') as file:
        print(f"Sequence symbols for {english_file_name}:")
        file_content = file.read()
        english_symbol_pair_counts = count_pair_symbols(file_content)
        print("\n")

    # Read the symbols inside the portuguese file
    with open(os.path.join(folder_path, portuguese_file_name), 'r') as file:
        print(f"Sequence symbols for {portuguese_file_name}:")
        file_content = file.read()
        portuguese_symbol_pair_counts = count_pair_symbols(file_content)
        print("\n")

    # Get the 5 most frequent symbol pairs for each language
    english_top_5 = sorted(english_symbol_pair_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    portuguese_top_5 = sorted(portuguese_symbol_pair_counts.items(), key=lambda x: x[1], reverse=True)[:5]

    print("Top 5 most frequent symbol pairs in English:")
    for pair, count in english_top_5:
        print(f"Pair: {pair}, Count: {count}")

    print("\nTop 5 most frequent symbol pairs in Portuguese:")
    for pair, count in portuguese_top_5:
        print(f"Pair: {pair}, Count: {count}")


main()
