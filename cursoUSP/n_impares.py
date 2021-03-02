def main():

    number = int(input("Digite um número inteiro positivo: "))
    impar = 1

    while number > 0:
        print(impar)
        impar = impar + 2
        number = number - 1

        if number <= 0:
            break

main()
