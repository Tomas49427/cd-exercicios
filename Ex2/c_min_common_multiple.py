import math

def mdc(a, b):
    #calculates the greatest common divisor between two integers a and b using euclidean algorithm
    while b != 0:
        a, b = b, a % b
    return a

def mmc(a, b):
    # determines the least common multiple between two integers a and b
    return abs(a * b) // mdc(a, b)



while True:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = mmc(a, b)
    print(result)
    answer = input("Do you wish to continue? (Y/N): ").lower()
    if answer == "y":
        continue
    elif answer == "n":
        break
    else:
        print("Invalid input. Please enter Y or N.")