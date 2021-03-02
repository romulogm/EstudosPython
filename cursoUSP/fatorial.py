def main():

    print("Vamos encontrar o valor de um número fatorial.")
    i = int(input("Digite o valor de n: "))
    result = 1

    while i != 0:
        result = result * i
        i = i - 1

    while i == 0:
        print(result)
        break
main()
