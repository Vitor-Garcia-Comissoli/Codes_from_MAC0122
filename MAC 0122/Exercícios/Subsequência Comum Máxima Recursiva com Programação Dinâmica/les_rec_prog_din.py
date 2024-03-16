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

CABECALHO = " "*7 + "n      lcsPD    lcs"

# comprimento as strings
MIN = 2**2
MAX = 2**6

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
        t_lcsPD, lcs  = execute(lcsPD, s, i, t, i) 

        # Hmm, pelo menos verificamos se lcs é subsec comum
        if not (subseq(lcs, s[:i]) and subseq(lcs, t[:i])):
            print("SOCORRO! lcsPD() retornou string que não é subseq comum!")
            return None
        
        # mostre resultados
        print(f"{i:8}{t_lcsPD:10.2f}     {lcs}")

        # dobre o tamanho da entrada
        i *= 2

    print("FIM")    
        
#----------------------------------------------------------------
def lcsPD(s, m, t, n):
    '''(str, int, str, int) -> str
    RECEBE uma string `s`, um inteiro `m`, uma string `t`, um inteiro `n`.
    RETORNA uma string que é lcs de s[:m] e t[:n].
    '''
    # tabela para armazenar valores calculados
    opt = np.full((m+1,n+1), -1)

    # compute as entradas da matriz opt[][] de uma maneira 'bottom up'
    # opt[i][j] contém o comprimento de uma LCS de s[0:i] e t[0:j]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[i-1] == t[j-1]:
                opt[i,j] = opt[i-1,j-1] + 1
            else:
                opt[i,j] = max(opt[i-1,j] , opt[i,j-1])

    # return opt[m][n]            
    return get_lcs(s, m, t, n, opt)

#----------------------------------------------            
def get_lcs(s, m, t, n, opt):
    '''(str, str, int, str, int, array) -> str
    RECEBE uma string `s`, um inteiro `m`, uma string `t`, um inteiro `n`
    e uma matriz `opt` tal que `opt[i][j] = len(lcs(s[:i],t[0:j]) 
    para todo i in range(m) e  j in range(n).
    RETORNA uma string que é lcs de s e t.
    '''
    lcs = ''        
    i, j  = m, n
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            lcs = s[i-1] + lcs
            i -= 1
            j -= 1
        elif opt[i-1][j] >= opt[i][j-1]:
            i -= 1
        else:
            j -= 1
    return lcs


#-------------------------------------------              
def subseq (s, t):
    ''' (str, str) -> bool 
    RECEBE strings `s` e `t`.
    RETORNA True se `s` é subsequência de t.
    '''
    i = len(s)-1
    j = len(t)-1
    while i >= 0 and j >= 0:
        if s[i] == t[j]: 
            i -= 1
        j -= 1 
    return i < 0

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
