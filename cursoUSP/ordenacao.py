def main():
    num1 = float(input("Insira um número: "))
    num2 = float(input("Insira um número: "))
    num3 = float(input("Insira um número: "))

    if (num1) < (num2) and (num2) < (num3) or num1 < 0 and num1 > num2 > num3:
        print ("crescente")

    else:
        print ("não está em ordem crescente")
main()
