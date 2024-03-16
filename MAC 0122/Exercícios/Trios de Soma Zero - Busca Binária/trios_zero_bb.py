#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:17:48 2020

@author: fradim
"""
import time
import random
from bisect import bisect_left

CABECALHO = " "*7 + "n" + " "*7 + "sort-bb     cont"

# tamanho das listas
MIN = 2**4
MAX = 2**17

# para reprodutibilidade
SEMENTE = 0

def main():
    print("Testes para 3SUM: versão com ordenação e busca binária")
    print(CABECALHO)
    i = MIN
    random.seed(SEMENTE)
    while i <= MAX:
        # sorteio de uma lista com i inteiros DISTINTOS
        # os inteiros estão em range(-i, i+1)
        v = random.sample(range(-i, i+1), i)

        #----------------------------------------
        # 3SUM versão "ordene e faça busca binária"
        t_bb, cont = execute(sort_bb, v) 
            
        # mostre resultados
        print(f"{i:9}{t_bb:12.2f}{cont:10}")

        # dobre o tamanho da entrada
        i *= 2
        
#---------------------------------------------------------
def sort_bb(v):
    '''(list) -> int
    RECEBE uma lista `v` de inteiros distintos.
    RETORNA o número trios v[i], v[j] e v[k], com 
    i < j < k tais que v[i] + v[j] + v[k] = 0. 
    '''
    conta = 0
    n = len(v)
    v = sorted(v) 
    for i in range(n):
        for j in range(i+1, n):
            k = index(v, -(v[i] + v[j]), j+1, n)
            if k != None: conta += 1
    return conta

#---------------------------------------------------------
# https://docs.python.org/3/library/bisect.html
def index(v, x, e, d):
    '''(list, obj, int, int) -> int | None
    RECEBE uma lista `v` crescente, um valor `x` e inteiros `e` e `d`.
    RETORNA o menor inteiro i em range(e, d) tal que v[i] == x.
    Se `x` não ocorre em `v` a função retorna None.
    '''
    i = bisect_left(v, x, e, d)
    if i != len(v) and v[i] == x:
        return i
    return None # raise ValueError

#-------------------------------------------              
def execute(f, v):
    '''(callable, list) -> float
    RECEBE uma função `f` e uma lista `v`.
    RETORNA o tempo gasto e valor retornado pela execução de `f(v)`.
    '''
    inicio = time.time()
    valor = f(v)
    fim = time.time()
    elapsed = fim-inicio
    return elapsed, valor      
        
#-------------------------------------------------------
if __name__ == "__main__":
    main()
