from EX6.binary_symetric_channel import binary_symmetric_channel

probability = 0.005  # BER
in_file_path = 'TestFilesEX6/alice29.txt'  # File to be transmitted
out_file_path = 'TestFilesEX6/alice29_out.txt'  # File to be received


# EX 6, c
# Function to simulate a binary symmetric channel that receives a file as input and a BER and writes the output to a file
def simulate_bsc_file(input_file, output_file, p):
    # Read the input file with bytes
    with open(input_file, 'rb') as input_file:
        data = input_file.read()

    # Convert the bytes to a binary string
    in_sequence = ''.join(format(byte, '08b') for byte in data)
    out_sequence = binary_symmetric_channel(in_sequence, p)

    # Write the output file with bytes
    with open(output_file, 'wb') as output_file:
        output_file.write(bytes(int(out_sequence[i:i + 8], 2) for i in range(0, len(out_sequence), 8)))

    # Calculate the number of errors
    num_errors = sum(a != b for a, b in zip(in_sequence, out_sequence))
    # Calculate the length of the sequence
    length = len(in_sequence)
    return num_errors, length


# Function to write a binary string to a file
def write_bsc_file(file, data):
    with open(file, 'wb') as file:
        file.write(bytes(int(data[i:i + 8], 2) for i in range(0, len(data), 8)))


def main():
    n_errors, length = simulate_bsc_file(in_file_path, out_file_path, probability)
    print(f"Number of errors for file {in_file_path} is {n_errors}, with p = {probability}")
    print(f"Error rate for file {in_file_path} is {n_errors / length}, with p = {probability}")


main()
