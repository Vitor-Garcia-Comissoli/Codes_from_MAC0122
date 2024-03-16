#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 2 23:15:18 2020

@author: fradim
"""
# https://docs.python.org/3/library/time.html
import time
# https://docs.python.org/3/library/random.html
import random
# https://docs.python.org/3/library/string.html
import string
# https://docs.python.org/3/library/itertools.html
import itertools

CABECALHO = " "*7 + "n     lcsTT     lcs"

# comprimento as strings
MIN = 2**2
MAX = 2**5

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
        t_lcsTT, lcs  = execute(lcsTT, s, i, t, i) 

        # Hmm, pelo menos verificamos se lcs é subsec comum
        if not (subseq(lcs, s[:i]) and subseq(lcs, t[:i])):
            print("SOCORRO! lcsTT() retornou string que não é subseq comum!")
            return None
        
        # mostre resultados
        print(f"{i:8}{t_lcsTT:10.2f}     {lcs}")

        # dobre o tamanho da entrada
        i *= 2

    print("FIM")
    
#----------------------------------------------------------------
def lcsTT(s, m, t, n):
    '''(str, int, str, int) -> str
    RECEBE uma string `s`, um inteiro `m`, uma string `t` e um inteiro `n`.
    RETORNA uma longest common substring de de s[0:m] e t[0:n].
    '''
    # pegue a menor sequência
    if m > n:
        s, t = t, s
        m, n = n, m

    for k in range(m, 0, -1):
        for z in itertools.combinations(s[:m], k):
            r = "".join(z)
            if subseq(r, t[:n]):
                return r
            
    return ""

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
    '''(callable, str, int, str, int) -> float, str
    EXECUTA f(s, len(s), t, len(t)).
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
