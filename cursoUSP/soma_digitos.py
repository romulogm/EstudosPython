def main():

    numero = int(input("Digite um número inteiro: "))
    result = 0

    while numero >= 0:
        result = result + numero % 10
        numero = numero // 10

        if numero == 0:
            print(result)
            break
        

main()
