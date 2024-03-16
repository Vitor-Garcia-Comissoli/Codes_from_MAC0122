#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 8 13:15:18 2020

@author: fradim
"""
# https://docs.python.org/3/library/time.html
import time
# https://docs.python.org/3/library/random.html
import random
# https://docs.python.org/3/library/heapq.html
import heapq

CABECALHO = " "*7 + "n" + " "*5 + "sort  heapsort heapsort_py"
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
    print(f"Testes para ordenação por seleção: lista {OPCAO}")
    print(CABECALHO)
    i = MIN
    while i <= MAX:
        # lista crescente [0, 1, ..., i-1]
        if  OPCAO == ALEATORIA:
            v_orig = [j for j in range(i)]
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

        #---------------------------------------    
        # ordenação por selecao (selection sort)
        # usa min() e index()  # fatias
        v = v_orig.copy()
        t_heapsort = execute(heapsort, v)
        for j in range(i):
            if v[j] != j:
                print("SOCORRO! heapsort(v) não ordenou v!") 
                return

        #---------------------------------------    
        # ordenação por selecao (selection sort)
        # usa min() e index()  # fatias
        v = v_orig.copy()
        t_heapsort_py = execute(heapsort_py, v)
        for j in range(i):
            if v[j] != j:
                print("SOCORRO! heapqsort_py(v) não ordenou v!") 
                return
            
        # mostre resultados
        print(f"{i:9} {t_sort:7.2f}{t_heapsort:8.2f}{t_heapsort_py:10.2f}")

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

#-------------------------------------------              
def heapsort(v):
    '''(list) -> None
    RECEBE uma lista `v`.
    REARRANJA os itens de `v` para que fiquem em ordem
    crescente.
    A função é uma implementação do heapsort.
    '''
    n = len(v)
    # remendo
    valmin = min(v) # hmm
    imin = v.index(valmin)
    # troca
    v[0],v[imin] = v[imin], v[0]
    
    # préprocessamento: faz de v[1:n] um max heap
    for i in range((n-1)//2, 0, -1):
        peneira(v, i, n)
        
    for i in range(n-1, 0, -1):    
        v[i], v[1] = v[1], v[i]
        peneira(v, 1, i)

#-------------------------------------------                      
def peneira(v, i, m):
    ''' (list, i, m) -> None
    RECEBE uma lista `v` e um inteiro `i` e `m` tais que os filhos
    do nó i são maxheaps em v[i:m].
    RERRANJA a lista de modo que v[i: m] seja um maxheap
    '''
    p = i   # pai
    f = 2*p # filho esquerdo
    while f < m:
        # f deve ser o filho mais valioso
        if f < m-1 and v[f] < v[f+1]: f+=1  
        if v[p] >= v[f]: break
        # pai desce, filho sobe
        v[p], v[f] = v[f], v[p]
        # filho será o pai
        p  = f
        f = 2*p
 
#-------------------------------------------                  
def peneiraX(v, i, m):
    ''' (list, i, m) -> None
    RECEBE uma lista `v` e um inteiro `i` e `m` tais que os filhos
    do nó i são maxheaps de v[i:m].
    RERRANJA a lista de modo que v[i: m] seja um maxheap
    '''
    p = i    # pai
    f = 2*p  # filho esquerdo
    x = v[p] 
    while f < m:
        # f deve ser o filho mais valioso
        if f < m-1 and v[f] < v[f+1]: f+=1  
        if t >= v[f]: break
        # filho é promovido
        v[p] = v[f]
        # filho vira pai
        p = f
        # filho esquerdo
        f = 2*p
    # encontramos posição de x    
    v[p] = x
        
        
#---------------------------------------------------------        
def heapsort_py(v):
    '''(list) -> list
    RECEBE uma lista `v`.
    RETORNA uma lista crescente com os itens de v.
    Usa espaço extra O(n), onde n = len(v).
    Usa as funções heapq.heappush() e heapq.heappop().  
    Adaptação in-place/mutadora de heapsort() em
    https://docs.python.org/3/library/heapq.html
    '''
    h = []
    for item in v:
        heapq.heappush(h, item)
    v[:] = [heapq.heappop(h) for i in range(len(h))]     
        
#-------------------------------------------------------
if __name__ == "__main__":
    main()
