# n = número de peças inicial
# m = número máximo de peças máximo de retirar
   
#deixar sempre um número de peças que seja múltiplo de (m+1)
#ao jogador.Caso isso não seja possível, deverá tirar o número
#máximo de peças possíveis.

def computador_escolhe_jogada(n, m):
    
    def test_divis(n,m):
        
        if (n - m) % (m+1) == 0:
            return True
        
        if(n - m) % (m+1) != 0:
            return False
        
    retirar = m

    if test_divis(n, retirar) == True:
        print("O computador tirou", retirar, "peças.")
        return retirar
    
    if n <= m: 
        print("O computador tirou", n, "peças.")
        return n
        
    while test_divis(n, retirar) == False:
        retirar = retirar - 1

        if retirar == 0:
            print("O computador tirou", m, "peças.")
            return m

        if test_divis(n, retirar) == True:
            print("O computador tirou", retirar, "peças.")
            return retirar