#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 17:29:09 2020

@author: fradim
"""
import time
import random
CABECALHO = " "*7 + "n" + "    index  buscaA  buscaB  buscaC"
MIN = 2**10
MAX = 2**25

def main():
    print("Testes apenas para buscas BEM-SUCEDIDAS: x está em v")
    print(CABECALHO)
    i = MIN
    while i <= MAX:
        # argumentos
        v = [j for j in range(i)] # v = [0, 1, ..., i-1]
        x = random.choice(v) 

        # list.index()
        # ATENÇÃO: se x não está em v, v.index(x) explode
        i_I, t_I = execute(list.index, v, x) 

        # buscaA()
        i_A, t_A = execute(buscaA, v, x)

        # buscaB()
        i_B, t_B = execute(buscaB, v, x)

        # buscaC()
        i_C, t_C = execute(buscaC, v, x)

        if not (i_I == i_A == i_B == i_C):
            print("SOCORRO!")
            return
        
        # mostre resultados
        print(f"{i:9} {t_I:7.2f}{t_A:8.2f}{t_B:8.2f}{t_C:8.2f}")
        i *= 2
        
#-------------------------------------------              
def execute(f, v, x):
    '''(callable, list, obj) -> int, float
    Executa f(v, x).
    RETORNA valor retornado por f() e tempo gasto.
    '''
    inicio = time.time()
    i = f(v, x)
    fim = time.time()
    elapsed = fim-inicio
    return i, elapsed      
        
#---------------------------------------------------------        
def buscaA(v, x):
    ''' (list, obj) -> int or None 
    RECEBE uma lista `v` e um objeto `x`.
    RETORNA o menor índice i tal que v[i] == x.
    Se o `x` não está na lista a função retorna None.
    '''
    n = len(v)
    for i in range(n):
        if x == v[i]: return i
    return None

#---------------------------------------------------------        
def buscaB(v, x):
    ''' (list, obj) -> int or None 
    RECEBE uma lista `v` e um objeto `x`.
    RETORNA o menor índice i tal que v[i] == x.
    Se o `x` não está na lista a função retorna None.
    '''
    v.append(x)
    i = 0
    while x != v[i]: i += 1
    v.pop() # corrige a v
    if i < len(v): return i
    return None

#---------------------------------------------------------        
def buscaC(v, x):
    ''' (list, obj) -> int or None 
    RECEBE uma lista `v` e um objeto `x`.
    RETORNA o menor índice i tal que v[i] == x.
    Se o `x` não está na lista a função retorna None.
    '''
    if x not in v: return None
    n = len(v)
    for i in range(n):
        if x == v[i]: return i


#-------------------------------------------------------
if __name__ == "__main__":
    main()