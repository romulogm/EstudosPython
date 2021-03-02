def maior_primo(x):
    maior = 2
    final = 0
    while maior <= x:
        if ePrimo(maior) == True:
            final = 0 + maior
            maior = maior + 1
        if ePrimo(maior) == False:
            maior = maior + 1
        if maior == x and ePrimo(maior) == True:
            final = 0 + maior
            return final
        if maior == x and ePrimo(maior) == False:
            return final
            
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
