# n = número de peças inicial
# m = número máximo de peças máximo de retirar
def computador_escolhe_jogada(n, m):
    #deixar sempre um número de peças que seja múltiplo de (m+1)
    #ao jogador.Caso isso não seja possível, deverá tirar o número
    #máximo de peças possíveis.
    retirar = m
    resto = n - retirar
    if resto % (m+1) == 0:
        print("O computador tirou", retirar, "peças.")
        return retirar
    while resto % (m+1) != 0:
        retirar = retirar - 1
        if retirar == 0 and resto % (m+1) != 0:
            retirar = m
            print("O computador tirou", retirar, "peças.")
            return retirar

def usuario_escolhe_jogada(n, m):
    retirar = int(input("Quantas peças você vai tirar?"))
    while retirar <= m:
        print("Você tirou", retirar, "peças.")
        return retirar
    while retirar <= 0:
        retirar = int(input("Quantas peças você vai tirar?"))
    while retirar > m:
        retirar = int(input("Quantas peças você vai tirar?"))


def partida():
    # inicio
    print("**** Rodada ****")
    # perguntar valores de n e m
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))
    # decidir quem inicia o game e atualizar o valor de n
    if (m + 1) % n == 0:
        print("Você começa!")
        inicio = 1
        usuario_escolhe_jogada(n, m)
    else:
        inicio = 0
        print("Computador começa!")
    #laço para intercalar as jogadas
    while inicio == 1 and n > 0:
        n = n - usuario_escolhe_jogada(n, m)
        if n == 0:
            vitoria = usuario
            print("Fim do jogo! O usuário ganhou!")
            return vitoria
        n = n - computador_escolhe_jogada(n, m)
        if n == 0:
            vitoria = pc
            print("Fim do jogo! O computador ganhou!")
            return vitoria
    while inicio == 0 and n > 0:
        n = n - computador_escolhe_jogada(n, m)
        print("Agora restam ", n, "peças no tabuleiro.")
        if n == 0:
            vitoria = pc
            print("Fim do jogo! O computador ganhou!")
            return vitoria
        n = n - usuario_escolhe_jogada(n, m)
        if n == 0:
            vitoria = usuario
            print("Fim do jogo! O usuário ganhou!")
            return vitoria
    #corrigir: quando tira mais peças e N fica negativo
    #definir quem ganhou o jogo (n == 0)

def campeonato():
    #chamar função partida() 3 vezes
    score_computador = 0
    score_usuario = 0
    partida()
    if vitoria == pc:
        score_computador = score_computador + 1
    if vitoria == usuario:
        score_usuario = score_usuario + 1
    partida()
    if vitoria == pc:
        score_computador = score_computador + 1
    if vitoria == usuario:
        score_usuario = score_usuario + 1
    partida()
    if vitoria == pc:
        score_computador = score_computador + 1
    if vitoria == usuario:
        score_usuario = score_usuario + 1
    print("**** Final do campeonato! ****")
    print("Placar: Você", score_usuario, "X", score_computador, "Computador")

def main():
    #criar função main chamando a função que dá início ao game
    print("Bem vindo ao jogo do NIM! Escolha: ")
    print("1 - para jogar com uma partida isolada")
    print("2 - para jogar um campeonato")
    jogo = int(input())
    while jogo == 1 or jogo == 2:
        if jogo == 1:
            print("Você escolheu uma partida isolada!")
            campeonato()
        if jogo == 2:
            print("Você escolheu campeonato")
            partida()
    if jogo != 1 or 2:
        int(input())
main()
