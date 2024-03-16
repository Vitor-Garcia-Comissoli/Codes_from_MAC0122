#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 17:18:18 2020

@author: fradim
"""
import time
import random

CABECALHO = " "*7 + "n" + " "*5 + "força-bruta   cont"

# tamanho das listas
MIN = 2**4
MAX = 2**17 # tamanho alvo

# para reprodutibilidade
SEMENTE = 0

def main():
    print("Testes para 3SUM: versão testa tudo")
    print(CABECALHO)
    i = MIN
    random.seed(SEMENTE)
    while i <= MAX:
        # sorteio de uma lista com i inteiros DISTINTOS
        # os inteiros estão em range(-i, i+1)
        v = random.sample(range(-i, i+1), i)

        #----------------------------------------
        # 3SUM versão força bruta
        t_fb, cont = execute(forca_bruta, v) 
            
        # mostre resultados
        print(f"{i:9}{t_fb:12.2f}{cont:10}")

        # dobre o tamanho da entrada
        i *= 2
        
#---------------------------------------------------------
def forca_bruta(v):
    '''(list) -> int
    RECEBE uma lista `v` de inteiros distintos.
    RETORNA o número trios v[i], v[j] e v[k], com 
    i < j < k tais que v[i] + v[j] + v[k] = 0. 
    '''
    conta = 0
    n = len(v)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if v[i] + v[j] + v[k] == 0:
                    conta += 1
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
