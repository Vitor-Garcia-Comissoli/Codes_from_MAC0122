#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 8 13:15:18 2020

@author: fradim
"""
import time
import random

CABECALHO = " "*7 + "n" + " "*5 + "sort  sorted  insercao  insercao_py"
MIN = 2**10
MAX = 2**26

# opções para as listas geradas
ALEATORIA   = 'aleatoria'
CRESCENTE   = 'crescente'
DECRESCENTE = 'decrescente'
OPCAO = ALEATORIA 
# OPCAO = CRESCENTE
# OPCAO = DECRESCENTE

def main():
    print(f"Testes para ordenação por inserção binária: lista {OPCAO}")
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

        #----------------------------------------
        # sorted(v)
        v = v_orig.copy()
        t_sorted = execute(sorted, v)
        # supomos a função sorted() correta

        #----------------------------------------
        # ordenação por inserção (insertion sort)
        v = v_orig.copy()
        t_insercao = execute(insercao, v) 
        for j in range(i):
            if v[j] != j:
                print("SOCORRO! insercao(v) não ordeneou v!")
                return

        #---------------------------------------    
        # ordenação por inserção (insertion sort)
        insercao_py = insercao_pyA # del, list.insert
        # insercao_py = insercao_pyB   # fatias
        v = v_orig.copy()
        t_insercao_py = execute(insercao_py, v)
        for j in range(i):
            if v[j] != j:
                print("SOCORRO! insercao_py(v) não ordeneou v!") 
                return
            
        # mostre resultados
        print(f"{i:9} {t_sort:7.2f}{t_sorted:7.2f}{t_insercao:9.2f}{t_insercao_py:12.2f}")

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
        
#---------------------------------------------------------
def insercao(v):
    '''(list) -> None
    RECEBE uma lista `v`.
    REARRANJA os itens de `v` para que fiquem em ordem
    crescente.

    A função é uma implementação de ordenação por inserção.
    '''
    n = len(v)
    for i in range(1, n):
        x = v[i]
        # encontre posição de x 
        j = i - 1
        while j >= 0 and v[j] > x:
            v[j+1] = v[j]
            j -= 1
        # coloque x na sua posição    
        v[j+1] = x    
        
#---------------------------------------------------------        
def insercao_pyA(v):
    '''(list) -> None
    RECEBE uma lista `v`.
    REARRANJA os itens de `v` para que fiquem em ordem
    crescente.

    A função é uma implementação de ordenação por inserção.
    Aqui é usado o comando del e o método list.insert()
    '''
    n = len(v)
    for i in range(1, n):
        x = v[i]
        del v[i]
        # encontre posição onde x deve ser inserido
        for j in range(i-1, -2, -1):
            if v[j] <= x: break
        v.insert(j+1, x)

#---------------------------------------------------------        
def insercao_pyB(v):
    '''(list) -> None
    RECEBE uma lista `v`.
    REARRANJA os itens de `v` para que fiquem em ordem
    crescente.

    A função é uma implementação de ordenação por inserção.
    Aqui é usado fatiamento
    '''
    n = len(v)
    for i in range(1, n):
        x = v[i]
        # encontre posição onde x deve ser inserido
        for j in range(i-1, -2, -1):
            if v[j] <= x: break
        v[j+2:i+1] = v[j+1:i]
        v[j+1] = x
        
#-------------------------------------------------------
if __name__ == "__main__":
    main()
