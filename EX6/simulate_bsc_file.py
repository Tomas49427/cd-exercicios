from EX6.binary_symetric_channel import binary_symmetric_channel

probability = 0.005
in_file_path = 'TestFilesEX6/alice29.txt'
out_file_path = 'TestFilesEX6/alice29_out.txt'


def simulate_bsc_file(input_file, output_file, p):
    with open(input_file, 'rb') as input_file:
        data = input_file.read()

    in_sequence = ''.join(format(byte, '08b') for byte in data)
    out_sequence = binary_symmetric_channel(in_sequence, p)

    with open(output_file, 'wb') as output_file:
        output_file.write(bytes(int(out_sequence[i:i + 8], 2) for i in range(0, len(out_sequence), 8)))

    num_errors = sum(a != b for a, b in zip(in_sequence, out_sequence))
    return num_errors / len(in_sequence)


def write_bsc_file(file, data):
    with open(file, 'wb') as file:
        file.write(bytes(int(data[i:i + 8], 2) for i in range(0, len(data), 8)))


def main():
    ber = simulate_bsc_file(in_file_path, out_file_path, probability)
    print(f"BER for file {in_file_path} is {ber} with p = {probability}")


main()