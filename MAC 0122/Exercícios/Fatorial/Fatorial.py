# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 08:50:27 2020

@author: vitor
"""

def fatorial(n):
    if n == 0: # base
        return 1
    return n * fatorial(n-1)