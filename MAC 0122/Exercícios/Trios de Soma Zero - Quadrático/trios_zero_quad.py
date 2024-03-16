#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 17:18:18 2020

@author: fradim
"""
import time
import random

CABECALHO = " "*7 + "n" + " "*7 + "quadrático    cont"

# tamanho das listas
MIN = 2**4
MAX = 2**17 

# para reprodutibilidade
SEMENTE = 0

def main():
    print("Testes para 3SUM: versão 'closing walls'")
    print(CABECALHO)
    i = MIN
    random.seed(SEMENTE)
    while i <= MAX:
        # sorteio de uma lista com i inteiros DISTINTOS
        # os inteiros estão em range(-i, i+1)
        v = random.sample(range(-i, i+1), i)

        #----------------------------------------
        # 3SUM versão que usa um dicionário
        t_quad, cont = execute(quadratico, v) 
            
        # mostre resultados
        print(f"{i:9}{t_quad:12.2f}{cont:12}")

        # dobre o tamanho da entrada
        i *= 2
        
        
#---------------------------------------------------------
def quadratico(v):
    '''(list) -> int
    RECEBE uma lista `v`
    RETORNA o número trios v[i], v[j] e v[k], com 
    i < j < k tais que v[i] + v[j] + v[k] = 0. 
    '''
    conta = 0
    n = len(v)
    v = sorted(v)
    for i in range(n-2):
        x = v[i]
        e = i+1
        d = n-1
        while e < d:
            y = v[e]
            z = v[d]
            soma = x + y + z
            if   soma > 0:
                d -= 1
            elif soma < 0:
                e += 1
            else:    
                conta += 1
                e += 1
                d -= 1
    return conta

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