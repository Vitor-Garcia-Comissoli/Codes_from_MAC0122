#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:14:41 2020

@author: fradim
"""
#------------------------------------------------    
def fibonacciI(n):
    '''(int) -> int
    RECEBE um inteiro nÃ£o negativos n.
    RETORNA o n-Ã©simo nÃºmero de Fibonacci.
    '''
    if n == 0: return 0
    if n == 1: return 1
    anterior = 0
    atual    = 1
    for i in range(1,n):
        proximo = atual + anterior
        anterior = atual
        atual = proximo
    return atual

#------------------------------------------------    
def fibonacciR(n):
    '''(int) -> int
    RECEBE um inteiro nÃ£o negativo n.
    RETORNA o n-Ã©simo nÃºmero de Fibonacci.
    '''
    if n == 0: return 0
    if n == 1: return 1
    return fibonacciR(n-1) + fibonacciR(n-2)

#------------------------------------------------    
def fibonacciRM(n):
    '''(int) -> int
    InvÃ³locro para fibonacciRCache().
    '''
    cache = [-1]*(n+1)
    cache[0] = 0
    cache[1] = 1
    return fibonacciRCache(n, cache)

#------------------------------------------------    
def fibonacciRCache(n, cache):
    '''(int) -> int
    RECEBE um inteiro nÃ£o negativos n.
    RETORNA o n-Ã©simo nÃºmero de Fibonacci.
    '''
    # BASE, jÃ¡ calculamos
    if cache[n] != -1: return cache[n]
    # REDUZA
    cache[n-1] = fibonacciRCache(n-1, cache)
    # cache[n-2] = fibonacciRCache(n-2, cache) jÃ¡ calculamos
    # RESOLVA
    cache[n] = cache[n-2] + cache[n-1]
    return cache[n]

#------------------------------------------------    
def fibonacciRx(n):
    '''(int) -> int, int
    RECEBE um inteiro positivo n >0.
    RETORNA o n-Ã©simo e o (n-1)-Ã©simo nÃºmero de Fibonacci
    '''
    if n == 0: return 0, 0   # 
    if n == 1: return 0, 1
    ant, ult = fibonacciRx(n-1)
    return ult, ant + ult