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
# https://docs.python.org/3/library/string.html
import string

import numpy as np

CABECALHO = " "*7 + "n" + " "*5 + "lcsRM     lcs"

# comprimento as strings
MIN = 2**2
MAX = 2**8

SEMENTEs = 1 # para reprodutibilidade
SEMENTEt = 2 # para reprodutibilidade

# para geração das strings aleatórias
# ALFABETO = string.ascii_uppercase
ALFABETO = "ACGT"

def main():
    print("Testes para strings aleatorias de mesmo comprimento")

    #---------------------------------------------------
    # gere s
    random.seed(SEMENTEs) # para reprodutibilidade
    s = "".join(random.choices(ALFABETO, k=MAX))
    print(f"s: {s}")
    #---------------------------------------------------
    # gere t
    random.seed(SEMENTEt) # para reprodutibilidade
    t = "".join(random.choices(ALFABETO, k=MAX))
    print(f"t: {t}")
    
    print(CABECALHO)
    i = MIN
    while i <= MAX:
        #---------------------------------------------    
        # função que retorna o comprimento de LCS(s,t)
        t_lcsRM, lcs  = execute(lcsRM, s, i, t, i) 

        # mostre resultados
        print(f"{i:8}{t_lcsRM:10.2f}     {lcs}")

        # dobre o tamanho da entrada
        i *= 2
    print("FIM")
    
#----------------------------------------------------------------
def lcsRM(s, m, t, n):
    '''(str, int, str, int) -> str
    RECEBE uma string `s` de comprimento `m` e uma string `t` de 
    comprimento `n`.
    RETORNA o comprimento de uma LCS entre s e t.
    Invólocro para lcsRCache.
    '''
    # tabela para armazenar valores calculados
    opt = np.full((m+1,n+1), -1)
    lcsRCache(s, m, t, n, opt)
    # compute as entradas da matriz opt[][] de uma maneira 'bottom up'
    # opt[i][j] contém o comprimento de uma LCS de s[0:i] e t[0:j]
    return opt[m][n]

#----------------------------------------------------------------
def lcsRCache(s, m, t, n, opt):
    '''(str, int, str, int, array) -> int
    RECEBE uma string `s` de comprimento `m` e uma string `t` de 
    comprimento `n` e uma tabela opt.
    RETORNA o comprimento de uma LCS entre s e t. 
    opt[m][n] contém o comprimento de uma LCS de s[0:m] e t[0:n].
    '''

    # BASE
    if opt[m][n] != -1: return opt[m, n]
    
    # BASE
    if m == 0 or n == 0: opt[m][n] = 0
        
    # REDUZ 
    elif s[m-1] == t[n-1]:
        opt[m, n] = 1 + lcsRCache(s, m-1, t, n-1, opt)
     
    # REDUZ
    else: 
        lcs1 = lcsRCache(s, m-1, t,   n, opt)
        lcs2 = lcsRCache(s,   m, t, n-1, opt)
        # COMBINA
        opt[m, n] = max(lcs1, lcs2)
        
    return opt[m, n]


#-------------------------------------------              
def execute(f, s, m, t, n):
    '''(callable, str, int, str, int) -> float. int
    EXECUTA f(s, m, t, n).
    RETORNA o tempo gasto pela execução e o valor retornado.
    '''
    inicio = time.time()
    lcs = f(s, m, t, n)
    fim = time.time()
    elapsed = fim-inicio
    return elapsed, lcs      

#-------------------------------------------------------
if __name__ == "__main__":
    main()
