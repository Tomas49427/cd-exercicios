def fatorial(a):
    #calculates the factorial of a number
    if a == 0:
        return 1
    resultado = 1
    for i in range(1, a + 1):
        resultado *= i
    return resultado

#ask user for input
while True:
    a = int(input("Enter a number: "))
    #call the function and store the result in a variable
    result = fatorial(a)
    print(result)
    # do you wish to continue?
    answer = input("Do you wish to continue? (Y/N): ").lower()

    # check if the user wants to continue
    if answer == "y":
        continue
    elif answer == "n":
        break
    else:
        print("Invalid input. Please enter Y or N.")


