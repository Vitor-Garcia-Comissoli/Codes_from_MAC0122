# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 11:24:13 2020

@author: Vítor Garcia Comissoli
"""

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

def main():
    
    mat = [ 
            [0, 0, 1, 1, 1, 0], # 0
            [0, 0, 1, 0, 1, 0], # 1
            [0, 0, 0, 0, 1, 0], # 2
            [0, 0, 0, 0, 1, 1], # 3
            [0, 0, 0, 0, 0, 1], # 4
            [0, 1, 0, 0, 0, 0], # 5
        ]
    
    # mat = input('Digite a matriz de Estradas: ')
    
    # origem = 0
    
    origem = int(input('Digite a cidade de origem: '))
    
    d = distancias(origem, mat)
    
    print('Distância da cidade %d a cidade (< %d):' % (origem, min(len(d), 20)), '\n')
    for i in range (min(len(d), 20)):
        print('  ', i, ':', d[i])
    
def distancias(c, rede):
    
    n = len(rede)
    
    q = Fila()
    q.insere(c)
    
    d = [ n ] * n
    d[c] = 0
    
    while not q.vazia():
        
        i = q.remove()
        for j in range(n):
            if rede[i][j] == 1 and d[j] > d[i] + 1:
                d[j] = d[i] + 1
                q.insere(j)
    
    return d
    
main()