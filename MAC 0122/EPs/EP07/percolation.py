# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
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
    monitores e colegas). Com exceção de material de MAC0110 e MAC0122, 
    caso você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''
import numpy as np

#-------------------------------------------------------------------------- 
# constantes
BLOCKED = 0  # sítio bloqueado
OPEN    = 1  # sítio aberto
FULL    = 2  # sítio cheio

class Percolation:
    '''
    Representa uma grade com todos os sítios inicialmente bloqueados.
    '''
    def __init__(self, shape):
        
        if type(shape) == tuple:
            self.nlin = shape[0]
            self.ncol = shape[1]
            
            if self.nlin < 0 or self.ncol < 0 or type(self.nlin) != int or type(self.ncol) != int:
                print('ERRO')
                return None
            else:
                self.shape = shape
            
        else:
            shape = int(shape)
            self.shape = (shape, shape)
            self.nlin = shape
            self.ncol = shape
         
        self.Array = np.full(self.shape, BLOCKED)
        
    def __str__ (self):
        
        nlin = self.nlin
        ncol = self.ncol
        
        array = self.Array
        
        s = (ncol * '+---') + '+\n'
        
        for i in range(nlin):
            for j in range(ncol):
                if array[i,j] == 0:
                    s += '|   '
                elif array[i,j] == 1:
                    s += '| o '
                elif array[i,j] == 2:
                    s += '| x '
                
            s += '|\n'
            s += (ncol * '+---') + '+\n'
                
        return s
    
    def shape(self):
        
        size = self.shape
        return size
    
    def is_open(self, lin, col):
        
        nlin = self.nlin
        ncol = self.ncol
        
        if nlin < lin:
            print('ERRO')
            return None
        
        if ncol < col:
            print('ERRO')
            return None
        
        array = self.Array
        
        if array[lin,col] == 1 or array[lin,col] ==  2:
            return True
        else:
            return False
        
    def is_full(self, lin, col):
        
        nlin = self.nlin
        ncol = self.ncol
        
        if nlin < lin:
            print('ERRO')
            return None
        
        if ncol < col:
            print('ERRO')
            return None
        
        array = self.Array
        
        if array[lin,col] ==  2:
            return True
        else:
            return False
    
    def percolates(self):
        
        array = self.Array
        nlin = self.nlin
        ncol = self.ncol
        
        size = self.shape
        
        Percolation = False
        
        if size == (1,1):
            if array[0,0] == 2: return True
        
        else:
            '''
            for j in range(ncol):
                for i in range(ncol):
                        if array[0,i] == 2:
                            Percolation = True
                for w in range(1, ncol):
                    if Percolation == False:
                        return False
                    else:
                        for i in range(ncol):
                            if array[w,i] == 2:
                                Percolation = True
                    
                if array[nlin-1,j] == 2:
                    if Percolation == True:
                        return True
            '''
        return False
    
    def no_open(self):
        
        array = self.Array
        nlin = self.nlin
        ncol = self.ncol
        
        abertos = 0
        
        for i in range(nlin):
            for j in range(ncol):
                if array[i,j] == 1 or array[i,j] == 2:
                    abertos += 1
        
        return abertos
    
    def open(self, lin, col):
        
        nlin = self.nlin
        ncol = self.ncol
        
        if nlin < lin:
            print('ERRO')
            return None
        
        if ncol < col:
            print('ERRO')
            return None

        if self.Array[lin,col] == 0:
            if lin == 0:
                self.Array[lin,col] = 2
            else:
                self.Array[lin,col] = 1
            '''
            if lin > 0 and lin < nlin-1 and col > 0 and col < ncol-1:
                if self.Array[lin-1,col] == 2 or self.Array[lin+1,col] == 2 or self.Array[lin,col-1] == 2 or self.Array[lin,col+1] == 2:
                    self.Array[lin,col] = 2
            '''
        return None
    
    def get_grid(self):
        
        array = self.Array[:]
        
        Novo_array = np.array(array)
        
        return Novo_array
    
#--------------------------------------------------------------------------

class Fila:
    
    def __init__(self):
        self.itens = []
        
    def __str__(self):
        return str(self.itens)
    
    def vazia(self):
        return self.itens == []
    
    def insere(self, item):
        self.itens.append(item)
        
    def remove(self):
        return self.itens.pop(0)
    
    def __len__(self):
        return len(self.itens)

#--------------------------------------------------------------------------
'''        
def distancias(origem, array):
    
    q = Fila()
    q.insere(origem)
    
    tamanho = array.shape
    
    Novo_array = Percolation(tamanho)
    a, b = origem
    
    Novo_array.open(a,b)
    
    while not q.vazia():
        
        i = q.remove()
        lin = i[0]
        col = i[1]
        
        if array[lin-1,col] == 1 or array[lin-1,col] == 2:
            q.insere((lin-1,col))
                       
        if array[lin+1,col] == 1 or array[lin+1,col] == 2:
            q.insere((lin+1,col))
                       
        if array[lin,col-1] == 1 or array[lin,col-1] == 2:
            q.insere((lin,col-1))
                       
        if array[lin,col+1] == 1 or array[lin,col+1] == 2:
            q.insere((lin,col+1))
                       
        # pintar de azul:
                       
        if array[lin-1,col] == 2:
            Novo_array[lin,col] = 2
            
        elif array[lin+1,col] == 2:
            Novo_array[lin,col] = 2
            
        elif array[lin,col-1] == 2:
            Novo_array[lin,col] = 2
            
        elif array[lin,col+1] == 2:
            Novo_array[lin,col] = 2
        
    return Novo_array
'''    
