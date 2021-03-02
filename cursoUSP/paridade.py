def main():

    print("Descubra se um número é par ou ímpar.")
    number = int(input("Digite o número desejado: "))
    parimpar = number / 2

    if parimpar == int(parimpar):
        print("par")

    if parimpar == float(parimpar) and not parimpar == int(parimpar):
        print("ímpar")

main()
