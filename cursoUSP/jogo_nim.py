# n = número de peças inicial
# m = número máximo de peças máximo de retirar
   
#deixar sempre um número de peças que seja múltiplo de (m+1)
#ao jogador.Caso isso não seja possível, deverá tirar o número
#máximo de peças possíveis.

def computador_escolhe_jogada(total, m):
    if test_divis(total, m, m) == True:
        print("O computador tirou", m, "peças.")
        return m
    
    if total <= m: 
        print("O computador tirou", total, "peças.")
        return total

    retirar = m-1
    while test_divis(total, m, retirar) == False:
        if retirar == 0:
            print("O computador tirou", m, "peças.")
            return m

        retirar = retirar - 1

    print("O computador tirou", retirar, "peças.")    
    return retirar
    
    
def test_divis(n,m, retirar):
    if (n - retirar) % (m+1) == 0:
        return True
    else:
        return False

def usuario_escolhe_jogada(n, m):
    retirar = int(input("Quantas peças você vai tirar?"))
    while retirar <= m:
        print("Você tirou", retirar, "peças.")
        return retirar
    while retirar <= 0:
        retirar = 1
        print("Você tirou", retirar, "peças.")
        return retirar
    while retirar > m:
        retirar = m
        print("Você tirou", retirar, "peças.")
        return retirar


def erro_input(total, input): 
    if input <= 0: 
        return True
    if input < total:
        return True


def partida():
    # inicio
    vitoria = 0
    print("**** Rodada ****")
    # perguntar valor de n
    n = int(input("Quantas peças?"))
    while n <= 0:
        n = int(input("Quantas peças?"))
    # perguntar valor de m
    m = int(input("Limite de peças por jogada?"))
    while m > n:
        m = int(input("Limite de peças por jogada?"))
    while m <= 0:
        m = int(input("Limite de peças por jogada?"))
        
    # decidir quem inicia o game e atualizar o valor de n
    if n % (m + 1)  == 0:
        print("Você começa!")
        inicio = 1
        usuario_escolhe_jogada(n, m)
    else:
        inicio = 0
        print("Computador começa!")
    #laço para intercalar as jogadas
    while inicio == 1 and n > 0:
        n = n - int(usuario_escolhe_jogada(n, m))
        if n == 0:
            vitoria = 2
            print("Fim do jogo! O usuário ganhou!")
            return vitoria
        n = n - int(computador_escolhe_jogada(n, m))
        if n == 0:
            vitoria = 1
            print("Fim do jogo! O computador ganhou!")
            return vitoria
    while inicio == 0 and n > 0:
        n = n - int(computador_escolhe_jogada(n, m))
        print("Agora restam ", n, "peças no tabuleiro.")
        if n == 0:
            vitoria = 1
            print("Fim do jogo! O computador ganhou!")
            return vitoria
        n = n - int(usuario_escolhe_jogada(n, m))
        if n == 0:
            vitoria = 2
            print("Fim do jogo! O usuário ganhou!")
            return vitoria
    #corrigir: quando tira mais peças e N fica negativo
    #definir quem ganhou o jogo (n == 0)

def campeonato():
    #chamar função partida() 3 vezes
    score_computador = 0
    score_usuario = 0
    vitoria = 0
    partida()
    if vitoria == 1:
        score_computador = score_computador + 1
    if vitoria == 2:
        score_usuario = score_usuario + 1
    partida()
    if vitoria == 1:
        score_computador = score_computador + 1
    if vitoria == 2:
        score_usuario = score_usuario + 1
    partida()
    if vitoria == 1:
        score_computador = score_computador + 1
    if vitoria == 2:
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

# def main():
#     print(test_divis(13, 4, 3))

main()
