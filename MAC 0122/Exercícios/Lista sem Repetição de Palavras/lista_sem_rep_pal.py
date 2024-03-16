#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 17:18:18 2020

@author: fradim
"""
# para cronometrar o tempo consumido
import time
# para a busca binária
import bisect

# constantes
N    = "       n  "
LIST = "    list  "
SORT = " list-bb  "
SET  = "     set  "
MIN = 2**4
# MAX = 2**15 # não usado

# textos sem pentuação
# ARQUIVO = "lusiadas_sem_pontuacao.txt" # está no e-Disciplinas
# ARQUIVO = "tinyTale.txt" # está no e-Disciplinas
ARQUIVO = "bible_sem_pontuacao.txt" # está no e-Disciplinas
# ARQUIVO = "dickens_sem_pontuacao.txt" # não está no e-Disciplinas

# seletores de funções
lista          = True
lista_ordenada = True
conjunto       = True

def main():
    print(f"Testes para o arquivo '{ARQUIVO}'")

    # leia o arquivo
    print("lendo o arquivo...")
    with open(ARQUIVO, "r", encoding="utf-8") as arq:
        txt = arq.read()
    print("arquivo lido")

    # construa a lista de palavras
    print("criando lista de palavras...")
    v = txt.split()
    n = len(v)
    txt = None # não precisa mais
    print(f"lista criada com {n} itens")
    
    # cabeçalho
    print(N, end="")
    if lista: print(LIST, end="")
    if lista_ordenada: print(SORT, end="")
    if conjunto: print(SET, end="")
    print()

    i = MIN    
    while i < n:
        print(f'{i:8}', end="")
        
        #----------------------------------------
        if lista:
            t_list, lstA = execute(dedup_list, v, 0, i)
            print(f'{t_list:10.2f}', end="")  

        #----------------------------------------
        if lista_ordenada:
            t_lista_sort, lstB = execute(dedup_list_sort, v, 0, i) 
            print(f'{t_lista_sort:10.2f}', end="")  

        #----------------------------------------
        if conjunto:
            t_set, conj = execute(dedup_set, v, 0, i) 
            print(f'{t_set:10.2f}', end="")  

        if not (len(conj) == len(lstA) == len(lstB))\
           or not (conj == set(lstA) == set(lstB)):
            print("SOCORRO! Tem algo errado!")
            return

        # mude de linha
        print()

        # dobre o tamanho da lista sendo considerada
        i *= 2

        
#---------------------------------------------------------
def dedup_list(v, e, d):
    '''(list) -> list
    RECEBE uma lista `v` e inteiros `e` e `d`.
    RETORNA uma lista sem repetições dos  itens em `v[e:d]`.
    '''
    lst = []
    for i in range(e, d):
        item = v[i]
        if item not in lst:
            lst.append(item)
    return lst

#---------------------------------------------------------
def dedup_list_sort(v, e, d):
    '''(list) -> list
    RECEBE uma lista `v` e inteiros `e` e `d`.
    RETORNA uma lista crescente e sem repetições dos itens em `v[e:d]`.
    '''
    lst = []
    for i in range(e, d):
        item = v[i]
        # encontre posição onde item está ou deve ser inserido
        # busca binária
        j = bisect.bisect_left(lst, item, lo=0, hi=len(lst))
        # se o item não está na lista, ele é inserido
        if j >= len(lst) or lst[j] != item:
            lst.insert(j, item)
    return lst

#---------------------------------------------------------
def dedup_set(v, e, d):
    '''(list) -> set
    RECEBE uma lista `v` e um inteiros `e` e `d` .
    RETORNA um conjunto dos itens em `v[e:d]`.
    '''
    conj = set()
    for i in range(e, d):
        item = v[i]
        conj.add(item)
    return conj
    # return {v[i] for i in range(e, d)}
    # return set(v[e:d])
    
#-------------------------------------------              
def execute(f, v, e, d):
    '''(callable, list) -> float
    RECEBE uma função `f` e uma lista `v`.
    RETORNA o tempo gasto e valor retornado pela execução de `f(v, e, d)`.
    '''
    inicio = time.time()
    valor = f(v, e, d)
    fim = time.time()
    elapsed = fim-inicio
    return elapsed, valor      
        

#-------------------------------------------------------
if __name__ == "__main__":
    main()
