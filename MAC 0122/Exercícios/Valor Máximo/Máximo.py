#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:14:41 2020

@author: fradim
"""
import numpy  as np
import random as rd

### Para o limite da recursÃ£o
import sys
# MAX_LIMIT = 10000
# sys.setrecursionlimit(MAX_LIMIT)
print(f"limite de recursÃ£o = {sys.getrecursionlimit()}")
###

#========================================================
def maximo(v):
    '''(list) -> item

    RECEBE uma lista v.
    RETORNA o maior elemento da lista.
    '''
    # pegue o comprimento da lista
    n = len(v)

    # retorne o maior elemento
    return maximoR(n,v)

#--------------------------------------------------------
def maximoR(n,v):
    '''(int,list) -> item

    RECEBE um inteiro positivo n e uma lista v.
    RETORNA o maior elemento das n primeiras posiÃ§Ãµes.
    '''
    if n == 1: return v[0]
    x = maximoR(n-1,v)
    if x > v[n-1]: return x
    return v[n-1]

#=======================================================
#
#  FATIA
# 
#======================================================
def maximoRF(v):
    '''(list) -> item

    RECEBE inteiros positivos i e n e uma lista v. 
    RETORNA o maior elemento das posiÃ§Ãµes de Ã­ndices entre i e n-1.
    '''
    n = len(v)
    if n == 1: return v[0]
    x = maximoRF(v[0:n-1]) # FATIA, Ã© clone para list e vista para array
    if x > v[n-1]: return x
    return v[n-1]


#=======================================================
#
#
#======================================================
def rand_list(n):
    v = [i for i in range(n)]
    rd.shuffle(v)
    return v

def rand_array(n):
    v = np.arange(n)
    np.random.shuffle(v)
    return v