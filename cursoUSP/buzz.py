def main():

    i = int(input("Insira um número: "))

    result = i * 1

    while i != 0:
        result = result + (i * (i - 1))
        i = i - 1
        

    while i == 0:
        print(result)
        break

main()
