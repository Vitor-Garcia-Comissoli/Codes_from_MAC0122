# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM OUTRO import ...
#------------------------------------------------------------------

'''

    Nome: Vítor Garcia Comissoli
    NUSP: 11810411

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0122, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função 
        split(), strip(), map() e filter() para leitura dos dados
        no arquivo.

    Descrição de ajuda ou indicação de fonte:

'''

import random
FILMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

def main(args=None):
    ''' (None) -> None
        Essa função main está aqui para testar a classe Cliente.
        Você pode alterá-la e incluir os seus próprios testes.
        '''
    # para podermos reproduzir os testes
    random.seed(0) # para outros testes, troco valor

    # lst de filmes
    lst_filmes = args
    if lst_filmes == None: lst_filmes = FILMES
    n_filmes = len(lst_filmes)

    print("Cliente(): iniciando teste...")
    lst_clientes = []
    lst_clientes.append(Cliente("T'Challa"))
    lst_clientes.append(Cliente('Nakia'))
    lst_clientes.append(Cliente('Natasha Romanoff'))
    print("Cliente() não explodiu... :-)")
    
    print("put_classificacao(): iniciando teste...")
    lst_clientes[0].put_classificacao(lst_filmes[:5]) 
    random.shuffle(lst_filmes)
    lst_clientes[1].put_classificacao(lst_filmes[:10])
    random.shuffle(lst_filmes) 
    lst_clientes[2].put_classificacao(lst_filmes[:7])
    print("put_classificao() não explodiu... :-)")

    
    print("__str__(): iniciando teste:")
    for cliente in lst_clientes:
        print(cliente)
    print("__str__(): não explodiu... :-)")
    
    print("get_nome() e get_classificacao(): iniciando teste")
    for cliente in lst_clientes:
        print("%s: %s"%(cliente.get_nome(), cliente.get_classificacao())) 
    print("get_nome() e get_classificacao() não explodiu :-)\n")
        
    print("distancia(): iniciando teste...")
    for cliente0 in lst_clientes:
        for cliente1 in lst_clientes:
            print("distancia(%s,%s)= %s"%(cliente0.get_nome(),
                                          cliente1.get_nome(),
                                          cliente0.distancia(cliente1)))
    print("distancia(): não explodiu... :-)")

#-----------------------------------------------------------------------------

class Cliente:
    '''
        Siga as especificações do enunciado para 
        construir a classe Cliente.

        Coloque o seu código a seguir.
    '''
    def __init__(self, nome):
        self.nome = str(nome)
        self.lista = []
        
    def get_nome(self):
        return self.nome
        
    def put_classificacao(self, filmes):
        self.lista = filmes
        
    def get_classificacao(self):
        cópia = self.lista[:]
        return cópia
        
    def __str__ (self):
        
        lista = self.lista
        
        nome = self.nome
        s = f'{nome}\n'
        
        tamanho = len(lista)
        
        for i in range(tamanho):
            s += f'{i}: {lista[i]}\n'
        
        return s
    
    def distancia(self, Y):
        X = self.lista[:]
        Y = Y.lista[:]
        
        cont = 0
        
        Nova_X = []
        Nova_Y = []
        
        for i in range(len(X)):
            if X[i] in Y:
                Nova_X += X[i]
                cont += 1
        
        if cont < 3:
            return None
        
        for j in range(len(Y)):
            if Y[j] in Nova_X:
                Nova_Y += Y[j]
        
        dist = 0
        
        for i in range(len(Nova_X)):
            
            if Nova_X == Nova_Y:
                return dist
            
            else:
                valor = Nova_X[i]
                for j in range(len(Nova_Y)):
                    if Nova_Y[j] == valor:
                        pos = j
                
                while Nova_Y[i] != valor:
                    
                    if pos > 0:
                        ant = Nova_Y[pos-1]
                        
                    atual = Nova_Y[pos]
                    
                    if pos < len(Nova_Y)-1:
                        prox = Nova_Y[pos+1]
                    
                    if pos < i:
                        Nova_Y[pos] = prox
                        Nova_Y[pos+1] = atual
                        dist += 1
                        pos += 1
                    
                    elif pos > i:
                        Nova_Y[pos] = ant
                        Nova_Y[pos-1] = atual
                        dist += 1
                        pos -= 1
        
#-----------------------------------------------------------------------------        
    
main()
    
    
    
    