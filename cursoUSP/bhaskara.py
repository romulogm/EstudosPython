def main():

    print("Vamos resolver uma função de segundo grau, descobrindo o valor de X...")
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))
    c = int(input("Digite o valor de C: "))

    import math
    delta = b ** - 4 * a * c

    if delta > 0:
        xpositivo = (-b + math.sqrt(delta)) / (2 * a)
        xnegativo = (-b - math.sqrt(delta)) / (2 * a)

        print("As raízes reais são ", xpositivo, " e ", xnegativo, ".")

    if delta == 0:
        x = (-b + math.sqrt(delta)) / (2 * a)
        print("O valor de X é ", x, ".")

    if delta < 0:
        print("Não há raízes reais, pois DELTA é menor que 0.")

main()
