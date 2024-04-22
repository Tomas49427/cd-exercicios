# reads an input file, and prints out all the characters that have an occurence above a certain percentage

def symbols_above_percent(file, percent):
    # Read the file
    with open(file, 'r') as f:
        text = f.read()

    # Count the symbols
    symbols = {}

    # Count the symbols
    for char in text:
        if char in symbols:
            symbols[char] += 1
        else:
            symbols[char] = 1

    # Calculate the percentage
    total = sum(symbols.values())

    # Print the symbols that have an occurence above a certain percentage
    for char, count in symbols.items():
        # Calculate the percentage
        if count / total * 100 > percent:
            # Print the symbol, count and percentage
            print("Symbol:", char, "Count:", count, "Percentage:", count / total * 100)


def main():
    file = input("Enter file name: ")
    percent = float(input("Enter percent: "))
    symbols_above_percent(file, percent)


main()