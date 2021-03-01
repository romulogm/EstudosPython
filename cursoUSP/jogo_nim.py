

def computador_escolhe_jogada(n, m):
    retirar = 0
    resto = n - retirar
    while resto % n != 0 and retirar <= m:
        retirar = retirar + 1
        if resto % n == 0 and retirar <= m:
        return retirar

def usuario_escolhe_jogada(n, m):
    retirar = input("Quantas peças você vai tirar?")
    return retirar

def partida():
    # inicio
    print("**** Rodada 1 ****")
    print("")
    n = input("Quantas peças?")
    m = input("Limite de peças por jogada?")

    if (m + 1) % n == 0:
        print("Você começa!")
    else:
        print("Computador começa!")
        n = n - computador_escolhe_jogada(n, m)



def campeonato():
    score_pn = 0
    score_player = 0

print("Bem vindo ao jogo do NIM! Escolha: ")
print("1 - para jogar com uma partida isolada")
print("2 - para jogar um campeonato")
jogo = int(input())
    if jogo == 1:

    if jogo == 2:

    else:
        print("Opção incorreta.")


# n = número de peças inicial
# m = número máximo de peças máximo de retirar
