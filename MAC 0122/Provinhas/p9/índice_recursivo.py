# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 22:24:53 2020

@author: vitor
"""

def indice(v, n, x):
    if n==-1:
        return None
    if v[n]==x:
        return n
    return indice(v, n-1, x)
