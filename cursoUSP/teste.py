def maior_primo(x):
        maior = 2
        while ePrimo(maior) == True:
                maior = maior + 1
        if maior == x:
                print(maior)

def ePrimo(k):
    if k % 2 == 0:
        return False
    elif k % 3 == 0:
        return False
    elif k % 5 == 0:
        return False
    elif k % 7 == 0:
        return False
    elif k % 11 == 0:
        return False
    elif k % 13 == 0:
        return False
    elif k % 17 == 0:
        return False
    elif k % 23 == 0:
        return False
    else:
        return True
