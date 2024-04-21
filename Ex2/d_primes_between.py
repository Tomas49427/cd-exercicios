
# Display all prime numbers between left and right index

def primes_between(left, right):
    primes = []
    # Check if the number is prime
    for i in range(left, right + 1):
        # Prime numbers are greater than 1
        if i > 1:
            # Check for factors
            for j in range(2, i):
                # If the number has a factor, it is not prime
                if i % j == 0:
                    # Not a prime number, so break the loop
                    break
            else:
                # If the loop ends without finding a factor, it is a prime number
                primes.append(i)
    return primes

def main():
    while True:
        # Get the left and right index
        left = int(input("Enter left index: "))

        # Check if the right index is greater than the left index
        right = int(input("Enter right index: "))

        # Display all prime numbers between left and right index
        print(primes_between(left, right))
        if input("Do you want to continue? (y/n): ") == "n":
            break

main()
