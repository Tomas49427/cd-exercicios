import os

folder_path = "../resources"
english_file_name = "ListaPalavrasEN.txt"
portuguese_file_name = "ListaPalavrasPT.txt"


# EX 3, b
def count_symbols_2(file):
    # Initialize the count of symbols
    invalid_symbols = {"\n", "'", " ", "-", "\"", "/"}
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

    return symbol_counts


def main():
    # Read the symbols inside the english file
    with open(os.path.join(folder_path, english_file_name), 'r') as file:
        print(f"Symbols for {english_file_name}:")
        file_content = file.read()
        english_symbol_counts = count_symbols_2(file_content)
        print("\n")

    # Read the symbols inside the portuguese file
    with open(os.path.join(folder_path, portuguese_file_name), 'r') as file:
        print(f"Symbols for {portuguese_file_name}:")
        file_content = file.read()
        portuguese_symbol_counts = count_symbols_2(file_content)
        print("\n")

    # Get the 5 most frequent symbols for each language
    english_top_5 = sorted(english_symbol_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    portuguese_top_5 = sorted(portuguese_symbol_counts.items(), key=lambda x: x[1], reverse=True)[:5]

    print("Top 5 most frequent symbols in English:")
    for symbol, count in english_top_5:
        print(f"Symbol: {symbol}, Count: {count}")

    print("\nTop 5 most frequent symbols in Portuguese:")
    for symbol, count in portuguese_top_5:
        print(f"Symbol: {symbol}, Count: {count}")


main()
