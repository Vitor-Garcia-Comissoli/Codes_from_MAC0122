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

#-------------------------------------------------------------------
#
# Funções administrativas mergeX() e mergesortX()
#
#-------------------------------------------------------------------
def mergeX(v, e, m, d):
    ''' (list, int, int, int) -> int

    RECEBE uma lista v tal que v[e:m] e v[m:d] estão em ordem crescente. 
    A função intercala essas fatias de forma que v[e:d] esteja em ordem crescente.

    RETORNA o número de transposições necessários para ordenar v[e:d].
    '''
    
    num = 0

    lstA = v[e:m]
    lstB = v[m:d]

    for i in range(len(lstA)):
        for j in range(len(lstB)):
            if lstA[i] > lstB[j]:
                num += 1
    
    n = d - e
    w = [0]*n
    k = 0
    i = e
    j = m
    
    while i < m and j < d:
        if v[i] < v[j]:
            w[k] = v[i]
            i += 1
        else:
            w[k] = v[j]
            j += 1
        k += 1    
    
    if i < m:
        w[k:] = v[i: m]
    else:   
        w[k:] = v[j: d] 
        
    v[e: d] = w
    
    return num

def mergesortX(v, e=None, d=None):
    ''' (list, int, int) -> int

    Recebe uma lista v e dois inteiros que definem 
    um segmento de v que deve ser ordenado. 

    Quando e e d são None, a lista inteira deve ser ordenada.

    A função retorna o número de transposições resultantes da ordenação 
    de v[e:d].
    '''
    
    if e == None:
        e = 0
        
    if d == None:
        d = len(v)
    
    soma = 0
    
    if e >= d-1:
        return 0
    
    if len(v) <= 1:
        return 0
    
    elif len(v) == 2:
        if v[0] >= v[1]:
            return 0
        else:
            a = v[0]
            v[0] = v[1]
            v[1] = a
            return 1
    
    m = (e + d) // 2
    
    soma += mergesortX(v, e, m)
    soma += mergesortX(v, m, d)
    num = mergeX(v, e, m, d)
    
    soma += num
    
    return soma

#-----------------------------------------------------------
class Cliente:
    '''
        Copie a sua classe Cliente do EP10 para aqui.

        Estenda essa classe adicionando os métodos:
           em_comum() e distanciaX()
        como especifado no enunciado.
 
        Coloque o seu código a seguir.
    '''
    
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
                        
    def em_comum(self, Y):
        
        X = self.lista[:]
        Y = Y.lista[:]
        
        pos = []
        
        for i in range(len(Y)):
            for j in range(len(X)):
                if  X[j] == Y[i]:
                    pos += [j]
                    
        return pos
        
    def distanciaX(self, Y):

        X = self.lista
        Y = Y.lista
        
        x = len(X)
        y = len(Y)
        
        cont = 0
        
        Nova_lst = []
        
        for i in range(x):
            for j in range(y):
                if X[i] == Y[j]:
                    Nova_lst += [j]
                    cont += 1
        
        if cont < 3:
            return None
        
        return mergesortX(Nova_lst)
        
        # return self.distancia(Y)
        
