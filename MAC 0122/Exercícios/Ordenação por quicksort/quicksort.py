#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 10:15:18 2020

@author: fradim
"""
import time
import random

CABECALHO = " "*7 + "n" + " "*5 + "sort  quicksortR"
MIN = 2**10
MAX = 2**26

# opções para as listas geradas
ALEATORIA   = 'aleatória'
CRESCENTE   = 'crescente'
DECRESCENTE = 'decrescente'
OPCAO = ALEATORIA 
# OPCAO = CRESCENTE
# OPCAO = DECRESCENTE

def main():
    print(f"Testes para ordenação por intercalação: lista {OPCAO}")
    print(CABECALHO)
    i = MIN
    while i <= MAX:
        # lista crescente [0, 1, ..., i-1]
        if  OPCAO == ALEATORIA:
            v_orig = [j for j in range(i)]
            random.seed(0) # para reprodutibilidade
            random.shuffle(v_orig)  
        elif OPCAO == CRESCENTE:
            # [0, 1, ..., i-1]
            v_orig = [j for j in range(i)]
        else: # DECRESCENTE
            # [i-1, i-2, ..., 1, 0]
            v_orig = [j for j in range(i-1,-1,-1)] 

        #-----------------------------------------    
        # list.sort()
        v = v_orig.copy()
        t_sort = execute(list.sort, v) 
        # supomos o método list.sort() correto

        #----------------------------------------
        # ordenação por quicksort recursivo 
        v = v_orig.copy()
        t_quicksortR = execute(quicksort, v) 
        for j in range(i):
            if v[j] != j:
                print("SOCORRO! quickdort(v) não ordenou v!")
                return
            
        # mostre resultados
        print(f"{i:9} {t_sort:7.2f}{t_quicksortR:10.2f}")

        # dobre o tamanho da entrada
        i *= 2
        
#-------------------------------------------              
def execute(ordena, v):
    '''(callable, list) -> float
    Executa ordena(v).
    RETORNA o tempo gasto para a ordenação.
    '''
    inicio = time.time()
    ordena(v)
    fim = time.time()
    elapsed = fim-inicio
    return elapsed      

#-----------------------------------------------        
def quicksort(v):
    '''(list) -> None
    RECEBE uma lista `v`.
    REARRANJA os itens de `v` para que fiquem em ordem crescente.
    É um implementação do algoritmo quicksort
    '''
    
    quicksortR(v, 0, len(v))
    
    '''
    if len(v) <= 1: return
    e, d = 0, len(v)
    m = separe(v, e, d)
    quicksort(v[0: m])
    quicksort(v[m+1:d])
    '''
#---------------------------------------------------------
def quicksortR(v, e, d):
    '''(list, int, int) -> None
    RECEBE uma lista `v` e índice `e` e `d`.
    REARRANJA os itens de `v[e: d]` para que fiquem em ordem crescente.
    É um implementação do algoritmo quicksort, versão recursiva
    '''
    if e >= d-1: return
    m = separe(v,   e, d) # v[m] está na posição correta
    quicksortR(v,   e, m) # ordene v[e: m]
    quicksortR(v, m+1, d) # ordene v[m+1: d]
        
#---------------------------------------------------------
def separe(v, e, d):
    '''(list, int, int) -> int
    RECEBE uma lista `v` e inteiros `e` e `d`.
    REARRANJA os itens de `v[e: d]` e RETORNA um 
    índice m tal que v[e:m] <= v[m] < v[m+1:d].
    PRÉ-CONDICÃO: e < d
    '''
    x = v[d-1] # pivo
    i = e-1
    for j in range(e, d): #A#
        if v[j] <= x:
            i += 1
            v[i], v[j] = v[j], v[i]
    return i

#-----------------------------------------------
def separePF(v, e, d):
    '''(list, int, int) -> int
    RECEBE uma lista `v` e inteiros `e` e `d`.
    REARRANJA os itens de `v[e: d]` e RETORNA um 
    índice m tal que v[e:m] <= v[m] < v[m+1:d].
    Implementa a estratégia de "Paredes Fechando".
    PRÉ-CONDICÃO: e < d
    '''
    x  = v[e] # pivo
    i, j = e+1, d-1
    while i <= j:
        while i <= j and v[i] <  x: i += 1
        while j >= i and v[j] >= x: j -= 1
        if i < j:
            # v[i] >= x e v[j] < x
            v[i], v[j] = v[j], v[i]
            i += 1
            j -= 1
    # v[e  :i] < x e v[j+1:d] >= x e i == j+1
    v[e], v[j] = v[j], v[e]
    return j

#-------------------------------------------------------
if __name__ == "__main__":
    main()
