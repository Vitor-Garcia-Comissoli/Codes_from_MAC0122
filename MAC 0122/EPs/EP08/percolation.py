# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
#------------------------------------------------------------------

'''

    Nome: Maria Cristina Santos Andrijic
    NUSP: 11916109

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
        if type(shape) == int:
            shape = (shape, shape)
        self.data = np.full(shape, BLOCKED)
        self.shape = shape
       
    def __str__(self):
        data = self.data
        lin, col = self.shape
        abertos = 0
        barra = '+---+' + (col-1)*'---+'
        s = barra
        for i in range(lin):  
            s += '\n|'
            for j in range(col):
                if data[i][j] == FULL:
                    s += " x |"
                    abertos += 1
                elif data[i][j] == OPEN:
                    s += " o |"
                    abertos += 1
                else:
                    s += '   |'
            s += "\n" + barra
        s += f'\ngrade de dimensão: {lin}x{col}\nno. sítios abertos: {abertos}\npercolou: {self.percolates()}'
        return s
    
    def open(self, lin, col): 
        shape = self.shape
        if lin>=shape[0] or col>=shape[1]:
            print (f"open(): posição [{lin},{col}] está fora da grade")
        else:
            data = self.data
            lst = self.lista(lin, col)
            if lin == 0:
                data[lin, col] = FULL
            elif FULL in lst:
                data[lin, col] = FULL
            else:
                data[lin, col] = OPEN
            if OPEN in lst and data[lin, col] == FULL:
                lim_lin, lim_col = self.shape
                if lin-1 >= 0 and data[lin-1,col] == OPEN:
                    self.open(lin-1, col)
                if lin+1 < lim_lin and data[lin+1,col] == OPEN:
                    self.open(lin+1, col)
                if col-1 >= 0 and data[lin,col-1] == OPEN:
                    self.open(lin, col-1)
                if col+1 < lim_col and data[lin,col+1] == OPEN:
                    self.open(lin, col+1)
                    
    def no_open(self):
        cont = 0
        lin, col = self.shape
        for i in range(lin):
            for j in range(col):
                if self.data[i, j] == OPEN or self.data[i, j] ==FULL:
                    cont += 1
        return cont
                
    def is_open(self, lin, col):
        if self.data[lin, col] == OPEN: return True
        if self.data[lin, col] == FULL: return True
        return False
        
    def is_full(self, lin, col):
        if self.data[lin, col] == FULL: return True
        return False

    def percolates(self):
        lin, col = self.shape
        if FULL in self.data[lin-1, :]: return True
        return False
 
    def get_grid(self):
        return self.data.copy()

    def lista(self, lin, col):
        data = self.data
        lim_lin, lim_col = self.shape
        lst = []
        # lst = [data[lin-1,col], data[lin+1,col], data[lin,col-1], data[lin,col+1]]
        if lin-1 >= 0:
            lst += [int(data[lin-1,col])]
        if lin+1 < lim_lin:
            lst += [int(data[lin+1,col])]
        if col-1 >= 0:
            lst += [int(data[lin,col-1])]
        if col+1 < lim_col:
            lst += [int(data[lin,col+1])]
        return lst














