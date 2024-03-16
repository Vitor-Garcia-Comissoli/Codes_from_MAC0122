#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 7 13:15:18 2020

@author: fradim
"""
# https://docs.python.org/3/library/time.html
import time
# https://docs.python.org/3/library/random.html
import random
# https://docs.python.org/3/library/string.html
import string

CABECALHO = " "*7 + "n     lrsSA     lrs"

# comprimento as strings
MIN = 2**2
MAX = 2**15 #20

SEMENTEs = 1 # para reprodutibilidade

# para geração das strings aleatórias
# ALFABETO = string.ascii_uppercase
ALFABETO = "ACGT"
ARQUIVO  = "pi-1million.txt"

# True para s  aleatória ou False para dígitos de pi
TESTE_ALEATORIO = False # True 

# True para exibir s e False para não exibir
EXIBE_S = False

def main():
    if TESTE_ALEATORIO:
        print("Testes para string aleatoria...")
        # gere s aleatoriamente
        random.seed(SEMENTEs) # para reprodutibilidade
        s = "".join(random.choices(ALFABETO, k=MAX))
    else:
        #---------------------------------------------------
        print("Testes para string dos dígitos de pi ...")
        print(f"lendo {ARQUIVO} ...")
        with open(ARQUIVO, 'r', encoding='utf-8') as arq:
            s = arq.read()
        print(f"{ARQUIVO} lido")
        
    if EXIBE_S: print(f"s: {s[:MAX]}")
          
    print(CABECALHO)
    i = MIN
    while i <= MAX:
        #---------------------------------------------    
        # função que retorna o comprimento de LRS(s,t)
        t_lrsSA, lrs  = execute(lrsSA, s, i) 

        # mostre resultados
        print(f"{i:8}{t_lrsSA:10.2f}     {lrs}")

        # dobre o tamanho da entrada
        i *= 2

    print("FIM")
    
#--------------------------------------------
def lrsSA(s, n):
    '''(str, int) -> str
    RECEBE uma string `s` e um inteiro `n`.
    RETORNA uma LRS de `s[:n]`
    '''
    # cria um lista dos sufixo de s
    sufixo = [s[i:n] for i in range(n)] 

    # ordena os sufixo de s
    sufixo.sort() 

    # encontra lrs comparando sufixos adjacentes
    lrs = ''
    for i in range(n-1): 
        x = lcp(sufixo[i], sufixo[i+1])
        if len(x) > len(lrs):
             lrs = x
                
    return lrs            

#--------------------------------------------
def lcp(s, t):
    '''(str, str) -> str
    RECEBE duas strings s e t.
    RETORNA o prefixo comum mais longo de s e t
    '''
    n = min(len(s), len(t))
    for i in range(n):
        if s[i] != t[i]:
            return s[0:i]
    return s[0:n]

#-------------------------------------------              
def execute(f, s, n):
    '''(callable, str, int) -> float, str
    EXECUTA f(s, n).
    RETORNA o tempo gasto pela execução e o valor retornado.
    '''
    inicio = time.time()
    lrs = f(s, n)
    fim = time.time()
    elapsed = fim-inicio
    return elapsed, lrs      

#-------------------------------------------------------
if __name__ == "__main__":
    main()