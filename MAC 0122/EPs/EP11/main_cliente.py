# importa a classe Cliente e as funções mergeX() e mergesortX()
from cliente import * 

# para teste da classe Cliente
import random  

#####################################################################
# CONSTANTES
# cada caractere representará o nome de um filme para testes
FILMES = list('ABCDEFGHIJKL') # = ['A', 'B', ..., 'L']

#------------------------------------------------------------
def main(args=None):
    # para podermos reproduzir os testes
    random.seed(0)

    # lst de filmes
    lst_filmes = args
    if lst_filmes == None: lst_filmes = FILMES
    n_filmes = len(lst_filmes)
    
    print("Cliente(), EP10: iniciando teste...")
    lst_clientes = []
    lst_clientes.append(Cliente("T'Challa"))
    lst_clientes.append(Cliente('Nakia'))
    lst_clientes.append(Cliente('Natasha Romanoff'))
    print("Cliente() não explodiu... :-)")
    
    print("put_classificacao(), EP10: iniciando teste...")
    lst_clientes[0].put_classificacao(lst_filmes[:5]) 
    random.shuffle(lst_filmes)
    lst_clientes[1].put_classificacao(lst_filmes[:10])
    random.shuffle(lst_filmes) 
    lst_clientes[2].put_classificacao(lst_filmes[:7])
    print("put_classificao() não explodiu... :-)")

    print("__str__(), EP10: iniciando teste:")
    for cliente in lst_clientes:
        print(cliente)
    print("__str__(): não explodiu... :-)\n")
    
    print("get_nome() e get_classificacao(), EP10: iniciando teste")
    for cliente in lst_clientes:
        print("    %s: %s"%(cliente.get_nome(), cliente.get_classificacao())) 
    print("get_nome() e get_classificacao() não explodiu :-)\n")
        
    print("distancia(), EP10: iniciando teste...")
    for cliente0 in lst_clientes:
        for cliente1 in lst_clientes:
            print("    distancia(%s,%s)= %s"%(cliente0.get_nome(),
                                          cliente1.get_nome(),
                                          cliente0.distancia(cliente1)))
    print("distancia(): não explodiu... :-)\n")

    print("mergeX(), EP11: iniciando teste...")
    A = [3,  7, 10, 14, 18]
    B = [2, 11, 16, 20, 23]
    C = A + B
    print("    A: ", A)
    print("    B: ", B)
    print("    C  antes: ", C)
    print("    mergeX('A+B'): retornou ", mergeX(C, 0, 5, 10) )
    print("    C depois: ", C)
    print("mergeX(): não explodiu :-)\n")

    print("mergesortX(), EP11: iniciando teste...")
    V = [10, 14, 18, 7, 3, 20, 23, 11, 2, 16]
    print("V  antes: ", V)
    print("mergesortX(V): ", mergesortX(V,0,10))
    print("V depois: ", V)
    print("mergesortX(): não explodiu :-)\n")

    print("em_comum(), EP11: iniciando teste...")
    for cliente0 in lst_clientes:
        for cliente1 in lst_clientes:
            print("    em_comum(%s, %s)= %s"%(cliente0.get_nome(),
                                             cliente1.get_nome(),
                                             cliente0.em_comum(cliente1)))
    print("em_comum(): não explodiu... :-)\n")

    
    print("distanciaX(), EP11: iniciando teste...")
    for cliente0 in lst_clientes:
        for cliente1 in lst_clientes:
            print("    distanciaX(%s, %s)= %s"%(cliente0.get_nome(),
                                               cliente1.get_nome(),
                                               cliente0.distanciaX(cliente1)))
    print("distanciaX(): não explodiu... :-)\n")

#------------------------------------------------------------
        
if __name__ == '__main__':
    main()