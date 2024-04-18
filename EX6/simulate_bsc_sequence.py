import random

from EX6.binary_symetric_channel import binary_symmetric_channel

sequence_lengths = [1024, 10240, 102400, 1024000, 10240000]
probability = 0.1


def simulate_bsc_sequence(L, p):
    in_sequence = ''.join(random.choice('01') for _ in range(L))
    out_sequence = binary_symmetric_channel(in_sequence, p)
    num_errors = sum(a != b for a, b in zip(in_sequence, out_sequence))

    real_ber = num_errors / L

    return real_ber


def main():
    for L in sequence_lengths:
        ber = simulate_bsc_sequence(L, probability)
        print(f"BER for L = {L} is {ber} with p = {probability}")


main()