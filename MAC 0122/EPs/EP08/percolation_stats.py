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
    monitores e colegas). Com exceção de material de MAC0110 ou MAC0122, 
    caso  você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''
from percolation import Percolation
import numpy as np
import random
import math
                 
class PercolationStats:
    '''Classe utilizada para estimar o limiar de percolação.
    '''
    
    def __init__(self, shape, t):
        
        self.exp = t
        
        if type(shape) == int:
            shape = (shape, shape)
        
        self.shape = shape
        self.nlin = shape[0]
        self.ncol = shape[1]
        
        limiar = []
        no_abertos = []
        
        for i in range(t):
            percolation = Percolation(shape)
            while percolation.percolates() == False:
                
                coordenada = (random.randint(0, self.nlin-1), random.randint(0, self.ncol-1))
                
                percolation.open(coordenada[0], coordenada[1])
                
            num = percolation.no_open()
            no_abertos += [num]
            limiar += [(num/(self.nlin * self.ncol))]
            
        self.limiar = limiar
        self.abertos = no_abertos
        
    def no_abertos(self):
        
        abertos = self.abertos[:]
            
        Array = np.array(abertos)
        
        return Array
    
    def mean(self):
        
        limiar = self.limiar
        t = self.exp
        
        soma = 0
        
        for i in range(t):
            soma += limiar[i]
            
        soma = soma / t
        
        return soma
        
      
    def stddev(self):
        
        limiar = self.limiar
        t = self.exp
        
        média = self.mean()
        
        soma = 0
        
        for i in range(t):
            soma += ((limiar[i] - média)**2)
            
        soma = soma / (t-1)
        
        desvio_p = math.sqrt(soma)
        
        return desvio_p
        
      
    def confidenceLow(self):
        
        média = self.mean()
        s = self.stddev()
        t = self.exp
        
        minimo = (média - ((1.96 * s) / math.sqrt(t)))
        
        return minimo
        
    def confidenceHigh(self):
         
        média = self.mean()
        s = self.stddev()
        t = self.exp
        
        maximo = (média + ((1.96 * s) / math.sqrt(t)))
        
        return maximo
    