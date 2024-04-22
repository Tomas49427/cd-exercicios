def progressao_aritmetica(N, u, r):
    #Gera os primeiros N termos de uma progressão aritmética de primeiro termo u e razão r
    resultado = []
    for i in range(N):
        resultado.append(u + i * r)
    return resultado


while True:
    #result = progressao_aritmetica(10, 5, 3)
    #ask user for input
    n = int(input("Enter the number of terms: "))
    u = int(input("Enter the first term: "))
    r = int(input("Enter the ratio: "))
    #call the function and store the result in a variable
    result = progressao_aritmetica(n, u, r)

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
