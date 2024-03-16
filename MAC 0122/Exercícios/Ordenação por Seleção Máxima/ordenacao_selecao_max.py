#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 13:15:18 2020

@author: fradim
"""
import time
import random

CABECALHO = " "*7 + "n" + " "*5 + "sort  selecao  selecao_py"
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

        #----------------------------------------
        # ordenação por selecao (selection sort)
        v = v_orig.copy()
        t_selecao = execute(selecao, v) 
        for j in range(i):
            if v[j] != j:
                print("SOCORRO! selecao(v) não ordenou v!")
                return

        #---------------------------------------    
        # ordenação por selecao (selection sort)
        # usa min() e index()  # fatias
        v = v_orig.copy()
        t_selecao_py = execute(selecao_py, v)
        for j in range(i):
            if v[j] != j:
                print("SOCORRO! selecao_py(v) não ordenou v!") 
                return
            
        # mostre resultados
        print(f"{i:9} {t_sort:7.2f}{t_selecao:8.2f}{t_selecao_py:10.2f}")

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
def selecao(v):
    '''(list) -> None
    RECEBE uma lista `v`.
    REARRANJA os itens de `v` para que fiquem em ordem
    crescente.

    A função é uma implementação de ordenação por selecao
    '''
    n = len(v)
    for i in range(n-1, 0, -1):
        # encontra o dono da posição i
        imax = i
        for j in range(i-1, -1, -1):
            if v[j] > v[imax]: 
                imax = j
        # troca
        v[i], v[imax] = v[imax], v[i]
        
#---------------------------------------------------------        
def selecao_py(v):
    '''(list) -> None
    RECEBE uma lista `v`.
    REARRANJA os itens de `v` para que fiquem em ordem
    crescente.

    A função é uma implementação de ordenação por selecao.
    Aqui é usada a função max() e o método list.index()
    '''
    n = len(v)
    for i in range(n-1, 0, -1):
        # encontra o dono da posição i
        valmax = max(v[:i+1]) # hmm
        imax = v.index(valmax)
        # troca
        v[i], v[imax] = v[imax], v[i]
        
#-------------------------------------------------------
if __name__ == "__main__":
    main()